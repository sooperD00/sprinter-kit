# Expectation Notes Template

e-<sprint>-<leg>-<short-description>.md

## Expect -- write first and freeze

### `<file-name>` (`<path/to/file>`)

<!-- One block per file under review. Copy the block for each file. -->

Expected: <YYYY-MM-DD> · Compared: <YYYY-MM-DD>

| E# | Expect | Status | Evidence | Found by | Lands in |
|---|---|---|---|---|---|
| E<n> | <one thing the file must check, keep consistent, or never do> | pending | | | ||

### Fields

Filled at step 1, EXPECT, then frozen:

- **E#**: `E1`, `E2`, ... Numbering continues across the file blocks, so the test file's first line follows the source file's last.
- **Expect**: one claim on one short line, written before reading the spec, the design doc or the repo tree. Never edited afterward. A better idea found later goes in "Found in the code".

Filled at step 2, COMPARE:

- **Status**: `pending` until COMPARE, then one of:
  - `met`: the file does it, and a test or probe shows it
  - `met elsewhere`: another file does it; Evidence says where
  - `partly`: Evidence says which part holds and which doesn't
  - `gap`: nothing in the repo does it
  - `n/a by design`: a project doc says it shouldn't; Evidence names the section

  `met`, `met elsewhere` and `n/a by design` close the row here. `partly` and `gap` move it to the r- file.
- **Evidence**: `file:line`, a spec section by name, or `(tested)` for a probe run that day.
- **Found by**: who surfaced the finding:
  - `human`: the g- note
  - `review agent`: seen while reading the code or docs
  - `spec`: a project doc says something the code doesn't do
  - `tool`: the suite, coverage, a probe or a mutation run
  - `—`: a closed row, nothing found
- **Lands in**: the r- file item an open row became, or `—` when the row closed here:
  - `D#`: a decision (Decide)
  - `C#` or `F#`: a check or fix (Agent Checklist)
  - `P#`: text to paste into housekeeping, tech debt or a sprint file (Agent Checklist)
  - `already tracked: <ID>`: a one-line Agent Checklist item for something a tracker already holds


### Mutation runs

Each row is one line of `<file>` changed in a scratch copy, then the whole suite run against the copy. A change the suite still passes has no test that pins it.

<!-- Why the review agent: a mutation run tests whether the tests actually pin each rule, so it's evidence for the blind check, just like a probe. If the coding agent graded its own tests, it would be the over-the-shoulder buddy check you don't trust.
Where: in a scratch copy outside the repo. The review agent changes no repo code.
What comes after: a mutation the suite missed becomes a test fix (F#) in the r- file, and the coding agent writes that fix. Re-running the missed mutation afterward is a check (C#). I'd give that check to the review agent too, for the same independence reason. -->

| # | Change | Result |
|---|---|---|
| M1 | `:<line>` <what changed> | <N pass> or <N fail, in which test file> |
| controls | <changes that should be caught, at least one per rule> | <each fails N to M tests> |

<N> changes in all: <N> caught, <N> missed by the whole suite, <N> missed by this file's tests and caught by another.
