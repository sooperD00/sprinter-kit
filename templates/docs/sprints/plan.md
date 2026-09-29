# Sprint Plan

How all of this works — the vocabulary, the rules, and what to do at each step — is
[{{adr}}]({{adr-link}}). Read that once; this file is the live state.
Work with no sprint yet waits in [housekeeping.md](housekeeping.md), and deferred work in
[techdebt.md](techdebt.md).

LLM MODEL = {{model}}

<!-- kit:phases -->
## Phases

Delivery milestones, each designed in [{{phase-doc-name}}]({{phase-doc}}).

{{phase-list}}

<!-- /kit:phases -->
## Order

Top-down. `NNN` stays empty until a sprint closes, and then records the order it was actually
done in. Re-order by moving a row: no sprint file changes when the order does.

| NNN | id | name | status | depends on | reading list |
|-----|----|------|--------|------------|--------------|

**depends on** names required entry gates only. Each sprint file carries the full gate line,
recommended gates included, pointing at the leg that owns the work. Anything not named here may
be reordered freely.

**ASAP** on a row means a clock outside this repo is running, which {{adr}} defines. It runs
next, behind only the sprint in flight.

Whatever a `[SPRINT-<id>-CLEANUP]` marker names has to exist in this table — which is why a
parked sprint still gets a row and an ID.

A **reading list** is linked with the date it was written. Where the row and the file disagree,
the file wins. One list per leg, and only for the sprint in progress or already finished.

## Completed

| NNN | id | name | handoff |
|-----|----|------|---------|
| {{legacy-nnn}} | — | [{{legacy-range}}](completed/{{legacy-archive}}) | dates in the file | <!-- kit:brownfield -->

The counter starts at 001. <!-- kit:greenfield -->
The counter continues at {{counter}}. <!-- kit:brownfield -->
