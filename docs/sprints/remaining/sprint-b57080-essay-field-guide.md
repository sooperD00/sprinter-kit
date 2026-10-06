# Essay and field guide templates

**ID**: `[s-b57080]`
**Status**: in progress

Ships `docs/ESSAY.md` and `docs/field-guide.md` as templates that init writes into any project that doesn't have them, and carries the field guide's entry rules back to one-big-map.

**Kind:** feature, then a migration. Leg a builds in the kit, with the commits ordered so every one leaves init working. Leg b carries the change to the kit's first consumer.
**Legs:** a lands everything in the kit. b changes one-big-map, the first project to take a kit change through a carry-back branch. They meet at a merged kit commit, so a problem in one-big-map never hides a problem in the kit.
**Entry gate:** none.

**Why now** It's the smallest change in the plan, and the first to run the carry-back process end to end: a kit change, a `kit-sync/` branch in one-big-map, and a Carry back line marked merged. Every later sprint takes the same path.

**Brings in:** `[h-f44ef7]` from one-big-map's housekeeping.md.
**Carry back:**
- one-big-map, on branch `kit-sync/b57080` — pending

## Decisions

Decided in planning, 2026-10-06.

- D1. A repo that already has `docs/ESSAY.md` or `docs/field-guide.md` keeps it. init leaves the file alone, lists it, and writes everything else. A dangling symlink at either path still stops init, as any blocked path does.
- D2. The handbook doesn't change. Neither file is a planning file, and reviewers reach the field guide through pointers in the code. So this repo's own copies have nothing to carry back.
- D3. The field guide's entry rules live in a comment in its template, and the comment says to keep it. People read the field guide for its terms; agents read the raw file. prompt6 and prompt7 restate these rules today, until `[s-b34c63]` points them at the comment. The rules:
  - The test: could a strong engineer with no background in this domain tell whether a line of code is right? If not, and what's missing is domain knowledge rather than code knowledge, it's an entry.
  - Look for numbers and limits with a domain reason; orders and conventions that come from a standard or a data source (axis order, units, ID formats); deliberate omissions that look like bugs; domain names and acronyms in identifiers, docstrings and comments; standards cited with no explanation.
  - Skip language and library mechanics, which are code knowledge. Why the project chose one thing over another belongs in design.md or a decision record.
  - Group entries under an area named with the standard or source it follows: `## Dates (ISO 8601)`. Under the heading, "Used by:" names the modules that rely on it. Lead each entry with a bold claim, then explain it.
  - Point code at the area once per module, from the highest docstring that covers it: `(See docs/field-guide.md#dates-iso-8601.)` GitHub builds the anchor from the heading: lower case, punctuation dropped, spaces as hyphens.
- D4. The essay's "what goes in it" line lives in its HOW TO comment, which is deleted once the essay is written. A line about the file reads oddly at the top of a public essay. The field guide keeps its line visible, as one-big-map's does.
- D5. No opt-out flag. A project that doesn't want either file deletes it before committing. init never commits, so that costs nothing.
- D6. An implementation-plan template is out of scope: `[h-8976df]`.

**Template outlines**, approved with the decisions. Placeholders are in angle brackets.

```
templates/docs/ESSAY.md

# <The claim, in a few words>
<!-- HOW TO USE THIS FILE: the argument this project makes (what people assume about the
problem, what is true instead, and how the design follows). It is the page you link when you
share the project. How it differs from README (what the project is, how to run it) and
design.md (why each choice was made). Delete every comment as you fill it in. -->
<The common picture of the problem, and where it breaks.>
## <Something true instead, stated as a claim>
## Where this comes from
## What this does not claim
```

```
templates/docs/field-guide.md

# Field guide
Domain terms a reviewer may not know, how they relate, and where they bite.
<!-- HOW TO ADD AN ENTRY. Keep this comment. The rules in D3. -->
## <Area> (<the standard or source it follows>)
Used by: `<module>`
**<A claim about a term.>** <What it means, and where it bites.>
```

## leg a — the templates, and init leaving a project's own copies alone (feature) --- handed off 2026-10-06

