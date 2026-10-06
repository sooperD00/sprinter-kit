# Commit hooks and linters for the kit

**ID**: `[s-2f14eb]`
**Status**: planned

Puts the kit's own Python and Markdown under a linter, a formatter and commit hooks, designed to run beside the private-words hook rather than in its place.

**Kind:** feature, after a design leg.
**Legs:**
- a — design session: the pre-commit framework or plain `core.hooksPath` (the framework refuses to install while `core.hooksPath` is set, and the privacy plan sets it), what runs locally and what runs in CI. Start from your existing drafts.
- b — linter and formatter config for `scripts/sprinter.py` and the Markdown, with one formatter-only commit listed in `.git-blame-ignore-revs`.
- c — the hooks and the CI workflow.

**Entry gate:** recommended `[s-cd5ee3]` before leg c, so the commit-message check has a rule to check.

**Why now** The kit ships a Python script with no checks on it, and the hooks design blocks the private-words guard.

**Watch** Whatever leg a picks has to leave room for `[s-7cc4a8]`'s hook. Decide them together.

**Watch** Match one-big-map's Ruff and pyright settings (`[h-2c3eb1]`, `[h-f7478e]`), so `[s-319ddd]` extracts one version, not two.

**Drafts:** `[s-cd5ee3]`'s [CI script](../drafts/s-cd5ee3-check-commit-msgs.sh), which runs every commit-msg hook over a range of commits.
**Carry back:** none. This is the kit's own tooling.
