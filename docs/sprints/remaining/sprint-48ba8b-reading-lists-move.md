# Reading lists moved under sprints and converted to Markdown

**ID**: `[s-48ba8b]`
**Status**: planned

Moves `docs/reading/` to `docs/sprints/reading/`, renames the lists from `.txt` to `.md` with a path rule in place of the `.txt` read guard, and stops a reading list from planning commits a second time.

**Kind:** migration. Every file that names a reading list is a consumer. The guard changes first, so no consumer is ever left without one.
**Legs:**
- a — the replacement guard, "open nothing in `docs/sprints/reading/` unless the prompt names the file", written into the handbook and every prompt's guard.
- b — move and rename in the kit: templates, init, scan, the handbook, interface-spec, SKILL.md, README, design.md and the prompts. examples/ keeps its verbatim copies, renamed only, and examples/README says so. Each grep hit is a judgment call, not a sed.
- c — the reading-list template's WHAT YOU ARE DOING points at the sprint file's Commits table instead of planning the commits again. The handbook says a Commits table orders at graph-node granularity, and only where the Kind makes the order a safety property: migration and bugfix, not refactor or upgrade.
- d — carry back to one-big-map: `docs/reading/`, the links in `plan.md`, and its handbook copy.
- e — the private devlog repo: every prompt's guard and read list, and leg-template.txt. You do this one, or hand that repo to an agent.

**Entry gate:** required `[s-b34c63-c]` before leg a. The prompts' guards are rewritten there, and this changes one rule in them.

**Why now** Reading lists belong to sprints, and the `.txt` guard is a rule every new prompt has to restate.

**Brings in:** `[h-723c72]` and `[h-a8f367]` from one-big-map's housekeeping.md, and the move, which you raised on 2026-10-05.
**Carry back:**
- one-big-map, on branch `kit-sync/48ba8b` — pending
- the private devlog repo, yours — pending
- this repo's own copies — pending
