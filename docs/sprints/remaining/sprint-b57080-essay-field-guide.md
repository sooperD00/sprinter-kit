# Essay and field guide templates

**ID**: `[s-b57080]`
**Status**: planned

Ships `docs/ESSAY.md` and `docs/field-guide.md` as templates that init writes into every project, each opening with one line on what goes in it.

**Kind:** feature. The import graph orders the commits: the templates, then the init code that writes them, then the docs that describe them.
**Legs:**
- a — the two templates under `templates/docs/`. ESSAY.md takes its shape from one-big-map's: the claim as the title, what people assume, what is true instead, how the design follows, where this comes from, and what this does not claim. field-guide.md: domain terms, how they relate, where they bite, and the docstring pointer that sends a reviewer there.
- b — init writes both into a new repo, and leaves an existing one alone and lists it. The handbook's "Where things live" names them.
- c — README, interface-spec and design.md say they ship and why. The kit's own `docs/ESSAY.md` stays the kit's essay, not the template.
- d — carry back to one-big-map. It already has both files, so compare their openings with the templates and clear `[h-f44ef7]`.

**Entry gate:** none.

**Why now** It's small and independent, so it goes first and proves the path every later template takes: template, init, docs, carry back.

**Brings in:** `[h-f44ef7]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/b57080` — pending
- this repo's own copies — pending
