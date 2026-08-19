#!/usr/bin/env python3
"""Filter a domain's candidate fleeting paths through the landscape cache.

Optional narrowing step for `/curate --focused`'s researcher-dispatch
gather (see docs/curation.md, "Landscape pre-filter"): reads
landscape/overlap.jsonl (written by fleeting-researcher's landscape mode;
see docs/landscape.md) and drops candidate paths that HAVE a landscape entry
which does not list the given domain among its overlapping bundles.

A candidate with no landscape entry yet passes through unfiltered
(fail-open) -- landscape mode is an optimization, not a new gate, so a note
the sweep has not reached must still reach the domain's scorer exactly as it
would without this filter. The same fail-open treatment applies to a
malformed cache line for a path (missing/invalid `bundles`): it is treated
as not-yet-mapped rather than as an exclusion, since a data problem in the
cache must never silently hide a candidate from a domain.

Reads candidate paths from stdin, one per line (blank lines ignored).
Prints survivors to stdout, one per line, in input order. Prints a one-line
summary to stderr (kept off stdout so callers piping stdout are unaffected).

Usage (from repo root, or any cwd -- script locates the root):
  python3 scripts/list-... | python3 scripts/filter-by-landscape.py <domain-slug>
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

    A line that fails to parse, or whose `path`/`bundles` shape is not
    usable, is skipped entirely rather than recorded with an empty list --
    that keeps such a path in the "not yet mapped" (fail-open) state instead
    of wrongly treating a malformed entry as "mapped, overlaps nothing".
    Later lines for the same path (e.g. from a manually merged cache)
    override earlier ones, matching the append-only log's natural read
    order.
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


def filter_candidates(
    paths: list[str], overlap: dict[str, list[str]], domain: str
) -> list[str]:
    """Keep every path with no cache entry, plus paths whose entry lists
    `domain`. Order and duplicates from `paths` are preserved as given."""
    survivors: list[str] = []
    for path in paths:
        bundles = overlap.get(path)
        if bundles is None or domain in bundles:
            survivors.append(path)
    return survivors


def read_candidate_paths(stream) -> list[str]:
    return [
        line.strip() for line in stream if line.strip()
    ]


def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:
        raise SystemExit(
            "usage: filter-by-landscape.py <domain-slug> "
            "(candidate paths on stdin, one per line)"
        )
    domain = args[0]

    root = find_root(Path.cwd())
    bundle_dir = root / domain
    if not bundle_dir.is_dir():
        raise SystemExit(f"error: bundle folder not found: {bundle_dir}")

    overlap = load_overlap(root / "landscape" / "overlap.jsonl")
    candidates = read_candidate_paths(sys.stdin)
    survivors = filter_candidates(candidates, overlap, domain)

    for path in survivors:
        print(path)

    dropped = len(candidates) - len(survivors)
    unmapped = sum(1 for p in candidates if p not in overlap)
    print(
        f"landscape filter: kept {len(survivors)}/{len(candidates)} "
        f"candidates for {domain} ({dropped} dropped as out of scope, "
        f"{unmapped} not yet mapped and passed through)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
