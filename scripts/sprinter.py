#!/usr/bin/env python3
"""Put a repo under the sprinter-kit planning system, and hand out IDs for it.

  python3 <kit>/scripts/sprinter.py scan                 what is here to set up or migrate
  python3 <kit>/scripts/sprinter.py init --greenfield    write the planning files into the repo
  python3 <kit>/scripts/sprinter.py init --brownfield    the same, keeping the migration blanks
  python3 <kit>/scripts/sprinter.py id [--count N]       fresh IDs, checked against the repo

Run it from anywhere inside the repo you are setting up, or pass --repo. It finds its templates
next to itself, so the kit can live anywhere on disk. scan and id write nothing. init only adds
files: if one it would write already exists, it writes none of them. Nothing is staged or
committed. Windows Git Bash runs it as `python`, not `python3`.

Exit status: 0 clean, 1 findings (suspects from scan, or blanks init left for you to fill),
2 couldn't check, or init stopped before writing.

What each command answers
  scan   Is this repo already set up? Where are its ADRs, and what number is free? Is there an
         old plan, a phase doc, a spike folder, an agent file? Which lines carry a banned word or
         a sprint number? It prints suspects and never judges them.
  init   Copies templates/ into the repo, fills the blanks it can, and lists the rest with line
         numbers. Writes LF and UTF-8 on every platform.
  id     Six hex characters from a real random source. Rerolled if it reads as a number, if it
         is the documentation example 9cf8b9, or if it is already anywhere in the repo, in a
         file's text or a file's name, untracked files included.
"""
import argparse
import datetime
import re
import secrets
import subprocess
import sys
from pathlib import Path, PurePosixPath

KIT = Path(__file__).resolve().parent.parent
TEMPLATES = KIT / "templates"
EXAMPLE_ID = "9cf8b9"   # the ID every document uses as its example; never assigned
SHOW = 12               # suspect lines listed per finding before "... and N more"

# What scan looks for. Word boundaries are checked here in Python, never by git grep -E: macOS's
# git grep -E has no \b, and an empty result from it looks exactly like good news.
BANNED = re.compile(r"\b(TODO|FIXME|XXX|HACK)\b")
NUMBERED = re.compile(r"\b[Ss]print[ _-]?\d+[A-Za-z]?\b(?!-[0-9a-f]{6})")
TAG = re.compile(r"\[[sht]-[0-9a-f]{6}(?:-[a-z])?\]|\[SPRINT-[0-9a-f]{6}(?:-[a-z])?-CLEANUP\]")
CODE_SPAN = re.compile(r"(`+).+?\1")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
DOC_SUFFIXES = (".md", ".markdown", ".txt", ".rst", ".org", ".adoc")
ADR_NAME = re.compile(r"^(adr[-_]?)?(\d{3,4})[-_].*\.md$", re.I)
STD_ADR = re.compile(r"^adr-\d{3}-")
DECISION_DIRS = {"decisions", "adr", "adrs", "architecture-decisions", "decision-records"}
DECISION_LOG = re.compile(r"^(decisions?|adrs?|decision[-_]log)\.md$", re.I)
PLANNING_NAME = re.compile(r"sprint|roadmap|backlog|todo|milestone|remaining|plan", re.I)
PHASE_NAME = re.compile(r"implementation[-_ ]?plan|roadmap|phases?|milestones?", re.I)
QUARANTINE_NAME = re.compile(
    r"^(test[-_]?vehicles?|spikes?|sandbox(es)?|experiments?|playgrounds?|labs?|scratch|prototypes?)$", re.I)
AGENT_FILES = ("CLAUDE.md", "CLAUDE.local.md", "AGENTS.md", ".cursorrules", ".github/copilot-instructions.md")

