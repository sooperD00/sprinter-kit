# Standing checks and the optional Python checks record

**ID**: `[s-319ddd]`
**Status**: planned

Adds a STANDING CHECKS line to `plan.md` that every leg's done-when list opens with, and extracts an optional Python checks record from the version one-big-map gets passing.

**Kind:** feature.
**Legs:**
- a — `plan.md` gains STANDING CHECKS beside LLM MODEL, naming whatever commands the stack uses, and the sprint template's Done when opens with "the standing checks in plan.md are clean."
- b — the optional record, extracted from one-big-map's: Ruff with `extend-select`, a formatter-only commit listed in `.git-blame-ignore-revs`, pyright in standard mode, and ignores that name the rule and give a reason. init adds it with `--with python-checks`. Tool facts (versions, pyright fetching Node, the ty 1.0 recheck) go in the stack notes, not the record.
- c — carry back to one-big-map: clear `[h-7da3ca]`.

**Entry gate:** required `[s-b34c63-a]` before leg a, which decides what `plan.md` carries. Required before leg b, outside this repo: one-big-map's `[h-2c3eb1]`, `[h-f7478e]` and `[h-a211a0]` have landed.

**Why now** Not yet. Leg b extracts from a passing version, and one-big-map doesn't have one.

**Brings in:** `[h-7da3ca]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/319ddd` — pending
- this repo's own copies — pending
