#!/usr/bin/env python3
"""List seed fleeting paths for `/source-watch`.

Ranks bundle `sources:` citations (same helpers as
`bundle-cited-sources.py`), maps them to onboarded `fleeting/` groups, and
prints Related Work / survey-style note paths from those cores for the
source-watch researcher to read.

Also includes agent-heavy chapters from known survey books when those folders
exist (`ai-engineering` ch.06–07; `prompt-engineering-for-llms` agent/reasoning
chapters).

Usage (from repo root, or any cwd — script locates the root):
  python3 scripts/list-source-watch-seeds.py <domain-slug>
  python3 scripts/list-source-watch-seeds.py <domain-slug> --top 8 --json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path

RELATED_NAME = re.compile(
    r"(related|discussion|survey|conclusion|background|prior.?work|"
    r"agents?|memory|rag|reasoning|workflow|tool|orchestr)",
    re.I,
)

# Chapter number prefixes (as in fleeting filenames) to always consider.
BOOK_SEED_HINTS: dict[str, tuple[str, ...]] = {
    "ai-engineering": ("06", "07"),
    "prompt-engineering-for-llms": ("05", "06", "09", "10"),
}


def load_bundle_cited_module():
    script = Path(__file__).resolve().parent / "bundle-cited-sources.py"
    spec = importlib.util.spec_from_file_location("bundle_cited_sources", script)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def chapter_prefix(name: str) -> str | None:
    m = re.match(r"^(\d+)", name)
    return m.group(1) if m else None


def pick_seeds_for_group(slug: str, paths: list[str]) -> list[str]:
    hints = BOOK_SEED_HINTS.get(slug, ())
    # Large survey books: stay inside hinted chapters only (avoid whole-book
    # RELATED_NAME sweeps that pull finetuning / data chapters).
    if hints:
        in_chapters = [
            p for p in paths if chapter_prefix(Path(p).name) in hints
        ]
        related_in = [
            p for p in in_chapters if RELATED_NAME.search(Path(p).name)
        ]
        return sorted(set(related_in) | set(in_chapters))
    related = [p for p in paths if RELATED_NAME.search(Path(p).name)]
    if related:
        return related
    return paths[:3]


def add_book_hint_seeds(
    root: Path, seed_paths: list[str], seen: set[str]
) -> None:
    for slug, prefixes in BOOK_SEED_HINTS.items():
        folder = root / "fleeting" / slug
        if not folder.is_dir():
            continue
        for md in sorted(folder.glob("*.md")):
            prefix = chapter_prefix(md.name)
            if prefix not in prefixes:
                continue
            # Prefer dense agent/reasoning notes; for ai-engineering include
            # all ch.06–07 notes (prompt + agents + memory + rag).
            if slug != "ai-engineering" and not RELATED_NAME.search(md.name):
                continue
            rel = str(md.relative_to(root))
            if rel not in seen:
                seen.add(rel)
                seed_paths.append(rel)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List source-watch seed fleeting paths for a domain."
    )
    parser.add_argument("domain_slug", help="Bundle / domain slug")
    parser.add_argument(
        "--top",
        type=int,
        default=8,
        help="How many top-cited sources to seed from (default: 8)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print a JSON object instead of plain paths",
    )
    args = parser.parse_args()
    if args.top < 1:
        raise SystemExit("error: --top must be >= 1")

    mod = load_bundle_cited_module()
    root = mod.find_root(Path.cwd())
    bundle_dir = root / args.domain_slug
    if not bundle_dir.is_dir():
        raise SystemExit(f"error: bundle folder not found: {bundle_dir}")

    counts: Counter[str] = Counter()
    title_display: dict[str, str] = {}
    for md in sorted(bundle_dir.glob("*.md")):
        for title, _resource in mod.parse_sources(md):
            key = mod.normalize(title)
            if not key:
                continue
            counts[key] += 1
            title_display.setdefault(key, title)

    targets = mod.list_fleeting_targets(root / "fleeting")
    ranked = counts.most_common(args.top)

    cores: list[dict] = []
    seed_paths: list[str] = []
    seen: set[str] = set()

    for key, cite_count in ranked:
        title = title_display[key]
        match = mod.best_fleeting_match(title, targets)
        if not match:
            cores.append(
                {
                    "title": title,
                    "citations": cite_count,
                    "fleeting": None,
                    "seed_paths": [],
                }
            )
            continue
        label, paths = match
        slug = label.rstrip("/")
        if slug.endswith(".md"):
            slug = Path(slug).stem
            slug = re.sub(r"-part\d+$", "", slug)
        chosen = pick_seeds_for_group(slug, paths)
        core_seeds = []
        for p in chosen:
            if p not in seen:
                seen.add(p)
                seed_paths.append(p)
                core_seeds.append(p)
        cores.append(
            {
                "title": title,
                "citations": cite_count,
                "fleeting": label,
                "seed_paths": core_seeds,
            }
        )

    add_book_hint_seeds(root, seed_paths, seen)

    payload = {
        "domain": args.domain_slug,
        "cores": cores,
        "seed_paths": seed_paths,
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(
            f"# domain={args.domain_slug} seeds={len(seed_paths)} "
            f"cores={len(cores)}"
        )
        for p in seed_paths:
            print(p)


if __name__ == "__main__":
    main()
