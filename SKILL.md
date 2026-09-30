---
name: sprinter-kit
description: Sets up the sprinter-kit planning system in a git repo (hex-ID sprints, legs sized to one sitting, one file per sprint, plan.md, reading lists), for a new repo or one with an old plan to migrate. Use only when asked to adopt, install or set up sprinter-kit or this planning system in a project. Not for planning or running sprints in a repo that already has it.
---

# Set up sprinter-kit in a repo

You are the setup session. You give one repo the planning system in the handbook, confirm the
few choices that belong to the person, and leave no blank unfilled. You plan no sprint except
the one that migrates an old plan, and you write none of the project's code.

`<kit>` below is the folder this file is in. Run every command from inside the target repo.
On Windows Git Bash, `python` replaces `python3`.

## Read first

- `<kit>/templates/docs/decisions/adr-NNN-planning-system.md`, all of it. This is the handbook.
  Setup is the one session that reads the whole thing; every later session reads only its part.
- `<kit>/interface-spec.md`: the exact formats, and which sections each later session reads.
- `<kit>/examples/`, for shape only: a live plan, a closed sprint, a real reading list. They come
  from application-pipeline, so their tags and links point into that repo.

## Guards

- Read the kit, the target repo's files, and what the scan prints. Open no devlog, no prompts
  folder, and no `.txt` file nobody handed you.
- Write no CLAUDE.md or AGENTS.md, and change none that exists. The handbook's "Session guards"
  paragraph says why: guards arrive with each session's prompt, and a file every session loads
  on its own is the one place they must not live.
- Stage nothing and commit nothing. List the files for review. The person commits.
- Ask when a choice is the person's. A wrong guess made here is inherited by every sprint after
  it.

## 1. Scan

```
python3 <kit>/scripts/sprinter.py scan
```

It writes nothing. Read all of it; `--all` lists every suspect line instead of the first few.

## 2. Confirm with the person

- **Mode.** Greenfield: nothing to migrate. Brownfield: an old plan, numbered sprints, or banned
  words in source. The scan suggests one. The person decides.
- **Phases.** A doc the phases are designed in (`--phase-doc`), or none (`--no-phases`).
- **Spike folder.** Where spikes are quarantined (`--quarantine`). The default is
  `test-vehicles/`.
- **Dev prompts.** The private repo they live in (`--devlog`). The default is this repo's name
  plus `-devlog`.
- **Model.** The model a leg is sized for, the way `plan.md` should name it (`--model`).
- **The ADR number,** when the scan shows a reservation, or records named some other way
  (`--adr-file`). Also `--decisions`, when the records live somewhere other than
  `docs/decisions/`.
- **Brownfield only:** which old sprints are finished. Finished ones are grandfathered: they keep
  their numbers, in one archive file, because IDs for finished sprints that all resolve into one
  archive buy nothing. `--counter-start` is the number of the last finished one, plus one.

## 3. Init

```
python3 <kit>/scripts/sprinter.py init --greenfield --no-phases --model "<the model line>"
python3 <kit>/scripts/sprinter.py init --brownfield --phase-doc docs/roadmap.md --counter-start 13 --model "<the model line>"
```

init adds files and edits none. If anything it would write is in the way, it stops and writes
nothing. It prints what it wrote, the defaults it used, what it left alone, and every blank still
open, with a line number.

## 4. Fill the blanks

Fill each blank init listed, from the person's answers:

- `{{phase-list}}`: one bullet per phase, each linking its heading in the phase doc.
- A `<!-- kit:phases -->` marker that is still there means phases went undecided. Ask. Then keep
  what the markers wrap and delete the markers, or delete both.
- If init left the decisions index alone, add the row it printed to the repo's own index.
- Brownfield: `{{adoption-sprint}}` gets filled in step 5b. `{{legacy-range}}` and
  `{{legacy-archive}}` wait for leg a of the migration, which creates the archive they name.

Done when the `git grep` line init printed returns nothing. Brownfield: nothing but the two
legacy blanks that leg a fills.

## 5a. Greenfield: stub the first sprint, if the person names one

