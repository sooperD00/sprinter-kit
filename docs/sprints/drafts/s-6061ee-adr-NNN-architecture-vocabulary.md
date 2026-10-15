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
| core | code that imports no adapters | each feature folder, outside the adapter modules |
| port | an interface the core owns (ABC or Protocol) | `port.py` |
| adapter | implements one port for one outside thing | one module per outside thing |
| driving adapter | calls into the core: HTTP route, CLI, test | |
| driven adapter | the core calls it: database, API client, queue | |

Python's habit is `base.py` for abstract classes. I use `port.py` so the file says its role.
The README says "hexagonal" once, for searchability. Everywhere else says "ports and adapters."

### Rejected alternatives
- For the inside: "domain" (collides with the field guide's domain), "application" (collides with the whole app).
- For ports and adapters: interface/implementation, gateway, provider, client, backend, driver, connector, plugin, base.
- For the two sides: primary/secondary. (Same meaning as driving/driven. Pick one pair.)
- "Repository" is fine as the name of one specific persistence port, never as a role word.
- A specific class can still describe its job (`MaricopaAssessorAdapter`). The role words are only port and adapter.