# A clean-clone check and CI workflow that init installs

**ID**: `[s-fc4d9e]`
**Status**: planned

Lets init give a new project a clean-clone script and a CI workflow that runs it on every push, extracted from one-big-map's once it runs green there.

**Kind:** feature, after a design leg.
**Legs:**
- a — design session. Decide what part is stack-agnostic, what joins `[s-319ddd]`'s Python add-on, and what init writes for a stack it doesn't know.
  - Stack-agnostic: a script that clones the last commit into a throwaway folder, installs and tests, and a workflow that runs it on every push and pull request.
  - The Python add-on: `uv sync --locked`, the uv-managed Python check, and the Ruff and pyright steps.
  - A stack init doesn't know: blanks it lists, or nothing.
  - Also: GitHub Actions only, or a seam for other CI.
- b — the templates under `templates/`, written by init. The Python steps come with `--with python-checks`.
- c — carry back to one-big-map: diff its script and workflow against the templates, and reconcile each difference in one direction or the other.

**Entry gate:**
- Required before leg a, outside this repo: one-big-map's `[s-8d5bb5]` has landed, so the design starts from a workflow that has run green.
- Required: `[s-319ddd-b]` before leg b, which creates the `--with python-checks` add-on the Python steps join.

**Why now** Not yet: there's nothing to extract until one-big-map's CI runs. The cost of waiting is that each new project starts with the clean clone as a manual step, the way one-big-map's `[s-faab97-a]` did.

**Watch** The kit's own CI is `[s-2f14eb-c]`. Give both one workflow shape, or record why they differ.

**Watch** The script's safety rules travel with it. It makes its folder with `mktemp` under `/tmp`, checks the path before `rm -rf`, and keeps the folder when a step fails, so the failure can be looked at.

**Watch** init writes the script executable, and with LF line endings. A CRLF on the shebang line names an interpreter with `\r` in it (stack-notes `git.md`, "One line-ending convention, set before the first cross-machine commit").

**Brings in:** the kit candidate in one-big-map's `[s-8d5bb5]` Out of Scope. It has no ID of its own.
**Carry back:**
- one-big-map, on branch `kit-sync/fc4d9e` — pending
