#!/usr/bin/env python3
"""Deterministic candidate + bundle selection for the `/catch-up` skill.

For each bundle, computes the three-way intersection the skill needs before
it will dispatch a focused curation batch:

  unreviewed (per curation/<bundle>.txt)
  ∩ landscape-tagged for this bundle (per landscape/overlap.jsonl)
  ∩ rated at or above --min-confidence for this bundle (per ratings/<bundle>.jsonl)

Unlike scripts/filter-by-landscape.py (used ahead of *scoring*, deliberately
fail-open so an unmapped note still gets scored), this is a hard,
three-way AND: a note with no landscape entry, or one whose entry excludes
this bundle, is never a catch-up candidate -- catch-up only curates notes
already fully vetted by both a landscape sweep and a charter-scoring pass.

Prints one JSON line per bundle with at least one candidate, ordered by
priority -- highest max candidate confidence first, then most candidates,
then bundle slug for a stable tiebreak:

  {"bundle": "telemetry-state", "count": 3, "max_confidence": 0.93,
   "candidates": ["fleeting/.../a.md", "fleeting/.../b.md", ...]}

`candidates` is itself sorted descending by confidence, matching
select-focused-candidates.py's ranking within a bundle. Prints nothing
(exit 0) if no bundle has any qualifying candidate.

Usage (from repo root, or any cwd -- script locates the root):
  python3 scripts/select-catchup-candidates.py
  python3 scripts/select-catchup-candidates.py --min-confidence 0.8
  python3 scripts/select-catchup-candidates.py telemetry-state capacity-load
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from domains import load_domains  # noqa: E402

DEFAULT_MIN_CONFIDENCE = 0.7


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


def load_ratings(ratings_file: Path) -> list[dict]:
    """Return cached rating entries, one dict per JSONL line. A line that
    fails to parse becomes an empty dict rather than raising -- confidence()
    treats a missing/invalid confidence as -inf, so a malformed line is
    simply never a candidate.
    """
    if not ratings_file.is_file():
        return []
    entries: list[dict] = []
    for line in ratings_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            obj = {}
        if not isinstance(obj, dict):
            obj = {}
        entries.append(obj)
    return entries


def confidence(entry: dict) -> float:
    """Confidence as a sortable float; missing/non-numeric/NaN/inf -> -inf.

    Mirrors sort_key() in select-focused-candidates.py -- see that module's
    docstring for why NaN and out-of-range values must not compare as
    real candidates.
    """
    value = entry.get("confidence")
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    ):
        return float(value)
    return float("-inf")


def rated_at_or_above(entries: list[dict], min_confidence: float) -> dict[str, float]:
    """Return {path: confidence} for entries at/above min_confidence.

    Duplicate paths (e.g. from a manually merged cache) keep the highest
    confidence seen, matching select-focused-candidates.py's dedup rule.
    """
    best: dict[str, float] = {}
    for entry in entries:
        value = confidence(entry)
        if value < min_confidence:
            continue
        path = entry.get("path")
        if not isinstance(path, str) or not path:
            continue
        if path not in best or value > best[path]:
            best[path] = value
    return best


def bundle_candidates(
    unreviewed: set[str],
    landscape_paths: set[str],
    rated: dict[str, float],
) -> list[tuple[str, float]]:
    """The three-way intersection, sorted descending by confidence."""
    qualifying = unreviewed & landscape_paths & rated.keys()
    return sorted(
        ((path, rated[path]) for path in qualifying),
        key=lambda item: item[1],
        reverse=True,
    )


def bundle_priority_key(result: dict) -> tuple[float, int, str]:
    """Sort key for ready bundles: highest max confidence first, then most
    candidates, then bundle slug ascending for a stable, deterministic
    tiebreak. Returned as a tuple to negate for a descending sort on the
    first two fields while keeping the slug ascending."""
    return (-result["max_confidence"], -result["count"], result["bundle"])


def select_ready_bundles(
    root: Path, domains: list[str], min_confidence: float
) -> list[dict]:
    fleeting_paths = load_fleeting_paths(root)
    overlap = load_landscape_overlap(root / "landscape" / "overlap.jsonl")

    ready: list[dict] = []
    for bundle in domains:
        reviewed = load_ledger_paths(root / "curation" / f"{bundle}.txt")
        unreviewed = fleeting_paths - reviewed
        landscape_paths = landscape_paths_for_bundle(overlap, bundle)
        rated = rated_at_or_above(
            load_ratings(root / "ratings" / f"{bundle}.jsonl"), min_confidence
        )
        candidates = bundle_candidates(unreviewed, landscape_paths, rated)
        if not candidates:
            continue
        ready.append(
            {
                "bundle": bundle,
                "count": len(candidates),
                "max_confidence": candidates[0][1],
                "candidates": [path for path, _confidence in candidates],
            }
        )

    ready.sort(key=bundle_priority_key)
    return ready


def min_confidence_type(value: str) -> float:
    """argparse `type=` for `--min-confidence`: finite and within [0, 1].
    See select-focused-candidates.py's min_confidence_type for the NaN
    footgun this guards against; the reasoning is identical here.
    """
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid float value: {value!r}") from exc
    if not math.isfinite(parsed):
        raise argparse.ArgumentTypeError(
            f"--min-confidence must be finite, got {value!r}"
        )
    if not 0.0 <= parsed <= 1.0:
        raise argparse.ArgumentTypeError(
            f"--min-confidence must be within [0, 1], got {value!r}"
        )
    return parsed


def main() -> None:
    root = find_root(Path.cwd())
    all_domains = load_domains(root)

    parser = argparse.ArgumentParser(
        description=(
            "Select bundles ready for a /catch-up focused curation round: "
            "unreviewed ∩ landscape-tagged ∩ rated-above-threshold, per bundle."
        )
    )
    parser.add_argument(
        "bundles",
        nargs="*",
        metavar="bundle-slug",
        help=f"Restrict to these domain slugs (default: all {len(all_domains)})",
    )
    parser.add_argument(
        "--min-confidence",
        type=min_confidence_type,
        default=DEFAULT_MIN_CONFIDENCE,
        help=(
            "Minimum rating confidence to count as scored, in [0, 1] "
            f"(default: {DEFAULT_MIN_CONFIDENCE})"
        ),
    )
    args = parser.parse_args()

    domains = args.bundles or all_domains
    unknown = sorted(set(domains) - set(all_domains))
    if unknown:
        raise SystemExit(f"error: unknown domain slug(s): {', '.join(unknown)}")

    for result in select_ready_bundles(root, domains, args.min_confidence):
        print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
