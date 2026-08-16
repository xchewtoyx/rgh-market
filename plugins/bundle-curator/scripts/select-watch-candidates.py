#!/usr/bin/env python3
"""Deterministic candidate selection for `/source-watch`.

Reads the per-domain watch cache written by `source-watch-researcher`
(`watch/<domain>.jsonl`), drops titles that already match onboarded
`fleeting/` sources, groups remaining lines by normalized title, and keeps
groups with enough distinct citing cores and sufficient charter_fit.

Prints JSON lines for survivors (highest core count, then charter_fit).
Prints nothing (exit 0) if no candidates qualify.

Usage:
  python3 scripts/select-watch-candidates.py <domain-slug>
  python3 scripts/select-watch-candidates.py <domain-slug> --min-cores 2
  python3 scripts/select-watch-candidates.py <domain-slug> --limit 10
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

DEFAULT_MIN_CORES = 2
DEFAULT_MIN_CHARTER_FIT = 0.7
DEFAULT_LIMIT = 10


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"['’]", "", text)
    text = re.split(r":\s*", text, maxsplit=1)[0]
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\b(the|a|an|and|of|for|in|to|on)\b", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def slugify(text: str) -> str:
    return normalize(text).replace(" ", "-")


def load_watch_entries(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    entries: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            entries.append(obj)
    return entries


def onboarded_keys(fleeting: Path) -> set[str]:
    """Normalized titles/slugs already present under fleeting/."""
    keys: set[str] = set()
    if not fleeting.is_dir():
        return keys
    for child in fleeting.iterdir():
        if child.name.startswith(".") or child.name == "README.md":
            continue
        if child.is_dir():
            keys.add(normalize(child.name.replace("-", " ")))
            keys.add(slugify(child.name))
            # Also read first note title if present
            notes = sorted(child.glob("*.md"))
            if notes:
                text = notes[0].read_text(encoding="utf-8", errors="replace")
                if text.startswith("---"):
                    end = text.find("\n---", 3)
                    fm = text[3:end] if end > 0 else ""
                    m = re.search(
                        r"^  title:\s*(.+)$", fm, flags=re.M
                    )
                    if m:
                        raw = m.group(1).strip().strip('"').strip("'")
                        keys.add(normalize(raw))
                        keys.add(slugify(raw))
        elif child.suffix == ".md":
            stem = re.sub(r"-part\d+$", "", child.stem)
            keys.add(normalize(stem.replace("-", " ")))
            keys.add(slugify(stem))
    return keys


def is_onboarded(title: str, keys: set[str]) -> bool:
    n = normalize(title)
    s = slugify(title)
    if n in keys or s in keys:
        return True
    for k in keys:
        if not k:
            continue
        if k in n or n in k or k in s or s in k:
            # Require meaningful overlap length to avoid tiny false hits
            if min(len(k), len(n.replace(" ", "-"))) >= 12:
                return True
    return False


def charter_fit(entry: dict) -> float:
    value = entry.get("charter_fit")
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    ):
        return float(value)
    return float("-inf")


def select_candidates(
    entries: list[dict],
    onboarded: set[str],
    min_cores: int,
    min_charter_fit: float,
    limit: int,
) -> list[dict]:
    groups: dict[str, list[dict]] = defaultdict(list)
    display_title: dict[str, str] = {}
    for entry in entries:
        title = entry.get("title")
        if not isinstance(title, str) or not title.strip():
            continue
        if is_onboarded(title, onboarded):
            continue
        key = normalize(title)
        if not key:
            continue
        groups[key].append(entry)
        display_title.setdefault(key, title.strip())

    survivors: list[dict] = []
    for key, group in groups.items():
        cores = {
            e.get("citing_core")
            for e in group
            if isinstance(e.get("citing_core"), str) and e.get("citing_core")
        }
        fit = max((charter_fit(e) for e in group), default=float("-inf"))
        if len(cores) < min_cores:
            continue
        if fit < min_charter_fit:
            continue
        # Prefer richest notes / authors / year from highest-fit line
        best = max(group, key=charter_fit)
        survivors.append(
            {
                "title": display_title[key],
                "authors": best.get("authors"),
                "year": best.get("year"),
                "arxiv_id": best.get("arxiv_id"),
                "core_count": len(cores),
                "citing_cores": sorted(cores),
                "charter_fit": fit,
                "notes": best.get("notes"),
            }
        )

    survivors.sort(
        key=lambda s: (s["core_count"], s["charter_fit"]), reverse=True
    )
    return survivors[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Select source-watch candidates from the watch cache."
    )
    parser.add_argument("domain_slug", help="Bundle / domain slug")
    parser.add_argument(
        "--min-cores",
        type=int,
        default=DEFAULT_MIN_CORES,
        help=f"Minimum distinct citing cores (default: {DEFAULT_MIN_CORES})",
    )
    parser.add_argument(
        "--min-charter-fit",
        type=float,
        default=DEFAULT_MIN_CHARTER_FIT,
        help=(
            "Minimum max charter_fit in the group "
            f"(default: {DEFAULT_MIN_CHARTER_FIT})"
        ),
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"Max survivors to print (default: {DEFAULT_LIMIT})",
    )
    args = parser.parse_args()
    if args.min_cores < 1:
        raise SystemExit("error: --min-cores must be >= 1")
    if args.limit < 1:
        raise SystemExit("error: --limit must be >= 1")

    root = find_root(Path.cwd())
    entries = load_watch_entries(root / "watch" / f"{args.domain_slug}.jsonl")
    onboarded = onboarded_keys(root / "fleeting")
    survivors = select_candidates(
        entries,
        onboarded,
        min_cores=args.min_cores,
        min_charter_fit=args.min_charter_fit,
        limit=args.limit,
    )
    for item in survivors:
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
