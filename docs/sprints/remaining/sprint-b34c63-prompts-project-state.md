# Prompts parameterized by project files, and docs for the kit's wider scope

**ID**: `[s-b34c63]`
**Status**: planned

Changes the prompts to read the leg, model, phase and handbook from the project's own files instead of carrying them, and rewrites the kit's docs for what it is now: how one person works with AI agents, not only how they plan.

**Kind:** refactor for the prompts, after a design leg: what each prompt does is the invariant. The docs follow the prompts.
**Legs:**
- a — design the contract. List every value the prompts carry today (the handbook's ADR number, the current sprint and leg, the phase, the model, paths to the kit and the stack notes, memory files, the DEVLOG and quarantine names) and give each one a home: `plan.md`, the handbook, a per-machine setting, or the command that runs the prompt. Write down the prompt ↔ ADR numbering (prompt6 ↔ ADR-006).
- b — `plan.md`'s template gains the lines the contract assigns it, and scan checks them.
- c — prompts 3, 5, 6 and 7 read those values instead of carrying them, and lose their one-big-map and application-pipeline specifics. A prompt with no record of its own gets a housekeeping item for one.
- d — README, design.md, interface-spec and ESSAY describe the wider scope, the console direction (`/plan`, `/review`), and the plugin `[t-7cab9c]` as the way it gets delivered. The handbook template's "Dev prompts" paragraph still calls them private; this repo's ADR-010 already says otherwise.
- e — carry back to one-big-map: its `plan.md` gains the new lines.

**Entry gate:** required `[s-a0f5d1-a]` before leg a. Whether prompts ship into projects decides who reads the contract.

**Why now** Every prompt run starts with hand edits: the sprint names in prompt7, Phase 0 in prompt3, the leg in prompt5. A console can't run a prompt that has to be edited first.

**Watch** `[s-319ddd]` adds a STANDING CHECKS line to `plan.md`. Leave room for it in leg a's contract.

**Carry back:**
- one-big-map, on branch `kit-sync/b34c63` — pending
- this repo's own copies — pending
