# A drafts folder for unadopted ideas

**ID**: `[s-db928b]`
**Status**: planned

Gives every project `docs/sprints/drafts/`, a committed place for half-built records, prompts and plans that belong to a sprint, housekeeping or tech-debt ID, so agents can pass drafts to each other without reading them as rules.

**Kind:** feature.
**Legs:**
- a — the rule, piloted in this repo's [drafts README](../drafts/README.md): a draft is named `<item-id>-<short-name>.<ext>`, its item links to it, no session reads it unless a prompt or reading list names the file, and it is deleted when its item lands.
- b — a template folder with that README. init writes it, and scan reports a draft whose ID is in no list.
- c — carry back to one-big-map.

**Entry gate:** recommended `[s-48ba8b-a]`, which sets the same kind of path rule for reading lists.

**Why now** You have drafts for the hooks design (`[s-2f14eb]`) and nowhere to put them. DEVLOG holds notes, but no other agent can read it.

**Carry back:**
- one-big-map, on branch `kit-sync/db928b` — pending
- this repo's own copies — pending
