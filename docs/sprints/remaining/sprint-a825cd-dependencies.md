# Dependency installs as a shipped decision record

**ID**: `[s-a825cd]`
**Status**: planned

Moves the rule that the human installs and the package manager writes versions out of the leg template and the prompts into one decision record that init writes, with each stack's commands spliced in by `--stack`, so templates and prompts point at the record instead of carrying the rule.

**Kind:** refactor: what an agent is told about dependencies is the invariant; where it's written moves.
**Legs:**
- a — the record. The decision is stack-free: the human installs; the agent names packages and never writes a version; the package manager writes versions and lock files; an agent that touched a dependency file restores it first. The commands go in `kit:python`, `kit:node` and `kit:dotnet` blocks, moved whole from `leg-template.md`. init numbers the record after the handbook and fills `{{deps-adr}}` wherever a template names it.
- b — the pointers. `leg-template.md`'s Dependencies block keeps its checkbox lines and takes its commands from the record: the planning agent copies them into each leg, so the checklist stays copy-paste. prompt5 and promptX point at the record in place of their package-manager lines. `[s-cd5ee3]`'s draft points its "add the dev dependency" lines at the record.
- c — carry back to one-big-map, and to Hello_Eliza if it has taken the kit by then.

**Entry gate:** required `[s-a0f5d1-b]` before leg a, which teaches init to number a second record after the handbook. Required `[s-bbcfb5-a]` before leg a, which creates the stack blocks. Recommended `[s-d6ac46-a]` before leg b, which decides how a prompt finds a record's number.

**Why now** The rule lives in four copies: the leg template, prompt5, promptX, and `[s-cd5ee3]`'s draft, which already restates it and hard-codes uv and pnpm commands. Every add-on record to come (lint, format, type checks) will want to say it again.

**Watch** One record with stack blocks, not one record per stack. The decision is the same on every stack; only the commands and file names differ.

**Watch** Name the file for the topic, not the verdict (`[h-317d79]`'s rule): `adr-NNN-dependencies.md`, not `adr-NNN-human-installs.md`.

**Carry back:**
- one-big-map, on branch `kit-sync/a825cd` — pending
- Hello_Eliza, if it has taken the kit — pending
