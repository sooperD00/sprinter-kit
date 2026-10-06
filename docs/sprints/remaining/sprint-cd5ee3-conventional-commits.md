# Commit message conventions

**ID**: `[s-cd5ee3]`
**Status**: planned

Adds a decision-record template that says the project uses Conventional Commits, with the commit types this workflow already uses.

**Kind:** feature, after a design leg.
**Legs:**
- a — design: the type list (`docs:`, `plan:`, `chore:` and the standard ones), whether the workflow's own types stay as custom types, and how a Kind maps to a type. `reading lists:` isn't a valid type as written, because a type has no spaces.
- b — the ADR template, an init option, and a pointer from the handbook.
- c — carry back to one-big-map.

**Entry gate:** none. It feeds `[s-2f14eb]`, where a commit-message hook can check it.

**Why now** The prompts already ask for `docs:` and `plan:` prefixes, and nothing defines them. The kit's ESSAY cites Conventional Commits as the source of Kind.

**Carry back:**
- one-big-map, on branch `kit-sync/cd5ee3` — pending
- this repo's own copies — pending
