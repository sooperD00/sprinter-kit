# Housekeeping

Work with no sprint yet.

IDs are identity, not order: nothing here is renumbered, and the count is what matters. Past
about fifty unassigned items, hold a planning session before adding features.

- [ ] [h-e9e6bb] application-pipeline runs ADR-021, but was never set up from the kit. Adopt
      the kit there with init, in a pass of its own. It waits until one-big-map's current work
      is done.
      (Raised while setting up this plan, 2026-10-05.)
- [ ] [h-8976df] An implementation-plan template: init writes `docs/implementation-plan.md` when
      a repo has none, the way `[s-b57080]` makes it write the essay and the field guide.
      application-pipeline's and one-big-map's plans are the inputs; both work, and they
      differ. It waits because it changes `--phase-doc`'s default, so phases would come on by
      default, and that needs a design pass of its own. It would land as a sprint after
      `[s-b57080]`, reusing that sprint's rule for a project's own copies.
      (From [s-b57080]'s Out of Scope, 2026-10-06.)
- [ ] [h-616c5d] A reading list for the person: each agent step names what the person reads
      while it runs, as data the console can show. Pairs with stop modes (stop, don't stop,
      stop when conditions hold), where an unread backlog can be a condition. The kit
      declares what to read; the console decides when and how, and keeps read state.
      Draft and references: [h-616c5d-human-reading.md](drafts/h-616c5d-human-reading.md).
      (Raised while reviewing the kit, 2026-10-17.)