# What init fills. A {{blank}} is the kit's; <angle brackets> and HTML comments in the two
# templates are the project's, filled each time a sprint or a list starts, and never reported.
BLANK = re.compile(r"\{\{([a-z][a-z-]*)\}\}")
BLOCK_OPEN = re.compile(r"^\s*<!-- kit:([a-z]+) -->\s*$")
BLOCK_CLOSE = re.compile(r"^\s*<!-- /kit:([a-z]+) -->\s*$")
LINE_OPTION = re.compile(r"\s*<!-- kit:([a-z]+) -->\s*$")
MARKER = re.compile(r"<!-- /?kit:([a-z]+) -->")
HELP = {
    "model": "the model a leg is sized for, the way plan.md should name it (--model)",
    "phase-doc": "the doc the phases are designed in (--phase-doc), or --no-phases",
    "phase-doc-name": "the phase doc's file name, as link text (--phase-doc fills it)",
    "phase-list": "one bullet per phase, each linking its heading in the phase doc",
    "quarantine": "the folder spikes are quarantined in (--quarantine)",
    "counter": "the execution-order number the next closed sprint takes (--counter-start)",
    "legacy-nnn": "the old sprints' execution-order range, e.g. 001-012 (--counter-start fills it)",
    "legacy-range": "what the old sprints are called, e.g. Sprints 1 through 12",
    "legacy-archive": "the file in completed/ the finished old sprints were moved into",
    "adoption-sprint": "the tag of the sprint that migrates this repo, e.g. [s-<id>]",
    "kit:phases": "phases undecided: keep what the markers wrap and delete the markers, or delete both",
}


class CantCheck(Exception):
    pass


def run(cmd, cwd, ok=(0,)):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError as e:
        raise CantCheck(f"`{' '.join(cmd)}` could not start: {e}")
    if r.returncode not in ok:
        raise CantCheck(f"`{' '.join(cmd)}` failed:\n{r.stderr.strip()}")
    return r


def git(cwd, *args, ok=(0,)):
    return run(["git", *args], cwd, ok)


def short(path):
    home, path = str(Path.home()), str(path)
    return "~" + path[len(home):] if path.startswith(home) else path


def plural(n, word):
    return f"{n} {word}" + "s" * (n != 1)


