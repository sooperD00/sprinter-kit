# Sprint Plan

How all of this works — the vocabulary, the rules, and what to do at each step — is
[ADR-010](../decisions/adr-010-planning-system.md). Read that once; this file is the live state.
Work with no sprint yet waits in [housekeeping.md](housekeeping.md), and deferred work in
[techdebt.md](techdebt.md).

LLM MODEL = Claude Opus 5.5 Max Effort

## Order

Top-down. `NNN` stays empty until a sprint closes, and then records the order it was actually
done in. Re-order by moving a row: no sprint file changes when the order does.

| NNN | id | name | status | depends on | reading list |
|-----|----|------|--------|------------|--------------|
| | `[s-b57080]` | [Essay and field guide templates](remaining/sprint-b57080-essay-field-guide.md) | planned | — | — |
| | `[s-a0f5d1]` | [Review files as a shipped decision record](remaining/sprint-a0f5d1-review-files.md) | planned | — | — |
| | `[s-b34c63]` | [Prompts parameterized by project files, and docs for the kit's wider scope](remaining/sprint-b34c63-prompts-project-state.md) | planned | [s-a0f5d1] | — |
| | `[s-48ba8b]` | [Reading lists moved under sprints and converted to Markdown](remaining/sprint-48ba8b-reading-lists-move.md) | planned | [s-b34c63] | — |
| | `[s-db928b]` | [A drafts folder for unadopted ideas](remaining/sprint-db928b-drafts-folder.md) | planned | — | — |
| | `[s-06c862]` | [Test traceability tooling](remaining/sprint-06c862-test-traceability.md) | planned | [s-b34c63] | — |
| | `[s-9abfbf]` | [Handbook wording and scan fixes](remaining/sprint-9abfbf-handbook-fixes.md) | planned | — | — |
| | `[s-41a8b1]` | [Backlog prefixes and stack notes in planning](remaining/sprint-41a8b1-prefixes-stack-notes.md) | planned | — | — |
| | `[s-484bd5]` | [Kinds for demos, design sessions and contracts](remaining/sprint-484bd5-kinds.md) | planned | — | — |
| | `[s-2f14eb]` | [Commit hooks and linters for the kit](remaining/sprint-2f14eb-hooks-linters.md) | planned | — | — |
| | `[s-cd5ee3]` | [Commit message conventions](remaining/sprint-cd5ee3-conventional-commits.md) | planned | — | — |
| | `[s-7cc4a8]` | [Private-words guard and a setup guide](remaining/sprint-7cc4a8-private-words.md) | planned | [s-2f14eb] | — |
| | `[s-319ddd]` | [Standing checks and the optional Python checks record](remaining/sprint-319ddd-standing-checks.md) | planned | [s-b34c63] | — |
| | `[s-b0557c]` | [Agent reflection process](remaining/sprint-b0557c-reflection.md) | planned | — | — |

**Carry back.** Most sprints here change a template that projects already hold copies of. Each
sprint file lists those copies under Carry back, `— pending` until the update lands, and lists
what it took from a project under Brings in, by the item's own ID. The project's item stays put
until its carry back lands. `git grep -n -- '— pending$' docs/sprints` lists what is still owed.
`[s-41a8b1]` decides whether this becomes a handbook rule.

**depends on** names required entry gates only. Each sprint file carries the full gate line,
recommended gates included, pointing at the leg that owns the work. Anything not named here may
be reordered freely.

**ASAP** on a row means a clock outside this repo is running, which ADR-010 defines. It runs
next, behind only the sprint in flight.

Whatever a `[SPRINT-<id>-CLEANUP]` marker names has to exist in this table — which is why a
parked sprint still gets a row and an ID.

A **reading list** is linked with the date it was written. Where the row and the file disagree,
the file wins. One list per leg, and only for the sprint in progress or already finished.

## Completed

| NNN | id | name | handoff |
|-----|----|------|---------|

The counter starts at 001.
