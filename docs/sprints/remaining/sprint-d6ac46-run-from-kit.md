# Prompts that run unedited from the kit, and docs for its wider scope

**ID**: `[s-d6ac46]`
**Status**: planned

Changes the prompts to read the leg, model, phase and handbook from the project's own files instead of carrying them, so each one runs from the kit without hand edits, and rewrites the kit's docs for what it is now: how one person works with AI agents, not only how they plan.

**Kind:** refactor for the prompts, after a design leg: what each prompt does is the invariant. The docs follow the prompts.
**Legs:**
- a — design the contract. List every value the prompts carry today (the handbook's ADR number, the current sprint and leg, the phase, the model, paths to the kit and the stack notes, memory files, the DEVLOG and quarantine names) and give each one a home: `plan.md`, the handbook, a per-machine setting, or the command that runs the prompt. Write down the prompt ↔ ADR numbering (prompt6 ↔ ADR-006).
- b — `plan.md`'s template gains the lines the contract assigns it, and scan checks them.
- c — every prompt in `prompts/` reads those values instead of carrying them. Prompts 3, 5 and 6 lose their one-big-map and application-pipeline specifics, and prompt6 points at the field guide's entry-rules comment instead of restating it. prompt3 commits once its turns are approved, as the other prompts do. Prompts 4 and 7 already find their own inputs, so they change only where the contract says. Any other prompt with no record of its own gets a housekeeping item for one.
- d — README, design.md, interface-spec and ESSAY describe the wider scope, the console direction (`/plan`, `/review`), and the plugin `[t-7cab9c]` as the way it gets delivered. The handbook template's "Dev prompts" paragraph still calls them private; this repo's ADR-010 already says otherwise.
- e — carry back to one-big-map: its `plan.md` gains the new lines.

**Entry gate:** required `[s-a0f5d1-a]` before leg a. Whether prompts ship into projects decides who reads the contract. Required `[s-b34c63]` before leg c, which rewrites prompt4 once it has landed.

**Why now** Every prompt run starts with hand edits: Phase 0 in prompt3, the leg in prompt5, and the handbook's ADR number in every prompt that names it. A console can't run a prompt that has to be edited first.

**Watch** `[s-319ddd]` adds a STANDING CHECKS line to `plan.md`. Leave room for it in leg a's contract.

**Carry back:**
- one-big-map, on branch `kit-sync/d6ac46` — pending
- this repo's own copies — pending
