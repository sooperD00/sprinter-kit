# Notes on sizing model legs and gating design

Draft for `[s-484bd5]`, and for the test habits in `[s-06c862]`. From DEVLOG, 2026-10-05, during one-big-map's faab97 leg-a coding session. Kept as written.

```text
10/5/2026 11:35a
one-big-map-20261001: cc sprint-faab97-foundation.md -- leg a -- CODE
sizing-appetite-modeling-and-design-gating-20261005.txt

- [ ] new Kind = contract / models, see below
- [ ] separate, additional planning session after the "first" on specifically for
	the models / contract following the rules below
- [ ] count new decisions during code plan, and abort if > NEW_DECISION_LIMIT
- [ ] run the test to check it fails first (TDD isn't the default with claude, huh)
- [ ] -> you need a test guidance ADR for Claude

---

good job keeping track of everything. But how's your context? there's 3, 4, 5, and
 6 to get through. Maybe (maybe) tests are easier while data models are hard, since 
they are pure spec and each token really defines so much of the app in terms of functionality and correctness... I'm thinking of giving guidelines to my planner 
and the sprinter-kit planning system to treat data models are more expensive than 
other code, not exactly sure how to deal with this, still muddling on it. What do 
you think? And then... check your context... when I have feedback on commits 3-6, 
will you have room left to implement with good judgement and accuracy?

---

_ My context: I can't see a meter, so this is an estimate. The token count I'm shown 
is the session's overall budget, not my working window. This conversation is long: 
every spec read, diff, decision file and test run is in it. When it gets long enough, 
older turns get summarized. That's where the risk sits: the details most likely to blur 
are the early, fine-grained ones, and those are exactly what a review of commits 3_6 
leans on.
  For example:
  - why Dossier has *_given fields
  - why parcel_id is a NamedTuple
  - which "" tests are canaries

  What I'd do with your feedback on 3_6:
  - Small, local fixes (add a test, rename, tighten a message): fine here.
  - Anything that touches a decision (how a rule is enforced, a model's shape, 
a new spec question): start a fresh session with a short reading list. The durable 
state is already in the repo, which is the planning system working as intended:
    - the spec and the sprint file's Decisions and Follow-up
    - the commits, which each say what they did and why
    - your r-, a- and leg files

    A fresh session reading those will judge better than this one recalling them 
from a summary. Its reading list would be your review notes, the files under review, 
and the spec sections they implement.

On models costing more: I agree, and this leg is evidence. But the cost wasn't in 
writing the code. Leg a's code fit easily, and the tests were the cheapest part, 
because most are rows copied from spec tables. The cost was decisions the spec hadn't 
made, surfacing one at a time:
  - 8 gaps in turn 1
  - D1_D11 and F1_F10 in review
  - the JSON-NaN gap and the nullable-unit trap while building

  Each one changed what every later sprint will see, and that's why each was expensive. Models are where the spec gets tested against reality, and every gap turns into a decision.

  For the planner, I'd suggest these, roughly in order of payoff:

  1. Interrogate the spec before the model leg, not during review. Give the planner a 
per-field checklist, built from what this leg actually hit:
     - type and nullability, in both directions (G6)
     - blank versus absent (D6)
     - units, and where they're declared (D3)
     - ranges
     - serialized form (whole seconds, Z, int versus float)
     - enum membership and ordering (D5, D9)
     - cross-field rules (D4)
     - Python input versus JSON input (the strict-mode loading rule, NaN)
     - evolution: what an added field does to stored rows (the cache miss)

 The C1_C8 checks your reviewer ran were this checklist, discovered late. Run at 
planning time, it turns  review findings into planning decisions, which ADR-001 already 
says are cheaper.

  2. Treat removing an enum member, or changing a field's type, as one-way. D5's 
point applies: removing breaks stored records, while adding is free. So model legs 
should prune before anything is stored, and planning should flag them as the last 
cheap moment.

  3. Size model legs by decisions, not by lines. Leg a "fit" by token count but held 
about 30 decisions. The appetite check for a contract leg could be "how many open 
questions does the checklist leave?", with a split when the answer is more than a handful.

  4. Make a few habits of this leg into standard gates for contract legs:
     - Run each new test against the code before the change, and see it fail. That 
	caught tests that couldn't fail.
     - Probe library behavior on the model's real field types, not toy ones. That's 
	the Landed lesson.
     - Write tests as rows traced to spec lines, so review reads tables, not logic.

  5. Possibly a Kind. "contract" doesn't fit ADR-001's table, since its order isn't 
	an import graph: it's spec gaps resolved _ test rows _ model. ADR-001 says 
	to discuss before inventing a Kind, so that's a question for later, not a
	recommendation.

  When you've settled your thinking, I can draft this as a kit: item, or as a checklist section for the reading-list template. I'd wait until after your review of 3_6, since that will either confirm the list or add to it.
```