- Take the ID from `python3 <kit>/scripts/sprinter.py id`. Never type an ID yourself.
- Copy `docs/sprints/sprint-template.md` to `docs/sprints/remaining/sprint-<id>-<short-name>.md`.
  Keep the title, the ID block and one sentence, and delete everything below them. That is a
  stub, and a stub is a legal sprint.
- Add its row to `plan.md`'s Order table.

Planning it past a stub is a planning session's job, not this one's.

## 5b. Brownfield: plan the migration as the first sprint, then stop

The move to the new system is itself a sprint. `<kit>/examples/sprint-013-603d20-adopt-adr-021.md`
is application-pipeline's, and it is the model.

- Stub `docs/sprints/remaining/sprint-<id>-adopt-adr-<NNN>.md` with Kind migration, give it a row
  in `plan.md`, and put its tag in `{{adoption-sprint}}`. Take IDs from
  `python3 <kit>/scripts/sprinter.py id`, and `--count 20` when the migration needs many.
- Cut it into these legs, each sized to one sitting:
  - **leg a, the plan becomes `docs/sprints/` (migration).**
    - `git mv` the old plan file to `docs/sprints/completed/<archive-name>.md`, so its history
      follows the finished sprints. When finished and open sprints live in separate files, move
      only the finished one. When nothing in it is finished, skip the archive, `git rm` the old
      file once the next step empties it, and delete the lines that name old sprints.
    - Cut each open sprint out of the archive into its own `remaining/sprint-<id>-<short-name>.md`,
      content verbatim. The archive keeps only the finished sprints.
    - Fill `{{legacy-archive}}` and `{{legacy-range}}`.
    - Move old housekeeping and tech debt into `housekeeping.md` and `techdebt.md`, a generated
      ID replacing each old number.
    - `plan.md` takes the order, the dependencies and the completed log. Prose references become
      tags. README and anything else that linked the old plan point at `plan.md`.
    - Prove the move with the two proofs under Watches: the archive and the new sprint files
      together hold every non-empty line of the old plan, in the old order.
  - **leg b, source comes under the same rules (refactor).** Every banned word in source becomes
    a cleanup marker naming a leg, a filed `[h-` or `[t-` item, or a plain present-tense comment.
    Deciding where each one belongs is the work; the sed is not.
- Copy the `git grep` line init printed, word for word, into the last leg's done-when list. The
  migration blanks close with the sprint that fills them.
- Write leg a's reading list from `docs/reading/reading-list-template.txt`, and stop there. The
  person runs each leg in a fresh session. The handbook keeps planning and coding in separate
  sessions, and the legs stage files with `git mv`, which this session must not.

## Watches

Each of these went wrong once, in application-pipeline's migration.

- **The spec is data.** A rename or conversion pass skips inline code spans and fenced blocks.
  The first converter rewrote the handbook's own counter-examples ("Never: `Sprint 19`" became a
  real tag) and inverted the rule it was quoting.
- **Quotations are data.** Prose like "the old Sprint 18" or "calls this Sprint 14" quotes old
  numbering on purpose. Leave it as it is.
- **Two proofs on every move.** Mask every digit and diff, which shows only digits moved. Compare
  the non-empty lines in order, before and after, which shows nothing was lost. Both found real
  bugs.
- **Old numbers point at old lists.** A list renumbered once makes an old `H-4` point at a
  different item than today's `H-4`. Resolve each old number against the list as it stood when
  the reference was written.
- **macOS `git grep -E` has no `\b`.** Two empty searches there looked like good news. Use `-P`,
  or the scan, before trusting an empty result.
- **`9cf8b9` is the documentation example.** Never assign it.

## Done when

- [ ] every scan finding is migrated, filed, or confirmed as nothing to do (brownfield: or owned
      by a leg of the adoption sprint)
- [ ] the `git grep` line init printed returns nothing (brownfield: nothing but the two legacy
      blanks that leg a fills)
- [ ] the handbook has its row in the decisions index
- [ ] brownfield: the adoption sprint has its file, its legs, its `plan.md` row, and a reading
      list for leg a
- [ ] no CLAUDE.md or AGENTS.md was written or changed
- [ ] the person has the list of files to review, and nothing is staged
