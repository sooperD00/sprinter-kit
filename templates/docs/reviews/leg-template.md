# [s-<id>-<leg>] <what the leg does>  YYYY-MM-DD
`[repo-name]-YYYYmmDD-HHMM`

kind: [the leg's Kind, from the sprint file]
start time: [YYYYmmDD-HHMM]

## Constraints

> LLMs **DO NOT** run git commands that write. Read-only git (status, diff, log,
> grep, show) is fine and expected.

> BE CAREFUL DURING UPDATES NOT TO DELETE COMMENTS — I worked hard to place them

This is a checklist an LLM fills in and *the human* executes by hand. That is
deliberate: it forces a review and an understanding of each commit by the human.
If you are an LLM, **DO NOT** "help" by executing commits.

## Vocabulary

RNU = Read and Understand
`[r]` = a reminder of a command expected to be *r*epeated during the review process
`[c]` = a marker that shows that the item was conceived here, but *c*aptured in the
  place it should be done (housekeeping, techdebt, a sprint)
`[!]` = there's an issue, had to stop. Help needed. (usually spawns a separate or
    nested item tree).

## Files: the human to review. Does each file's existence, and Claude's reasoning, make sense?
(a git status review with Claude's reasoning; run git status as well)
- [ ] [new file] — [one line on what it does]
- [ ] [modified file] — [what changed]

## LLM Instructions

### Commit order
Order the commits by the leg's Kind (ADR-001's Kind table). The sprint file's
Commits table is the starting order; mark every departure.

### Rules
- The human reads the actual diffs before committing.
- Claude never generates lockfiles or version-pinned dependency entries, only the
  package names to install. The human runs the package manager.
- Claude never generates alembic migration files. Use the autogenerator so alembic
  generates and tracks the IDs, and give the human what to add or revise inside them.
- Every gate is an exact command (with flags) the human can paste (not a desciption).
- Claude runs each gate command before writing it down, and copies "expect" from
  the real output.
- A test gate runs only the test files committed so far, so its count is this
  commit's, not the final total. Untracked files from later commits are on disk
  while the human reviews.
- Humans mark a review that changed the code [!] and say what changed beneath it.
  The gates at each commit step helps the human during these changes.

### Watches
- Copy each Watch from the sprint file that this leg touches, at the commit where it bites.
- Then open ~/repos/stack-notes/README.md, and read the note file for each tool this leg
  actually touches. Copy each gotcha that applies to the commit where it bites, and give
  its file and heading so it can be traced back.
- An `unverified` note is a lead, not a rule. Check it before a commit relies on it.
- A gotcha you hit that has no note goes under Issues as stack: <tool> — <gotcha>, written for a public repo: no project names, paths or data.

## Commit Plan:
- [r] git status  # repeat and watch progress
- [r] git diff --stat  # repeat and watch progress

0. Docs Commit:
	If nothing flagged in the Files or Watches reviews, or in the LLMs output, 
	the human commits the docs of the handoff.
	- [ ] human confirms nothing flagged in Files or Watches
	- [ ] git add '*.md'
	- [ ] git commit -m "docs: handoff [s-<id>-<leg>] <what the leg does>"

1. Dependencies
	(The human installs these. The package manager writes uv.lock / pnpm-lock.yaml.)
	(Claude writes package NAMES only. No version numbers, ever.)
	(If Claude touched pyproject.toml, uv.lock, package.json or pnpm-lock.yaml: restore them first.)
	- [ ] git checkout -- [file]  # if needed
	# uv (backend)
	- [ ] uv add [package]  # [why, runtime]
	- [ ] uv add --dev [package]  # [why, test/build only]
	# pnpm (frontend)
	- [ ] cd frontend
	- [ ] pnpm add [packages]  # [why, runtime]
	- [ ] pnpm add -D [packages]  # [why, test/build only]
	# manual edits to package.json (things pnpm add won't generate, e.g. scripts)
	- [ ] add to "scripts": "test": "[command]"  # exact lines provided
	- [ ] git add [dependency files only: pyproject.toml, uv.lock, package.json, pnpm-lock.yaml]
	- [ ] git commit -m "[message]"
