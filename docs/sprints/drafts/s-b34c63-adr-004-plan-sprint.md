<!-- DRAFT for [s-b34c63]: the reasoning behind the prompt4 draft beside it. It becomes the
kit's ADR-004 when that sprint's leg a lands. -->

# ADR-004: How the Next Leg Is Planned

**Date**: 2026-10-06 (reworked 2026-10-17)
**Status**: Proposed — drafted from the session that planned [s-b57080] in full, and reworked when [s-b34c63] became the flip turn.

**Decision**: The next leg is planned in a session apart from coding, at the close of the leg before it: the next leg of the sprint in progress, or, after a sprint's last leg, the next sprint in full from its stub. The planner first reviews the whole plan against what landed, then proposes before it writes: every decision only the person can make, with one recommendation each, and each leg's Kind, done-when list, Watches and Out of Scope. Each output is committed on its own once it's approved, and the last one is the next leg's reading list.

**Why**
- A plan made at a leg's close meets the code as it landed. A plan made early describes a repo that no longer exists by the time it runs.
- What landed can break a later sprint as easily as the next one. A short review of the whole plan finds that while it's still one line to fix.
- A proposal turn puts every decision the person owns in one table, while changing one costs a sentence instead of a rewrite.
- The planner holds two pulls on purpose. Completeness alone grows the sprint past a sitting. Smallness alone ships a plan the coder has to finish, and the coder is the session least placed to make those calls.
- A sprint file is run by a coding agent and checked by a reviewer, so it's written for a human engineer and complete enough for an agent.

## Plan late, at the close

- Plan the next leg at the close of the one before it. Leave later sprints as stubs.
- Run it as the second half of the flip turn (ADR-007), after the docs pass. Run it alone when ADR-007 says the docs pass can wait.
- Read the sprint, the handbook's planning sections, the backlog, and the code the sprint will change, as it is that day.
- Take in anything from `housekeeping.md` that belongs to the sprint, with its provenance line.

## Review the whole plan first

- Find what landed since the last close tag. A leg's close waits for its next leg's plan, so the last close tag is when the plan was last made.
- Check each sprint still in the order against it: whether it's blocked, broken or partly unnecessary, whether each gate still points at the leg that owns the work, and whether anything should move into the next step.
- Report only the rows that change. "Nothing changes" is a one-line answer, which keeps the review cheap enough never to skip.
- When a sprint's scope moves, grep its ID and say where each broken reference goes. A gate that points at a leg whose meaning has changed is wrong without anything looking wrong.

## Read what the plan rests on, and nothing that would anchor it

- Read memory only for the machine notes. Memory is a second, unversioned plan, and a planner that reads it plans against what someone said rather than what the docs say. Where the two disagree, the person hears about it and the doc gets fixed.
- Read no past conversations. The coder can't open them, so a plan that leans on one leaves out what the coder needs.
- Read the project's own docs, in slices: README, design, spec, essay, field guide. Planning has no blind pass to protect, and the design decides where a change belongs.
- Read the other planned sprints for their scope, legs, gates and Out of Scope, enough to check a gate or pick a destination. A guessed destination is worse than none. From the archive, read only the sprint that just closed, for its Landed notes.
- Read no worked example from another project. Its shape becomes the plan's shape.
- Write no person's or company's name into a repo file.

## Propose before writing

- Write nothing in the first turn. Propose the plan review's changes, what changed from the stub, the decisions table, the legs, Out of Scope, and an outline of any format the sprint creates.
- Recommend one option per decision. The person decides; the recommendation makes deciding quick.
- Ask every question. A question costs the person a sentence, and a guess is a decision the person never saw.

## Hold two pulls

| Pull | Means | Fails alone because |
|------|-------|---------------------|
| Correct and complete | the handbook's rules, and the field's practice where the person isn't the expert | the sprint grows past a sitting |
| Ruthlessly small | the stub's scope, with everything else under Out of Scope and a destination | the coder inherits the decisions |

## Commit each output on its own

- Commit the plan review's changes first, then the sprint file with its `plan.md` row and any IDs it filed. Each waits for the person's approval, and each diff is reviewed on its own.
- Put the settled decisions in the sprint file under `## Decisions`, where the coder and the reviewer both read them.

## Write the reading list last

- Write it after the plan is approved, only for a leg that runs next, and against the code as it is that day.
- Point at the leg's Watches instead of restating them. Judgment belongs in the sprint file, which outlives the leg. The list is thrown away when the leg closes.
- Measure what the leg is about to destroy, and stop there. A planner that prototypes the change does the build to find out how the build goes.
- When the list finds a gap, fix the sprint file first, in its own commit. The next planner reads the plan, not a list that's been thrown away.
- Keep the list shorter than the leg's section of the sprint file. A longer list is carrying content that belongs in the plan.

**Consequences**
- A planning session at every leg's close, and the person's approval before any writing.
- A decision approved without reading it is the plan's weakest point. The table keeps them few and short so they get read.
- The same model plans, codes and reviews, so its blind spots are shared. The blind review in ADR-006 and the person's approval are the checks that don't share them.
- The plan review reads every stub each time. Stubs stay short so that stays cheap.

**Alternatives considered**
- **Plan every sprint in full up front.** prompt3 plans the first sprint in full and leaves the rest as stubs for this reason: a full plan of the fifth sprint describes code that doesn't exist yet.
- **Plan inside the coding session.** Planning and coding compete for the same attention and the same context, and the handbook keeps them apart.
- **One pull request per plan.** It would make approving the plan and starting the code separate clicks. Work lands on main, reviewed commit by commit, until `[t-fdfca5]`.
