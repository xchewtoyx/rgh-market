#!/usr/bin/env python3
"""Deterministic candidate selection for `/curate --focused`.

Reads the per-domain ratings cache written by `fleeting-researcher`
(`ratings/<domain>.jsonl`), filters out paths already curated (per
`curation/<domain>.txt`), sorts the remainder descending by confidence, and
walks from the top, stopping at the first entry below `--min-confidence`.
Because the list is sorted, one sub-threshold hit is sufficient to stop --
no need to scan the rest (see docs/curation.md, Ratings cache).

Prints the surviving candidate paths to stdout, one per line, highest
confidence first. Prints nothing (exit 0) if no candidates qualify.

Usage (from repo root, or any cwd -- script locates the root):
  python3 scripts/select-focused-candidates.py <domain-slug>
  python3 scripts/select-focused-candidates.py --bundle <domain-slug>
  python3 scripts/select-focused-candidates.py <domain-slug> --min-confidence 0.8
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

DEFAULT_MIN_CONFIDENCE = 0.7


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def load_ledger_paths(ledger: Path) -> set[str]:
    """Return the set of paths already ledgered (reviewed) for a domain.

    Mirrors the ledger convention documented in docs/curation.md: one path
    per line, `#`-prefixed lines are comments, blank lines are ignored.
    """
    if not ledger.is_file():
        return set()
    paths: set[str] = set()
    for line in ledger.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        paths.add(line)
    return paths


def load_ratings(ratings_file: Path) -> list[dict]:
    """Return cached rating entries for a domain, one dict per JSONL line.

    A line that fails to parse as JSON becomes an empty dict rather than
    raising -- `sort_key` treats a missing/invalid confidence as -inf, so a
    malformed line always sorts last and never breaks the run.
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


def sort_key(entry: dict) -> float:
    """Confidence as a sortable float; missing/non-numeric -> -inf (last).

    NaN is numeric-typed but explicitly excluded: `float('nan') < x` is
    always False (NaN never compares true either way), so a NaN confidence
    would otherwise never trigger the threshold-walk break and would be
    unconditionally selected regardless of `--min-confidence`. Guarding with
    `math.isfinite` treats it the same as any other unusable value -> -inf,
    last. (This also maps a literal `+inf` confidence to -inf; unlike NaN,
    `+inf` doesn't have a comparison-bypass bug -- `inf < x` is correctly
    False -- but a confidence value outside a sane range is equally not a
    real score, so it is excluded for the same reason.)
    """
    value = entry.get("confidence")
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    ):
        return float(value)
    return float("-inf")


def select_candidates(
    entries: list[dict], curated_paths: set[str], min_confidence: float
) -> list[str]:
    """Sort descending by confidence; walk from the top; stop at the first
    entry below `min_confidence` (short-circuit -- entries after that point
    are never inspected further, so a malformed entry beyond the cutoff
    cannot break the run). Paths already in `curated_paths` are dropped
    before sorting so they never count as a stopping point or a result.

    Duplicate paths above the cutoff (e.g. from manual cache edits/merges,
    or a prior scoring bug) are deduplicated as the walk proceeds, keeping
    only the first occurrence seen in descending-confidence order -- which
    is also the highest-confidence occurrence for that path. This dedup is
    applied during the walk, not before sorting, so it never changes which
    entries the short-circuit break sees or where it stops.
    """
    remaining = [
        entry for entry in entries if entry.get("path") not in curated_paths
    ]
    ranked = sorted(remaining, key=sort_key, reverse=True)

    candidates: list[str] = []
    seen_paths: set[str] = set()
    for entry in ranked:
        confidence = sort_key(entry)
        if confidence < min_confidence:
            break
        path = entry.get("path")
        if not isinstance(path, str) or not path:
            # Malformed: numeric confidence cleared the threshold but there
            # is no usable path. Skip it rather than emit a bad candidate;
            # it was never a real "hit".
            continue
        if path in seen_paths:
            # Duplicate of an already-kept (higher-or-equal confidence)
            # occurrence -- skip without breaking the walk.
            continue
        seen_paths.add(path)
        candidates.append(path)
    return candidates


def min_confidence_type(value: str) -> float:
    """argparse `type=` for `--min-confidence`: finite and within [0, 1].

    Plain `type=float` accepts NaN/inf and out-of-range values. In
    particular, `--min-confidence nan` breaks the threshold walk in
    `select_candidates`: `confidence < nan` is always False (NaN never
    compares true either way), so the walk never sees a sub-threshold
    entry and never stops, which can select unintended entries. This is
    the same NaN-comparison footgun already guarded for cache-entry
    confidence in `sort_key` (see `math.isfinite` there), but here it
    applies to the CLI argument -- so it is guarded the same way, at
    parse time, with a clear argparse error rather than silent broken
    behavior.
    """
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid float value: {value!r}"
        ) from exc
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
    parser = argparse.ArgumentParser(
        description=(
            "Deterministically select /curate --focused candidates from "
            "the ratings cache."
        )
    )
    parser.add_argument(
        "bundle_positional",
        nargs="?",
        metavar="bundle",
        help="Domain slug (positional form)",
    )
    parser.add_argument(
        "--bundle",
        dest="bundle_flag",
        help="Domain slug (flag form; alternative to the positional arg)",
    )
    parser.add_argument(
        "--min-confidence",
        type=min_confidence_type,
        default=DEFAULT_MIN_CONFIDENCE,
        help=(
            "Minimum confidence to select, in [0, 1] "
            f"(default: {DEFAULT_MIN_CONFIDENCE})"
        ),
    )
    args = parser.parse_args()

    if args.bundle_positional and args.bundle_flag:
        if args.bundle_positional != args.bundle_flag:
            raise SystemExit(
                "error: give the domain slug once, either positionally or "
                "via --bundle, not both with different values"
            )
        bundle = args.bundle_positional
    else:
        bundle = args.bundle_positional or args.bundle_flag

    if not bundle:
        raise SystemExit(
            "error: domain slug required (positional or --bundle)"
        )

    root = find_root(Path(__file__).resolve().parent)
    bundle_dir = root / bundle
    if not bundle_dir.is_dir():
        raise SystemExit(f"error: bundle folder not found: {bundle_dir}")

    ledger = root / "curation" / f"{bundle}.txt"
    ratings_file = root / "ratings" / f"{bundle}.jsonl"

    curated_paths = load_ledger_paths(ledger)
    entries = load_ratings(ratings_file)
    candidates = select_candidates(entries, curated_paths, args.min_confidence)

    for path in candidates:
        print(path)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
