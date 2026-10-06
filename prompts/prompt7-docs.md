Please verify you are Claude Opus 5. Stop if you are not. Remind me, the human, to
check that extended thinking is on and at Max.

# ── READ FIRST: CONTEXT GUARDS ─────────────────────────────────────
This is a docs review session and I'm controlling your context deliberately.

1. Do NOT memory_read anything except these files:
     /topics/dev-environment.md   — my machines, SSH/tmux/SMB, shell

2. Do NOT use conversation_search or recent_chats.

3. The docs in the project folder are the source of truth for this project. 
   Where they contradict anything in memory or in your file listing, tell me 
   about the conflict -- we need to fix any documentation conflicts before 
   coding.

4. You can use the memory file names as an index to understand what kind of
   information is in them. That way, if you think information inside these
   files would help us, you can **ASK ME**, but don't open them until you ask.

5. Do not add any new memory edits during this session unless it is an 
   explicit fix from documentation conflict resolution and I have OK'd it.

6. Do NOT read any prior conversation about this project. The docs must
   stand alone — that is what is being tested.

7. Do NOT read any files ending in *.txt, especially anything in `docs/DEVLOG/`
   unless I specifically white-list the files for you. If you think it would be
   necessary or useful to read a *.txt file, **ASK ME** first.

8. Do NOT read anything in `test-vehicles/` — that is a lab for me to poke around
   in. Ignore this folder.

# ── 4. Docs Assessment ───────────────────────────────────────────
PROMPT (YOUR TASK):

Find the .md docs for this project and read them. You are in project root.

