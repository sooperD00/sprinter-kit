<!-- DRAFT for [s-b34c63]: the reasoning behind the prompt4 draft beside it. It becomes the
kit's ADR-004 when that sprint's leg a lands. -->

# ADR-004: Rolling Wave Planning

**Date**: 2026-10-06 (reworked 2026-10-17)
**Status**: Proposed — drafted from the session that planned [s-b57080] in full, and reworked into rolling wave planning while [s-b34c63] was planned.

**Decision**: Planning runs as a rolling wave: the near work is planned in detail, the far work stays coarse, and every leg's close rolls the wave forward. A stub becomes a sprint in two steps. When it's next, it's planned in full, every leg together. Then, at each leg's close, the next leg is made ready: checked against the code as it landed, and given its reading list. Every planning session ends with the next leg ready, and starts with a look across the whole plan at whatever detail it has. It runs as the second half of the flip turn (ADR-007), and at each level it proposes before it writes.

**Why**
- Detail is cheapest to get right when the work is near. A plan made at a leg's close meets the code as it landed, and a full plan of a far sprint describes code that doesn't exist yet.
- Legs are cut at factor boundaries, and those only show with the whole sprint in view. So a sprint is planned in full, every leg together, and a leg is made ready rather than planned on its own.
- What landed can break a later sprint as easily as the next one. A short look across the whole plan finds that while it's still one line to fix.
- A proposal at each level puts the decisions the person owns in front of them while changing one costs a sentence instead of a rewrite.
- The planner holds two pulls on purpose. Completeness alone grows the sprint past a sitting. Smallness alone ships a plan the coder has to finish, and the coder is the session least placed to make those calls.
- A sprint file is run by a coding agent and checked by a reviewer, so it's written for a human engineer and complete enough for an agent.
- Rolling wave planning is project management's name for this, so an engineer who knows the term knows the shape. Here the wave rolls once a leg.

## Three levels, each kept at its own depth

| Level | Kept at | At every leg's close |
|-------|---------|----------------------|
| The plan | stubs that stay true, ordered and gated | a look across every sprint, at the detail it already has |
| The sprint | planned in full, every leg | a stub that's next is planned in full; a sprint already in full is checked |
| The leg | ready | the next leg is checked against the code as it landed, takes in the last leg's lessons, and gets its reading list |

- Run the levels in order, each in a turn of its own, and write the reading list in a fourth. When the plan or the sprint level has nothing to change and no question, it says so in one line and the session goes on: a quiet level costs the person a line, not a stop.
- The sprint level sets the session's size. After a leg in the middle of a sprint it's a check, and the session is short. After a sprint's last leg, the next leg sits in a stub, and planning that stub in full is most of the session.
- prompt3 builds the three levels once: every sprint as a stub, the first sprint in full, and its first leg ready. prompt4 rolls them forward.
- Run planning as the second half of the flip turn, after the docs pass. Run it alone when ADR-007 says the docs pass can wait.

## Look across the plan first

- Find what landed since the last close tag. A leg's close waits for its next leg to be ready, so the last close tag is when the plan was last looked across.
- Check each sprint still in the order against it, at the detail the sprint already has: whether it's blocked, broken or partly unnecessary, whether each gate still points at the leg that owns the work, whether a gap has opened that no sprint holds, and whether anything should move, between sprints, in the order, or in from `housekeeping.md`.
- Add no detail to a stub. Fix what's wrong at the depth it has. A stub planned early is the far wave planned in detail, against code that doesn't exist yet.
- Report only the rows that change. "Nothing changes" is a one-line answer, which keeps the look cheap enough never to skip.
- When a sprint's scope moves, grep its ID and say where each broken reference goes. A gate that points at a leg whose meaning has changed is wrong without anything looking wrong.

## How a stub becomes a sprint

- Plan a stub in full when it's next, every leg together. Pick the Kind first, then cut the legs at factor boundaries, so one red suite has one cause.
- Take in anything from `housekeeping.md` that belongs to the sprint, with its provenance line.
- Put the settled decisions in the sprint file under `## Decisions`, where the coder and the reviewer both read them.
- When the sprint is planned in full already, check that it still holds against what landed: its scope, the order of its legs, a file that needs splitting or a shared piece pulled out, and whether every leg still fits a sitting.

