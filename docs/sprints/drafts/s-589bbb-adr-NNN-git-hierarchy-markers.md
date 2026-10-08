# ADR-NNN: Marking the sprint hierarchy in git

**Status:** Proposed (2026-10-07)
**Builds on:** ADR-021 (sprint planning)

## Context

ADR-021 nests the work four levels deep:

```
sprint > leg > commit block > commit
```

The planning agent groups files into commit blocks (`layer.py` with `test_layer.py`, then `dossier.py` with `test_dossier.py`). The coding agent runs a whole leg and commits each block as it goes. I review block by block afterward, and every change I make lands as its own atomic commit.

My DEVLOG records when I close a block, but the DEVLOG is private. The history should say "reviewed and closed" on its own, to anyone reading the repo.

Today I tag the end of each leg and don't use PRs. Legs will become PRs later.

The markers need to:

1. Mark each level with its own mechanism, so the level is readable from the marker alone.
2. Carry a summary of my review changes at the block level.
3. Survive the normal workflow: push, rebase, PR merge.
4. Keep the tag list short.

## Decision

| Level | Marker | Made by | Carries |
|---|---|---|---|
| Sprint | annotated tag `sprint-<id>` | me | one line per leg |
| Leg | PR merge commit | me, on GitHub | PR description built from the seals |
| Commit block | empty **seal** commit | me | one bullet per review change |
| Commit | ordinary commit | agent or me | the change |

### The seal

A seal is an empty commit (`git commit --allow-empty`) that closes a commit block after review.

```
review(<leg>.<block>): seal <block name>

- <one bullet per change I made in review>
```

A block I accept untouched still gets a seal:

```
review(<leg>.<block>): seal <block name>, no changes
```

### What a leg looks like

Newest first. The agent's commits come first in time; my review follows, block by block.

```
*   Merge PR #5: leg 2, layer + dossier
|\
| * review(L2.2): seal dossier, no changes
| * review(L2.1): seal layer
| * fix(layer): handle empty geometry
| * feat(dossier): build dossier from layer output      (agent, block 2)
| * feat(layer): add layer resolver                     (agent, block 1)
|/
```

### Rules

1. Every commit block gets exactly one seal. A block without a seal is unreviewed.
2. Only the reviewer writes seals. An agent never seals its own block.
3. Seals land in review order, after the agent's commits for the leg. Each seal follows my fix commits for its block, and its scope names the block, because the block's own commits sit earlier in the history.
4. Legs merge with a merge commit. Squash and rebase merging are off in the repo settings (squash deletes the seals; rebase deletes the leg's merge commit).
5. Tags mark sprints and nothing else.

### Until legs are PRs

A leg ends with an annotated tag `leg-<sprint-id>-<leg>`. The first leg that ships as a PR retires these tags, and the merge commit takes over.

## Consequences

**Good**

- The history tells the review story without the DEVLOG.
- The tag count equals the sprint count.
- Each level's summary is assembled from the level below it:

```bash
# every seal so far
git log --oneline --grep="^review"

# PR description for the current leg
git log main..HEAD --grep="^review" --reverse --format="%s%n%b"

# sprint tag message (GitHub puts the PR title in the merge commit body)
git log <prev-sprint-tag>..HEAD --merges --first-parent --reverse --format="- %b"
```

**Costs**

- One extra commit per block, so `git log --oneline` gets longer (`--invert-grep --grep="^review"` hides the seals).
- The Conventional Commits checker must allow the `review` type (for commitlint, add it to `type-enum`).
- The SprintN template gets a seal step as the last line of each block's review checklist, so every plan the agent writes carries the `[ ]` box.

(Rebasing is safe: git keeps commits that start empty by default. Only commits that *become* empty during a rebase get dropped.)

## Rejected alternatives

| Alternative | Why not |
|---|---|
| No marker; my last fix commit closes the block | Can't close a block I didn't change. "Reviewed" and "in progress" look the same. |
| Tag per block | Hundreds of tags. Pushed tags are hard to retract, and a rebase leaves them pointing at dead commits. |
| `git notes` on the block's last commit | GitHub doesn't show notes, they don't push by default, and a rebase drops them unless configured. |
| Branch and `--no-ff` merge per block | That is the leg mechanism. Using it per block flattens the hierarchy this ADR exists to show. |

## Open questions

- Should agent commits carry the block id in their scope (`feat(L2.1): ...`)? Then a script could list blocks that have commits but no seal.
