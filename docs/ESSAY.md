## Why this exists

I'm a process engineer. I spent thirteen years at Intel in yield and lithography, and then building data platforms behind that work. I kept meeting workflows that people said needed an engineer's judgment. Most of each one was procedure: the same lookups, comparisons and thresholds, in the same order. I built platforms that ran the procedure and left the judgment with the engineers.

Writing software looks the same to me. A change holds fewer real decisions than it feels like while you write it. The spec, the codebase's conventions, the import graph and the tests already determine most of each line. That's why language models predict code well, and why linters, formatters, code generators and CI took over work people once called judgment.

This kit finds the few real decisions, writes each one down where a human and an agent both read it, and turns the rest into procedure. Humans and agents read the same specs for how code, tests, reviews and docs are done, so quality comes from the process, not from the model of the month.

## Where the parts come from

Most parts of the kit are established practice:

| In the kit | Established practice | Source |
| --- | --- | --- |
| Appetite | Fixed time, variable scope | Ryan Singer, *Shape Up* (Basecamp, 2019) |
| Why now, Out of Scope | Shaping: the problem and its no-gos | *Shape Up*; Google's design docs; Amazon's working-backwards PR/FAQ |
| Entry gate | Definition of Ready; stage-gate review | Scrum practice; Robert G. Cooper's Stage-Gate |
| Legs ordered by the import graph | Topological order of a dependency graph; stacked diffs | Graph theory; stacked-PR workflows |
| One failure class per leg | Fault isolation; unconfounded causes | Design of experiments; `git bisect` |
| Kind | Change types | Conventional Commits |
| Done when | Definition of Done; acceptance criteria | Scrum; behavior-driven development |
| Watch | Pre-mortem; rabbit holes | Gary Klein, "Performing a Project Premortem," *Harvard Business Review* (2007); *Shape Up* |
| Landed: Plan, Happened, Lesson | After-action review | U.S. Army |
| Decisions | Architecture Decision Records | Michael Nygard, "Documenting Architecture Decisions" (2011) |
| Review checks before fixes | Root cause before corrective action | 8D problem solving (Ford) |
| Spec rule → test | Requirements traceability | DO-178C (avionics); IEC 62304 (medical device software) |
| Field guide | Explanation docs | Diátaxis (Daniele Procida) |
| Reflect loop | Plan-do-study-act; statistical process control | W. Edwards Deming; Walter Shewhart |

## What the kit adds

The parts are known. The kit's contribution is the assembly.

- **One document, two readers.** The sprint file is the agent's instructions and the human's acceptance criteria. A disagreement between them becomes a diff in the spec.
- **One failure class per leg.** Each leg adds one class of thing a failing suite can blame, so a red suite names its cause. In design-of-experiments terms, no two causes are confounded.
- **An after-action review on every leg.** Plan, Happened and Lesson are written before the next leg starts, so the gap between plan and outcome is on record where the next plan can use it.
- **Evidence before decisions.** Read-only checks run before fixes and spec decisions, and their answers cite file and line at a pinned commit.
- **The process is the control factor.** Taguchi's robust design tunes the factors you control so the result holds up against the ones you don't. The model is a noise factor: its version and sampling change outside my control. The kit puts the effort into specs, sizing rules, review formats and checks.
- **The loop closes on the process itself.** A reflect agent reads past reviews and proposes changes to the kit, the way statistical process control watches a production line.

## Status

This is v0. It grew out of one project and has run on a second. The reflect loop keeps tuning it.