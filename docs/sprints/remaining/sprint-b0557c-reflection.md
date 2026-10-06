# Agent reflection process

**ID**: `[s-b0557c]`
**Status**: planned

Defines how an agent reflects on finished work, with its own prompt and an output template, so each finding lands in a known place with a destination and a verdict you fill in.

**Kind:** feature, after a design leg.
**Legs:**
- a — design. The read scope: reflection needs DEVLOG and completed legs, which no agent reads today, so write the exception down and hand the inputs over through a reading list. The two triggers: in-leg, when a review finding needs explaining, and batch, across r-/a- review pairs at a kit review.
- b — the template: one entry per finding with what happened, evidence (file and leg ID), why, the proposed change, a destination (ADR, prompt, hook, script, stack notes, field guide, kit), and a verdict slot only you fill. A finding with no destination goes to learnings.
- c — the prompt, in `prompts/`. It proposes and never edits; you route what you accept.
- d — the handbook's "Reflection" section, with `docs/sprints/reflection/` as the home. one-big-map has the folder already.
- e — carry back to one-big-map.

**Entry gate:** recommended `[s-a0f5d1]` and `[s-b34c63]`. Reflection reads review files, and runs from a prompt that follows the contract.

**Why now** The loop has already run once by hand: a coding agent wrote weak tests, reflected on them, and proposed text for a test-writing record. The kit's ESSAY and the review-files record both promise a reflect agent.

**Watch** `[h-6c1d2c]` says the prompt lives with your private prompts. That changed when the prompts went public.

**Brings in:** `[h-6c1d2c]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/b0557c` — pending
- this repo's own copies — pending
