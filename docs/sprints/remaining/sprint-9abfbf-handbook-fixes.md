# Handbook wording and sprinter.py fixes

**ID**: `[s-9abfbf]`
**Status**: planned

Fixes two small errors one-big-map found: the handbook says `plan.md` holds one table, and scan counts the `9cf8b9` documentation examples as tags in use. It also lets sprinter.py run on the kit's own repo, so the kit can plan itself.

**Kind:** bugfix: reproduce, fix, confirm.
**Legs:**
- a — "Order and re-order" says `plan.md` holds two tables, Order and Completed. one-big-map has already fixed its copy, so match its wording. And the cleanup-marker check can never pass: a filled reading list quotes `SPRINT-<id>-<leg>`, the pattern it tells you to grep for. Exclude the docs, `git grep --untracked 'SPRINT-<id>-<leg>' -- ':!docs'`, in the handbook's "Hand off a leg" and "Hand off a sprint", the reading-list template and prompt5. (Found by `[s-b57080-a]`'s coding agent, 2026-10-06.)
- b — scan's "tags in use" skips `9cf8b9`, or skips code spans the way its other checks do, with a test. And sprinter.py runs on the kit's own repo. init and id refuse to ("this is the kit's own repo"): the guard catches a wrong working directory, but it also stops the kit from planning itself. This plan was set up by pointing a scratch clone's script here with `--repo`, and its IDs are taken by the handbook's openssl method. Add an explicit `--self` flag, or keep the guard on init and let id run anywhere. scan has the same blind spot from the other side: run here, it reports the kit's own `examples/` and sprinter.py as banned words and sprint numbers. A `--self` scan would skip `examples/` and `templates/`. (Found while setting up this plan as `[h-fec4e6]`, 2026-10-05. Pulled from Housekeeping, 2026-10-18.)
- c — carry back to one-big-map: clear `[h-f5c195]` and `[h-e136d2]`.

**Entry gate:** none.

**Why now** Each fix is small. The scan error inflates every scan's tag count, and the kit-repo guard makes every planning session here take its IDs by hand.

**Brings in:** `[h-f5c195]` and `[h-e136d2]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/9abfbf` — pending
- this repo's own copies — pending
