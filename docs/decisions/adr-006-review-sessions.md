# ADR-006: How a Handed-Off Leg Is Reviewed

**Date**: 2026-10-05
**Status**: Accepted — the review prompt has been in use on a private project since 2026-10-05.
It moves into `prompts/` with this record.

**Decision**: A handed-off leg is reviewed one file at a time, by a fresh session that reviews
blind first and compares second. It writes down what each file should handle before it reads the
spec, and it reads the plan only in a COMPARE turn after the last file. Every finding goes into
exactly one of three buckets (Decide, Learn, Agent queue). The queue becomes written work orders
only after COMPARE, and the human's learning never blocks the leg.

**Why**
- A reviewer that reads the plan first checks the code against the plan, and misses what the plan
  left out. A blind pass is the only way to find gaps in the plan itself.
- Comparing afterwards turns the blind pass's double finds into a measure: how often the
  reviewer re-derives the plan, and how often it finds something the plan lacks.
- A review session is also where the human learns the stack. Learning and delivering need
  separate lists, or the learning stalls the delivery.
- Memory notes from informal chats are a second, unversioned plan. Read too early, they anchor the
  review and hide the doc gaps the review exists to find.

## Review blind, then compare

Do the work before reading the answer, the way a fab engineer predicts a result before opening the
analysis, or a team reveals planning-poker estimates at the same moment.

- Find the leg from the `--- handed off` line in `docs/sprints/remaining/`. Read only its ID and
  title.
- For each file, the human names it and says first, in their own words, what they think it does.
  That is the human's blind pass.
- Write the file's EXPECT list before searching the spec: what the file should handle, from its
  own purpose and its language's standards. Never revise it afterwards.
- Then check `interface-spec.md` and `design.md` before calling anything missing. They are the
  requirements, not the plan, and many gaps are handled by design.
- Open nothing in `docs/sprints/` until COMPARE.
- At COMPARE, read the leg's section and sort every finding:

| Sort | Means | Then |
|------|-------|------|
| plan gap | the plan didn't cover it | keep it; write the line the planning docs need, ready to paste |
| already decided | the plan chose otherwise on purpose | drop it, citing the decision |
| confirms the plan | found blind, and the plan has it | drop it; it counts as agreement |
| intent gap | memory holds a reason no doc states | keep it; write the line `design.md` or the spec needs |

- List the done-when items that no reviewed file showed at the code.
- Print the tally, one row per finding, with **found by**: the human, the reviewer, the spec, or a
  tool. The totals row is the review's measurement.

## Sort every finding into one bucket

| Bucket | What goes in it | Who works it | Blocks the leg? |
|--------|-----------------|--------------|-----------------|
| Decide | a choice only the human can make | the human, in the chat | yes |
| Learn | a look, run or read that teaches; changes no code | the human, by hand | never |
| Agent queue | checks (C), fixes (F), doc edits, from a written order | an agent, after COMPILE | if its status says so |

- Give the human at most three Learn items per file. Each one names a path or spec section, and
  says what to expect there.
- Treat Decide items as provisional until COMPARE. The human knows the plan and can say "already
  decided" at any point.
- Give every queued item an ID and a status. Never ask the human to work the queue.

## Turn the queue into work orders

- COMPILE once, after COMPARE. Compiling earlier would put the plan into context before the blind
  pass ends.
- Write work orders to `docs/sprints/reviews/` as `r-<sprint>-<leg>-<short-description>.md`. The
  agent that works one answers in `a-<sprint>-<leg>-<short-description>.md`.
- Keep the IDs: C for a read-only check, F for a fix, D for a decision write-up. A D item lays out
  the options and their costs; the decision itself stays with the human.
- Split work orders by agent role and by when they run: checks, coding fixes and tests, a docs
  pass, decision write-ups.
- Open each work order with where it came from, who it is for, and its rules. A checks order says:
  change nothing, answer by ID, cite file and line as of a named commit.
- Leave Decide and Learn items out of every work order.

## Keep memory out of the blind pass

- During the file turns, read only the memory the session needs to run commands: the machine and
  shell notes.
- At COMPARE, read the project's memory file as a third reference, after the code and the plan.
- Write nothing from memory into a repo file. A finding that memory shaped is written in the docs'
  terms.
- Never write a person's or company's name from memory into any output file. At COMPARE, scan the
  reviewed files for any such name; each hit is a finding.

## Run it where the reading is comfortable

- Run reviews in a chat interface while the human is learning the stack, and hand it files
  directly. Handing over files enforces blindness: the reviewer never has the plan until it is
  given one.
- Run the work orders in a coding agent on the machine that holds the repo.
- Move reviews into the coding agent once fetching files costs more than reading them.
- Keep the prompt portable. Where the reviewer can't run a command, it prints the command and the
  human pastes the output.

**Consequences**
- Fixes start after the review, not during it. The human works their Learn list while the agents
  work the queue.
- The human carries the plan in their head through the blind pass, and answers "already decided"
  by hand.
- The EXPECT list and the COMPARE turn cost tokens on every review. The tally is what pays for
  them.
- Until COMPARE, the reviewer can't flag a private name it doesn't know. A mechanical
  private-words check is the backstop.
- The reviewer and the coder are the same model, so their errors are correlated. A fresh session
  removes anchoring, not shared blind spots. Today the human's blind read, the spec and the tools
  are the checks that don't share them. The found-by column is how the size of this gap gets
  measured before anything more is spent on it.

**Alternatives considered**
- **Informed review: the plan first.** Cheaper, with no double finds. It verifies the code against
  the plan, and can't see the plan's own gaps.
- **Fully blind: never the plan.** Finds gaps, but can't check done-when items, and argues again
  with decisions already made. COMPARE keeps the blind pass and adds the check.
- **Review with repo access: a connector, or a coding agent in the repo.** Less fetching, but
  blindness then depends on the agent obeying the prompt, and long teaching replies are harder to
  read in a terminal.