1. [commit name]
   Work: [what this commit does]
   Gate before moving on: [what must be true, in a sentence]
        Reviews:
        - [ ] git diff --word-diff -- [modified files]
        - [ ] RNU [new files]
        - [ ] git add [files]
        Gates:
        - [ ] [exact command, copy-pasteable, run from the repo root]
                - expect: [the literal output or count, e.g. "48 passed"]
                - actual [ ]
        - [ ] [next gate command]
                - expect: [ ]
                - actual [ ]
        Commit:
        - [ ] git commit -m "[message]"

2. [commit name]
   Work: [what this commit does]
   Gate before moving on: [what must be true, in a sentence]
        Reviews:
        - [ ] git diff --word-diff -- [modified files]
        - [ ] RNU [new files]
        - [ ] git add [files]
        Gates:
        - [ ] [exact command, copy-pasteable, run from the repo root]
                - expect: [the literal output or count, e.g. "48 passed"]
                - actual [ ]
        - [ ] [next gate command]
                - expect: [ ]
                - actual [ ]
        Commit:
        - [ ] git commit -m "[message]"
...
N. Final tests (code review, and confirm they collect and wire up)
	- [ ] git diff --word-diff -- [file]
	- [ ] uv run pytest tests/[file].py --collect-only -q
	- [ ] cd frontend && pnpm exec vitest list src/__tests__/[file].ts
	  - expect: [N] tests collected (no ERROR:)

Run real tests, and address or log issues:
(check .gitignore covers these result files before the first run)
- [ ] uv run pytest -v --color=no | tee "tests/leg-<id>-<leg>_$(date +%Y%m%d_%H%M%S).txt"
  - expect: [N] passed, [N] skipped
  - gotcha: [the thing I know will bite you]
- [ ] cd frontend && pnpm exec vitest run --reporter=verbose --no-color 2>&1 | tee "src/__tests__/leg-<id>-<leg>_$(date +%Y%m%d_%H%M%S).txt"
  - expect: [N] passed, [N] skipped
  - gotcha: [the thing I know will bite you]
  (2>&1 because vitest writes some output to stderr; verbose gives the full describe > it tree)

Smoke tests (Swagger), if needed:
prereqs:
  - [ ] [seed step or setup needed]
[Smoke test name]
- [ ] [METHOD] [route] — send [payload] — expect [status + key fields]
  - watch for: [the field that confirms the invariant held]

Issues:

do now:
- [ ] [issue] — [why now]

moved to a later leg or sprint (written into that sprint file):
- [c] [issue] — [s-<id>-<leg>]

housekeeping (unassigned, can join any sprint); file in housekeeping.md, mark [c]:
- [c] [h-<id>] [issue]

tech debt (deferred, probably a while); file in techdebt.md, mark [c]:
- [c] [t-<id>] [issue]

## Handoff (the agent wrote it; the human reviews it, last commit)
- [ ] review the leg in the sprint file: done-when marks, the Landed note, the handoff date
- [ ] any done-when item still [ ]: its sentence says why, and what would verify it
- [ ] items the agent filed: housekeeping.md / techdebt.md, each with an ID
- [ ] git grep --untracked 'SPRINT-<id>-<leg>'  # expect nothing
- [ ] git add docs/sprints [and the docs the leg changed]
- [ ] git commit -m "sprints: hand off [s-<id>-<leg>]"
- [ ] git push

## Done (when the human is satisfied)
- [ ] the leg's heading says done YYYY-MM-DD (wait for human approval)
- [ ] git commit -m "sprints: [s-<id>-<leg>] done"
end time: [YYYYmmDD-HHMM]
