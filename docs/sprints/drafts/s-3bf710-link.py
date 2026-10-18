#!/usr/bin/env python3
"""Make each of the kit's prompts a Claude Code slash command on this machine.

  python3 <kit>/docs/sprints/drafts/s-3bf710-link.py              write or refresh the commands
  python3 <kit>/docs/sprints/drafts/s-3bf710-link.py --dry-run    list what it would write

Each prompts/prompt*.md becomes ~/.claude/skills/sprinter-kit-<name>/SKILL.md: a pointer that
tells Claude to read the prompt from the kit. prompt5-code.md becomes /sprinter-kit-code. The
prompt's text is never copied, so editing a prompt in the kit changes its command too.

link writes only the pointers it wrote itself. A SKILL.md without its marker is left alone and
reported. A pointer whose prompt is gone is reported, never deleted. Nothing in any repo is
touched. Run it once per machine, and again when a prompt is added or renamed.

Exit status: 0 clean, 1 findings (a skill in the way, or a stale pointer), 2 couldn't check.

DRAFT for [s-3bf710]. Leg a moves CantCheck's twin, command_name, pointer and cmd_link into
scripts/sprinter.py as its link command, with KIT pointing at scripts/'s parent.
"""
import argparse
import re
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parents[3]  # drafts/ -> sprints/ -> docs/ -> the kit
PREFIX = "sprinter-kit-"
MARK = "<!-- written by sprinter-kit link: rerun link to refresh it, delete this folder to remove it -->"
STEM = re.compile(r"^prompt[^-]*-(.+)$")


class CantCheck(Exception):
    pass


def short(path):
    home, path = str(Path.home()), str(path)
    return "~" + path[len(home):] if path.startswith(home) else path


def command_name(stem):
    """prompt5-code -> sprinter-kit-code. A name without the promptN- prefix keeps its stem."""
    m = STEM.match(stem)
    return PREFIX + (m.group(1) if m else stem)


def pointer(cmd, prompt):
    return (
        "---\n"
        f"name: {cmd}\n"
        f"description: Runs sprinter-kit's {prompt.stem} prompt.\n"
        "disable-model-invocation: true\n"
        "---\n"
        "\n"
        f"Read {prompt} and follow it as your prompt for this session. An HTML comment at its "
        "top is a note about the file, not an instruction.\n"
        "\n"
        "What I typed after the command, if anything: $ARGUMENTS\n"
        "\n"
        f"{MARK}\n"
    )


def ours(skill_md):
    try:
        return MARK in skill_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False


def cmd_link(a):
    folder = KIT / "prompts"
    prompts = sorted(folder.glob("prompt*.md"))
    if not prompts:
        raise CantCheck(f"no prompt*.md in {short(folder)}")
    skills = Path(a.skills_dir).expanduser() if a.skills_dir else Path.home() / ".claude" / "skills"
    if skills.exists() and not skills.is_dir():
        raise CantCheck(f"{short(skills)} is not a folder")

    wanted = {}
    for p in prompts:
        cmd = command_name(p.stem)
        if cmd in wanted:
            raise CantCheck(f"{wanted[cmd].name} and {p.name} both make /{cmd}. Rename one.")
        wanted[cmd] = p

    verb = "would write" if a.dry_run else "wrote"
    done, blocked = [], []
    new_top = not skills.exists()
    for cmd, p in wanted.items():
        home = skills / cmd
        target = home / "SKILL.md"
        text = pointer(cmd, p.resolve())
        if home.is_symlink() or (home.exists() and not home.is_dir()):
            blocked.append((cmd, f"{short(home)} is not a folder link made"))
            continue
        if target.exists():
            if not ours(target):
                blocked.append((cmd, f"{short(target)} has no link marker, so it isn't link's to change"))
                continue
            if target.read_text(encoding="utf-8", errors="replace") == text:
                done.append((cmd, "already current"))
                continue
            state = "would refresh" if a.dry_run else "refreshed"
        elif home.exists() and any(home.iterdir()):
            blocked.append((cmd, f"{short(home)} holds files link didn't write"))
            continue
        else:
            state = verb
        if not a.dry_run:
            home.mkdir(parents=True, exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
        done.append((cmd, state))

    stale = []
    if skills.is_dir():
        for d in sorted(skills.iterdir()):
            if (d.name.startswith(PREFIX) and d.name not in wanted and d.is_dir()
                    and ours(d / "SKILL.md")):
                stale.append(d.name)

    width = max(len(c) for c in list(wanted) + stale) + 2
    print(f"Commands in {short(skills)}, from {short(folder)}:")
    for cmd, state in done:
        print(f"    /{cmd:<{width}}{state}")
    if blocked:
        print("Left alone, because link didn't write them:")
        for cmd, why in blocked:
            print(f"    /{cmd:<{width}}{why}")
    if stale:
        print("Stale, because their prompt is gone (delete the folder to remove one):")
        for cmd in stale:
            print(f"    /{cmd:<{width}}{short(skills / cmd)}")
    if new_top and not a.dry_run:
        print(f"Created {short(skills)}. A Claude Code session that was already open needs "
              "/reload-skills once.")
    return 1 if blocked or stale else 0


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except AttributeError:
            pass
    ap = argparse.ArgumentParser(prog="link", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="list what it would write; write nothing")
    ap.add_argument("--skills-dir", metavar="PATH",
                    help="where Claude Code reads personal skills (default: ~/.claude/skills)")
    return cmd_link(ap.parse_args())


if __name__ == "__main__":
    try:
        sys.exit(main())
    except CantCheck as e:
        print(f"link: {e}", file=sys.stderr)
        sys.exit(2)
