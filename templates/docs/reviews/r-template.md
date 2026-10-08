# Review Notes Template

r-<sprint>-<leg>-<short-description>.md

## Vocabulary

RNU = Read and Understand
`[r]` = a reminder of a command expected to be *r*epeated during the review process
`[c]` = a marker that shows that the item was conceived here, but *c*aptured in the
  place it should be done (housekeeping, techdebt, a sprint)
`[!]` = there's an issue, had to stop. Help needed. (usually spawns a separate or
    nested item tree).

## Decide
     - [ ] Decide: <the choice>. My recommendation: <one line>, because <one line>.
   <!-- I will answer these, usually with help from the planning agent. -->

## Exercises (<= 3 items the human can do by hand to learn)

> These are learning items for the human. They do not gate agent work and are optional.

     ### <file>: for me
     - [ ] <action>: `<path>` or spec → <section>
       - expect: <what I see if it's fine>

## Agent Checklist

TURN 1: docs updates, including housekeeping and techdebt items (Ref: ADR-001)
TURN 2: quick fixes
TURN 3+: more difficult fixes, blocked into reasonable turns for attention

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
- When an item needs text in a planning doc, write it ready to paste in that doc's
  format: a Watch line `- (leg b) ...`, a tech-debt item `- [ ] [t-xxxxxx] ...`.
