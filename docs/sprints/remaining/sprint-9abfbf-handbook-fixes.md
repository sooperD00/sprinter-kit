# Handbook wording and scan fixes

**ID**: `[s-9abfbf]`
**Status**: planned

Fixes two small errors one-big-map found: the handbook says `plan.md` holds one table, and scan counts the `9cf8b9` documentation examples as tags in use.

**Kind:** bugfix: reproduce, fix, confirm.
**Legs:**
- a — "Order and re-order" says `plan.md` holds two tables, Order and Completed. one-big-map has already fixed its copy, so match its wording. And the cleanup-marker check can never pass: a filled reading list quotes `SPRINT-<id>-<leg>`, the pattern it tells you to grep for. Exclude the docs, `git grep --untracked 'SPRINT-<id>-<leg>' -- ':!docs'`, in the handbook's "Hand off a leg" and "Hand off a sprint", the reading-list template and prompt5. (Found by `[s-b57080-a]`'s coding agent, 2026-10-06.)
- b — scan's "tags in use" skips `9cf8b9`, or skips code spans the way its other checks do, with a test.
- c — carry back to one-big-map: clear `[h-f5c195]` and `[h-e136d2]`.

**Entry gate:** none.

**Why now** Both are small, and the second inflates every scan's tag count.

**Brings in:** `[h-f5c195]` and `[h-e136d2]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/9abfbf` — pending
- this repo's own copies — pending
