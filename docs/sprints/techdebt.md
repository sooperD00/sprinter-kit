# Tech Debt

Deferred work, probably for a while. Anything that turns out to be needed soon belongs in a sprint
or in Housekeeping, not here.

IDs are identity, not order: nothing here is renumbered, and the count is what matters.

- [ ] [t-7cab9c] Package the kit and the stack notes as one Claude Code plugin: slash commands
      for the prompts (/plan, /review), the stack notes available to every session without
      --add-dir, and the private-words check and the linters as hooks. One install per machine
      in place of two clones, an alias and per-repo setup. Wait until both have settled: a
      second project has run on the kit, a review has promoted its kit: and stack: items, and
      the note format has stopped changing. Packaging before then freezes the shape of one
      project.
      (Brought in from one-big-map's techdebt.md, 2026-10-05, where it was raised while
      setting up stack-notes, 2026-10-02.)
      Carry back: one-big-map, clear its line — pending
- [ ] [t-ce8ab9] Test validity, the second pass: does each test check what its name says?
      Coverage says a line ran, not that anything checked it. The tool for this is mutation
      testing, which breaks the code on purpose and checks that a test fails (mutmut is one
      for Python). It isn't worth it at one-big-map's size. Worth doing once a suite is too
      big to read every assertion by hand, or once `[s-06c862]`'s traceability table is
      routine and the gaps it misses are validity, not coverage.
      (Raised in one-big-map's faab97 leg-a review, 2026-10-05.)
