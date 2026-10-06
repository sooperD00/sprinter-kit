<!-- DRAFT for [s-b34c63]: prompt7's reasoning, as I understood it from the prompt and from
Nicole on 2026-10-06. She corrects it before it becomes the kit's ADR-007. -->

# ADR-007: One Session Between Sprints for the Docs, the Next Plan and Its Reading List

**Date**: 2026-10-06
**Status**: Proposed — the practice is older than the record. prompt7 ran it on application-pipeline.

**Decision**: Between sprints, one session does three things in order. It checks the docs against the code and fixes what drifted. Then it plans or tightens the next sprint, by prompt4's turns. Then it writes that sprint's first reading list. Each output lands as its own commit, approved before the next turn starts.

**Why**
- The docs pass reads every doc fresh, and that is the context the next plan needs. Three sessions would read it three times.
- Drift the docs pass finds changes the plan, so planning comes after it, in the same context.
- The handbook makes the reading list planning's last step, written against the code as it landed.
- Separate commits keep each output reviewable on its own, though one session wrote all three.

## Run the three turns in order

| Turn | Does | Commit prefix |
|------|------|---------------|
| Docs | checks every doc against the code, proposes the fixes, then makes them | `docs:` |
| Plan | prompt4's turns, for the next sprint | `plan:`, or `docs(sprints):` once [s-cd5ee3] lands |
| Reading list | the first leg's list | `reading lists:`, or `docs(reading):` once [s-cd5ee3] lands |

- Each turn proposes, waits for approval, then writes.
- The docs turn handles the notes the person tags in the docs: `DECIDED`, `DRAFT` and `PARK`.

**Consequences**
- A long session. When the docs pass leaves too little room, the plan and the list move to a fresh session that runs prompt4.
- The reading list comes from the session that planned the sprint, so the coding session gets the list from the agent that knows the plan best, and inherits that agent's blind spots.

**Alternatives considered**
- **Three sessions.** Each re-reads the docs, and the plan loses what the docs pass found.
- **Plan before the docs pass.** The plan is written against docs the next turn corrects.
- **A fresh session writes the reading list.** It re-reads everything. Worth it only when the planning session is near its limit.
