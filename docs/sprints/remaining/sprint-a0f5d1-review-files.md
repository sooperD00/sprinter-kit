# Review files as a shipped decision record

**ID**: `[s-a0f5d1]`
**Status**: planned

Ships the review-files decision (work orders and answers as `r-`/`a-` pairs in `docs/sprints/reviews/`) as a decision-record template that init writes, and records that prompts stay in the kit.

**Kind:** feature, after a design leg. The import graph orders the build: the template, then init, then the handbook and docs that point at it.
**Legs:**
- a — design: whether every project gets the record or init adds it on request; whether prompts ship into projects (recommended no: rules travel into the project, the tooling stays in the kit); and the file name, by `[h-317d79]`'s rule (name the topic, not the verdict), which goes into the ADR template's comment.
- b — generalize `templates/docs/decisions/ADR-NNN-review-files.md`: lowercase `adr-NNN-` like the handbook, a blank for the handbook's ADR, and no project specifics (faab97, D1–D11, `5a0443e`). init numbers it after the handbook, adds its index row, and stops copying it unchanged into a fresh repo.
- c — the handbook gets a "Review a leg" step between handoff and close, and `docs/sprints/reviews/` in "Where things live". interface-spec gets the file names and the C/F/D IDs.
- d — carry back to one-big-map. It takes the record as its next ADR with its own specifics, prompt5's `ADR-NNN` placeholder resolves, and `[h-7617ad]` clears.

**Entry gate:** recommended `[s-b57080]` before leg b, since it lays down the template-and-init path this sprint reuses.

**Why now** init copies the raw template, one-big-map's specifics included, into any fresh repo today (tested 2026-10-05). The process already runs: ADR-006 and prompt6 describe it, and one-big-map has six review files.

**Brings in:** `[h-7617ad]` and `[h-317d79]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/a0f5d1` — pending
- this repo's own copies — pending
