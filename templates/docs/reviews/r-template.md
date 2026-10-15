# Review Notes Template

r-<sprint>-<leg>-<short-description>.md

## Vocabulary

- RNU = Read and Understand
- `[r]` = a reminder of a command expected to be *r*epeated during the review process
- `[c]` = a marker that shows that the item was conceived here, but *c*aptured in the
  place it should be done (housekeeping, techdebt, a sprint)
- `[!]` = there's an issue, had to stop. Help needed. (usually spawns a separate or
    nested item tree).
- `F` =  a fix to source or tests, described, not written: the gap, the expect, the check.
- `P` = doc text: ok to provide "code" blocks, because this is not source code
- `C` = commands: ok to provide "code" or "code" blocks in these items, because 
  this is not source code


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
- End each item with the decision it comes from, `(D#)`, or the finding, `(E#)`.

## Coding Agent's Checklist

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
- When an item needs text in a planning doc, write it ready to paste in that doc's
  format: a Watch line `- (leg b) ...`, a tech-debt item `- [ ] [t-xxxxxx] ...`.
- After you copy a paste block into its landed location, mark its boxes [c] captured
  here in the r- file.
- Code blocks are for P items (doc text) and C items (commands) only.
- An answer to a [!] says which way to go and what must hold. If the coding agent proposed code in the flag, the answer may say "add what you measured," with any changes in words.
- You may quote existing code (this is for basic communication)
- You may name a new test function (it makes the suite count checkable)
- The spec's code block counts as spec (not source code)
- A P item is the review agent's unless it touches text a test reads
