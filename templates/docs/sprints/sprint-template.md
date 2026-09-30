# The category of work, named the way a manager would recognize it next time

<!-- HOW TO USE THIS FILE
Copy it to remaining/sprint-<id>-<short-name>.md. Take the ID from sprinter-kit's `sprinter.py id`,
or from `openssl rand -hex 3` and the checks in {{adr}}'s "IDs and file names". Add the sprint's
row to plan.md in the same commit.

A stub is a legal sprint, and a sprint gets its file as soon as it has a name. For a stub, keep
the title, the ID block and one sentence, and delete everything below them. Everything from Kind
down gets written when the sprint is planned, in a session of its own.

Delete every comment as you fill it in. Delete any block that has nothing to say.
-->

**ID**: `[s-<id>]`
**Status**: planned
**Phase**: <!-- the phase this sprint delivers into --> <!-- kit:phases -->

<!-- One sentence: the change this sprint makes to the system. -->
**Kind:** <!-- feature | migration | refactor | upgrade | spike / investigation | bugfix, and what
orders the commits: the import graph, the consumer graph, the suite as the invariant, the lock. -->
**Legs:** <!-- each leg in a few words, and the factor boundary between them: which merge would
leave a red suite unable to say what broke it. -->
**Entry gate:** <!-- none, or the leg that owns earlier work this sprint leans on, as
[s-<id>-<leg>], required or recommended, before which leg here, and why. -->

**Why now** <!-- the cost of waiting. An ASAP sprint names the clock that is running. -->

## leg a — what this leg does (kind) --- planned

**Done when**
- [ ] a check that someone who did not write this plan can run at the code

**Commits**
| # | | |
|---|---|---|
| 0 | ground truth | what gets measured before anything moves (artifact, not a commit) |
| 1 | new beside old | what this commit does |

**Watch** <!-- a known trap, written where the work is. One Watch per trap. -->

<!-- At handoff, add under the leg:
**Landed.** What the plan said, what actually happened, and the lesson worth carrying.
and set the heading's status to `handed off YYYY-MM-DD`. -->

## Out of Scope
- something this sprint will not do → where it goes: a sprint's tag, a housekeeping or tech debt
  ID, or a named milestone

<!-- At sprint handoff, add a **Handoff**: YYYY-MM-DD line under Status and a closing section:
## Handoff, YYYY-MM-DD
- Every leg handed off, and `git grep 'SPRINT-<id>'` returns nothing.
- The housekeeping count.
-->
