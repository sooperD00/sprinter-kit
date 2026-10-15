# ADR-XXX: Code layout: package by feature or package by layer

Status: Proposed (kit add-on, offered at every init)
Flag: `--layout feature | layer | flat | feature+layer` (default: `feature`)

<!-- init: the chosen option goes under Decision. The other rows move to Rejected alternatives, with their "Bad at" cell as the reason. Same mechanics as the Conventional Commits add-on. -->

## Context

### Why this ADR exists
In one-big-map, the README tree grouped code by subject (`parcels/`, `layers/`). The design agent made that choice in one line of the README. Every later agent read it and followed it. I didn't choose it. I found out from a review note.

Writing by hand, I would have picked `ports/` and `adapters/`, so I could say "now I'm writing a port." Seeing the result, I prefer the agent's choice. But I want to make it at init, on purpose, every time.

### Two decisions hide in one folder tree
| Decision | Question | Decided in |
|---|---|---|
| Architecture | Which way do dependencies point? | ADR-YYY (vocabulary): ports and adapters |
| Layout | Where do the files live? | This ADR |

Every layout below can hold ports and adapters. Choosing `feature` does not mean giving up ports. The role moves from the folder name to the file name.

### Terms
- **Package by feature:** group code by subject. One folder per thing the system knows about (`parcels/`, `layers/`). Close cousin: *vertical slices* (Jimmy Bogard, 2018).
- **Package by layer:** group code by role. One folder per kind of code (`ports/`, `adapters/`, `models/`).
- **Screaming architecture** (Robert C. Martin, 2011): the top-level tree should tell you what the system does, not which framework or pattern it uses. Package by feature screams "parcels." Package by layer screams "hexagonal."

## Options (simplest → most structure)

| `--layout` | Tree | Good at | Bad at |
|---|---|---|---|
| `flat` | one package | single-purpose tools, scripts | collapses past ~10 modules |
| `layer` | `ports/ adapters/ models/` | pattern visible at a glance; matches some FastAPI starter templates; good for teaching repos | every feature leg edits every folder; folders become junk drawers sorted by role |
| `feature` | `parcels/ layers/`, each with its interface and what implements it | a feature leg mostly adds files to one folder; conventions checkable against sibling folders; deleting a feature = deleting a folder | pattern invisible in the tree; needs rules for shared code and sibling drift |
| `feature+layer` | `parcels/ports/ parcels/adapters/` | features with many adapters | nesting overkill for small features |

## Decision
Default: `feature`.

1. Legs map to features. A feature leg mostly adds files to one new folder. Additive diffs review faster and split legs less often, which is the kit's own success metric.
2. Conventions become checkable. A new feature folder either matches its siblings or it doesn't, and any reviewer (me or an agent) can see which.
3. A feature is one folder. I can delete it, replace it, or hand it to someone as a unit.
4. I still write ports by hand. The port lives at `parcels/port.py` instead of `ports/parcels.py`. <!-- file name pinned in ADR-YYY -->

### Rules that ship with `feature`
1. **Sibling rule.** Every feature folder has the same internal shape: one interface file, one module per implementation, tests mirrored under `tests/<feature>/`. The interface file is `port.py` when the folder holds a port, and `base.py` when it holds an extension point. The swap test in ADR-YYY decides which: one-big-map's `parcels/` holds a port, and its `layers/` an extension point.
2. **Shared-code rule.** Code moves to `shared/` only when a second feature imports it. Not before. (This is why one-big-map's `layers/` got its own base file instead of sharing one with `parcels/`.)
3. **README line.** The tree can't show the architecture, so the README says it once: "Ports and adapters, packaged by feature."
4. **Framework wins.** If the framework prescribes a layout, follow it and note that here. (Django apps are already features, so Django agrees with the default.)

### When to pick something else at init
- `flat`: one adapter or none, and fewer than ~10 modules expected.
- `layer`: a tiny single-domain app, a framework template that is already layered, or a teaching repo where the pattern should show in the tree.
- `feature+layer`: don't start here. Start with `feature`, and split one folder into `ports/` and `adapters/` when it passes ~3 adapters.

## Consequences
- Cheap to change later: `feature` → `feature+layer`, one folder at a time.
- Expensive to change later: `feature` ↔ `layer`. That is a repo-wide rename touching every import, which is why the choice belongs at init.
- Design docs and sprint plans name feature legs by their folder.
- Without the sibling rule, feature folders drift into different shapes. The review prompt checks it.

## Rejected alternatives
<!-- init fills this from the unchosen rows of the Options table -->