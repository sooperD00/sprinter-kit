# Stack options for init: Python, Node and .NET

**ID**: `[s-bbcfb5]`
**Status**: planned

Lets init write a project's commands for the stack it runs, with `--stack python,node` or `--stack dotnet`, so a .NET repo takes the kit with no Python words in its templates.

**Kind:** feature. The option mechanism already exists (`phases`, `brownfield`), so the commits follow it: the flag, then the template blocks, then adoption.
**Legs:**
- a — `--stack` in sprinter.py and interface-spec. Options `python`, `node` and `dotnet` are plain on/off blocks, so one repo can hold more than one. A name init doesn't know stops it (exit 2). No `--stack` leaves every block in place and reports it, as `phases` does today. scan prints the stack it sees: `pyproject.toml` → python, `package.json` → node, `*.sln`, `*.slnx` or `*.csproj` → dotnet.
- b — the blocks. `leg-template.md`'s Dependencies, Final tests and Smoke tests split into python, node and dotnet blocks; python and node keep today's text. The dotnet block: `dotnet add <project> package <name>` and `dotnet add <project> reference <project>`, the restore rule as "don't touch PackageReference lines" (a `.csproj` mixes packages with build settings), `dotnet test --list-tests` to collect, `dotnet test` piped to a dated log, and smoke as run-and-browse. `r-template.md`'s example gate goes stack-neutral. prompt5 and promptX name dotnet beside uv and pnpm, one line each. The field guide says "doc comments" where it says "docstrings".
- c — adopting a repo that started without the kit. scan skips vendored folders (`wwwroot/lib`, `node_modules`, `vendor`, and anything `.gitattributes` marks `linguist-vendored`). init leaves an existing `housekeeping.md` or `techdebt.md` in place and lists it beside the template's path, the way it treats `docs/ESSAY.md`. `id --fill <file>` gives every open top-level item with no ID, or with `[h-PLACEHOLDER]`, a fresh one (`h-` or `t-` by file) and writes in place. Indented lines ride with their item; `[x]` items and prose stay as they are. The leg ends with init on a copy of Hello_Eliza with `--stack dotnet`: it exits 0, and `git grep -n -i -E 'uv |pytest|pnpm|pyproject' docs/` returns nothing there.

**Entry gate:** none.

**Why now** Hello_Eliza is the first .NET repo to take the kit. Today init refuses it (its `housekeeping.md` exists), scan calls it brownfield over 76 TODO lines in vendored Bootstrap and jQuery, and the leg template would hand it uv, pytest and pnpm commands.

**Watch** `--stack` picks commands inside templates; `[s-319ddd]`'s `--with python-checks` adds a record. Keep the two flags apart. Block names match `[a-z]+` today, so `python-checks` can't be one until `[s-cd5ee3-b]` extends the grammar.

**Watch** Stacks are on/off blocks, not `[s-cd5ee3-b]`'s choose-one form, because one-big-map is python and node at once. Record why in interface-spec.

**Watch** `[s-d6ac46-c]` rewrites every prompt. Keep this sprint's prompt edit to the one package-manager line, so that rewrite carries it.

**Watch** `[s-fc4d9e-a]` decides what CI is stack-agnostic. Use these three option names there, so CI steps key on the same blocks.

**Carry back:** none. Repos that took the kit before this sprint already carry their own stack's commands.
