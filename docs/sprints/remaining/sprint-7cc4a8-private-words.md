# Private-words guard and a setup guide

**ID**: `[s-7cc4a8]`
**Status**: planned

Adds a names check to scan that reads its word list from outside the repo and searches history too, has init remind a new repo to set one up, and documents the privacy-repo setup so anyone can build their own.

**Kind:** feature, after a design leg shared with `[s-2f14eb-a]`.
**Legs:**
- a — design: decisions D1–D3 in your private-words guard plan (the hook path on Windows, one CI workflow per repo or a shared one, and whether agents may push to a public repo at all).
- b — scan reads the list from a path outside the repo, checks the tree and `git log -S`, and prints file names only. init's greenfield checklist says to set it up on day one.
- c — the setup guide: a private repo that holds the list and the hook, `core.hooksPath`, the CI secret, and upkeep. Generic, with no real words in it.
- d — carry back to one-big-map: clear `[h-35b068]`, and `[t-dd2089]` once the privacy repo is live.

**Entry gate:** required `[s-2f14eb-a]` before leg b.

**Why now** On 2026-10-05 a full-desktop screenshot with private detail reached this public repo. A person caught it, not a check.

**Brings in:** `[h-35b068]` from one-big-map's housekeeping.md, and `[t-dd2089]` from its techdebt.md.
**Carry back:**
- one-big-map, on branch `kit-sync/7cc4a8` — pending
- this repo's own copies — pending
