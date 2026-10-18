# Rolling wave planning, run as the flip turn at the end of every leg

**ID**: `[s-b34c63]`
**Status**: planned

Makes rolling wave planning the way the plan moves forward, in the flip turn at the end of every leg. prompt7 checks the docs against what the leg landed. Then prompt4, in the same session, looks across the whole plan, plans the next leg's sprint in full if it's still a stub, and makes the next leg ready with its reading list. prompt4 moves from its draft into `prompts/`, and ADR-004 and ADR-007 record why.

**Kind:** feature. The import graph orders the commits: prompt4 lands before the records that cite it, and the handbook after them, since it will cite them too.
**Legs:**
- a — prompt4, ADR-004 and ADR-007 land from their drafts, with what the first flip turns taught them. ADR-007 is checked against `prompts/prompt7-docs.md` as it runs. The ADR index gets both rows, and interface-spec's sprint-file section names the `## Decisions` block that planning writes. Last, as the close-out, the handbook catches up: Plan a sprint names rolling wave planning and its three levels and says a stub is planned in full when it's next, Vocabulary adds "planned in full" and "ready", and the tag line under Three clocks says a close tag means the next leg is ready.

**Entry gate:** none.

**Why now** `[s-d6ac46]` rewrites prompt4 once it has landed, and three sprints wait on `[s-d6ac46]`. Until then the flip turn runs from drafts, which nothing may cite as a reason.

**Drafts:** [prompt4](../drafts/s-b34c63-prompt4-plan.md), [ADR-004](../drafts/s-b34c63-adr-004-rolling-wave-planning.md) and [ADR-007](../drafts/s-b34c63-adr-007-flip-turn.md).
