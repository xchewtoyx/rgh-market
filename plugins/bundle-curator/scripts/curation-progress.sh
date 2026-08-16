#!/bin/sh
# Print per-domain curation progress: reviewed / total / pending, plus ratings
# backlog stats (max pending confidence and count with p >= 0.7).
# Path-and-ledger only — never opens fleeting note bodies.
#
# Usage (from repo root, or any cwd — script locates the root):
#   sh scripts/curation-progress.sh
#   sh scripts/curation-progress.sh --pending-only
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$SCRIPT_DIR/curation-progress.py" "$@"
