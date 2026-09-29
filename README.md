# sprinter-kit

A sprint planning system for building software with AI agents. Sprints are named by hex IDs that
never move, each sprint is one file, each leg fits one sitting, and every coding session gets a
reading list.

On 2026-09-19, inserting one sprint into application-pipeline's plan cost 117 edits across four
documents. The sprints were numbered by their order, so everything behind the new one had to be
renumbered, and no regex could tell a sprint number from a test count. I rebuilt the plan the
next day around IDs that mean nothing, so the order lives in exactly one table and moving a
sprint costs one line. This kit is that system, pulled out so the next repo starts with it.

## What's in it

```
SKILL.md              the setup prompt: hand it to an agent in the repo you are setting up
scripts/sprinter.py   scan, init and id (stdlib Python, nothing to install)
templates/            what init writes, laid out the way it lands in your repo
examples/             a live plan, a closed sprint and a reading list, from application-pipeline
interface-spec.md     the formats: IDs, tags, file names, headings, who reads what
design.md             why the kit is shaped this way
```

The handbook is `templates/docs/decisions/adr-NNN-planning-system.md`. init copies it into your
repo as your own ADR, and your repo edits its copy from then on.

## Use it

Clone the kit anywhere. Then open an agent session in the repo you are setting up, and hand it
the prompt:

```
Read ~/repos/sprinter-kit/SKILL.md and set this repo up.
```

Or run it by hand, from inside that repo:

```
python3 ~/repos/sprinter-kit/scripts/sprinter.py scan
python3 ~/repos/sprinter-kit/scripts/sprinter.py init --greenfield --no-phases --model "Claude Opus 5 Max Thinking"
python3 ~/repos/sprinter-kit/scripts/sprinter.py id --count 3
```

(Windows Git Bash says `python`, not `python3`. Every command exits 0 clean, 1 with findings, and
2 when it couldn't check. `--help` on each one has the rest.)

After setup the repo stands on its own. The handbook says how to make an ID with `openssl` on a
machine without the kit.

To run it as a Claude Code skill, link the folder in. It is already shaped like one:

```
ln -s ~/repos/sprinter-kit ~/.claude/skills/sprinter-kit
```

## What it does not do

- Write a CLAUDE.md. Session guards arrive with each session's prompt, never from a file every
  session loads on its own.
- Plan your sprints. It builds the place they live.
- Commit. You review, you commit.

## Later ++

- **Plugin.** Once a second project has run on the kit, wrap it as a Claude Code plugin:
  `/sprint-new`, `/leg-handoff` and `/sprint-close` as commands, and the linter as a hook. Same
  folder, commands on top.
- **The scripts application-pipeline's developer tooling sprint specs:** a linter, a sprint
  closer, and a reading-list drafter. They belong here, so a fix lands once. Write three reading
  lists by hand before building the drafter. A generator built after one list encodes the shape
  of one list.

## License

Business Source License 1.1, the same as application-pipeline. Use it to plan and run your own
projects, for an employer or a client included. Don't sell the kit itself. It converts to Apache
2.0 on 2029-03-01. The details are in [LICENSE](LICENSE).
