# ADR-NNN: Conventional Commits for Commit Messages

<!-- SPRINTER-KIT ADD-ON. For the setup agent and sprinter.py. Delete this comment when rendering.

WHAT THIS IS
An add-on ADR. Commit subjects follow Conventional Commits, checked by one commit-msg hook that
the pre-commit framework runs. The project picks ONE checker at init. That checker's blocks stay;
every other checker becomes a row under "Alternatives Considered". Everything without a marker
(Context, Decision, Where Each Rule Comes From, the conventions table, References) renders as is.

THE CHOICE: --commit-check <value>

| value                   | runtime     | good at                                     | bad at                                         | choose it when                         |
|-------------------------|-------------|---------------------------------------------|------------------------------------------------|----------------------------------------|
| none                    | -           | zero setup                                  | nothing enforces it                            | a throwaway or one-week project        |
| regex                   | none        | no dependency; the rule is visible in YAML  | failure prints only a file name; you own the pattern | a repo with no Python or Node toolchain |
| conventional-pre-commit | Python (uv) | does exactly this check; clear errors       | check only: no prompts, no releases            | the default                            |
| commitizen              | Python (uv) | also writes messages (cz commit) and cuts releases (cz bump) | most to learn and configure       | the project ships versioned releases   |
| commitlint              | Node (pnpm) | most rules; the JS ecosystem's standard     | Node toolchain plus a config file              | a JS-first repo that already has pnpm  |

No flag: the choice is undecided. init leaves every marker in place and reports them. Show the
table above, recommend conventional-pre-commit, and ask. Then keep or drop blocks by hand.

MARKER GRAMMAR THIS FILE NEEDS (a sprinter.py change)
The kit's options so far are on/off (`kit:phases`). This one is choose-one, so markers carry a value:
  <!-- kit:commit-check=commitizen --> ... <!-- /kit:commit-check=commitizen -->    kept only when chosen
  <!-- kit:commit-check!=none --> ... <!-- /kit:commit-check!=none -->              kept unless chosen
  The same two forms work at the end of a single line, as `kit:brownfield` does in plan.md.
The marker regexes need `[a-z][a-z-]*` names plus an optional `=value` or `!=value`.
argparse `choices=` on --commit-check keeps it to exactly one value.
Lint, format and type-check add-ons will have the same choose-one shape and can reuse this.

BLANKS
{{date}}           init fills it.
{{precommit-adr}}  a link to the project's pre-commit ADR. Until the kit ships that ADR, init
                   reports this blank and the setup agent fills it by hand.

SHIPS WITH
check-commit-msgs.sh, which CI runs (see "How It's Checked"). Copy it for every choice. With
`none` there is no commit-msg hook, so it has nothing to fail.

SETUP
The rendered ADR's "How It's Checked" section is the setup checklist. The human runs every
package-manager command. The agent names packages, writes config, and runs nothing that installs.
The Python checkers assume a uv project. In a repo without pyproject.toml, offer regex or commitlint.
-->

**Status:** accepted
**Date:** {{date}}
**Builds on:** {{precommit-adr}} (pre-commit runs every hook in this repo)

## Context

