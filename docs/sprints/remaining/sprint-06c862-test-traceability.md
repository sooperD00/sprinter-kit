# Test traceability tooling

**ID**: `[s-06c862]`
**Status**: planned

Adds a collector that builds a traceability table for a review to fill in: each spec rule, the tests that cover it, and the lines no test ran. Test validity, the second pass, waits as tech debt.

**Kind:** feature, after a design leg.
**Legs:**
- a — design: where the table lives (a review file, or one per leg), its columns, and how a spec rule gets an ID. Start from the table the faab97 leg-a review produced by hand.
- b — the collector for Python: test IDs from `pytest --collect-only -q`, classes and functions from the module under test, and missing lines from `pytest-cov --cov-report=term-missing`. It writes the table with the verdict cells empty. It's stack-specific, so it ships with the Python checks `[s-319ddd]` or as an init option of its own.
- c — the review prompt calls it, and the handbook names the two passes: traceability (every spec rule maps to a test) and validity (each test checks what its name says).
- d — carry back to one-big-map: a first run on `tests/contract/test_parcel.py`.

**Entry gate:** required `[s-b34c63-a]` before leg a. The contract says where tool output lives and how a prompt calls a tool.

**Why now** The faab97 leg-a review found weak tests by hand, and the commands that check them already exist.

**Brings in:** your note `adr-for-writing-tests-20261005.txt`, which can wait in `docs/sprints/drafts/`. Pass 2 is `[t-ce8ab9]`.
**Carry back:**
- one-big-map, on branch `kit-sync/06c862` — pending
- this repo's own copies — pending
