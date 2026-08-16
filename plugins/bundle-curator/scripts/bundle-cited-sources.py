#!/usr/bin/env python3
"""Rank sources cited by a domain bundle and map them to fleeting paths.

Used by /charter-review. Reads wiki note frontmatter only — never opens
fleeting note bodies.

For large multi-domain source folders, also derives a chapter-narrowed
dispatch list from `resource:` locators (e.g. "ch. 14") so the researcher
can fully read the chapters this bundle actually cites.

Usage (from repo root, or any cwd — script locates the root):
  python3 scripts/bundle-cited-sources.py <domain-slug>
  python3 scripts/bundle-cited-sources.py <domain-slug> --top N
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Prefer full-group dispatch at or below this size; above it, prefer
# chapter-narrowed paths from resource locators when available.
LARGE_GROUP = 15


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"['’]", "", text)
    text = re.split(r",\s*\d+(?:st|nd|rd|th)\s+edition", text, maxsplit=1)[0]
    text = re.split(r":\s*", text, maxsplit=1)[0]
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\b(the|a|an|and|of|for|in|to|on)\b", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def slugify(text: str) -> str:
    return normalize(text).replace(" ", "-")


def strip_quotes(raw: str) -> str:
    raw = raw.strip()
    if (raw.startswith('"') and raw.endswith('"')) or (
        raw.startswith("'") and raw.endswith("'")
    ):
        return raw[1:-1]
    return raw


def parse_sources(md: Path) -> list[tuple[str, str]]:
    """Return (title, resource) pairs from concept frontmatter."""
    text = md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end < 0:
        return []
    fm = text[3:end]
    pairs: list[tuple[str, str]] = []
    in_sources = False
    current_title: str | None = None
    for line in fm.splitlines():
        if re.match(r"^sources:\s*$", line):
            in_sources = True
            continue
        if in_sources:
            if line and not line[0].isspace() and not line.startswith("-"):
                if current_title:
                    pairs.append((current_title, ""))
                    current_title = None
                in_sources = False
                continue
            m_title = re.match(r"^\s*-\s+title:\s*(.+?)\s*$", line)
            if m_title:
                if current_title:
                    pairs.append((current_title, ""))
                current_title = strip_quotes(m_title.group(1))
                continue
            m_res = re.match(r"^\s+resource:\s*(.+?)\s*$", line)
            if m_res and current_title:
                pairs.append((current_title, strip_quotes(m_res.group(1))))
                current_title = None
                continue
    if current_title:
        pairs.append((current_title, ""))
    return pairs


def extract_chapters(resource: str) -> set[int]:
    """Parse chapter numbers from resource locator strings.

    Supports lists and ranges such as: "ch. 10 & 11", "ch. 2-3", "ch. 1–3".
    """
    chapters: set[int] = set()
    if not resource:
        return chapters

    seq_re = re.compile(
        r"\b(?:ch|chapter|chap)\.?\s*"
        r"(\d+(?:\s*(?:-|–|to)\s*\d+)?"
        r"(?:\s*(?:,|&|and)\s*\d+(?:\s*(?:-|–|to)\s*\d+)?)*)",
        flags=re.I,
    )

    for m in seq_re.finditer(resource):
        seq = m.group(1)
        for item in re.split(r"\s*(?:,|&|and)\s*", seq, flags=re.I):
            if not item:
                continue
            m_range = re.match(
                r"^\s*(\d+)\s*(?:-|–|to)\s*(\d+)\s*$", item, flags=re.I
            )
            if m_range:
                start, end = int(m_range.group(1)), int(m_range.group(2))
                if start <= end:
                    chapters.update(range(start, end + 1))
                continue
            m_num = re.match(r"^\s*(\d+)\s*$", item)
            if m_num:
                chapters.add(int(m_num.group(1)))

    return chapters


def list_fleeting_targets(fleeting: Path) -> list[tuple[str, str, list[str]]]:
    """Return (label, match_key, paths) for dirs and loose part files."""
    targets: list[tuple[str, str, list[str]]] = []
    if not fleeting.is_dir():
        return targets

    root = fleeting.parent
    for child in sorted(fleeting.iterdir()):
        if child.name.startswith(".") or child.name == "README.md":
            continue
        if child.is_dir():
            notes = sorted(
                str(p.relative_to(root)) for p in child.rglob("*.md")
            )
            if notes:
                targets.append((child.name + "/", slugify(child.name), notes))
        elif child.suffix == ".md":
            stem = child.stem
            key = re.sub(r"-part\d+$", "", stem)
            rel = str(child.relative_to(root))
            merged = False
            for i, (label, mkey, paths) in enumerate(targets):
                if mkey == slugify(key) and not label.endswith("/"):
                    targets[i] = (
                        f"{key}-part*.md",
                        mkey,
                        sorted(paths + [rel]),
                    )
                    merged = True
                    break
            if not merged:
                targets.append((f"{stem}.md", slugify(key), [rel]))
    return targets


def best_fleeting_match(
    title: str, targets: list[tuple[str, str, list[str]]]
) -> tuple[str, list[str]] | None:
    title_slug = slugify(title)
    title_norm = normalize(title)
    if not title_slug:
        return None

    best: tuple[int, str, list[str]] | None = None
    for label, key, paths in targets:
        key_norm = key.replace("-", " ")
        score = 0
        if key == title_slug or key_norm == title_norm:
            score = 100
        elif title_slug.startswith(key) or key.startswith(title_slug):
            score = 80 + min(len(key), len(title_slug))
        elif key in title_slug or title_slug in key:
            score = 60 + min(len(key), len(title_slug))
        else:
            t_tokens = set(title_norm.split())
            k_tokens = set(key_norm.split())
            if not t_tokens or not k_tokens:
                continue
            overlap = len(t_tokens & k_tokens) / max(
                len(t_tokens), len(k_tokens)
            )
            if overlap >= 0.6:
                score = int(40 + 40 * overlap)
        if score and (best is None or score > best[0]):
            best = (score, label, paths)
    if best is None or best[0] < 40:
        return None
    return best[1], best[2]


def paths_for_chapters(paths: list[str], chapters: set[int]) -> list[str]:
    """Select fleeting paths whose basename starts with zero-padded ch num."""
    if not chapters:
        return []
    selected: list[str] = []
    for p in paths:
        name = Path(p).name
        m = re.match(r"^0*(\d+)-", name)
        if m and int(m.group(1)) in chapters:
            selected.append(p)
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rank bundle source citations and map to fleeting paths."
    )
    parser.add_argument("domain_slug", help="Bundle / domain slug")
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="How many top-cited sources to print (default: 5)",
    )
    args = parser.parse_args()
    if args.top < 1:
        raise SystemExit("error: --top must be >= 1")

    root = find_root(Path(__file__).resolve().parent)
    bundle = root / args.domain_slug
    if not bundle.is_dir():
        raise SystemExit(f"error: bundle folder not found: {bundle}")

    title_counts: Counter[str] = Counter()
    # Canonical title (first spelling) -> chapters cited in resource fields
    chapters_by_title: dict[str, set[int]] = defaultdict(set)
    canonical: dict[str, str] = {}

    note_count = 0
    for md in sorted(bundle.glob("*.md")):
        note_count += 1
        for title, resource in parse_sources(md):
            key = slugify(title)
            if key not in canonical:
                canonical[key] = title
            title_counts[canonical[key]] += 1
            chapters_by_title[canonical[key]].update(
                extract_chapters(resource)
            )

    fleeting_targets = list_fleeting_targets(root / "fleeting")

    print(f"bundle: {args.domain_slug}")
    print(f"notes_scanned: {note_count}")
    print(f"distinct_sources: {len(title_counts)}")
    print()
    print(
        f"{'rank':<5} {'cites':<6} {'all':<5} {'dispatch':<9} "
        f"{'source_title'}"
    )
    print("-" * 88)

    if not title_counts:
        print("(no sources: titles found in bundle frontmatter)")
        return

    ranked = title_counts.most_common(args.top)
    for i, (title, n) in enumerate(ranked, 1):
        match = best_fleeting_match(title, fleeting_targets)
        n_all = len(match[1]) if match else 0
        if match:
            label, paths = match
            chans = chapters_by_title.get(title, set())
            narrowed = paths_for_chapters(paths, chans)
            if n_all > LARGE_GROUP and narrowed:
                n_disp = len(narrowed)
            else:
                n_disp = n_all
        else:
            n_disp = 0
        print(f"{i:<5} {n:<6} {n_all:<5} {n_disp:<9} {title}")

    print()
    print("## fleeting path groups (for researcher dispatch)")
    print(
        f"# For groups larger than {LARGE_GROUP} notes, dispatch_paths "
        "prefer chapters"
    )
    print("# cited in this bundle's resource: locators when parseable.")
    for i, (title, n) in enumerate(ranked, 1):
        match = best_fleeting_match(title, fleeting_targets)
        print()
        print(f"### {i}. {title} ({n} cites)")
        if not match:
            print("fleeting_match: NONE — map manually or skip")
            print("dispatch_mode: none")
            continue
        label, paths = match
        chans = sorted(chapters_by_title.get(title, set()))
        narrowed = paths_for_chapters(paths, set(chans))
        print(f"fleeting_match: {label}")
        print(f"all_fleeting_notes: {len(paths)}")
        if chans:
            print(
                "cited_chapters: "
                + ", ".join(f"ch.{c}" for c in chans)
            )
        else:
            print("cited_chapters: (none parsed from resource: fields)")

        if len(paths) > LARGE_GROUP and narrowed:
            dispatch = narrowed
            mode = "cited-chapters"
        else:
            dispatch = paths
            mode = "full-group"
        print(f"dispatch_mode: {mode}")
        print(f"dispatch_paths: {len(dispatch)}")
        for p in dispatch:
            print(p)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
