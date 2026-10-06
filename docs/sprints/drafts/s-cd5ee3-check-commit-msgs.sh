#!/usr/bin/env bash
# Check every commit message in a range with this repo's own commit-msg hooks.
# CI runs it so a commit made with --no-verify, or from a clone that never ran
# `pre-commit install`, still gets checked. Local and CI use the same hook config.
#
# Usage:   scripts/check-commit-msgs.sh <range>
# Example: scripts/check-commit-msgs.sh origin/main..HEAD
# Exit:    0 every message passed, 1 at least one failed, 2 couldn't check
set -u

range="${1:-}"
if [ -z "$range" ]; then
  echo "usage: check-commit-msgs.sh <range>   e.g. origin/main..HEAD" >&2
  exit 2
fi
if [ ! -f .pre-commit-config.yaml ]; then
  echo "no .pre-commit-config.yaml here; run from the repo root" >&2
  exit 2
fi
if ! shas="$(git rev-list --no-merges "$range" 2>&1)"; then
  echo "couldn't read the range $range: $shas" >&2
  exit 2
fi

msg="$(mktemp)"
trap 'rm -f "$msg"' EXIT
fail=0
for sha in $shas; do
  git log -1 --format=%B "$sha" > "$msg"
  if ! out="$(pre-commit run --hook-stage commit-msg --commit-msg-filename "$msg" 2>&1)"; then
    echo "bad commit message: $(git log -1 --format='%h %s' "$sha")"
    echo "$out" | sed 's/^/    /'
    fail=1
  fi
done
exit "$fail"
