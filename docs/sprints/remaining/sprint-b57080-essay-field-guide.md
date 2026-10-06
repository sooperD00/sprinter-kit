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
- D3. The field guide's entry rules live in a comment in its template, and the comment says to keep it. People read the field guide for its terms; agents read the raw file. The comment becomes the one home for the rules prompt6 and prompt7 restate today.
- D4. The essay's "what goes in it" line lives in its HOW TO comment, which is deleted once the essay is written. A line about the file reads oddly at the top of a public essay. The field guide keeps its line visible, as one-big-map's does.
- D5. No opt-out flag. A project that doesn't want either file deletes it before committing. init never commits, so that costs nothing.
- D6. An implementation-plan template is out of scope: `[h-8976df]`.

## leg a — the templates, and init leaving a project's own copies alone (feature) --- in progress

**Done when**
- [ ] Before commit 1, the files `init --greenfield --no-phases --model test` writes into a fresh scratch repo are on record (commit 0). After the leg, the same command writes that list plus `docs/ESSAY.md` and `docs/field-guide.md`, and nothing else in the list changes.
- [ ] In a scratch repo that already has `docs/ESSAY.md`, init writes everything else, leaves the essay unchanged (the same `git hash-object` before and after), lists it as left alone, and exits as it would in a repo without one.
- [ ] A dangling symlink at `docs/ESSAY.md` still stops init: exit 2, nothing written.
- [ ] scan, in the repo that has the essay, reports it as here already and the field guide as one init will write.
- [ ] Each file init writes matches its template byte for byte (`cmp`), and `grep -n '{{' templates/docs/ESSAY.md templates/docs/field-guide.md` finds nothing.
- [ ] `git grep -niE 'one-big-map|parcel|apn|crs84|faab97' -- templates/` finds nothing.
- [ ] The essay's HOW TO comment says what goes in the file, how it differs from README and design.md, and to delete the comment. The field guide's first line says what goes in it, and its entry-rules comment says to keep it.
- [ ] Each of these names both files: README ("What's in it", or the paragraph after it), interface-spec (Files, Kit blanks, and the list of what stops init), design.md (the exception to "anything in the way stops it", and why these two files ship) and SKILL.md (step 3: init writes both, and they are the person's to write).
- [ ] `python3 -c "import ast; ast.parse(open('scripts/sprinter.py').read(), feature_version=(3, 8))"` passes.

**Commits**
| # | | |
|---|---|---|
| 0 | ground truth | the file list init writes in a fresh scratch repo today (an artifact, not a commit) |
| 1 | `feat(init): leave a project's own essay and field guide alone` | the rule, and scan's report of it. No template exists yet, so no repo sees a change. |
| 2 | `feat(templates): essay and field guide` | init now writes them where they're missing |
| 3 | `docs: what init writes for a project's essay and field guide` | README, interface-spec, design.md, SKILL.md |

**Watch** The order is the safety property. The rule lands before the templates, so no commit makes init refuse a repo that already has an essay. Derive what scan reports from the templates that exist, so commit 1 changes nothing anyone can see.

**Watch** design.md says "Anything in the way stops it." These two files are the exception. Write the exception where that rule is stated (design.md, and interface-spec's list of what stops init), or the next reader restores the old rule.

**Watch** Every kit template says to delete its comments as you fill it in. The field guide's entry-rules comment is the one that stays, and it has to say so itself.

**Watch** Keep both templates thin. The field guide rests on one example, and the essay on two with different shapes. Give each its purpose, its rules and a skeleton, and nothing neither example has. Take nothing from one-big-map, whose domain would become the template's shape. Where an example helps, use a neutral one, like `## Dates (ISO 8601)`.

**Watch** sprinter.py supports Python 3.8: no `str.removeprefix`, no `match`.

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
