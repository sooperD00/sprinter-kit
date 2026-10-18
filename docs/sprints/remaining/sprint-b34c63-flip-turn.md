# The flip turn: a docs pass and the next plan at the end of every leg

**ID**: `[s-b34c63]`
**Status**: planned

Lands the flip turn as the way a leg ends: prompt7 checks the docs against what the leg landed, then prompt4, in the same session, reviews the plan, plans the next leg and writes its reading list. prompt4 moves from its draft into `prompts/`, and ADR-004 and ADR-007 record why.

**Kind:** feature. The import graph orders the commits: prompt4 lands before the records that cite it.
**Legs:**
- a — prompt4, ADR-004 and ADR-007 land from their drafts, with what the first flip turns taught them. ADR-007 is checked against `prompts/prompt7-docs.md` as it runs. The ADR index gets both rows, and interface-spec's sprint-file section names the `## Decisions` block that planning writes.

**Entry gate:** none.

**Why now** `[s-d6ac46]` rewrites prompt4 once it has landed, and three sprints wait on `[s-d6ac46]`. Until then the flip turn runs from drafts, which nothing may cite as a reason.

**Drafts:** [prompt4](../drafts/s-b34c63-prompt4-plan-sprint.md), [ADR-004](../drafts/s-b34c63-adr-004-plan-sprint.md) and [ADR-007](../drafts/s-b34c63-adr-007-docs-session.md).
