#!/usr/bin/env python3
"""List fleeting note paths not yet mapped in the landscape overlap cache.

Path-only: never opens fleeting note bodies. Compares paths under fleeting/
to the `path` keys already present in landscape/overlap.jsonl (see
docs/landscape.md).

Prints unmapped paths to stdout, one per line, sorted. Prints nothing
(exit 0) if every fleeting note already has a landscape entry.

Usage (from repo root, or any cwd -- script locates the root):
  python3 scripts/list-landscape-unmapped.py
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


def load_fleeting_paths(root: Path) -> set[str]:
    """Return every source note under fleeting/<source-slug>/*.md.

    Files directly under fleeting/ (not inside a source subfolder) are
    excluded -- fleeting/ is a folder-per-source layout, and a stray file at
    its top level (e.g. a README) is never itself a literature note to map,
    score, or curate.
    """
    fleeting = root / "fleeting"
    if not fleeting.is_dir():
        raise SystemExit("error: fleeting/ directory missing")
    return {
        str(path.relative_to(root)).replace("\\", "/")
        for path in fleeting.rglob("*.md")
        if path.is_file() and path.parent != fleeting
    }


def load_mapped_paths(overlap_file: Path) -> set[str]:
    """Return the set of paths already mapped (have a landscape entry).

    A line that fails to parse as JSON, or whose `path` is missing/not a
    string, is skipped rather than raising -- a malformed line must not stop
    every other note from being correctly reported as mapped or unmapped.
    """
    if not overlap_file.is_file():
        return set()
    mapped: set[str] = set()
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
        if isinstance(path, str) and path:
            mapped.add(path)
    return mapped


def unmapped_paths(
    fleeting_paths: set[str], mapped_paths: set[str]
) -> list[str]:
    return sorted(fleeting_paths - mapped_paths)


def main() -> None:
    root = find_root(Path.cwd())
    fleeting_paths = load_fleeting_paths(root)
    mapped_paths = load_mapped_paths(root / "landscape" / "overlap.jsonl")
    for path in unmapped_paths(fleeting_paths, mapped_paths):
        print(path)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