## Make the next leg ready

- Check the leg against the code as it landed: the files, functions and fixtures it names, and the checks in its done-when list.
- Carry the last leg's lessons, from its Landed note and Choices, into this leg's Watches or done-when list. A lesson left in a Landed note gets read once, by the reviewer.
- The leg is ready when the handbook's test passes: its done-when list can be checked by someone who didn't write it, its entry gates name their owners, and its reading list exists.
- Write the reading list last, in a turn of its own, only for a leg that runs next, and against the code as it is that day. The leg's turn always stops before it, even when nothing changed, so the person can check the leg before the list is built on it.
- Point at the leg's Watches instead of restating them. Judgment belongs in the sprint file, which outlives the leg. The list is thrown away when the leg closes.
- Measure what the leg is about to destroy, and stop there. A planner that prototypes the change does the build to find out how the build goes.
- When the list finds a gap, fix the sprint file first, in its own commit. The next planner reads the plan, not a list that's been thrown away.
- Keep the list shorter than the leg's section of the sprint file. A longer list is carrying content that belongs in the plan.

## Read what the plan rests on, and nothing that would anchor it

- Read the sprint, the handbook's planning sections, the backlog, and the code the sprint will change, as it is that day.
- Read memory only for the machine notes. Memory is a second, unversioned plan, and a planner that reads it plans against what someone said rather than what the docs say. Where the two disagree, the person hears about it and the doc gets fixed.
- Read no past conversations. The coder can't open them, so a plan that leans on one leaves out what the coder needs.
- Read the project's own docs, in slices: README, design, spec, essay, field guide. Planning has no blind pass to protect, and the design decides where a change belongs.
- Read the other planned sprints for their scope, legs, gates and Out of Scope, enough to check a gate or pick a destination. A guessed destination is worse than none.
- Of the finished work, read only the leg that just ended, for its Landed note and Choices. Earlier legs' lessons were carried forward at their own closes.
- Read no worked example from another project. Its shape becomes the plan's shape.
- Write no person's or company's name into a repo file.

## Propose before writing

- Write nothing at a level until the person approves its proposal. For a stub, that's what changed from the stub, the decisions table, the legs, Out of Scope, and an outline of any format the sprint creates.
- Put every decision only the person can make in one table, and recommend one option for each. The person decides; the recommendation makes deciding quick.
- Ask every question. A question costs the person a sentence, and a guess is a decision the person never saw.

## Hold two pulls

| Pull | Means | Fails alone because |
|------|-------|---------------------|
| Correct and complete | the handbook's rules, and the field's practice where the person isn't the expert | the sprint grows past a sitting |
| Ruthlessly small | the stub's scope, with everything else under Out of Scope and a destination | the coder inherits the decisions |

## Commit each output on its own

- Each level commits its own output once it's approved: the plan's changes, then the sprint file with its `plan.md` row and any IDs it filed, then the leg's fixes, and last its reading list. Each diff is reviewed on its own.

**Consequences**
- A planning session at every leg's close, and the person's approval before any writing. Its size swings with the sprint level: short in the middle of a sprint, long at a sprint's boundary.
- A decision approved without reading it is the plan's weakest point. The table keeps them few and short so they get read.
- The same model plans, codes and reviews, so its blind spots are shared. The blind review in ADR-006 and the person's approval are the checks that don't share them.
- The look across the plan reads every stub each time. Stubs stay short so that stays cheap.

**Alternatives considered**
- **Plan every sprint in full up front.** prompt3 plans the first sprint in full and leaves the rest as stubs for this reason: a full plan of the fifth sprint describes code that doesn't exist yet.
- **Plan one leg at a time.** Each leg would meet the code as it landed, but the Kind, the decisions and the cuts between legs belong to the whole sprint, and a leg planned on its own sees none of them.
- **Plan inside the coding session.** Planning and coding compete for the same attention and the same context, and the handbook keeps them apart.
- **One pull request per plan.** It would make approving the plan and starting the code separate clicks. Work lands on main, reviewed commit by commit, until `[t-fdfca5]`.