def repo_root(arg):
    start = Path(arg).expanduser() if arg else Path.cwd()
    if not start.is_dir():
        raise CantCheck(f"{start} is not a folder")
    root = Path(git(start, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if root == KIT:
        raise CantCheck("this is the kit's own repo. Run it from inside the repo you are setting up, "
                        "or pass --repo.")
    return root


def repo_name(root):
    """The repo's name on its remote, falling back to the folder's."""
    try:
        url = git(root, "remote", "get-url", "origin").stdout.strip()
    except CantCheck:
        return root.name
    name = re.split(r"[/:]", url.rstrip("/"))[-1]
    return name[:-4] if name.endswith(".git") else (name or root.name)


def repo_files(root):
    """Tracked and untracked files, with git's ignore rules applied."""
    out = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard").stdout
    return sorted({p for p in out.split("\0") if p and (root / p).is_file()})


def rel_path(arg, flag):
    """A repo-relative POSIX path from what someone typed, or a refusal."""
    p = PurePosixPath(arg.replace("\\", "/").strip("/"))
    if p.is_absolute() or ".." in p.parts or not p.parts:
        raise CantCheck(f"{flag} wants a path inside the repo, like docs/decisions (got {arg!r})")
    return p


def link(target, source):
    """Relative link from the file at `source` to `target`, both repo-relative POSIX paths."""
    t, s = PurePosixPath(target).parts, PurePosixPath(source).parent.parts
    i = 0
    while i < min(len(t), len(s)) and t[i] == s[i]:
        i += 1
    return "/".join([".."] * (len(s) - i) + list(t[i:])) or "."


# ---------------------------------------------------------------- suspects

def grep(root, pattern):
    """(path, line, text) for lines matching an extended regex, untracked files included."""
    out = git(root, "grep", "--untracked", "-I", "-n", "-z", "-E", "-e", pattern, ok=(0, 1)).stdout
    hits = []
    for rec in out.split("\n"):
        parts = rec.split("\0", 2)
        if len(parts) == 3 and parts[1].isdigit():
            hits.append((parts[0], int(parts[1]), parts[2].rstrip("\r")))
    return hits


def fenced(path):
    """Line numbers inside fenced code blocks, fences included."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
    except OSError:
        return set()
    inside, found = None, set()
    for n, line in enumerate(lines, 1):
        m = FENCE.match(line)
        if inside is None:
            if m:
                inside = m.group(1)
                found.add(n)
        else:
            found.add(n)
            if m and m.group(1)[0] == inside[0] and len(m.group(1)) >= len(inside):
                inside = None
    return found


def real(root, hits, rx):
    """The hits that are prose or code rather than quotation. Inline code spans, fenced blocks and
    lines carrying no-lint are skipped in docs: that is where counter-examples and example IDs
    live, and a tool that reads them as subjects rewrites the rules it quotes."""
    keep, fences = [], {}
    for path, n, text in hits:
        if "no-lint" in text:
            continue
        if path.lower().endswith(DOC_SUFFIXES):
            if path not in fences:
                fences[path] = fenced(root / path)
            if n in fences[path] or not rx.search(CODE_SPAN.sub("", text)):
                continue
        elif not rx.search(text):
            continue
        keep.append((path, n, text))
    return keep


def adr_records(folder):
    """(number, file name) for every file in a folder named like a numbered decision record."""
    if not folder.is_dir():
        return []
    return sorted((int(m.group(2)), p.name) for p in folder.iterdir()
                  if p.is_file() and (m := ADR_NAME.match(p.name)))


def decision_folders(files):
    found = {}
    for f in files:
        p = PurePosixPath(f)
        m = ADR_NAME.match(p.name)
        if m and (m.group(1) or p.parent.name.lower() in DECISION_DIRS):
            found.setdefault(p.parent.as_posix(), []).append((int(m.group(2)), p.name))
    return {d: sorted(v) for d, v in sorted(found.items())}


def listing(rows, limit, indent="    "):
    for path, n, text in rows[:limit] if limit else rows:
        text = " ".join(text.split())
        print(f"{indent}{path}:{n}  {text[:96] + '...' if len(text) > 99 else text}")
    if limit and len(rows) > limit:
        print(f"{indent}... and {len(rows) - limit} more (--all lists them)")


def cmd_scan(a):
    root = repo_root(a.repo)
    files = repo_files(root)
    have = set(files)
    limit = None if a.all else SHOW
    print(f"sprinter-kit scan of {short(root)}  (reads only; writes nothing)\n")

    adopted = "docs/sprints/plan.md" in have
    if adopted:
        print("set up already  docs/sprints/plan.md exists, so init will refuse to write.\n")

    folders = decision_folders(files)
    if folders:
        for d, recs in folders.items():
            nums = [n for n, _ in recs]
            odd = [name for _, name in recs if not STD_ADR.match(name)]
            w = max(len(ADR_NAME.match(name).group(2)) for _, name in recs)
            print(f"decisions      {d}/  {plural(len(recs), 'record')}, "
                  f"{min(nums):0{w}d}-{max(nums):0{w}d}, next free number {max(nums) + 1:0{w}d}")
            if odd:
                print(f"               named like {odd[0]}, not adr-NNN-name.md: init needs --adr-file")
            index = root / d / "README.md"
            if index.is_file():
                lines = index.read_text(encoding="utf-8", errors="replace").split("\n")
                for n, line in enumerate(lines, 1):
                    if re.search(r"reserved", line, re.I):
                        print(f"               {d}/README.md:{n} mentions a reservation: {line.strip()[:70]}")
        if "docs/decisions" not in folders:
            print("               init writes to docs/decisions/ unless you pass --decisions")
    else:
        print("decisions      none found. init writes docs/decisions/ with an index and a template.")
    logs = [f for f in files if DECISION_LOG.match(PurePosixPath(f).name)]
    for f in logs:
        print(f"               {f} looks like a decision log in one file")

    ours = ("docs/sprints/", "docs/reading/")
    phase = [f for f in files if f.lower().endswith(DOC_SUFFIXES) and not f.startswith(ours)
             and PHASE_NAME.search(PurePosixPath(f).name)]
    print(f"phase doc?     {', '.join(phase) if phase else 'none found. Phases are optional (--no-phases).'}")

    tops = sorted({f.split("/")[0] for f in files if "/" in f})
    spikes = [t + "/" for t in tops if QUARANTINE_NAME.match(t)]
    print(f"spike folder?  {', '.join(spikes) if spikes else 'none found. init defaults to test-vehicles/.'}")

    records = {(PurePosixPath(d) / name).as_posix() for d, recs in folders.items() for _, name in recs}
    plans = [f for f in files if f.lower().endswith(DOC_SUFFIXES) and not f.startswith(ours)
             and f not in records and PLANNING_NAME.search(PurePosixPath(f).name)]
    print(f"planning docs  {', '.join(plans) if plans else 'none found by name'}")

    agents = [f for f in AGENT_FILES if f in have] + sorted({f.split("/")[0] + "/" for f in files if f.startswith(".claude/")})
    if agents:
        print(f"agent files    {', '.join(agents)}. Setup writes nothing into these.")

    banned = real(root, grep(root, "TODO|FIXME|XXX|HACK"), BANNED)
    print(f"\nbanned words   {plural(len(banned), 'line')} in {plural(len({h[0] for h in banned}), 'file')}"
          + (":" if banned else ""))
    listing(banned, limit)

    numbered = real(root, grep(root, "[Ss]print[ _-]?[0-9]"), NUMBERED)
    print(f"sprint numbers {plural(len(numbered), 'line')} in {plural(len({h[0] for h in numbered}), 'file')}"
          + (":" if numbered else ""))
    listing(numbered, limit)

    tagged = grep(root, r"\[[sht]-[0-9a-f]{6}|SPRINT-[0-9a-f]{6}")
    tagged = [h for h in tagged if TAG.search(h[2])]
    if tagged:
        print(f"tags in use    {plural(len(tagged), 'line')} in {plural(len({h[0] for h in tagged}), 'file')}, "
              f"e.g. {tagged[0][0]}:{tagged[0][1]}")

    migrate = bool(plans or logs or banned or numbered)
    print()
    if adopted:
        print("This repo is set up already. Nothing for init to do.")
    elif migrate:
        print("Looks brownfield: there is a plan or tagged source to migrate. The mode is yours to pick.")
    else:
        print("Looks greenfield: nothing to migrate. The mode is yours to pick.")
    return 1 if adopted or migrate else 0


# ---------------------------------------------------------------- init

def apply_options(text, options):
    """Keep or drop the option blocks a template carries. On: the content stays and the markers go.
    Off: both go. Undecided: both stay, so the choice is visible and gets reported."""
    out, stack = [], []
    for line in text.split("\n"):
        opened, closed = BLOCK_OPEN.match(line), BLOCK_CLOSE.match(line)
        if opened or closed:
            if opened:
                stack.append(options.get(opened.group(1)))
                state, outer = stack[-1], stack[:-1]
            else:
                state, outer = (stack.pop() if stack else None), stack
            if state is None and False not in outer:
                out.append(line)
            continue
        if False in stack:
            continue
        m = LINE_OPTION.search(line)
        if m:
            state = options.get(m.group(1))
            if state is False:
                continue
            if state is True:
                line = line[:m.start()]
        out.append(line)
    return "\n".join(out)


def render(text, values, options, out):
    text = apply_options(text, options)

    def fill(m):
        v = values.get(m.group(1))
        v = v(out) if callable(v) else v
        return m.group(0) if v is None else v
    return BLANK.sub(fill, text)


def blanks(text):
    found = []
    for n, line in enumerate(text.split("\n"), 1):
        found += [(n, m.group(1)) for m in BLANK.finditer(line)]
        found += [(n, "kit:" + m.group(1)) for m in MARKER.finditer(line)]
    return found


def kit_version():
    """sprinter-kit@<sha>, so a repo's copy of the handbook can be diffed against the kit later."""
    try:
        if Path(git(KIT, "rev-parse", "--show-toplevel").stdout.strip()).resolve() != KIT:
            return "sprinter-kit"
        sha = git(KIT, "rev-parse", "--short", "HEAD").stdout.strip()
        dirty = git(KIT, "status", "--porcelain").stdout.strip()
    except CantCheck:
        return "sprinter-kit"
    return f"sprinter-kit@{sha}" + (" with local changes" if dirty else "")


def cmd_init(a):
    root = repo_root(a.repo)
    brown = a.brownfield
    if a.counter_start is not None and not brown:
        raise CantCheck("--counter-start is for --brownfield: a greenfield counter starts at 001")
    if a.adr is not None and a.adr_file:
        raise CantCheck("pass --adr or --adr-file, not both")
    try:
        date = datetime.date.fromisoformat(a.date).isoformat() if a.date else datetime.date.today().isoformat()
    except ValueError:
        raise CantCheck(f"--date wants YYYY-MM-DD (got {a.date!r})")

    decisions = rel_path(a.decisions, "--decisions")
    records = adr_records(root / decisions)
    fresh = not records and not (root / decisions / "README.md").exists()
    if a.adr_file:
        name = PurePosixPath(a.adr_file).name
        m = ADR_NAME.match(name)
        if not m:
            raise CantCheck("--adr-file wants a number up front and .md at the end, "
                            "like adr-004-planning-system.md or 0004-planning-system.md")
        digits = m.group(2)
    else:
        odd = [n for _, n in records if not STD_ADR.match(n)]
        if odd:
            raise CantCheck(f"records in {decisions}/ are named like {odd[0]}. "
                            "Pass --adr-file with a name that matches them.")
        num = a.adr if a.adr is not None else max([n for n, _ in records], default=0) + 1
        if not 1 <= num <= 999:
            raise CantCheck(f"--adr wants a number from 1 to 999 (got {num})")
        digits = f"{num:03d}"
        name = f"adr-{digits}-planning-system.md"
    taken = [n for k, n in records if k == int(digits)]
    if taken:
        raise CantCheck(f"ADR number {digits} is taken by {decisions}/{taken[0]}")
    adr_rel = (decisions / name).as_posix()

    writes, left = [], []
    for t in sorted(TEMPLATES.rglob("*")):
        if not t.is_file():
            continue
        rel = t.relative_to(TEMPLATES).as_posix()
        if rel.startswith("docs/decisions/"):
            leaf = rel[len("docs/decisions/"):]
            if leaf == "adr-NNN-planning-system.md":
                writes.append((t, adr_rel))
            elif fresh:
                writes.append((t, (decisions / leaf).as_posix()))
            else:
                left.append((decisions / leaf).as_posix())
        else:
            writes.append((t, rel))
    in_the_way = [out for _, out in writes if (root / out).exists()]
    if in_the_way:
        raise CantCheck("init writes nothing when a file is in the way, and these exist already:\n"
                        + "\n".join(f"  {p}" for p in in_the_way))

    phase_doc = rel_path(a.phase_doc, "--phase-doc").as_posix() if a.phase_doc else None
    options = {"greenfield": not brown, "brownfield": brown}
    if phase_doc:
        options["phases"] = True
    elif a.no_phases:
        options["phases"] = False
    start = a.counter_start
    values = {
        "adr": f"ADR-{digits}",
        "adr-num": digits,
        "adr-file": name,
        "adr-path": adr_rel,
        "adr-link": lambda out: link(adr_rel, out),
        "date": date,
        "kit": kit_version(),
        "project": repo_name(root),
        "model": a.model,
        "quarantine": rel_path(a.quarantine, "--quarantine").as_posix() + "/" if a.quarantine else None,
        "counter": f"{start:03d}" if start else None,
        "legacy-nnn": f"001–{start - 1:03d}" if start and start > 1 else None,
        "phase-doc": (lambda out: link(phase_doc, out)) if phase_doc else None,
        "phase-doc-name": PurePosixPath(phase_doc).name if phase_doc else None,
    }

    found = {}
    for t, out in writes:
        text = render(t.read_text(encoding="utf-8"), values, options, out)
        dest = root / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        for n, key in blanks(text):
            found.setdefault(key, []).append(f"{out}:{n}")

    mode = "--brownfield" if brown else "--greenfield"
    print(f"sprinter-kit init {mode} in {short(root)}")
    print(f"  {values['adr']}, adopted from {values['kit']}, dated {date}\n")
    print(f"Wrote {plural(len(writes), 'file')}:")
    for _, out in writes:
        print(f"  {out}")
    if left:
        print(f"\nNot written, because {decisions}/ already has records or an index of its own")
        print("(the kit's copies are in its templates/ folder, if you want them):")
        for p in left:
            print(f"  {p}")
        print("If the index is a table, the new record's row reads:")
        print(f"  | {digits} | [How Sprints Are Planned, Tracked and Closed]({name}) | Accepted | {date} |")
    if phase_doc and not (root / phase_doc).is_file():
        print(f"\n{phase_doc} does not exist yet, so the phase links point at nothing until it does.")
    if found:
        total = sum(len(v) for v in found.values())
        print(f"\n{plural(total, 'blank')} left for you to fill:")
        for key, where in found.items():
            print(f"  {key:<16} {HELP.get(key, '')}")
            for w in where:
                print(f"      {w}")
        print("\nWhen they are filled, this returns nothing:")
        print(f"  git grep --untracked -nE '\\{{\\{{[a-z-]+\\}}\\}}|<!-- /?kit:' -- {adr_rel} docs/sprints docs/reading")
    print("\nNothing is staged or committed.")
    return 1 if found else 0


# ---------------------------------------------------------------- id

def reads_as_number(s):
    """True for 123456 and for 4194e9, which a spreadsheet stores as 4.194 trillion."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def in_use(root, candidate, paths):
    """Anywhere in the repo, untracked files included: in a file's text, or in a file's name."""
    if any(candidate in p for p in paths):
        return True
    return git(root, "grep", "--untracked", "-I", "-q", "-F", "-e", candidate, ok=(0, 1)).returncode == 0


def cmd_id(a):
    root = repo_root(a.repo)
    if a.count < 1:
        raise CantCheck("--count wants 1 or more")
    paths = repo_files(root)
    ids = []
    while len(ids) < a.count:
        c = secrets.token_hex(3)
        if c == EXAMPLE_ID or reads_as_number(c) or c in ids or in_use(root, c, paths):
            continue
        ids.append(c)
    print("\n".join(ids))
    return 0


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except AttributeError:
            pass
    ap = argparse.ArgumentParser(prog="sprinter.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", metavar="command")
    sub.required = True
    repo_help = "the repo to work on (default: the one you are in)"

    s = sub.add_parser("scan", help="what is here to set up or migrate; writes nothing")
    s.add_argument("--repo", metavar="PATH", help=repo_help)
    s.add_argument("--all", action="store_true", help="list every suspect line, not the first few")

    i = sub.add_parser("init", help="write the planning files into the repo")
    mode = i.add_mutually_exclusive_group(required=True)
    mode.add_argument("--greenfield", action="store_true", help="nothing to migrate")
    mode.add_argument("--brownfield", action="store_true",
                      help="an old plan or tagged source to migrate; keeps the migration blanks")
    i.add_argument("--repo", metavar="PATH", help=repo_help)
    i.add_argument("--decisions", default="docs/decisions", metavar="DIR",
                   help="where the repo keeps its ADRs (default: %(default)s)")
    i.add_argument("--adr", type=int, metavar="N", help="the ADR number to take (default: the next free one)")
    i.add_argument("--adr-file", metavar="NAME", help="the record's file name, when the repo names records its own way")
    phases = i.add_mutually_exclusive_group()
    phases.add_argument("--phase-doc", metavar="PATH", help="the doc the phases are designed in, repo-relative")
    phases.add_argument("--no-phases", action="store_true", help="the project has no phases; drop them everywhere")
    i.add_argument("--quarantine", default="test-vehicles/", metavar="DIR",
                   help="the folder spikes are quarantined in (default: %(default)s)")
    i.add_argument("--model", metavar="TEXT",
                   help='the model a leg is sized for, the way plan.md should name it, e.g. "Claude Opus 5 Max Thinking"')
    i.add_argument("--counter-start", type=int, metavar="N",
                   help="brownfield: the execution-order number the next closed sprint takes, e.g. 13")
    i.add_argument("--date", metavar="YYYY-MM-DD", help="the adoption date (default: today)")

    d = sub.add_parser("id", help="fresh IDs, one per line, checked against the repo")
    d.add_argument("--repo", metavar="PATH", help=repo_help)
    d.add_argument("--count", type=int, default=1, metavar="N", help="how many (default: %(default)s)")

    a = ap.parse_args()
    return {"scan": cmd_scan, "init": cmd_init, "id": cmd_id}[a.cmd](a)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except CantCheck as e:
        print(f"sprinter: {e}", file=sys.stderr)
        sys.exit(2)