- People and agents both commit here. Some agents work from fresh clones, where no hook runs until someone runs `pre-commit install`.
- A subject that starts with its kind of change makes `git log --oneline` scannable, and filterable: `git log --oneline --grep '^fix'`.
- [Conventional Commits 1.0.0][cc] is a published spec. It grew out of [Angular's commit guidelines][angular] and generalizes them for any project.
- The spec lines up with [Semantic Versioning][semver]: `fix` is a patch release, `feat` a minor one, and a breaking change a major one. Changelog and release tools read it, so a project that later cuts versioned releases gets them without rewriting its history.

## Decision

1. Write every commit subject as `type(scope)!: description`. Scope and `!` are optional.
   - Yes: `feat: add search filter`, `build(deps-dev): add pytest-cov`, `feat(api)!: drop v1 endpoints`, `docs(sprints): close leg b`
   - Never: `Add pytest-cov`, `scripts: refuse paths outside the repo`, `feat:no space`, `wip: half done`
2. Pick the type from this table. Nothing else passes the check.

   | Type | Use it for |
   |------|------------|
   | `feat` | A capability someone using the project would notice |
   | `fix` | A bug fix |
   | `docs` | Documentation only, sprint and planning files included |
   | `refactor` | A code change that neither fixes a bug nor adds a feature |
   | `perf` | A change that only makes something faster or smaller |
   | `test` | Adding or correcting tests |
   | `build` | Dependencies and the build system |
   | `ci` | CI configuration and the scripts only CI runs |
   | `style` | Formatting and whitespace, with no change in behavior |
   | `chore` | Maintenance that fits nothing above: tool config, housekeeping files |
   | `revert` | Undoing an earlier commit |

3. Give each commit one type. When a change fits two, split it into two commits.
4. Use `build(deps)` for a runtime dependency change and `build(deps-dev)` for a dev-only one. Keep `chore` for maintenance that touches neither dependencies nor code.
5. Add a scope when it helps a reader filter: the area of the repo, like `parser`, `sprints` or `deps`. Leave it off when nothing fits.
6. Mark a breaking change with `!` before the colon, or with a `BREAKING CHANGE:` footer. Write any footer as `Token: value` on its own line after a blank line, like `Refs: #142`.
7. Start the description lower-case and in the imperative (`add`, not `added`), with no closing period. Keep the whole subject under 72 characters, and aim for 50.
8. To revert, run `git revert -e <sha>` and change only the subject, from git's `Revert "<original subject>"` to `revert: <original subject>`. Keep the body line git writes, `This reverts commit <sha>.`, because it names the commit being undone. `git revert` never runs the commit-msg hook, so this step is on you; CI catches it if you forget.
9. Leave merge commits and `fixup!` / `squash!` commits as git writes them. The check lets them through.

## Where Each Rule Comes From

| Rule | Source |
|------|--------|
| The `type(scope)!: description` shape, the `!` and the `BREAKING CHANGE` footer (items 1, 6) | [Conventional Commits 1.0.0][cc], rules 1–13 |
| `feat` and `fix` | The spec itself. They are the only two types it defines |
| `build`, `ci`, `docs`, `perf`, `refactor`, `test` | [Angular's current guidelines][angular] |
| `chore`, `style`, `revert` | The older [AngularJS conventions][angularjs]. Angular has since dropped `chore` and `style`; [commitlint's preset][commitlint-preset] keeps all eleven, and the spec points to that preset for its examples |
| One type per commit (item 3) | The spec's FAQ: go back and make several commits |
| `build(deps)` over `chore(deps)` (item 4) | Angular defines `build` as the build system *or external dependencies* |
| Footers as `Token: value` (item 6) | The spec's footer rule, modeled on [git trailers][trailers] |
| Lower-case after the colon (item 7) | Angular. [Beams][beams] capitalizes subjects, but after a `type:` prefix the description reads as one phrase with it |
| Imperative, no period (item 7) | Angular, [the Linux kernel][kernel], [Go][go] and [Beams][beams] all agree |
| Under 72, aim for 50 (item 7) | [Go][go] caps the subject at about 72 and the kernel at 70–75. [Beams][beams] sets 50 as the target |
| The revert subject (item 8) | Angular: `revert: ` plus the original header, with the reverted SHA in the body. The spec's FAQ also suggests naming the SHA |

## How It's Checked

<!-- kit:commit-check!=none -->
One `commit-msg` hook checks each message as it's written. pre-commit runs it at commit time, and CI runs the same hook over every pushed commit, so the two can't drift.

- Keep this line at the top of `.pre-commit-config.yaml`. Plain `pre-commit install` sets up only the pre-commit hook, and without this line the commit-msg hook never runs ([pre-commit docs][pc-install-types]):

  ```yaml
  default_install_hook_types: [pre-commit, commit-msg]
  ```

- Run `pre-commit install` once in every clone, an agent's fresh one included.
- In CI, run `scripts/check-commit-msgs.sh <base>..HEAD` over the commits a push or pull request adds. It feeds each message to the same hook, so it catches commits made with `--no-verify` or from a clone that never ran `pre-commit install`.
<!-- /kit:commit-check!=none -->

<!-- kit:commit-check=conventional-pre-commit -->
**Checker: [`conventional-pre-commit`][cpc]**, a Python hook that does this one check.

- Add the dev dependency `conventional-pre-commit` (`uv add --dev conventional-pre-commit`).
- Add the hook under `repos:` in `.pre-commit-config.yaml`:

  ```yaml
    - repo: local
      hooks:
        - id: conventional-pre-commit
          name: conventional commit message
          language: system
          entry: uv run conventional-pre-commit
          stages: [commit-msg]
  ```

- Its default type list is the table in Decision item 2.
- It rejects git's default `Revert "..."` subject. Because `git revert` skips the hook, that subject commits locally and then fails in CI. Item 8 avoids it.
- It accepts `Feat:`, because the spec says types are case-insensitive.
<!-- /kit:commit-check=conventional-pre-commit -->

<!-- kit:commit-check=commitizen -->
**Checker: [`commitizen`][cz]**, a Python tool that checks messages, helps write them, and cuts releases.

- Add the dev dependency `commitizen` (`uv add --dev commitizen`).
- Add the hook under `repos:` in `.pre-commit-config.yaml`:

  ```yaml
    - repo: local
      hooks:
        - id: commitizen
          name: conventional commit message
          language: system
          entry: uv run cz check --commit-msg-file
          stages: [commit-msg]
  ```

- Run `uv run cz commit` to be walked through a message.
- Configure `[tool.commitizen]` in `pyproject.toml` before the first `cz bump`. A bump reads the history since the last tag, picks the next version (`fix` is a patch, `feat` a minor, `!` a major) and writes the changelog.
- Its check also accepts `bump:`, the type `cz bump` gives its own release commits.
<!-- /kit:commit-check=commitizen -->

<!-- kit:commit-check=commitlint -->
**Checker: [`commitlint`][commitlint]**, the Node tool most JavaScript projects use.

- Add the dev dependencies `@commitlint/cli` and `@commitlint/config-conventional` (`pnpm add -D @commitlint/cli @commitlint/config-conventional`).
- Add `commitlint.config.mjs` at the repo root:

  ```js
  export default { extends: ['@commitlint/config-conventional'] };
  ```

- Add the hook under `repos:` in `.pre-commit-config.yaml`:

  ```yaml
    - repo: local
      hooks:
        - id: commitlint
          name: conventional commit message
          language: system
          entry: pnpm exec commitlint --edit
          stages: [commit-msg]
  ```

- It is stricter than Decision item 7: it rejects a capitalised description and a subject over 100 characters.
<!-- /kit:commit-check=commitlint -->

<!-- kit:commit-check=regex -->
**Checker: a regex hook.** pre-commit's built-in [`pygrep`][pc-pygrep] hook type matches the start of the message against one pattern. Nothing to install.

- Add the hook under `repos:` in `.pre-commit-config.yaml`:

  ```yaml
    - repo: local
      hooks:
        - id: conventional-commit-msg
          name: conventional commit message
          language: pygrep
          entry: '\A(?:(?:build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(?:\([a-z0-9-]+\))?!?: \S|Merge |Revert "|fixup! |squash! )'
          args: [--multiline, --negate]
          stages: [commit-msg]
  ```

- `--negate` fails the hook when the pattern finds no match. `\A` with `--multiline` anchors it to the first line, so a valid-looking line in the body can't rescue a bad subject.
- A failure prints only the message file's name. Check the subject against Decision item 1.
<!-- /kit:commit-check=regex -->

<!-- kit:commit-check=none -->
**No checker.** The convention is a written rule, and review catches what slips.

- Read the commit subjects as part of every review.
- Rewrite a bad subject with `git commit --amend` before it's pushed.
<!-- /kit:commit-check=none -->

## Alternatives Considered

**Conventions**

| Option | Rejected because |
|--------|------------------|
| Free-form subjects, written well ([Beams' seven rules][beams]) | Readable, but the subject never says what kind of change it is, so there is nothing to filter on or check against. Item 7 keeps its imperative mood and length target |
| An area prefix, `subsystem: summary` ([Linux kernel][kernel], [Go][go]) | It names where a change is, not what kind it is, so release tools can't read it. Conventional Commits keeps the area as the optional scope: `fix(parser):` |
| Angular's own guidelines ([Angular][angular]) | They are the source of this convention, but written for one project: a fixed scope list, a body required on most commits, and no `chore` |

**Checkers**

| Option | Rejected because |
|--------|------------------|
| No checker | Agents commit unattended, and an unchecked rule drifts from the first commit | <!-- kit:commit-check!=none -->
| A regex hook (`pygrep`) | A failure prints only a file name, and the type list lives in a pattern someone has to maintain | <!-- kit:commit-check!=regex -->
| `conventional-pre-commit` | It only checks: no help writing a message and nothing for releases | <!-- kit:commit-check!=conventional-pre-commit -->
| `commitizen` | Its prompts, version bumps and changelog go unused in a project that doesn't cut versioned releases | <!-- kit:commit-check!=commitizen -->
| `commitlint` | It brings a Node toolchain and a config file into the repo to check one line | <!-- kit:commit-check!=commitlint -->

All four checkers were run on 2026-10-05 under pre-commit 4.6.2 (conventional-pre-commit 4.4.0, commitizen 4.19.1, commitlint 21.2.3). They agree on every Yes and Never example in item 1, on merges, and on `fixup!`. They differ only at the edges: git's default `Revert "..."` (conventional-pre-commit rejects it), `bump:` (only commitizen accepts it), `Feat:` (only conventional-pre-commit accepts it), and a capitalised description or a subject over 100 characters (only commitlint rejects them).

## Consequences

- Every subject costs a moment's thought about its type.
- A hook runs only in a clone where `pre-commit install` ran. CI is the backstop. On a direct push to `main` it reports after the commit has landed; it blocks only when changes arrive by pull request with the check required. <!-- kit:commit-check!=none -->
- `git commit --no-verify` skips the hook, and so does `git revert`. CI still sees both. <!-- kit:commit-check!=none -->
- A bad subject that's already pushed stays. Rewriting published history to fix one line costs more than the line.
- The type list lives in the hook's pattern as well as in Decision item 2. Change both together. <!-- kit:commit-check=regex -->
- `[tool.commitizen]` is config to keep current once releases start. <!-- kit:commit-check=commitizen -->
- The repo carries `node_modules` and a `package.json` even when its code isn't JavaScript. <!-- kit:commit-check=commitlint -->
- Nothing enforces the rule, so the history is only as consistent as the last reviewer. <!-- kit:commit-check=none -->

## References

- [Conventional Commits 1.0.0][cc]: the spec, its 16 rules and FAQ
- [Angular commit message guidelines][angular]: the current types, scope list, body and revert rules
- [AngularJS commit conventions][angularjs]: the original list, where `chore` and `style` come from
- [`@commitlint/config-conventional`][commitlint-preset]: the eleven-type list most tools use
- [Linux kernel, "The canonical patch format"][kernel]: `subsystem: summary phrase`
- [Go wiki, "Commit messages"][go]: `package: summary`
- [Chris Beams, "How to Write a Git Commit Message"][beams]: the seven rules, including 50/72
- [Semantic Versioning][semver]: what patch, minor and major mean
- [git interpret-trailers][trailers]: the `Token: value` footer format
- [pre-commit: `default_install_hook_types`][pc-install-types], [the `commit-msg` stage][pc-commit-msg], [`pygrep`][pc-pygrep]
- Checkers: [conventional-pre-commit][cpc], [commitizen `cz check`][cz], [commitlint][commitlint]

[cc]: https://www.conventionalcommits.org/en/v1.0.0/
[angular]: https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md
[angularjs]: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits
[commitlint-preset]: https://github.com/conventional-changelog/commitlint/tree/master/@commitlint/config-conventional
[kernel]: https://www.kernel.org/doc/html/latest/process/submitting-patches.html#the-canonical-patch-format
[go]: https://go.dev/wiki/CommitMessage
[beams]: https://cbea.ms/git-commit/
[semver]: https://semver.org/
[trailers]: https://git-scm.com/docs/git-interpret-trailers
[pc-install-types]: https://pre-commit.com/#top_level-default_install_hook_types
[pc-commit-msg]: https://pre-commit.com/#commit-msg
[pc-pygrep]: https://pre-commit.com/#pygrep
[cpc]: https://github.com/compilerla/conventional-pre-commit
[cz]: https://commitizen-tools.github.io/commitizen/commands/check/
[commitlint]: https://github.com/conventional-changelog/commitlint
