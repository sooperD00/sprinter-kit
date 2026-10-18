<!-- DRAFT for [s-b34c63]: the reasoning behind prompts/prompt7-docs.md and the session it
starts, as the agents that reworked prompt7 understood it. The person corrects it, and it's
checked against prompt7 as it runs, before it becomes the kit's ADR-007 in that sprint's leg a. -->

# ADR-007: The Flip Turn at the End of a Leg

**Date**: 2026-10-17
**Status**: Proposed — the practice is older than the record. The manual prompt7 ran it on application-pipeline as one long prompt, and was reworked in place on 2026-10-17 into the docs pass described here.

**Decision**: At the end of every leg, one session runs two prompts in order. prompt7 checks the project's docs against what the leg landed and fixes what drifted, then prompt4 reviews the plan, plans the next leg and writes its reading list. This is the flip turn: tuck, plan the next leg, and push off from prompt4. The leg doesn't close until the turn is done, because a close tag says the code is blessed, the docs passed and the next step is planned.

**Why**
- A leg isn't finished until the next one is ready. A leg whose next step nobody can name hasn't been checked against where it was going.
- The docs pass reads every doc fresh, and that is the context the plan needs. Two sessions would read it twice.
- Drift the docs pass finds changes the plan, so planning comes after it, in the same context.
- Two prompts keep each half runnable on its own: prompt4 without a docs pass, for a re-plan in the middle of a leg.
- Separate commits keep each output reviewable on its own, though one session wrote all of them.

## Run the turns in order

| Turn | Prompt | Does | Commits |
|------|--------|------|---------|
| Docs | prompt7 | checks the project's docs against what landed, proposes the fixes, then makes them | the doc fixes |
| Plan | prompt4 | reviews the whole plan, proposes the next leg or sprint, then writes it | the plan review's changes, then the sprint file |
| Reading list | prompt4 | the next leg's list, if that leg runs next | the list, on its own |

- Each turn proposes, waits for approval, then writes and commits.
- prompt7 checks the project's docs, and prompt4 owns the planning docs under `docs/sprints/`. Neither edits the other's.
- prompt7 handles the notes the person leaves in the docs, tagged with initials and a date: `DECIDED` is the answer, `DRAFT` needs the house voice, `PARK` goes to the backlog.
- prompt7 reports field-guide pointers and doesn't add them, so the code changes in a leg rather than in a docs pass.
- A decision record isn't edited to match the code. A contradiction is a finding: the code is wrong, or the record needs an Update note or a successor.
- prompt7 ends by handing over to prompt4 in the same session, and prompt4 skips the reads the docs pass already made.

## Skip the docs pass only on purpose

- Run prompt4 alone for a re-plan in the middle of a leg, or when nothing the docs describe has changed since the last flip turn.
- Never skip the plan review. It's the cheap half, and it's what keeps a stale plan from being coded.

**Consequences**
- A long session. When the docs pass leaves too little room, the plan and the list move to a fresh session that runs prompt4 alone.
- The reading list comes from the session that planned the leg, so the coding session gets its list from the agent that knows the plan best, and inherits that agent's blind spots.
- A leg's close waits on two more turns of the person's attention.

**Alternatives considered**
- **Three sessions.** Each re-reads the docs, and the plan loses what the docs pass found.
- **Plan before the docs pass.** The plan is written against docs the next turn corrects.
- **One prompt for the whole turn.** Simpler to paste, but a re-plan in the middle of a leg would skip half of it by instruction, and the two halves would share one record.
