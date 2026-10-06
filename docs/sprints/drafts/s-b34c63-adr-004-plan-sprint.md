<!-- DRAFT for [s-b34c63]: the reasoning behind the prompt4 draft beside it. It becomes the
kit's ADR-004 when that prompt lands in prompts/. -->

# ADR-004: How a Stub Becomes a Sprint

**Date**: 2026-10-06
**Status**: Proposed — drafted from the session that planned [s-b57080] in full.

**Decision**: The next sprint is planned in full in a session of its own, from its stub, at the close of the sprint before it. The planner proposes before it writes: what changed from the stub, the decisions only the person can make with one recommendation each, and each leg's Kind, done-when list, Watches and Out of Scope. The writing waits for approval, and lands as one pull request with the first leg's reading list.

**Why**
- A sprint planned late is planned against the code as it landed. A sprint planned early describes a repo that no longer exists by the time it runs.
- A proposal turn puts every decision the person owns in one table, while changing one costs a sentence instead of a rewrite.
- The planner holds two pulls on purpose. Completeness alone grows the sprint past a sitting. Smallness alone ships a plan the coder has to finish, and the coder is the session least placed to make those calls.
- A sprint file is run by a coding agent and checked by a reviewer, so it's written for a human engineer and complete enough for an agent.

## Plan from the stub, late

- Plan the next sprint at the close of the one before it. Leave later sprints as stubs.
- Read the stub, the handbook's planning sections, the backlog, and the code the sprint will change, as it is that day.
- Take in anything from `housekeeping.md` that belongs to the sprint, with its provenance line.

## Propose before writing

- Write nothing in the first turn. Propose the changes from the stub, the decisions table, the legs, Out of Scope, and an outline of any format the sprint creates.
- Recommend one option per decision. The person decides; the recommendation makes deciding quick.
- Ask at most three questions.

## Hold two pulls

| Pull | Means | Fails alone because |
|------|-------|---------------------|
| Correct and complete | the handbook's rules, and the field's practice where the person isn't the expert | the sprint grows past a sitting |
| Ruthlessly small | the stub's scope, with everything else under Out of Scope and a destination | the coder inherits the decisions |

## Write it as one pull request

- Write the sprint file, its `plan.md` row, IDs for anything filed, and the first leg's reading list.
- Put the settled decisions in the sprint file, where the coder and the reviewer both read them.
- Open one pull request. Approving the plan and starting the code are separate clicks.

**Consequences**
- One more session per sprint, and the person's approval before any writing.
- A decision approved without reading it is the plan's weakest point. The table keeps them few and short so they get read.
- The same model plans, codes and reviews, so its blind spots are shared. The blind review in ADR-006 and the person's approval are the checks that don't share them.

**Alternatives considered**
- **Plan every sprint in full up front.** prompt3 plans the first sprint in full and leaves the rest as stubs for this reason: a full plan of the fifth sprint describes code that doesn't exist yet.
- **Plan inside the coding session.** Planning and coding compete for the same attention and the same context, and the handbook keeps them apart.
- **Plan only inside the docs session (ADR-007).** That covers the step between sprints, but not a plan that has to change mid-sprint, or a sprint with no docs pass before it.
