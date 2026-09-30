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

## One clone, beside the projects

The kit lives in one clone next to the projects that use it. Each way of putting it inside a
project failed when tried on scratch repos on 2026-09-30:

| Layout | What happened |
|--------|---------------|
| A clone nested in the project | `git add -A` committed it as a bare commit pointer, and a fresh clone of the project got none of the kit. |
| A submodule | A plain clone got none of the kit. A `--recurse-submodules` clone landed on a detached HEAD, where a quick fix is easy to lose. Every kit update costs a pointer commit in every project. |
| A plain copy (a `git subtree` lands the same files) | The kit's own files became the project's scan suspects: 12 lines, from the old sprint numbers in the examples and the banned-word pattern in the script. A brand-new project scanned as brownfield. |

- A copy inside the project promises edits that travel with it. The project already has those.
  init copied the rules in, and the stamp in the handbook's Status line is the baseline for a
  diff against the kit.
- Reading the kit off github.com fails for a different reason. An agent's web fetch returns a
  small model's answer about the page, not the file, and the script can't run from a page.
- An agent in a project session needs permission to edit a clone outside the project. The kit
  then changes only when someone decides to change it.
- The capture step lives in the project because the kit is public and some projects are private.
  A promoted change gets rewritten in generic terms for the same reason.
- Promotion waits for a second project, for the reason in Thin on purpose: a generator built
  after one example encodes the shape of one example. (The general form is the rule of three,
  Don Roberts' via Fowler's *Refactoring*: do it once, wince the second time, refactor the
  third.)

The layout gets revisited the day the kit ships a linter. A newer linter can fail a project whose
handbook is older, so linters get pinned per project, the way a pre-commit hook pins its `rev:`.
That is the time to package the kit.

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
2. Phases became an option: the Phase row and its Why bullet go when a project has none. The Phase
   row's link to `implementation-plan.md` became the phase-doc blanks.
3. The spike folder became a blank, defaulting to `test-vehicles/`.
4. The layout gained `sprint-template.md` and `reading-list-template.txt`, and a line saying they
   are starting points, never records. The Reading lists section says to start from the template.
5. The Phase 0 archive and "Sprints 1 through 12" became brownfield-only blanks.
6. IDs: "reads as a number" covers `4194e9`, the in-use check is `git grep --untracked`, and the
   first ID step points at `sprinter.py id`.
7. "Two kinds of prompt" lost its application-specific half. "Public" became "live here", since a
   private repo's plan is not public. `<this-repo-name>-devlog` became the devlog blank.
8. Consequences point the tooling at the kit. Both Alternatives that quote figures name
   application-pipeline as where they happened (117 edits, 1,180 lines), instead of claiming them
   for every repo.
9. The Migration section became a pointer to the repo's own adoption sprint. Its steps are
   SKILL.md's brownfield path now.
10. Housekeeping's provenance example lost its "today", which was true only in
    application-pipeline.
11. Housekeeping and tech debt gained a last bullet: a change to the planning system itself goes
    in as a `kit:` item, for the kit review to collect.

Item 6 is worth carrying back to application-pipeline's ADR-021 by hand. Its tech debt already
holds `[t-4194e9]`.
