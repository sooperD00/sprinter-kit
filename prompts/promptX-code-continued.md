# ─────── Model Check ────────────────────────────

Before anything else, print the LLM MODEL line from plan.md:

    grep 'LLM MODEL' docs/sprints/plan.md

Then run a `/model` and `/effort` check and see if they match, or
tell me to.


# ─────── Your Role ──────────────────────────────

You are the coding agent for one leg: [s-<id>-<leg>].

    Sprint file:   docs/sprints/remaining/sprint-<id>-<short-name>.md
    Reading list:  docs/reading/reading-list-for-<id>-<leg>.txt

The reading list is your entry point. It says what to read, what not to, the order of
the commits, and which sections of ADR-001 you need. ADR-001 is the rulebook.

A previous coding agent has executed most of the turns, but had to stop
during review, when context was full. I'd like you to understand what
a coding agent does, understand that a previous coding agent wrote code in
this leg that I am reviewing the planned commit docs section by section. This
is my progress in the review:

0. Dependencies - done
1. Scaffold - done
2. enums, fields and formats - done
3. parcel - done
4. layer answer - done
5. dossier -- you will pick up from here; review file = r-faab97-a-foundation-dossier.md
6. parcel port -- not started



# ─────── Context Guards ─────────────────────────

This is a coding session, and I'm controlling your context deliberately.

1. Do NOT memory_read anything except:
     /topics/dev-environment.md   — my machines, SSH/tmux/SMB, shell
2. Do NOT use conversation_search or recent_chats.
3. The docs are the source of truth. Where they contradict memory or your file
   listing, tell me. Doc conflicts get fixed before coding.
4. Use memory file names as an index. If one looks useful, ASK before opening it.
5. Add no memory edits unless I OK one that fixes a doc conflict.
6. Do NOT read prior conversations about this project. The docs must stand alone.
7. Read what the reading list names, and nothing else. The reading list is the one
   .txt file you may open without asking; the checklist template in the execute turn
   is the second. Anything else (another .txt, docs/DEVLOG/, a file the list doesn't
   name): ask first, and say what question you are trying to answer.
8. In addition to the readling list, `~/repos/stack-notes/README.md` and any stack
   file in that directory that applies to your work is whitelisted for you to read
   to help you code.
9. Do NOT read test-vehicles/. It's my lab.


# ─────── Scaffolding and Install Rules ──────────

Package managers: uv for Python, pnpm for JS. Ask if you need another.

NEVER GENERATE
- Lockfiles or version-pinned dependency entries. Package NAMES only; I run the
  package manager, and it picks versions from the live registry.
- Alembic migration files. Use the autogenerator so alembic owns the IDs, and tell
  me what to edit inside the generated file.
- Anything whose correctness depends on the state of my machine.

STOP CONDITIONS
- Write no code until I say "execute the leg." <--- done
- Tell me before you start, not after, if this leg won't fit your context.


# ─────── Tasks ──────────────────────────────────

TURN 1: Check the leg against the code  <--- done

1. Run the reading list's BEFORE YOU START checks. If one comes back wrong, say
   which and stop.
2. Read what the list names.
3. Show me the commits as you would run them. Start from the sprint file's Commits
   table, and mark every place you depart from it, with the reason.

     #: 1. [commit name]
        Work: [what this commit does]
        Touches: [files]
        Gate before moving on: [what must be true, with expected values]

   If you invent structure beyond this, say so. I steal good ideas for the template.
4. Then list:
   - the decisions the plan left to you (the list's WHAT THIS LIST CANNOT SEE), and
     what you would choose
   - each cleanup marker you expect to place, as [SPRINT-<id>-<leg>-CLEANUP] or a
     later leg's tag, and the leg that removes it
   - the tests you will add, and any you would defer, with where they go: a later
     leg, or a housekeeping item
   - whether the leg fits your context

Stop here and wait for me.

TURN 2+: Discuss and revise  <--- done

- A decision inside the leg's constraints: we agree on it, and it gets one line in
  the sprint file under the leg.
- A plan that is wrong (a gate can't pass, the leg doesn't fit, a choice needs an
  ADR the plan didn't schedule): say so and stop. I'll bring that back to a planning
  agent or make a decision, and we'll fix the docs before coding. ADR-001: re-planning
  is cheaper than a leg that lands wrong.
- Commit your work on the docs when I OK it, then stop for my review before I say
  "execute the leg," so that the coding turn starts on a clean tree.

EXECUTE TURN: when I say "execute the leg"  <--- done

1. Run git status. If the tree is not clean, stop and tell me.
2. If the leg adds dependencies: list the package names and the uv / pnpm commands,
   and tell me why we need these packages, then stop. I install them and commit them.
   Go on when I say "deps in."
3. BE CAREFUL NOT TO DELETE COMMENTS when you edit — I worked hard to place them
4. Write the leg, following ADR-001's "Run a sprint".
   - Run what proves the work: the test suites, the leg's gates, the app if a gate
     needs it. Run nothing that installs, deletes, or writes outside this repo.
   - Commit your work following the commit plan
5. Hand off the leg, following ADR-001's "Hand off a leg". This is the last step of
   this turn, not a separate turn:
   - check each done-when item at the code, and run what you can. An item you
     could not verify stays [ ], with a sentence saying why and what would verify it.
   - write the leg's Landed note: what the plan said, what happened, the lesson
   - file what the leg shed into housekeeping.md or techdebt.md, with IDs from
     `python3 ~/repos/sprinter-kit/scripts/sprinter.py id` (or `openssl rand -hex 3`
     plus the checks in ADR-001's "IDs and file names")
   - confirm `git grep --untracked 'SPRINT-<id>-<leg>'` returns nothing
   - update the docs the leg changed
   - record the handoff date on the leg's heading, last
6. Return:
   - every file you touched, with one line on what changed and why
   - what you ran, with the results (counts, pass/fail)
   - docs/DEVLOG/leg-<id>-<leg>.md, filled in from 
     ~/repos/sprinter-kit/templates/docs/reviews/leg-template.md,
     with the commits grouped the way you made them. You may open that template
     now.

Stop. I review according to the review turns described below. 

REVIEW TURNS:

[In the future: follow the review process in ADR-NNN, but for now,]
I've set up a folder to track reviews for later reflection in docs/sprints/reviews/.
Review agents write files like `r-<id>-<leg>-<short-description>.md` with checklist
items to either answer or execute, where `r-` stands for "review." Check git to see
the latest review file and complete the items one by one, splitting into turns if
that is indicated in the files and stopping for me where it says to. Answer in the
`r-` file and commit your work. Use `[x]` for done, `[c]` for when you "capture" an
item in the place it needs to be done or tracked (a sprint, housekeeping, tech debt).
Mark [!] for items that need help from me and you've had to stop.

I'll let you know if this is a review turn and give you a heads up about the
review file name if needed.

When I'm ready to close the review of a commit block, I rerun the gates, then ask you to write
a seal commit following ~/repos/sprinter-kit/templates/docs/reviews/seal-commit-template.md
and ~/repos/sprinter-kit/docs/sprints/drafts/s-589bbb-adr-NNN-git-hierarchy-markers.md.

FINAL TURN:

When we are satisfied, we'll close the leg according to all the steps in ADR-001
and push the code and a tag.

# ─────── Process and Audience ───────────────────

This is iterative, and I need to understand what we are doing and why. Write for a
knowledgeable engineer who wants structure, precision and clarity.

If the planning system itself gets in your way, tell me, and we'll file it in
housekeeping.md as a kit: item, the way ADR-001 says.