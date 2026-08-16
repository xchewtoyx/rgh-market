#!/usr/bin/env python3
"""Deterministic candidate + bundle selection for the `/score-catchup` skill.

For each bundle, computes the notes that a landscape sweep already flagged
for that bundle but no charter-scoring pass has touched yet:

  (unreviewed (per curation/<bundle>.txt)
   ∩ landscape-tagged for this bundle (per landscape/overlap.jsonl))
  minus already-rated for this bundle (per ratings/<bundle>.jsonl, presence
  only -- any confidence value counts as "rated", there is no threshold
  here: the question is "has this ever been scored", not "how well did it
  score").

This is the mirror image of scripts/select-catchup-candidates.py, one stage
earlier in the pipeline: that script drains notes already vetted by *both*
a landscape sweep and a scoring pass into curation; this one drains notes
vetted by a landscape sweep *alone* into a scoring pass, so a later
`/catch-up` run has something to work with.

Prints one JSON line per bundle with at least one candidate, ordered by
priority -- most candidates first, then bundle slug for a stable tiebreak
(there is no confidence signal to rank by pre-scoring, unlike
select-catchup-candidates.py):

  {"bundle": "telemetry-state", "count": 12,
   "candidates": ["fleeting/.../a.md", "fleeting/.../b.md", ...]}

`candidates` is sorted alphabetically for a deterministic, reproducible
order (no meaningful ranking signal exists before scoring). Prints nothing
(exit 0) if no bundle has any qualifying candidate.

Usage (from repo root, or any cwd -- script locates the root):
  python3 scripts/select-score-catchup-candidates.py
  python3 scripts/select-score-catchup-candidates.py telemetry-state capacity-load
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from domains import load_domains  # noqa: E402


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def load_fleeting_paths(root: Path) -> set[str]:
    """Return every source note under fleeting/<source-slug>/*.md.

    Files directly under fleeting/ (not inside a source subfolder) are
    excluded -- see the matching note in list-landscape-unmapped.py.
    """
    fleeting = root / "fleeting"
    if not fleeting.is_dir():
        raise SystemExit("error: fleeting/ directory missing")
    return {
        str(path.relative_to(root)).replace("\\", "/")
        for path in fleeting.rglob("*.md")
        if path.is_file() and path.parent != fleeting
    }


def load_ledger_paths(ledger: Path) -> set[str]:
    if not ledger.is_file():
        return set()
    paths: set[str] = set()
    for line in ledger.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        paths.add(line)
    return paths


def load_landscape_overlap(overlap_file: Path) -> dict[str, list[str]]:
    """Return {path: bundles}, mirroring scripts/filter-by-landscape.py's
    loader: a line that fails to parse, or whose path/bundles shape is not
    usable, is skipped entirely (never recorded as an empty-bundle match).
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


def landscape_paths_for_bundle(
    overlap: dict[str, list[str]], bundle: str
) -> set[str]:
    return {path for path, bundles in overlap.items() if bundle in bundles}


def load_rated_paths(ratings_file: Path) -> set[str]:
    """Return the set of paths already present in a domain's ratings cache,
    regardless of confidence value -- presence alone means "already scored".
    A line that fails to parse, or has no usable path, is skipped rather
    than raising.
    """
    if not ratings_file.is_file():
        return set()
    rated: set[str] = set()
    for line in ratings_file.read_text(encoding="utf-8").splitlines():
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
            rated.add(path)
    return rated


def bundle_candidates(
    unreviewed: set[str],
    landscape_paths: set[str],
    rated_paths: set[str],
) -> list[str]:
    """Unreviewed and landscape-tagged for this bundle, minus already-rated,
    sorted alphabetically for a deterministic order."""
    qualifying = (unreviewed & landscape_paths) - rated_paths
    return sorted(qualifying)


def bundle_priority_key(result: dict) -> tuple[int, str]:
    """Sort key for ready bundles: most candidates first, then bundle slug
    ascending for a stable, deterministic tiebreak."""
    return (-result["count"], result["bundle"])


def select_ready_bundles(root: Path, domains: list[str]) -> list[dict]:
    fleeting_paths = load_fleeting_paths(root)
    overlap = load_landscape_overlap(root / "landscape" / "overlap.jsonl")

    ready: list[dict] = []
    for bundle in domains:
        reviewed = load_ledger_paths(root / "curation" / f"{bundle}.txt")
        unreviewed = fleeting_paths - reviewed
        landscape_paths = landscape_paths_for_bundle(overlap, bundle)
        rated_paths = load_rated_paths(root / "ratings" / f"{bundle}.jsonl")
        candidates = bundle_candidates(unreviewed, landscape_paths, rated_paths)
        if not candidates:
            continue
        ready.append(
            {
                "bundle": bundle,
                "count": len(candidates),
                "candidates": candidates,
            }
        )

    ready.sort(key=bundle_priority_key)
    return ready


def main() -> None:
    root = find_root(Path.cwd())
    all_domains = load_domains(root)

    parser = argparse.ArgumentParser(
        description=(
            "Select bundles ready for a /score-catchup scoring round: "
            "(unreviewed ∩ landscape-tagged) minus already-rated, per bundle."
        )
    )
    parser.add_argument(
        "bundles",
        nargs="*",
        metavar="bundle-slug",
        help=f"Restrict to these domain slugs (default: all {len(all_domains)})",
    )
    args = parser.parse_args()

    domains = args.bundles or all_domains
    unknown = sorted(set(domains) - set(all_domains))
    if unknown:
        raise SystemExit(f"error: unknown domain slug(s): {', '.join(unknown)}")

    for result in select_ready_bundles(root, domains):
        print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
