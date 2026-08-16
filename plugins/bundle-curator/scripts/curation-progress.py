#!/usr/bin/env python3
"""Per-domain curation progress with ratings-cache backlog stats.

Path-and-ledger only for fleeting notes — never opens note bodies. Compares
paths under fleeting/ to curation/<domain>.txt and ratings/<domain>.jsonl.

Usage (from repo root, or any cwd -- script locates the root):
  python3 scripts/curation-progress.py
  python3 scripts/curation-progress.py --pending-only
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from domains import load_domains  # noqa: E402

HIGH_CONFIDENCE_THRESHOLD = 0.7


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


def load_ratings(ratings_file: Path) -> list[dict]:
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


def confidence_value(entry: dict) -> float | None:
    value = entry.get("confidence")
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    ):
        return float(value)
    return None


def pending_ratings_stats(
    entries: list[dict], pending_paths: set[str]
) -> tuple[float | None, int]:
    """Return (max confidence, count with confidence >= threshold) for pending.

    The threshold comparison is `>=` here to match the selectors that
    actually gate on it (select-focused-candidates.py,
    select-catchup-candidates.py both use "at or above"); this table's
    P>=0.7 column is meant to preview what those selectors would pick up.
    """
    best_by_path: dict[str, float] = {}
    for entry in entries:
        path = entry.get("path")
        if not isinstance(path, str) or not path or path not in pending_paths:
            continue
        confidence = confidence_value(entry)
        if confidence is None:
            continue
        current = best_by_path.get(path)
        if current is None or confidence > current:
            best_by_path[path] = confidence

    if not best_by_path:
        return None, 0

    scores = list(best_by_path.values())
    max_confidence = max(scores)
    high_count = sum(
        1 for score in scores if score >= HIGH_CONFIDENCE_THRESHOLD
    )
    return max_confidence, high_count


def format_max_confidence(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.2f}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show reviewed / total / pending fleeting notes per domain."
    )
    parser.add_argument(
        "--pending-only",
        "-p",
        action="store_true",
        help="List only domains that still have unreviewed notes.",
    )
    args = parser.parse_args()

    root = find_root(Path(__file__).resolve().parent)
    domains = load_domains(root)
    fleeting_paths = load_fleeting_paths(root)
    total = len(fleeting_paths)

    header = (
        f"{'DOMAIN':<28} {'REVIEWED':>10} {'TOTAL':>10} {'PENDING':>10} "
        f"{'MAX_P':>8} {'P>=0.7':>8}"
    )
    divider = (
        f"{'-' * 28} {'-' * 10} {'-' * 10} {'-' * 10} "
        f"{'-' * 8} {'-' * 8}"
    )
    print(header)
    print(divider)

    pending_domains = 0
    any_shown = False

    for domain in domains:
        ledger = root / "curation" / f"{domain}.txt"
        curated_paths = load_ledger_paths(ledger)
        reviewed = len(curated_paths & fleeting_paths)
        pending = total - reviewed
        pending_paths = fleeting_paths - curated_paths

        ratings_file = root / "ratings" / f"{domain}.jsonl"
        max_confidence, high_count = pending_ratings_stats(
            load_ratings(ratings_file), pending_paths
        )

        if args.pending_only and pending == 0:
            continue

        any_shown = True
        marker = ""
        if pending > 0:
            marker = " *"
            pending_domains += 1

        print(
            f"{domain:<28} {reviewed:>10} {total:>10} {pending:>10} "
            f"{format_max_confidence(max_confidence):>8} {high_count:>8}{marker}"
        )

    print(divider)
    print(f"Fleeting notes total: {total}")
    if args.pending_only and not any_shown:
        print("No domains with pending work.")
    else:
        print(f"Domains with pending work: {pending_domains} (marked *)")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
