# Review Notes Template

r-<sprint>-<leg>-<short-description>.md

**Block:** <n>, <block name>, leg <leg> of [s-<id>]
**Files under review:** <paths>
**First commit of the block:** `<hash>`, the oldest commit in this block that touched a
file under review. The seal commit's summary and its `Review-range` start here:
`git log <hash>^..HEAD`.
**Repo at review start:** `<hash>`, HEAD when this file was created. Every review commit
comes after it.

<!-- The review agent fills these four lines when it creates this file, before any review
     commit. Find the first commit with
     `git log --reverse --format='%h %ad %s' --date=short -- <files under review>`, and take
     the first one that belongs to this block, not to an earlier leg. -->

## Vocabulary

- RNU = Read and Understand
- `[r]` = a reminder of a command expected to be *r*epeated during the review process
- `[ ]` = open: not run, not done, or not decided yet
- `[x]` = done. The one who ran it ticks it and records the `actual`. No commit hash.
- `[c]` = conceived here, *c*aptured where it gets done (a checklist item, housekeeping,
  techdebt, a sprint). Name where: `[c] → P43`, `[c] → [t-xxxxxx]`.
- `[!]` = stopped: the expect itself was wrong, or help is needed. The reasoning or a
  corrected command goes underneath, and any work it needs becomes a new item or a
  Decide question.
- `expect:` = what you see if it's fine, written by whoever wrote the item, before
  anyone runs it. A command plus its result: `uv run pytest -q` reads `495 passed`.
- `actual [ ]` = what it showed, filled in by whoever ran it. Empty brackets mean not
  run yet. The brackets stay, so `grep 'actual \[ \]'` finds every unrun check.

  - Match: say what it showed, not "ok": `actual [495 passed]`, `actual [no output]`.
  - Drift (a count moved, a line number shifted): still `[x]`, with the real value and
    the reason if it isn't obvious: `actual [497 passed: F58 added two tests]`.
  - A wrong expect: `[!]`, never `[x]`. Write why under it, or a corrected command
    with its own `expect:` and `actual [ ]`.

    - [x] **P43.** <what to change> (D35)
      - expect: `git grep -n 'contains the point' -- docs/interface-spec.md` prints nothing
      - actual [no output]

- `F` =  a fix to source or tests, described, not written: the gap, the expect, the check.
- `P` = doc text: ok to provide "code" blocks, because this is not source code
- `C` = commands: ok to provide "code" or "code" blocks in these items, because 
  this is not source code


## Expect and actual (both checklists)

Every item has an `expect:` and an `actual [ ]`. The rules are in Vocabulary, above.

## Decide
     - [ ] Decide: <the choice>. My recommendation: <one line>, because <one line>.
   <!-- I will answer these, usually with help from the planning agent. -->
   <!-- The review agent ticks a box here [x] only when it agrees the decision is
        made and every item it requires is in one of the two checklists below. -->

## Decisions

  <!-- this is where I'll put my answers later. -->
  <!-- mark any items here [c] → <item ids> when they are captured in the
       Doc Edits Checklist or the Coding Agent's Checklist below -->

## Doc Edits Checklist (Spec Before Code!)

P# items go here: Docs updates, including housekeeping and techdebt to be captured
(Ref: ADR-001).

Item rules:
- The Review Agent completes doc edits before handoff to Coding Agent
- A P item is the review agent's unless it touches text a test reads. A P item that
  edits text a test reads (today: the spec's code blocks and any table a test pins) is
  listed in the Coding Agent's Checklist instead, in the same turn as its F item.
- When an item needs text in a planning doc, write it ready to paste in that doc's
  format: a Watch line `- (leg b) ...`, a tech-debt item `- [ ] [t-xxxxxx] ...`.
- After you copy a paste block into its landed location, mark its boxes [c] captured
  here in the r- file.
- End each item with the decision it comes from, `(D#)`, or the finding, `(E#)`.

## Coding Agent's Checklist

**NEW WHITELIST**: <spec § heading>, <file>. (sections this checklist needs read)

TURN 1: quick fixes
TURN 2+: more difficult fixes, blocked into reasonable turns for attention

Status is one of: blocks the demo · check before leg <x> · handled by design; verify ·
carry forward to <s-id> · tick a follow-up · tech debt · already tracked. Blocking
items first, in every bucket.

Item rules:
- Every item is something someone does: look, run, decide, add, tick. Never a bare
  statement.
- Every look item names a path or spec section and says what to expect.
- A search gives the exact command, runnable from anywhere:
  `git grep --untracked -nE '<pattern>' -- ':/src' ':/tests'`. Plain git grep skips new
  files and reads paths from where you stand, so "no hits" can be a false pass.
- An item a tracker already holds gets one line: `already tracked: <ID>`.
- End each item with the decision it comes from, `(D#)`, or the finding, `(E#)`.
- Code blocks are for P items (doc text) and C items (commands) only.
- An answer to a [!] says which way to go and what must hold. If the coding agent proposed code in the flag, the answer may say "add what you measured," with any changes in words.
- You may quote existing code (this is for basic communication)
- You may name a new test function (it makes the suite count checkable)
- The spec's code block counts as spec (not source code)
