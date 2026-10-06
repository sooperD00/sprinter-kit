# ADR-NNN: Tracking code review work orders and answers in the repo

**Status:** accepted
**Date:** 2026-10-05
**Builds on:** ADR-001 (how sprints are planned and closed)

## Context

I review each leg's code file by file with a review agent. The review produces work for other agents: read-only checks, fixes and spec decisions. Those agents work from a written order and answer in writing. The first pair, `r-faab97-a-foundation-checks.md` and its answer, produced decisions D1–D11, which now live in the spec and in the sprint file's Follow-up.

Four readers need these files after a review ends:

- a person asking why a spec decision was made
- a reader evaluating the project, who wants to see how its decisions were checked
- the coding agents, which read their orders from the working tree
- a reflect agent that reads past reviews and proposes changes to the kit, hooks, prompts and scripts

## Decision

1. Review files are committed to the project in `docs/sprints/reviews/`.
2. Each order and its answer form a pair, named by sprint and leg:
   - `r-<sprint>-<leg>-<short-description>.md` is the order.
   - `a-<sprint>-<leg>-<short-description>.md` is the answer.
3. An order opens with where it came from, who it's for, and its rules. Every item has an ID: C for a read-only check, F for a fix, D for a spec decision. Each check names the fix or decision it feeds.
4. An answer replies by ID. It says what it read and ran, cites file and line, and pins line numbers to a named commit. Anything outside the order goes under "Also noticed," reported but not acted on.
5. Review files are evidence, not the record. Before a review closes, each outcome moves to its home: decisions to the spec, follow-ups to the sprint file, debt to `techdebt.md`, domain terms to the field guide.
6. A pair is never edited after its answer lands. A later finding starts a new pair.
7. The review conversation stays out of the repo. Teaching, today's learnings, my by-hand items, and any of my checks that a RESOLVE turn corrected go to DEVLOG. The review prompt owns the conversation's format; this ADR covers only the files.

## What the reflect agent reads

| Signal | Where it lives |
| --- | --- |
| Process friction an agent noticed | "Also noticed" in the a- files |
| Friction I hit in the planning system | `kit:` items in `housekeeping.md` |
| Checks of mine that misfired | RESOLVE corrections in DEVLOG |
| What I had to learn | Today's learnings in DEVLOG |

Every answer carries "Also noticed" for this reason. The last two signals live outside the repo, so the reflect agent reads DEVLOG as well.

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| DEVLOG only | Agents can't find their orders from the working tree, and the spec's decisions lose their evidence |
| One review log per sprint | Mixes audiences and agent roles in one file, and loses the pairing of order and answer |
| No files; the chat is the record | Nothing survives for a reader or the reflect agent |
| The conversation's format in this ADR | The review prompt changes as the reflect agent tunes it. An ADR should outlast that. |

## Consequences

- A decision in the spec traces back to the check that found it.
- A reader evaluating the project sees the checks behind its decisions, not only the outcomes.
- Each reviewed leg adds at least one pair of files.
- Line references go stale as the code moves. The commit pin and the no-edit rule keep each answer true as of its date. The first answer shows why: it flags a spec contradiction at line 59 that the spec has since fixed, and its pin to `5a0443e` keeps the finding readable.
- Review files are committed text, so they follow the repo's rules on private names like any other file.