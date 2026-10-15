# ADR-YYY: Architecture vocabulary

should I put a bunch of stuff in here or have separate ADRs for different
decisions conventions on architecture vocabulary?


## ports and adapters

Status: Proposed (kit, always on, no flag)

### Context
Agents need words for "the interface the core owns" and "the thing that implements it for one outside system." Without pinned words, each project picks its own, and I translate every time. The pattern is Alistair Cockburn's ports and adapters (2005), also called hexagonal architecture. The hexagon means nothing; Cockburn called it a placeholder name.

### Decision
Use these words in code, docs, and sprint plans.

| Term | Means | Lives in |
|---|---|---|
| core | code that makes the decisions: rules, thresholds, verdicts | each feature folder, outside the adapter modules |
| port | an interface the core owns, whose implementations each wrap a different outside system and can stand in for one another | `port.py` |
| adapter | implements one port for one outside thing | one module per outside thing |
| extension point | an interface the core owns, whose implementations are all core, all run, and each answer a different question | `base.py` |
| driving adapter | calls into the core: HTTP route, CLI, test | |
| driven adapter | the core calls it: database, API client, queue | |

The swap test: if one implementation can replace another without the core noticing, the interface is a port. If removing one implementation loses an answer, it is an extension point.

Declare a port once there is a second adapter, or a planned one. Before that, it's ceremony.

Core is defined by what it does, not by what it imports. A core that calls an outside client directly is still core; "imports no adapters" becomes true, and checkable by a linter, once that client sits behind a port.

Python's habit is `base.py` for any abstract class. Here `port.py` marks a port and `base.py` marks an extension point, so the file name says which.
The README says "hexagonal" once, for searchability. Everywhere else says "ports and adapters."

### Rejected alternatives
- For the inside: "domain" (collides with the field guide's domain), "application" (collides with the whole app).
- For ports and adapters: interface/implementation, gateway, provider, client, backend, driver, connector, plugin, base.
  "Extension point" doesn't reopen these. "Plugin" was rejected as another name for a port; an extension point is a different thing, and `base.py` names its file, not a port's.
- For the two sides: primary/secondary. (Same meaning as driving/driven. Pick one pair.)
- "Repository" is fine as the name of one specific persistence port, never as a role word.
- A specific class can still describe its job (`MaricopaAssessorAdapter`). The role words are only port and adapter.