**Done when**
- [x] Before commit 1, the files `init --greenfield --no-phases --model test` writes into a fresh scratch repo are on record (commit 0). After the leg, the same command writes that list plus `docs/ESSAY.md` and `docs/field-guide.md`, and nothing else in the list changes.
- [x] In a scratch repo that already has `docs/ESSAY.md`, init writes everything else, leaves the essay unchanged (the same `git hash-object` before and after), lists it as left alone, and exits as it would in a repo without one.
- [x] A dangling symlink at `docs/ESSAY.md` still stops init: exit 2, nothing written.
- [x] scan, in the repo that has the essay, reports it as here already and the field guide as one init will write.
- [x] The two files init writes match their templates byte for byte (`cmp`), and `grep -n '{{' templates/docs/ESSAY.md templates/docs/field-guide.md` finds nothing.
- [x] `git grep --untracked -niE 'one-big-map|parcel|apn|crs84|faab97' -- templates/docs/ESSAY.md templates/docs/field-guide.md` finds nothing. (`templates/docs/decisions/ADR-NNN-review-files.md` still names faab97. `[s-a0f5d1]` leg b clears it.)
- [x] The essay's HOW TO comment says what goes in the file, how it differs from README and design.md, and to delete the comment. The field guide's line under its title says what goes in it, and its entry-rules comment holds the rules in D3 and says to keep it.
- [x] Each of these names both files: README ("What's in it", or the paragraph after it), interface-spec (Files, Kit blanks, and the list of what stops init), design.md (the exception to "anything in the way stops it", and why these two files ship) and SKILL.md (step 3: init writes both, and they are the person's to write).
- [x] `python3 -c "import ast; ast.parse(open('scripts/sprinter.py').read(), feature_version=(3, 8))"` passes.

**Commits**
| # | | |
|---|---|---|
| 0 | ground truth | the file list init writes in a fresh scratch repo today (an artifact, not a commit) |
| 1 | `feat(init): leave a project's own essay and field guide alone` | the rule, and scan's report of it. No template exists yet, so no repo sees a change. |
| 2 | `feat(templates): essay and field guide` | init now writes them where they're missing |
| 3 | `docs: what init writes for a project's essay and field guide` | README, interface-spec, design.md, SKILL.md |
| 4 | `docs(sprints): hand off s-b57080 leg a` | the done-when ticks, Choices, Landed and the handoff date |

**Watch** The order is the safety property. The rule lands before the templates, so no commit makes init refuse a repo that already has an essay. Derive what scan reports from the templates that exist, so commit 1 changes nothing anyone can see.

**Watch** design.md says "Anything in the way stops it." These two files are the exception. Write the exception where that rule is stated (design.md, and interface-spec's list of what stops init), or the next reader restores the old rule.

**Watch** Every kit template says to delete its comments as you fill it in. The field guide's entry-rules comment is the one that stays, and it has to say so itself.

**Watch** Keep both templates thin. The field guide rests on one example, and the essay on two with different shapes. Give each its purpose, its rules and a skeleton, and nothing neither example has. Take nothing from one-big-map, whose domain would become the template's shape. Where an example helps, use a neutral one, like `## Dates (ISO 8601)`.

**Watch** sprinter.py supports Python 3.8: no `str.removeprefix`, no `match`.

**Choices**
- `PROJECT_DOCS` in sprinter.py lists the two docs, as a tuple of repo-relative paths beside `JUNK`. `own_copy()` is the one test for a project's own copy, shared by scan and init so scan reports what init does. It uses `os.path.isfile`, which follows symlinks: a symlink to a file counts as a copy, and a dangling symlink or a folder falls through to `blocked()`.
- init lists kept files under "Left alone, because the repo has its own", with the decisions block's pointer to the kit's `templates/` folder. The block sits just before the decisions block, so the two lists of files not written read together.
- scan prints a `project docs` line for each shipped template, after `planning docs`: here already, not found, or `blocked()`'s reason followed by "so init will refuse to write".
- The exception to the stop rule also went into sprinter.py's module docstring, which `--help` prints. The init subparser's help doesn't state the rule.
- The templates write their placeholders as prose, the way sprint-template.md writes its title, with no angle brackets. Three of the outline's bracketed placeholders parsed as HTML tags and vanished when rendered, and the rest rendered only because each held a comma.
- The field guide's comment carries D3's rules in D3's words, with the "Look for" list as bullets. It opens with "Keep this comment" and D3's reason.
- design.md states the exception under "Templates mirror the target tree", and the why in a new section after it, "The essay and the field guide".

**Landed.** Plan: the rule, then the templates, then the docs, so every commit leaves init working. Happened: the check against the code, before any write, found three gaps. D3's rules lived only in files the reading list barred, the term grep already failed on another template, and sprinter.py's docstring states the stop rule too. d9eba25 fixed the plan, and the leg then landed as planned, with the handoff as a fourth commit. Before review, the templates' placeholders moved from angle brackets to prose, and init's help now names the essay and field guide. Every done-when check passes in fresh scratch repos, and init's final file list is the ground truth plus the two docs. The Choices block is new structure: it holds the calls the plan left to the leg. Lesson: a reading list assembled by reading can bar the one file a decision rests on. Put a decision's substance in the sprint file, not a pointer to a file the leg may not open. An outline's notation is not template syntax: render a template before approving it.

## leg b — carry back to one-big-map (migration) --- planned

**Done when**
- [ ] one-big-map's `kit-sync/b57080` branch changes exactly two files (`git diff --stat main...kit-sync/b57080`): the entry-rules comment sits under `docs/field-guide.md`'s first line, and `[h-f44ef7]` is gone from `docs/sprints/housekeeping.md`.
- [ ] Its pull request names the kit commit it carries back.
- [ ] Once that pull request merges, this file's Carry back line reads `merged YYYY-MM-DD <sha>`.

**Commits**
| # | | |
|---|---|---|
| 1 | `docs(field-guide): the kit's rules for adding an entry` | the comment, copied from the kit's template, under the field guide's own first line |
| 2 | `docs(sprints): clear h-f44ef7, carried back from sprinter-kit` | the housekeeping line |

**Watch** one-big-map has other agents working in it. The carry back is a branch and a pull request, never a push to main. Branch from main as it is that day.

## Out of Scope
- prompt6 and prompt7 restate the field guide's entry rules → `[s-b34c63]` points them at the template
- whether planners read the essay → `[s-b34c63]`, whose contract decides what each prompt reads
- an implementation-plan template → `[h-8976df]`
- [~] a field guide for the kit itself: not done because the kit's terms already live in its handbook's Vocabulary and its ESSAY
- one-big-map's essay and field guide as filled examples in `examples/` → when one-big-map goes public
