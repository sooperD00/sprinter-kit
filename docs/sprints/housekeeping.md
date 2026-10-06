# Housekeeping

Work with no sprint yet.

IDs are identity, not order: nothing here is renumbered, and the count is what matters. Past
about fifty unassigned items, hold a planning session before adding features.

- [ ] [h-fec4e6] init and id refuse to run on the kit's own repo ("this is the kit's own repo").
      The guard catches a wrong working directory, but it also stops the kit from planning
      itself: this plan was set up by running a scratch clone's script with `--repo` pointed
      here. Add an explicit `--self` flag, or keep the guard on init and let id run anywhere.
      scan has the same blind spot from the other side: run here, it reports the kit's own
      examples/ and sprinter.py as banned words and sprint numbers. A `--self` scan would
      skip examples/ and templates/.
      (Found while setting up this plan, 2026-10-05.)
- [ ] [h-e9e6bb] application-pipeline runs ADR-021, but was never set up from the kit. Adopt
      the kit there with init, in a pass of its own. It waits until one-big-map's current work
      is done.
      (Raised while setting up this plan, 2026-10-05.)
