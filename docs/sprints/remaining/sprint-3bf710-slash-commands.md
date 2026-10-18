# Slash commands for the kit's prompts, installed once per machine

**ID**: `[s-3bf710]`
**Status**: planned

Adds `sprinter.py link`, which makes each prompt in `prompts/` a Claude Code slash command on the machine it runs on, as a pointer back to the kit, so a session starts with `/sprinter-kit-plan` instead of a pasted prompt.

**Kind:** feature. The import graph orders the commits: the command lands before the docs that describe it.
**Legs:**
- a — `link` lands in sprinter.py from its draft, checked in a scratch home folder. README's "Use it" gains the one-time step, interface-spec the pointer format and the name rule, and design.md the reasons in Decisions.

**Entry gate:** recommended `[s-b34c63-a]` before leg a. It moves prompt4 into `prompts/`, so `/sprinter-kit-plan` comes from link rather than by hand. Not required: link makes commands from whatever `prompts/` holds.

**Why now** Every session starts by switching screens to paste a long prompt, then checking it's the right version. A command reads the kit's current file every time. The console and the plugin `[t-7cab9c]` both need commands to call.

**Drafts:** [the link script](../drafts/s-3bf710-link.py), runnable as it is: `python3 ~/repos/sprinter-kit/docs/sprints/drafts/s-3bf710-link.py --dry-run`.

**Watch** The hand-made `~/.claude/skills/sprinter-kit-plan/` from 2026-10-17 has no marker, so link reports it and leaves it alone. Delete that folder before the first run after prompt4 moves.

**Watch** link takes no `--repo`. Don't route it through `repo_root()`, or it inherits `[h-fec4e6]`'s refusal to run in the kit's own repo.

**Watch** sprinter.py supports Python 3.8, and `write_text(newline=)` arrived in 3.10. The draft writes through `open(..., newline="\n")`.

## Decisions

Proposed in a design conversation, 2026-10-17. Confirm or change each when the sprint is planned in full.

- D1. A per-machine command, not part of init. init writes only inside a repo and runs once per repo. Skills live in the home folder, once per machine. Running link is the opt-in, so it takes no flag to say no.
- D2. Pointers, not copies or symlinks. Each SKILL.md tells Claude to read the prompt from the kit, so the prompt stays under `~/repos`, edits flow through, and the prompts keep their flat file names. A symlinked skill has to be a folder, and symlinks on Windows need Developer Mode.
- D3. In sprinter.py, not a shell script. One stdlib script runs on Mac, Linux and Windows. `Path.home()` writes a native path, which a Git Bash loop can't, and every file is LF and UTF-8, as init writes them.
- D4. The name is `sprinter-kit-` plus the prompt's file name without its `promptN-` prefix: `prompt5-code.md` makes `/sprinter-kit-code`. Two prompts that would make one name stop link before it writes.
- D5. Every pointer sets `disable-model-invocation: true`. A command runs only when the person types it, so no prompt loads itself, as the handbook's Session guards require.
- D6. link changes only pointers it wrote, which carry a marker line. Anything else in its way is reported and left alone. A pointer whose prompt is gone is reported as stale, and never deleted.
- D7. Text typed after a command reaches the prompt as `$ARGUMENTS`, which covers prompt4's "unless I named one."

## Out of Scope
- prompts that still carry one project's values, like ADR-001 in prompts 5 and 6 → `[s-d6ac46]` leg c. Their commands work, with the same hand edits as a paste.
- the docs for the console direction → `[s-d6ac46]` leg d, which should use these command names in place of `/plan` and `/review`
- deleting stale pointers → by hand for now, and a `--prune` flag if it comes up twice
- the plugin that replaces link → `[t-7cab9c]`
- the console calling the commands → sprint-runner

**Carry back:** none. link writes to the machine, not to a project, so no project holds a copy.