Then assess if the docs are stale (if they match or don't match the project) and 
let me know if you think I should do a docs update. Let me know if you think it's 
time that I split any docs, or add any new ones. Take your time, I'm going for a walk.

The main change was
***********
sprint-013-603d20-adopt-adr-021
***********

The next sprint is
***********
sprint-a75ff1-backend-dependencies.md
***********

AUDIENCE:
This is a public repo, but the application is for me, not for a portfolio project 
or an exam or assessment. I like to have a clean and professional repo, but I don't
like a lot of clutter if its not going to help me as a devloper later, or if it's not
going to help someone onboard as a collaborator or user later.


---

NOTES: 
If you see any notes tagged `nlr <date>`, those are mine. I may tag these with 
`DECIDED` = the answer; preserve the decision, and flag any doc that still calls it 
open. `DRAFT` = rewrite in house voice, keep the content. `PARK` = file it in the 
backlog, don't act. Untagged inline notes: ask before deleting. You may see none -- 
that's fine.

```
# Example good notes: draft or decided:
nlr 8/18 DECIDED  -- this is the answer. Formalize the wording, keep the decision.
                     If a doc still says the question is open, that doc is wrong.
nlr 8/18 DRAFT    -- rewrite this in house voice. Content is right, prose isn't.
nlr 8/18 PARK     -- a later maybe. Give it a home in the backlog, don't act on it.
```

---


DISCUSSION TURNS:
Confirm if my answers are clear and what you think about what I've said and asked.
Then wait for me to respond again before editing the docs.


AFTER:
If my answers are clear, then I agree with all your suggested updates.

OR

Great. We Agree.

Please execute the changes. Use a "docs: ..." prefix in the
commit messages. I'll review before we do more.

------------------------------
### Field-guide pointers

`docs/field-guide.md` explains domain knowledge (GIS, assessor data, and the other data layers) for reviewers who know software but not the domain. Find places in the code where a pointer to it would let a strong SWE judge whether the code is right.

**The test:** could a strong SWE with no domain background tell whether this line is correct? If not, and the missing piece is domain knowledge rather than code knowledge, it's a finding.

Look for:
- Numbers and limits with a domain reason (`min_length=4` on a ring).
- Orders and conventions that come from a standard or a data source (`(lon, lat)`, units, ID formats).
- Deliberate omissions that look like bugs, where a reviewer might "fix" correct code (winding order left unchecked).
- Domain names and acronyms in identifiers, docstrings, or comments (CRS84, Esri, APN).
- References to standards (RFC, EPSG, agency specs) with no explanation.

Skip:
- Language and library mechanics (Pydantic, typing, async). That's code knowledge.
- Why we chose X over Y. That belongs in `design.md` or `decisions/`. If the rationale is missing, list it under a separate "Missing rationale" heading.
- Spots already explained well in place, or already pointing to the right section.

Also check that every existing `docs/field-guide.md#...` pointer resolves to a real heading (GitHub anchor rules: lowercase, punctuation dropped, spaces become hyphens).

Report each finding as a table row:

| Location | What the reviewer needs to know | Field-guide coverage | Suggested pointer |
|---|---|---|---|

- Location: `path:line` or the symbol name.
- Field-guide coverage: the existing anchor, or `NEW` with a proposed heading and a one-sentence gist.
- Suggested pointer: where it goes (module docstring, class docstring, or inline comment) and the exact text, e.g. `(See docs/field-guide.md#geometry-geojson-crs84.)`

Rules:
- One pointer per concept per module, at the highest level that covers it. A module docstring beats the same pointer repeated on every line.
- Rank findings by risk. First come the ones where a reviewer would likely "fix" correct code or approve wrong code.
- Report only. Don't edit the code or the field guide.
- If there are no findings, say so in one line.

Calibration: `onebigmap/contract/geojson.py` is the reference case. Its docstring points to `#geometry-geojson-crs84`, which explains why `Position` is `(lon, lat)`, why a ring needs at least 4 positions, and why winding order isn't checked. A real finding looks like that: a line that is correct for a domain reason a SWE couldn't guess.
---------------


# ── 5. Sprint Plan Review ────────────────────────────────────────
# (same chat as docs assessment, after docs changes are done)

Great. We've implemented the doc updates and the docs commits. Now we will move
on to "plan: ..." commits. 

Please review the next sprint leg:
***********
sprint-a75ff1-backend-dependencies.md
***********

Is the sprint scope still right? Any code files need split or DRY extraction? 
Any Anything missing or misordered in the implementation plan ordering? The units 
of work should fit the Claude Opus 5 Max Thinking context and memory window. The 
sprints should also be small enough that a human can review in one long afternoon 
(3-5 hours).

---

I agree with all your suggested updates. Make the changes using a "plan: ..." 
commit message. Then wait for me to give you the reading list prompt from the
prompt bank.

# ── 6. Reading List ────────────────────────────────────────

Finally, Make a reading list for this sprint leg.
Do not read docs/reading/reading-list-example.txt -- that's from another project
and you may write a better one now -- we'll compare them next turn 
Do read `prompts/readinglist.sh` and tell me if any part of it is useful.
This script is also from another project -- let me know if there is any part of of it
that we should use to make a script for this project, or if it's no longer necessary
since we've specified a lot of rules in ADR-021.

---

Now that you have done your own work, read:
***********
docs/reading/reading-list-example.txt.
***********

What is the difference between the two styles and decisions in your file and this
one from another project?

---

[similar to the one in docs/reading/reading-list-example.txt.]

[Finally, would the next agent, a coding agent, benefit from a reading list, or is the 
codebase small enough to skip the reading list assembly step? I have a script
I can use to do this if you think it's necessary -- tell me and I'll share it.]

---

AFTER:
[If the above is clear and you agree with me, then]
I agree with all your suggested updates. Make the changes using a 
"plan: ..." commit message.


 # ── 6. Reading List ────────────────────────────────────────
  PROMPT (YOUR TASK):

  Write the reading list for the next leg to run:
  ***********
  [s-<id>-<leg>]
  ***********

  Read first: that leg's sprint file, docs/sprints/plan.md, and ADR-021's
  "Reading lists" section. Then the files the leg names. Read the previous
  leg's list for its shape, not its content.

  Write one file: docs/reading/reading-list-for-<id>-<leg>.txt
  Open it with the date and the commit you wrote it against.
  Keep these sections, in this order. If one is empty, say so in a line
  rather than dropping it _ I compare these across legs.

    THE ONE RULE             the seam, in two or three sentences. The thing
                             that, if violated, means the leg did the wrong
                             work. Name the leg that owns what it excludes.
    BEFORE YOU START         commands with expected results, and "if one
                             comes back wrong, say which and stop". Include
                             state the repo cannot show: dashboard settings,
                             gitignored files, whether the suite is already
                             red.
    WHAT YOU ARE DOING       the commits, in order, one line each, and what
                             orders them.
    READ THIS                   files and ADR sections, each with why and what
                             to look for. Name the ADR sections to skip as
                             well as the ones to read. Split the files into
                             ones the leg edits and ones it only reads.
    DO NOT READ              only the ones someone would reasonably reach
                             for, each with a reason. Where a file is off the
                             list because it is generated or huge, give the
                             command that answers the question instead.
    WHAT THIS LIST CANNOT SEE   the honest limits, including what the plan
                             left open on purpose.
    WHEN YOU ARE DONE        the handoff, in this leg's terms, pointing at
                             ADR-021 rather than restating it.

  How to write it:

  - Plain English, short sentences, no capitals for emphasis, no drama.
    Brief a competent colleague who is about to do the work and has not
    read this repo this week.
  - Point at the leg's Watches and say to read them twice. Do not restate
    what they say. They outlive the list; the list dies with the leg.
  - Do not design the implementation. Constraints, not shapes. If you find
    yourself writing what the code should be, you are doing the next
    session's job and wasting both of us.
 - You may measure what the leg is about to destroy _ a size, a count, a
    timing that only exists before the change. You may not prototype the
    change to find out what it will be like.
  - Report the reading cost in tokens at the top, and split it: how much is
    the system, how much is the planning docs.
  - If the list runs longer than the leg's own section of the sprint file,
    something in it belongs in the sprint file instead.

  If planning turns up something the sprint file gets wrong or leaves out,
  fix the sprint file first, in its own commit, prefix "plan: ". The list
  points at the plan; it never carries a correction the plan should hold.

  Then link the list from plan.md with the date it was written, and commit
  it on its own, prefix "reading lists: ".

  Report back to me, outside the file:
    - the token cost, split system vs process docs
    - how many files the leg has to understand, which is the coupling number
    - anything you could not resolve and want me to answer

  Four things in there are deliberate, in case you want to adjust them before it goes in the bank:

  - "Point at the Watches, don't restate them" is what keeps the list from becoming the example. Judgment belongs in the
    sprint file because it survives; the list is thrown away at close.
  - "Measure what the leg destroys, don't prototype the change" is the line between the 355MB baseline and sandbox-coding.
    It's the one rule that stops a planning agent from doing the build to find out how the build goes.
  - "Fix the sprint file first, in its own commit" is the part that makes this repo different from the old project. A
    finding gets patched into the plan, where the next planner sees it _ not buried in a disposable list.
  - "If the list runs longer than the leg's section of the sprint file" is a cheap length check that fails in the right
    direction: it tells you content is in the wrong file rather than just telling you to cut.

  For a75ff1-c specifically, the "measure what the leg destroys" line will point somewhere different than it did here: leg c
  reads the freeze snapshots and then deletes them, so the cheap before-measurement is the dep_freeze.py compare output
  against today's lock, captured before the constraint block comes out.
