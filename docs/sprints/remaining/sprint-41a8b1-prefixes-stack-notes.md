# Backlog prefixes and stack notes in planning

**ID**: `[s-41a8b1]`
**Status**: planned

Defines the `stack:` prefix beside `kit:`, sends planning sessions to the stack notes, and writes down how an item moves from a project into the kit and back.

**Kind:** feature.
**Legs:**
- a — the handbook's "Housekeeping and tech debt" gains two rules. The prefix: `[h-<id>] stack: <tool> — <gotcha>`, written for a public repo and held until a review moves it into the stack notes. Promotion landed early, on 2026-10-21, as the handbook's "Carry back a kit change": check it against what `[s-b57080-b]`'s pilot found, and clear the "this repo's own copies" Carry back lines it retires (13 sprint files, this one included). Leg d carries the section into one-big-map's handbook.
- b — "Plan a sprint" says to read the stack notes for each tool a leg touches, and copy each gotcha that applies into that leg's Watches. The notes' location becomes an init option.
- c — README's kit review gains the `stack:` grep and the `— pending` grep.
- d — carry back to one-big-map.

**Entry gate:** none.

**Why now** Planning sessions never read the stack notes today, so their gotchas never reach a Watch.

**Brings in:** `[h-a2bebd]` and `[h-d82de3]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/41a8b1` — pending
- this repo's own copies — pending
