# sprinter-kit

A sprint planning system for building software with AI agents. 
With documented processes that turn judgement into a shared proceedure.

Sprints are named by hex IDs that
never move, each sprint is one file, each leg fits one sitting, and every coding session gets a
reading list.

Humans and agents read the same specs for how code, tests, reviews and docs are done, so quality comes from the process, not from the model of the month. In DoE vocabulary, this robust design:
- The model is a noise factor. You don't control its version, its sampling, or what changes next month.
- The spec, sizing rules, review format and checks are control factors. You own them, so that's where the effort goes.
- The result is output that stays good across model changes, instead of output you hope for.

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
repo as your own ADR, and your repo edits its copy from then on. init also writes
`docs/ESSAY.md` and `docs/field-guide.md` where your repo has none, and leaves your own alone.
Both are yours to write: the essay is the argument your project makes, and the field guide holds
the domain terms a reviewer may not know.

## Use it

Clone the kit once, beside your projects, and never inside one
([design.md](design.md#one-clone-beside-the-projects) has the tested reasons). Then open an agent
session in the repo you are setting up, give it the kit's folder (in Claude Code,
`claude --add-dir ~/repos/sprinter-kit`), and hand it the prompt:

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

## Changing the kit

Expect the kit to change as projects use it. Capture those changes while you work on a project,
and decide them at a kit review. Never do both in one sitting.

**While you work on a project**

| You hit | Do this, then get back to work | Tracked in |
|---------|--------------------------------|------------|
| A rule or template that's wrong for this project | Edit the project's copy in place | the project |
| A helper script this project needs | Write it in the project's own `scripts/` | the project |
| Something the kit might want, that helper included | Add `[h-<id>] kit: <what and why>` to the project's `housekeeping.md` | the project |
| A kit bug that blocks you | Fix it here, commit it on its own, and describe it in generic terms | the kit |

Capture ideas in the project, never in this repo's issues. The kit is public, and some projects
are private.

**The kit review.** Hold one before you set up the next project, since that project benefits
first.

1. Collect the `kit:` lines from every project:
   ```
   grep -n '] kit:' ~/repos/*/docs/sprints/housekeeping.md
   ```
2. In each project, list what it changed in its copies since adopting the kit:
   ```
   init=$(git log --diff-filter=A --format=%h -- docs/sprints/plan.md)
   git diff $init -- 'docs/decisions/*planning-system.md' docs/sprints/sprint-template.md docs/reading/reading-list-template.txt
   ```
3. Decide each item:
   - **Promote** it when a second project wants it, or when it fixes something wrong for
     everyone.
   - **Keep it local** when it's specific to one project's domain, stack or people.
   - **Drop** it when it worked around something that has since been fixed.
4. Rewrite each promoted change into the kit in generic terms. Never cherry-pick a commit from a
   private project.
5. Clear each decided `kit:` line. Delete it, or drop the `kit:` prefix when it stays as work for
   that project.
6. Tag the kit: `git tag v0.2 && git push --tags` after the first review, `v0.3` after the next.

**Bringing a kit change into an older project.** Diff the kit from the project's stamp (the
version in its handbook's Status line) to the new tag:

```
git -C ~/repos/sprinter-kit diff <stamp>..v0.2 -- templates/
```

Apply what you want by hand, then update the stamp to the tag. Do this by hand a few times before
scripting it.

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
