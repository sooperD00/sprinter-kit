# Design

Why sprinter-kit is shaped the way it is. The formats are in
[interface-spec.md](interface-spec.md); this file holds the arguments, and it should change far
less often.

## Rules travel, machinery stays

- init copies the handbook into every repo as that repo's own ADR. A rule kept somewhere else is
  a rule nobody can find, and a coding session reads the repo, not the kit.
- The scripts, the templates and the setup prompt stay here. A fix lands once.
- After init, a repo needs nothing from the kit. The handbook says how to make an ID with
  `openssl` for the day the kit is not on the machine.
- Each repo edits its copy in place, the way a process handbook is meant to be edited. Copies
  drift on purpose. The Status line records the kit commit each copy came from, so the drift is
  one diff away.

## A script where the handbook gives an exact form, an agent where it says decide

| step | who | why |
|------|-----|-----|
| IDs | script | Randomness is a script's job. A model asked for hex hands back something patterned, and nothing makes it run the `git grep`. |
| folders, templates, the next free ADR number | script | The handbook gives the exact form. |
| suspects: banned words, sprint numbers, old plans | script | Printed, never judged. No regex can tell a sprint number from a test count. |
| splitting an old plan, retagging comments | agent | application-pipeline's source leg found that the sed everyone pictured was never the work. Deciding where each comment belonged was. |
| phases, the spike folder, the model line | agent proposes, person confirms | Needs reading the project, and a wrong guess is inherited by every sprint. |
| closing a sprint | the maintainer | The handbook reserves it. |

## No CLAUDE.md in the target repo

- The handbook's "Session guards" paragraph says a session's guards arrive with the prompt it is
  handed, never from the repo. A CLAUDE.md loads into every session automatically, which makes
  it the one file that paragraph rules out.
- It would also punch through the reading lists. A coding session reads what its list names and
  asks before opening anything else. A file that loads itself is not on the list.
- A CLAUDE.md in the kit would be harmless, but SKILL.md does that job and is handed over on
  purpose.

## Thin on purpose

- One project has run this system. A generator built after one example encodes the shape of one
  example. application-pipeline's `readinglist.sh` found this out four times before it worked out
  that its own default was inverted.
- So the kit ships scan, init and id, and nothing that plans, closes or lints. Those come after
  the second project, from lists and closes written by hand.
- What actually travels between projects is prompts, not templates. The kit is small enough to
  travel the same way.

## Templates mirror the target tree

- `templates/` is laid out the way the files land, so what init will write is visible before it
  runs, and init is a copy plus a fill.
- `{{blanks}}` belong to the kit. The placeholder prose in the sprint template and the angle
  brackets in the reading-list template belong to the project, and get filled every time a
  sprint or a list starts. init reports only the first kind.
- init adds files and never edits one. Anything in the way stops it before it writes. A file
  whose format drifted is a thing to read, not to repair silently.

## IDs

- `openssl rand -hex 3` is a real random source. The rerolls are what make it a rule.
- Rerolling all-digit IDs keeps an ID from reading as a number. `4194e9` reads as one too:
  4.194 trillion to a spreadsheet, a JSON parser or YAML 1.2. The kit rerolls anything Python's
  `float()` accepts, which covers both.
- The in-use check is `git grep --untracked`. A migration writes dozens of sprint files before
  anything is added, and a plain `git grep` cannot see them.

## License

- Business Source License 1.1, the same license and the same Change Date as
  application-pipeline. The handbook's text came from there, and it opens up under Apache 2.0 on
  2029-03-01 either way.
- The grant lets anyone use the kit to plan and run their own projects, for an employer or a
  client included. It keeps one thing back: selling the kit itself as a template, course, plugin
  or hosted tool.
- MIT is the alternative if spreading the method matters more than keeping the kit sellable.

## What changed on the way out of application-pipeline

The handbook is ADR-021 from application-pipeline at `8185187`, changed only here:

1. The number, date and status became blanks. The status records the kit commit.
2. Phases became an option: the Phase row and its Why bullet go when a project has none.
3. The spike folder became a blank, defaulting to `test-vehicles/`.
4. The layout gained `sprint-template.md` and `reading-list-template.txt`, and a line saying they
   are starting points, never records.
5. The Phase 0 archive and "Sprints 1 through 12" became brownfield-only blanks.
6. IDs: "reads as a number" covers `4194e9`, and the in-use check is `git grep --untracked`.
7. "Two kinds of prompt" lost its application-specific half. "Public" became "live here", since a
   private repo's plan is not public.
8. Consequences point the tooling at the kit. Alternatives name application-pipeline as where the
   117 edits happened, instead of claiming the system replaced something in every repo.
9. The Migration section became a pointer to the repo's own adoption sprint. Its steps are
   SKILL.md's brownfield path now.

Item 6 is worth carrying back to application-pipeline's ADR-021 by hand. Its tech debt already
holds `[t-4194e9]`.
