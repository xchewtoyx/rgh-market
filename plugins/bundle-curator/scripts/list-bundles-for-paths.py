#!/usr/bin/env python3
"""List the bundles that overlap a given set of fleeting note paths.

Reads landscape/overlap.jsonl (written by fleeting-researcher's landscape
mode; see docs/landscape.md) and prints the union of `bundles` entries
across the given paths -- the deterministic "which domains were identified"
step between a landscape-mode dispatch and the per-bundle charter-scoring
dispatches that follow it (used by /onboard's post-write pass; see
docs/landscape.md, Flow).

Reads candidate paths from stdin, one per line (blank lines ignored).
Prints bundle slugs to stdout, one per line, sorted, deduplicated. A path
with no landscape entry yet contributes nothing (silently) -- this script
does not tell you whether every path was actually mapped; pair it with the
caller's own bookkeeping (e.g. the landscape dispatch's own report) for
that. A bundle slug present in the cache with no matching bundle folder
(e.g. stale data from a renamed/removed domain) is dropped from stdout and
reported on stderr instead of being passed on to a dispatch that would fail.

Usage (from repo root, or any cwd -- script locates the root):
  printf '%s\n' path1.md path2.md | python3 scripts/list-bundles-for-paths.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def load_overlap(overlap_file: Path) -> dict[str, list[str]]:
    """Return {path: bundles} for every well-formed landscape cache line.

    Mirrors scripts/filter-by-landscape.py's loader: a line that fails to
    parse, or whose `path`/`bundles` shape is not usable, is skipped
    entirely. Later lines for the same path override earlier ones.
    """
    if not overlap_file.is_file():
        return {}
    overlap: dict[str, list[str]] = {}
    for line in overlap_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue
        path = obj.get("path")
        bundles = obj.get("bundles")
        if not isinstance(path, str) or not path:
            continue
        if not isinstance(bundles, list):
            continue
        overlap[path] = [b for b in bundles if isinstance(b, str)]
    return overlap


def read_candidate_paths(stream) -> list[str]:
    return [line.strip() for line in stream if line.strip()]


def bundles_for_paths(paths: list[str], overlap: dict[str, list[str]]) -> list[str]:
    """Union of bundles across the given paths' landscape entries, sorted.

    A path missing from `overlap` (not yet mapped) contributes nothing --
    it is neither an error nor a reason to stop; see the module docstring.
    """
    seen: set[str] = set()
    for path in paths:
        seen.update(overlap.get(path, []))
    return sorted(seen)


def filter_known_bundles(
    bundles: list[str], root: Path
) -> tuple[list[str], list[str]]:
    """Split bundles into (known, unknown) by bundle-folder existence."""
    known = [b for b in bundles if (root / b).is_dir()]
    unknown = [b for b in bundles if not (root / b).is_dir()]
    return known, unknown


def main() -> None:
    root = find_root(Path.cwd())
    overlap = load_overlap(root / "landscape" / "overlap.jsonl")
    paths = read_candidate_paths(sys.stdin)
    bundles = bundles_for_paths(paths, overlap)
    known, unknown = filter_known_bundles(bundles, root)

    for bundle in known:
        print(bundle)

    if unknown:
        print(
            f"list-bundles-for-paths: ignoring {len(unknown)} unknown bundle "
            f"slug(s) from the landscape cache with no matching folder: "
            f"{', '.join(unknown)}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
