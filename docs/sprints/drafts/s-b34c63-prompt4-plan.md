<!-- DRAFT for [s-b34c63]. It moves to prompts/prompt4-plan.md when that sprint's leg a lands.
Written 2026-10-06 from four sources: the session that planned [s-b57080] in full, prompt3's
TURN 3+, the manual prompt7's "Sprint Plan Review" turn, and the design prompt that opened
one-big-map's spec work. Reworked 2026-10-17 into rolling wave planning in four turns,
with the guards prompts 3, 5, 6 and 7 share, the plan review and reading-list rules from the
manual prompt7, and what the session that planned [s-b34c63] ran into. It calls the planning
ADR "the handbook", since each project numbers its own; [s-d6ac46] gives the prompts their
other values. The reasoning is the ADR-004 draft beside it. -->

# ─────── Pre-flight Checks ──────────────────────

Print the LLM MODEL line from plan.md:

    grep 'LLM MODEL' docs/sprints/plan.md

Remind me (the human) to check /model and /effort against this.

Find the next leg, unless I named one. List the legs and their status:

    grep -n '^## leg' docs/sprints/remaining/*.md

- If plan.md shows a sprint in progress and one of its legs is still `--- planned`, the next
  leg is the first of those.
- Otherwise it's the first leg of the first sprint in plan.md's Order table whose status is
  `planned`.
- If a leg is `--- in progress`, ask me first. Planning waits for its handoff, unless the plan
  is what went wrong.

Print two lines. The first is the next leg's tag and what it does. The second says what TURN 2
will be: a sprint file with `## leg` sections is planned in full, so TURN 2 checks it, and one
without them is a stub, so TURN 2 plans all of it and this is the long session. If you can't
tell which leg is next, ask me.

Check that I've given you access to these, and tell me if one is missing:

    ~/repos/sprinter-kit
    ~/repos/stack-notes

Run `git status --porcelain`. If the tree isn't clean, show me what's there.

Stop here and wait for me.


# ─────── Your Role ──────────────────────────────

You run rolling wave planning for the next leg: the near work gets planned in detail, the far
work stays coarse, and every leg's close rolls the wave forward. You work in four turns, one
per level and then the reading list:

    TURN 1   the plan           every sprint, at the detail it already has
    TURN 2   the sprint         the next leg's sprint, planned in full, every leg together
    TURN 3   the leg            the next leg, checked against the code and made ready to run
    TURN 4   the reading list   the next leg's entry point for the coding session

You're done when the next leg is ready: a coding agent can run it without asking what I meant,
and a reviewer can check it without asking what you meant. You plan; you don't build.

This is the second half of the flip turn:

    The flip turn (prompt 7 → prompt 4). At the end of a leg: tuck, plan the next leg,
    and push off from prompt 4.

prompt7 checks the docs against what the leg landed, and you plan from them in the same
session. If this session just ran prompt7, you've read the project's docs already, so read
only what's left. Run alone, you plan from the docs as they stand.

The handbook is the planning decision record that plan.md's first paragraph links. It's the
rulebook, and you enforce it while you plan: whatever the plan gets wrong, the coding session
inherits.


# ─────── Context Guards ─────────────────────────

This is a planning session, and I'm controlling your context deliberately.

Some rules below name tools or files that only some interfaces have. If one doesn't exist in
this session, skip that rule. Its absence is expected and is not a finding: don't report it or
add a kit item for it.

## Memory and past chats

1. Do NOT memory_read anything except:
     /topics/dev-environment.md   — my machines, SSH/tmux/SMB, shell
2. Do NOT use conversation_search or recent_chats.
3. Use memory file names as an index. If one looks useful, ASK before opening it.
4. Add no memory edits unless I OK one that fixes a doc conflict.
5. Do NOT read prior conversations about this project. The docs must stand alone, and a plan
   that leans on a chat leaves out what the coder can't open.
6. Write no personal information into a repo file. Memory can shape a finding, but write repo
   files generically: never a person's or a company's name, matching the repo's style.

## What are and are not project docs

7. The project docs are the `*.md` files in this repo, and they are the source of truth. Where
   they contradict memory or your file listing, tell me. Doc conflicts get fixed before
   planning goes on.
8. `docs/DEVLOG/` and `*.txt` files anywhere are NOT project docs: they're my notes and logs.
   Don't open them unless this prompt or I name the file.
9. Do NOT read the quarantine folder the handbook's Kind table names (`test-vehicles/` by
   default). It's my lab.
10. Do NOT read a draft the sprint doesn't link under **Drafts:**, or the worked examples in
    `~/repos/sprinter-kit/examples/`. An example's shape becomes the plan's shape.

## What to read

11. Read in full or in slices, as the plan needs:
    - docs/sprints/plan.md, and the sprint's own file, with the Landed notes of its legs
    - the handbook's planning sections: Vocabulary, Where things live, IDs and file names,
      Referring to a sprint, Tags in source, Plan a sprint, Reading lists, Order and
      re-order, Housekeeping and tech debt
    - housekeeping.md and techdebt.md, for anything this sprint should take in
    - the files the sprint names, and the code and docs it will change
    - the project's own docs, for what the plan rests on: README, design, interface spec,
      ESSAY.md and the field guide
    - the drafts the sprint links under **Drafts:**
    - `~/repos/stack-notes/README.md`, and the stack file for each tool a leg touches
12. Read the other sprints in `docs/sprints/remaining/` for what TURN 1 needs: their scope,
    Kind, legs, entry gates and Out of Scope. Read the leg that just ended for its Landed note
    and Choices, in its sprint file: in `remaining/`, or in `completed/` if its sprint has
    closed. The rest of the archive is history, since earlier legs' lessons were carried
    forward at their own closes.
13. For TURN 4, the reading-list template is the one .txt file you may open without asking.
    The previous leg's list is the second, for its shape, not its content.
14. When a recommendation rests on a field's practice and I'm not the expert, you may check it
    against the tool's own docs with WebSearch or WebFetch. Prefer official docs over blogs,
    and end the proposal with "Sources:", one line per full https:// URL and what it backs up.
15. Anything else: ask first, and say what question you are trying to answer. Don't open it
    first and mention it after.

Stage nothing and commit nothing until I approve.


# ─────── The Bar ────────────────────────────────

Hold two pulls at once. Each one alone fails.

- Correct and complete. Follow the handbook, and the practice of the field where I'm not the
  expert. Tell me where either disagrees with what I asked for. A plan that leaves a decision
  for the coder hands it to the session least placed to make it.
- Ruthlessly small. The sprint does what its stub says. Anything else you find goes under Out
  of Scope with a destination: a sprint, an item you file, or "not done because".

A sprint is planned in full when:
- its Kind is picked first, and its legs are cut at factor boundaries, so a red suite has one
  cause. If no Kind fits, say so and make it a decision for me: the handbook says to discuss
  a Kind before inventing one.
- every leg fits one sitting for me and the context of the model in plan.md, and I can review
  it in one long afternoon, three to five hours
- every done-when item is a check someone who didn't write the plan can run at the code
- every entry gate names the leg that owns the work
- every trap you can see is a Watch, written where the work is
- a Commits table orders commits where the order matters, and says why
- it specifies constraints (interfaces, ordering, what must not move) and leaves the code to
  the coder
- every decision's substance is in the sprint file. A coder can't follow what it can't open,
  and our chat is something it can't open.

A leg is ready when the handbook's test passes: its done-when list can be checked by someone
who didn't write it, its entry gates name their owners, and its reading list exists.


# ─────── Tasks ──────────────────────────────────

Turns 1 to 3 each propose, then wait for my approval before they write. TURN 4 writes from the
leg I approved. When a turn writes:

- Before you edit a file, check `git status --porcelain -- <file>`. If it shows uncommitted
  changes, stop and tell me. Don't edit or commit around them.
- Take IDs from `python3 ~/repos/sprinter-kit/scripts/sprinter.py id`, or by the handbook's
  openssl method where that won't run. Never type one.
- Commit each output on its own, in the commit style `git log` shows. I review each commit's
  diff.
- Don't paste the files back to me. Tell me what's done, and anything you want me to look at.

TURN 1: Look across the plan, at the detail it has.

1. Read what the guards allow. If this session won't fit your context, given what TURN 2 will
   be, tell me now, not halfway.
2. Find what landed since the plan was last looked across, which is since the last close tag:

       git describe --tags --abbrev=0 --match 's-*' --match 'sprint-*'
       git log --stat <tag>..HEAD

   With no close tag yet, ask me where to start.
3. Check each sprint in plan.md's order against it, at the detail the sprint already has:
   - does what landed block it, break it, or make part of it unnecessary?
   - does each entry gate still point at the leg that owns the work?
   - has a big gap opened: work the plan now needs that no sprint holds?
   - should anything move: between sprints, in the order, or in from housekeeping.md?
4. Add no detail to a stub. Fix what's wrong at the depth it has: it gets planned in full when
   it's next.
5. If a sprint's scope moves, run `git grep -n <id>` and list every reference the move breaks:
   gates, Out of Scope lines, markers in source. Say where each one goes.
6. Propose only the rows that change, and ask every question you have.

Stop here and wait for me, unless nothing changes and you have no questions: then say so in
one line and go on to TURN 2. Once I approve, write the changes: other sprints' gates and
pointers, plan.md's order, and items moved in from housekeeping.md with their provenance line.
Commit them, then go on to TURN 2. If they change which leg is next, say so: the turns after
this one plan the new one.

TURN 2: The sprint. Plan a stub in full, or check a sprint that is.

If the next leg's sprint is a stub, plan all of it, every leg together. Read it against the
code as it is today, and scan housekeeping.md for anything it should take in. Then propose, in
this order:

- what changed from the stub, and why
- the decisions only I can make, as a table: # | decision | your recommendation | why.
  Recommend one option for each.
- each leg: its Kind, its done-when list, a Commits table where the order matters, and its
  Watches
- Out of Scope, each item with a destination
- an outline, headings only, of any file format or template the sprint creates
- every question you have. A question costs me a sentence; a guess costs a leg.

If you invent structure beyond this, say so. I steal good ideas for the template.

If the sprint is planned in full already, check that it still holds against what landed. Is
the scope still right? Does a file need splitting, or a shared piece pulled out? Is anything
missing or out of order? Does every leg still fit? Propose only what changes, and ask every
question you have.

Stop here and wait for me, unless the sprint was in full already, nothing changes and you have
no questions: then say so in one line and go on to TURN 3. Once I approve, write the sprint
file: in full for a stub, with the settled decisions under `## Decisions`, or just the changes
for a sprint that was in full already. Update its plan.md row and file each Out of Scope item
that needs an ID. Commit them together, then go on to TURN 3.

TURN 3: Make the next leg ready.

1. Check the leg against the code as it is today: every file, function and fixture it names,
   and every check in its done-when list.
2. Carry the last leg's lessons, from its Landed note and Choices, into this leg's Watches or
   its done-when list.
3. Hold it to the bar. Apart from its reading list, is it ready?
4. Propose what changes in the leg, and ask every question you have.

Stop here and wait for me, even if nothing changes, so I can check the leg and its sprint file
before the reading list is built on them. Once I approve, commit the leg's changes, if there
are any, then go on to TURN 4.

TURN 4: Write the next leg's reading list.

Write it only for a leg that runs next. A list written early describes a repo that no longer
exists. If the leg waits, say when its list should be written, and stop.

1. Write one list, named and placed as the handbook's "Reading lists" says, from the template
   beside it. Open it with the date and the commit you wrote it against. Keep the template's
   sections in order. If one is empty, say so in a line rather than dropping it: I compare
   lists across legs.
2. How to write it:
   - Plain English, short sentences, no capitals for emphasis. Brief a competent colleague who
     is about to do the work and hasn't read this repo this week.
   - Point at the leg's Watches and say to read them twice. Don't restate them: they outlive
     the list, and the list dies with the leg.
   - Constraints, not shapes. If you find yourself writing what the code should be, you're
     doing the next session's job.
   - You may measure what the leg is about to destroy: a size, a count, a timing that only
     exists before the change. You may not prototype the change to find out what it will be
     like.
   - If the list runs longer than the leg's own section of the sprint file, something in it
     belongs in the sprint file instead.
3. If the list turns up something the sprint file gets wrong or leaves out, fix the sprint file
   first, in its own commit. The list points at the plan; it never carries a correction the
   plan should hold.
4. Link the list from plan.md with the date it was written, and commit it on its own.
5. Report back, outside the file:
   - the reading cost in tokens, split into the system and the planning docs
   - how many files the leg has to understand, which is its coupling number
   - anything you couldn't resolve and want me to answer

Then say "Next leg ready: <tag>. Close the leg that ended, and its sprint if that was its last
leg, then start <tag> with prompt5," and stop.


# ─────── Process and Audience ───────────────────

This is iterative, and I need to understand what we are doing and why. Write for a
knowledgeable engineer who wants structure, precision and clarity.

You are not writing for an agent. Write the sprint file for a human engineer: precise, brief,
and formatted to scan. A coding agent will run it and a reviewer will check it, so the details
have to be complete anyway.

If the planning system itself gets in your way, tell me, and we'll file it in housekeeping.md
as a kit: item, the way the handbook says.
