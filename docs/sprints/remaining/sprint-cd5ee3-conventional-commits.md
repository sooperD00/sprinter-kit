# Commit message conventions

**ID**: `[s-cd5ee3]`
**Status**: planned

Adds an add-on decision record that says the project uses Conventional Commits, with a checker the project picks at init and a script CI runs over every pushed commit.

**Kind:** feature. The draft record settles most of the design, so the build orders the commits: the marker grammar init needs, then the template, then the docs.
**Legs:**
- a — review the draft and settle what it leaves open: its `{{precommit-adr}}` blank, the default checker (conventional-pre-commit), and the workflow's old prefixes, which become scopes (`plan:` → `docs(sprints):`, as this repo already does).
- b — sprinter.py's markers gain a choose-one form, `kit:<name>=<value>` and `kit:<name>!=<value>`, with `--commit-check` as its first user. Later add-on records (lint, format, type checks) reuse it.
- c — the record and `check-commit-msgs.sh` move from drafts into `templates/`. init writes them when asked, and the handbook points at the record.
- d — carry back to one-big-map.

**Entry gate:** recommended `[s-2f14eb-a]` before leg a. The draft assumes the pre-commit framework, and the privacy plan's `core.hooksPath` keeps that framework from installing. That design leg settles both.

**Why now** The prompts ask for `docs:` and `plan:` prefixes, and nothing defines them. The kit's ESSAY cites Conventional Commits as the source of Kind.

**Drafts:** [the record](../drafts/s-cd5ee3-adr-conventional-commits.md), and [the CI script](../drafts/s-cd5ee3-check-commit-msgs.sh) that ships with it.
**Carry back:**
- one-big-map, on branch `kit-sync/cd5ee3` — pending
- this repo's own copies — pending
