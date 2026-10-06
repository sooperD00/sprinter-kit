# Backlog prefixes and stack notes in planning

**ID**: `[s-41a8b1]`
**Status**: planned

Defines the `stack:` prefix beside `kit:`, sends planning sessions to the stack notes, and writes down how an item moves from a project into the kit and back.

**Kind:** feature.
**Legs:**
- a — the handbook's "Housekeeping and tech debt" gains two rules. The prefix: `[h-<id>] stack: <tool> — <gotcha>`, written for a public repo and held until a review moves it into the stack notes. Promotion: an item keeps its ID when the kit takes it, the kit's sprint names it under Brings in, and its Carry back line stays pending until the project's copy is updated. This repo's sprint files pilot that format now.
- b — "Plan a sprint" says to read the stack notes for each tool a leg touches, and copy each gotcha that applies into that leg's Watches. The notes' location becomes an init option.
- c — README's kit review gains the `stack:` grep and the `— pending` grep.
- d — carry back to one-big-map.

**Entry gate:** none.

**Why now** Planning sessions never read the stack notes today, so their gotchas never reach a Watch.

**Brings in:** `[h-a2bebd]` and `[h-d82de3]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/41a8b1` — pending
- this repo's own copies — pending
