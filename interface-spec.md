# Interface spec

The formats sprinter-kit writes and its scripts parse. The handbook
(`templates/docs/decisions/adr-NNN-planning-system.md`) is the rule. Where this file and the
handbook disagree, the handbook wins and this file is the bug. The arguments behind all of it
are in [design.md](design.md).

## IDs

| rule | value |
|------|-------|
| shape | `^[0-9a-f]{6}$`, lowercase |
| never | anything that reads as a number (Python's `float()` accepts it: `123456`, `4194e9`) |
| never | `9cf8b9`, the example every document uses |
| never | anything already in the repo, untracked files included: in a file's text (`git grep --untracked -F <id>`) or in a file's name |
| from | `sprinter.py id`, or `openssl rand -hex 3` plus the three checks above by hand |

An ID is identity. It is never reused, never renumbered, and never means order.

## Tags

| tag | where it goes | regex |
|-----|---------------|-------|
| `[s-<id>]` | any doc | `\[s-([0-9a-f]{6})\]` |
| `[s-<id>-<leg>]` | any doc | `\[s-([0-9a-f]{6})-([a-z])\]` |
| `leg <x>` | inside that sprint's own file | `\bleg ([a-z])\b` |
| `[h-<id>]` | any doc, and source where the location is the information | `\[h-([0-9a-f]{6})\]` |
| `[t-<id>]` | same | `\[t-([0-9a-f]{6})\]` |
| `[SPRINT-<id>-CLEANUP]`, `[SPRINT-<id>-<leg>-CLEANUP]` | source only | `\[SPRINT-([0-9a-f]{6})(?:-([a-z]))?-CLEANUP\]` |
| `ADR-<NNN>` | anywhere, for why code is the way it is | `\bADR-(\d{3,4})\b` |

Banned in source: `\b(TODO|FIXME|XXX|HACK)\b`, case-sensitive.

Every checker is blind to three places, because that is where counter-examples and the example ID
live:

- inline code spans (`` `like this` ``)
- fenced code blocks
- any line carrying `no-lint` (`<!-- no-lint -->` in Markdown, `# no-lint` in source)

Excluding a whole file is the wrong fix. An exclusion that outlives its reason exempts everything
added to the file later.

## Files

| file | pattern |
|------|---------|
| planned sprint | `docs/sprints/remaining/sprint-<id>-<short-name>.md` |
| finished sprint | `docs/sprints/completed/sprint-<NNN>-<id>-<short-name>.md` |
| short name | `[a-z0-9]+(-[a-z0-9]+)*` |
| `<NNN>` | three digits, the order sprints actually finished in, from 001 |
| reading list | `docs/reading/reading-list-for-<id>-<leg>.txt` |
| close tag | `sprint-<NNN>-<id>` |
| the handbook | `<decisions>/adr-<NNN>-planning-system.md` |
| ADR template | `<decisions>/adr-000-adr-template.md` |

Not sprints and not lists, so checkers skip them: `docs/sprints/sprint-template.md`,
`docs/reading/reading-list-template.txt`, and dotfiles (`.gitkeep` holds `remaining/` and
`completed/` in git while they are empty, so the first `git mv` has somewhere to land).

## Sprint file

```
# <title: the category of work>

**ID**: `[s-<id>]`
**Status**: <status>
**Phase**: <phase>                only when the project has phases
**Handoff**: <YYYY-MM-DD>         added at sprint handoff
```

Then one or two sentences on the change, and these labels, each optional and in this order:
`**Kind:**`, `**Legs:**`, `**Entry gate:**`, `**Why now**`. Sprints also carry `**Decision**`,
`**Decides: <topic>**` and `**Reference**` blocks when they need them.

Leg heading:

```
## leg <x> — <what the leg does> (<kind>) --- <status>
```

Regex: `^## leg ([a-z]) — (.+) \(([^()]+)\) --- (.+)$`. Legs are `##`. (application-pipeline's
sprint-013 used `###`; every other file uses `##`, and `##` is the format.)

Under a leg, in order: `**Done when**`, `**Commits**`, `**Watch**`, and `**Landed.**` once it is
handed off. A leg may add prework blocks (`**Prework (<when>)**`) above Done when.

- **Commits** is a table: `| # | | |`, one row per commit, `0` for an artifact that is not a
  commit.
- **Out of Scope** is a closing `##` section, one line per item: `- <item> → <destination>`.
  The destination is a tag, an ID, or a named milestone.
- **Handoff** is a closing `## Handoff, YYYY-MM-DD` section when the sprint hands off.

## Status

| value | sprint | leg |
|-------|--------|-----|
| `planned` | yes | yes |
| `in progress` | yes | yes |
| `handed off YYYY-MM-DD` | yes | yes |
| `done YYYY-MM-DD` | yes | yes |
| `dropped`, then the reason | yes | yes |
| `parked` (no place in the order yet) | yes | no |

## Checklist marks

| mark | means | the line must also say |
|------|-------|------------------------|
| `[x]` | done as written | |
| `[ ]` | open | |
| `[-]` | skipped here and deferred | *deferred to <place>* and why |
| `[~]` | rejected | *not done because* and why |

A deferral to `housekeeping.md` or `techdebt.md` takes an ID there.

## plan.md

- `LLM MODEL = <model>`, one line.
- `## Phases`, a bullet per phase linking the phase doc, only when the project has phases.
- `## Order`, one table: `NNN | id | name | status | depends on | reading list`.
  - `NNN` is blank until the sprint closes.
  - `id` is `` `[s-<id>]` ``.
  - `name` links the sprint file, with `**ASAP** ` in front of the link when a clock is running.
  - `depends on` holds required gates only, as tags, or `—`.
  - `reading list` is `[leg <x>](../reading/reading-list-for-<id>-<x>.txt), YYYY-MM-DD`, or `—`.
- `## Completed`, one table: `NNN | id | name | handoff`.
- A counter line under it: `The counter continues at <NNN>.` (a fresh repo says `starts at 001`).

## housekeeping.md and techdebt.md

```
- [ ] [h-<id>] What the work is, why it waits, and where it would land.
      (From [s-<id>]'s Out of Scope, YYYY-MM-DD.)
```

Provenance lines seen so far: `From [s-<id>]'s Out of Scope`, `Filed from <where> by
[s-<id>-<leg>]`, `Pulled from Housekeeping`, `Moved out of [s-<id>]`, `Found in <review>`. The date
travels with the item every time it moves.

## Who reads what

The handbook is long so that each session can read only its part. These are the sections each
kind of session needs.

| session | reads in the handbook | leaves behind |
|---------|-----------------------|---------------|
| setup | all of it | the files, blanks filled, for review |
| planning | Vocabulary, Where things live, IDs and file names, Referring to a sprint, Tags in source, Plan a sprint, Reading lists, Order and re-order, Housekeeping and tech debt | the sprint file, its `plan.md` row, the next leg's reading list |
| coding (one leg) | Vocabulary with its Landed, Checklist marks and Entry gate paragraphs; Referring to a sprint; Tags in source; Reading lists; Run a sprint; Hand off a leg; Housekeeping and tech debt, plus the ID rule | the leg handed off |
| closing (maintainer) | Hand off a sprint, Close a sprint, Three clocks, Order and re-order | the `git mv`, the log row, the tag |

The coding row is the default READ THIS block in `reading-list-template.txt`. It comes from
application-pipeline's first reading list, `examples/reading-list-for-a75ff1-b.txt`.

## Kit blanks

Templates carry two kinds of blank. init fills or reports the first kind and never touches the
second.

| kind | looks like | whose |
|------|------------|-------|
| kit blank | `{{name}}` | the kit's: filled by init, or listed with a line number for you to fill |
| option | `<!-- kit:<option> -->` … `<!-- /kit:<option> -->` around lines, or at the end of one line | the kit's: kept when the option is on, dropped when off, left in place when undecided |
| per-use blank | HTML comments and placeholder prose in `sprint-template.md`; `<angle brackets>` in `reading-list-template.txt` | the project's, filled each time a sprint or a list starts |

Options: `greenfield`, `brownfield` (always decided, by the mode), and `phases` (on with
`--phase-doc`, off with `--no-phases`, otherwise undecided).

| blank | filled from |
|-------|-------------|
| `{{adr}}`, `{{adr-num}}`, `{{adr-file}}`, `{{adr-path}}`, `{{adr-link}}` | the next free ADR number, `--adr` or `--adr-file` |
| `{{date}}` | today, or `--date` |
| `{{kit}}` | `sprinter-kit@<short sha>` of the kit clone that ran init |
| `{{project}}` | the origin remote's repo name, or the folder's |
| `{{model}}` | `--model` |
| `{{quarantine}}` | `--quarantine`, default `test-vehicles/` |
| `{{phase-doc}}`, `{{phase-doc-name}}` | `--phase-doc` |
| `{{phase-list}}` | you: one bullet per phase |
| `{{counter}}`, `{{legacy-nnn}}` | `--counter-start` (brownfield) |
| `{{legacy-range}}`, `{{legacy-archive}}`, `{{adoption-sprint}}` | you, during the migration (brownfield) |

## sprinter.py

Stdlib-only Python 3.8 or later, run from anywhere inside the target repo (or `--repo PATH`).
It writes LF and UTF-8 on every platform.

| command | does | exit |
|---------|------|------|
| `scan [--all]` | prints what there is to set up or migrate; writes nothing | 0 nothing to migrate, 1 findings, 2 couldn't check |
| `init --greenfield` or `--brownfield`, plus options | copies `templates/` into the repo and fills blanks | 0 no blanks left, 1 blanks listed, 2 stopped before writing |
| `id [--count N]` | prints fresh IDs on stdout, one per line | 0, or 2 couldn't check |

init options: `--decisions DIR` (default `docs/decisions`), `--adr N`, `--adr-file NAME`,
`--phase-doc PATH` or `--no-phases`, `--quarantine DIR`, `--model TEXT`, `--counter-start N`
(brownfield only, 1 to 999), `--date YYYY-MM-DD`. A path may be repo-relative, or absolute when
it points inside the repo. A path outside the repo is refused.

init copies every file under `templates/` except the junk an OS or editor leaves behind
(`.DS_Store`, `Thumbs.db`, swap files, any dotfile but `.gitkeep`).

init stops before writing anything when a file it would write already exists, when the ADR number
is taken, or when the repo names its records some other way and `--adr-file` is missing. When the
decisions folder already has records or an index, init leaves `README.md` and
`adr-000-adr-template.md` alone and prints the index row to add.
