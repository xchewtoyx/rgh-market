#!/usr/bin/env python3
"""Dump PDF/EPUB sources into per-chapter plain markdown files.

Converts a source document into read-ready chapter dumps under
``incoming/<source-slug>/`` for downstream /onboard subagent dispatch.

Chapter boundaries come from the embedded document outline (``get_toc()``)
when available. When no outline exists, the script can extract cheap
front-matter text for an agent to build a chapter map, then slice using
``--chapter-map``.

Usage (from repo root, or any cwd — script locates the root):
  .venv/bin/python3 scripts/dump-source-chapters.py incoming/book.pdf
  .venv/bin/python3 scripts/dump-source-chapters.py incoming/book.pdf --slug my-book
  .venv/bin/python3 scripts/dump-source-chapters.py incoming/scan.pdf --chapter-map map.json
  .venv/bin/python3 scripts/dump-source-chapters.py incoming/scan.pdf --front-matter-only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:  # pragma: no cover - exercised via install checks
    fitz = None


CHAPTER_TITLE_RE = re.compile(
    r"\b(?:chapter|chap\.?)\s+(\d+)\b",
    re.IGNORECASE,
)
GENERATED_RAW_GLOB = "*-raw.md"
GENERATED_MAP_NAME = "chapter-map.json"
GENERATED_FRONT_MATTER_NAME = "front-matter.md"


@dataclass(frozen=True)
class ChapterSpec:
    number: int
    title: str
    start_page: int
    end_page: int

    @property
    def nn(self) -> str:
        return f"{self.number:02d}"

    @property
    def output_name(self) -> str:
        return f"{self.nn}-raw.md"


@dataclass(frozen=True)
class ChapterSpecDraft:
    number: int
    title: str
    start_page: int
    end_page: int | None = None


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def slugify_source_name(name: str) -> str:
    slug = re.sub(r"[^\w]+", "-", name, flags=re.UNICODE).strip("-").lower()
    if slug:
        return slug
    digest = hashlib.sha256(name.encode("utf-8")).hexdigest()[:12]
    return f"source-{digest}"


def normalize_slug(slug: str) -> str:
    """Reject path-like slugs; use --output-dir for custom locations."""
    cleaned = slug.strip()
    if not cleaned or cleaned in (".", ".."):
        raise SystemExit("error: --slug must be a single directory name")
    if "/" in cleaned or "\\" in cleaned:
        raise SystemExit("error: --slug must be a single directory name, not a path")
    if ".." in Path(cleaned).parts:
        raise SystemExit("error: --slug must be a single directory name, not a path")
    return cleaned


def starts_with_lower(text: str) -> bool:
    for char in text:
        if char.isalpha():
            return char.islower()
    return False


def merge_paragraph_lines(lines: list[str]) -> str:
    """Merge lines belonging to the same paragraph, resolving hyphenation."""
    merged = ""
    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue
        if not merged:
            merged = line_str
        elif merged.endswith("-") and not merged.endswith(" -"):
            merged = merged[:-1] + line_str
        else:
            merged += " " + line_str
    return merged


def clean_paragraph_flow(text: str) -> str:
    """Restore paragraph flows by joining lines that were split in PDFs."""
    if not text:
        return ""

    text = re.sub(r"\[([^\]]+)\]\(index\.html#[^)]*\)", r"\1", text)

    ends_with_newline = text.endswith("\n")
    raw_lines = text.splitlines()
    collapsed_lines: list[str] = []

    sentence_endings = (
        ".",
        "?",
        "!",
        ":",
        '"',
        "”",
        "’",
        ")",
        "]",
        "`",
        "}",
        ";",
    )

    def is_block_element(line_str: str) -> bool:
        stripped = line_str.strip()
        if not stripped:
            return True
        if stripped.startswith("#"):
            return True
        if stripped.startswith(("-", "*", "+")) or re.match(
            r"^\d+\.\s", stripped
        ):
            return True
        if stripped.startswith((">", "|", "<")):
            return True
        if stripped.startswith(("$$", "\\[", "\\(")) or stripped.endswith(
            ("$$", "\\]", "\\)")
        ):
            return True
        if re.match(r"^\(\d+[a-z]?\)\s*$", stripped):
            return True
        if (
            len(stripped) > 0
            and sum(1 for c in stripped if c in "=\\+-*/^_{}()$")
            / len(stripped)
            > 0.3
        ):
            return True
        return False

    i = 0
    while i < len(raw_lines):
        line = raw_lines[i]
        stripped = line.strip()

        if stripped == "":
            prev_line = ""
            for k in range(len(collapsed_lines) - 1, -1, -1):
                if collapsed_lines[k].strip() != "":
                    prev_line = collapsed_lines[k]
                    break

            next_line = ""
            for k in range(i + 1, len(raw_lines)):
                if raw_lines[k].strip() != "":
                    next_line = raw_lines[k]
                    break

            if prev_line and next_line:
                prev_stripped = prev_line.strip()
                next_stripped = next_line.strip()

                if is_block_element(prev_line) or is_block_element(next_line):
                    collapsed_lines.append(line)
                    i += 1
                    continue

                should_collapse = False
                if prev_stripped.endswith("-") and not prev_stripped.endswith(
                    " -"
                ):
                    should_collapse = True
                elif starts_with_lower(next_stripped):
                    should_collapse = True
                elif not prev_stripped.endswith(sentence_endings):
                    should_collapse = True

                if should_collapse:
                    i += 1
                    continue

        collapsed_lines.append(line)
        i += 1

    cleaned_lines: list[str] = []
    current_paragraph: list[str] = []

    for line in collapsed_lines:
        if is_block_element(line):
            if current_paragraph:
                cleaned_lines.append(merge_paragraph_lines(current_paragraph))
                current_paragraph = []
            cleaned_lines.append(line)
        else:
            current_paragraph.append(line)

    if current_paragraph:
        cleaned_lines.append(merge_paragraph_lines(current_paragraph))

    result = "\n".join(cleaned_lines)
    if ends_with_newline and not result.endswith("\n"):
        result += "\n"
    return result


def open_document(source_path: Path):
    if fitz is None:
        raise SystemExit(
            "error: PyMuPDF (pymupdf) is required; run scripts/setup.sh"
        )
    try:
        return fitz.open(source_path)
    except Exception as exc:  # pragma: no cover - depends on file validity
        raise SystemExit(f"error: could not open {source_path}: {exc}") from exc


def page_count(doc) -> int:
    return int(doc.page_count)


def chapter_entry_number(item: dict) -> int:
    if "chapter" in item:
        return int(item["chapter"])
    if "number" in item:
        return int(item["number"])
    raise KeyError("chapter")


def next_toc_boundary_after(
    toc: list, start_page: int, chapter_level: int
) -> int | None:
    """Return the page of the next peer-or-higher outline entry after start_page."""
    boundaries: list[int] = []
    for entry in toc:
        if len(entry) < 3:
            continue
        level, _title, page = int(entry[0]), str(entry[1]), int(entry[2])
        if page > start_page and level <= chapter_level:
            boundaries.append(page)
    return min(boundaries) if boundaries else None


def chapters_from_toc(toc: list, total_pages: int) -> list[ChapterSpec]:
    """Derive chapter boundaries from an embedded outline/bookmarks."""
    if not toc:
        return []

    candidates: list[tuple[int, str, int, int]] = []
    for entry in toc:
        if len(entry) < 3:
            continue
        level, title, page = int(entry[0]), str(entry[1]), int(entry[2])
        match = CHAPTER_TITLE_RE.search(title)
        if not match:
            continue
        number = int(match.group(1))
        candidates.append((number, title.strip(), page, level))

    if not candidates:
        return []

    by_number: dict[int, tuple[str, int, int]] = {}
    for number, title, page, level in candidates:
        if number not in by_number or page < by_number[number][1]:
            by_number[number] = (title, page, level)

    ordered = sorted(
        (
            (number, title, page, level)
            for number, (title, page, level) in sorted(by_number.items())
        ),
        key=lambda item: item[2],
    )

    bounded: list[ChapterSpec] = []
    for idx, (number, title, page, level) in enumerate(ordered):
        if idx + 1 < len(ordered):
            end_page = ordered[idx + 1][2] - 1
        else:
            end_page = total_pages
        boundary = next_toc_boundary_after(toc, page, level)
        if boundary is not None:
            end_page = min(end_page, boundary - 1)
        bounded.append(
            ChapterSpec(
                number=number,
                title=title,
                start_page=page,
                end_page=end_page,
            )
        )
    validate_chapter_plan(bounded, total_pages)
    return bounded


def chapters_from_map(
    data: object, total_pages: int
) -> list[ChapterSpec]:
    if not isinstance(data, list):
        raise SystemExit("error: chapter map must be a JSON array")
    if not data:
        raise SystemExit("error: chapter map is empty")

    chapters: list[ChapterSpec] = []
    for item in data:
        if not isinstance(item, dict):
            raise SystemExit("error: each chapter map entry must be an object")
        try:
            number = chapter_entry_number(item)
            title = str(item["title"])
            start_page = int(item["start_page"])
            end_page = (
                int(item["end_page"])
                if "end_page" in item and item["end_page"] is not None
                else None
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise SystemExit(
                "error: chapter map entries need chapter (or number), "
                "title, and start_page"
            ) from exc
        chapters.append(
            ChapterSpecDraft(
                number=number,
                title=title,
                start_page=start_page,
                end_page=end_page,
            )
        )

    return finalize_chapter_plan(chapters, total_pages)


def finalize_chapter_plan(
    chapters: list[ChapterSpecDraft], total_pages: int
) -> list[ChapterSpec]:
    """Sort, fill omitted end pages, and validate a chapter plan."""
    if not chapters:
        return []

    ordered = sorted(chapters, key=lambda ch: (ch.start_page, ch.number))
    filled: list[ChapterSpec] = []
    for idx, chapter in enumerate(ordered):
        if chapter.end_page is not None:
            end_page = chapter.end_page
        elif idx + 1 < len(ordered):
            end_page = ordered[idx + 1].start_page - 1
        else:
            end_page = total_pages
        filled.append(
            ChapterSpec(
                number=chapter.number,
                title=chapter.title,
                start_page=chapter.start_page,
                end_page=end_page,
            )
        )
    validate_chapter_plan(filled, total_pages)
    return filled


def resolve_repo_path(root: Path, path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (root / path).resolve()


def load_chapter_map(path: Path, total_pages: int) -> list[ChapterSpec]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: invalid JSON in {path}: {exc}") from exc

    if isinstance(raw, dict) and "chapters" in raw:
        raw = raw["chapters"]
    return chapters_from_map(raw, total_pages)


def validate_chapter_plan(
    chapters: list[ChapterSpec], total_pages: int
) -> None:
    seen_numbers: set[int] = set()
    prev_end = 0

    for chapter in chapters:
        if chapter.number in seen_numbers:
            raise SystemExit(
                f"error: duplicate chapter number {chapter.number} in map"
            )
        seen_numbers.add(chapter.number)

        if chapter.start_page < 1 or chapter.end_page < chapter.start_page:
            raise SystemExit(
                "error: invalid page range for "
                f"chapter {chapter.number}: "
                f"{chapter.start_page}-{chapter.end_page}"
            )
        if chapter.end_page > total_pages:
            raise SystemExit(
                f"error: chapter {chapter.number} end_page {chapter.end_page} "
                f"exceeds document length {total_pages}"
            )
        if chapter.start_page <= prev_end:
            raise SystemExit(
                "error: chapter ranges overlap or are out of order "
                f"(chapter {chapter.number} starts at {chapter.start_page}, "
                f"previous range ended at {prev_end})"
            )
        prev_end = chapter.end_page


# Backwards-compatible alias used in tests.
validate_chapters = validate_chapter_plan


def extract_page_range_text(
    doc,
    start_page: int,
    end_page: int,
    *,
    page_markers: bool = False,
) -> str:
    parts: list[str] = []
    for page_no in range(start_page, end_page + 1):
        page = doc[page_no - 1]
        text = page.get_text() or ""
        if not text.strip():
            continue
        if page_markers:
            parts.append(f"## Page {page_no}\n\n{text}")
        else:
            parts.append(text)
    return "\n\n".join(parts)


def extract_front_matter(doc, max_pages: int) -> str:
    end_page = min(max_pages, page_count(doc))
    return extract_page_range_text(doc, 1, end_page, page_markers=True)


def clear_generated_artifacts(output_dir: Path) -> None:
    if not output_dir.is_dir():
        return
    for path in output_dir.glob(GENERATED_RAW_GLOB):
        path.unlink()
    for name in (GENERATED_MAP_NAME, GENERATED_FRONT_MATTER_NAME):
        path = output_dir / name
        if path.is_file():
            path.unlink()


def format_chapter_markdown(chapter: ChapterSpec, body: str) -> str:
    cleaned = clean_paragraph_flow(body).strip()
    heading = f"# {chapter.title}\n\n"
    if cleaned:
        return heading + cleaned + "\n"
    return heading + "\n"


def write_chapter_dump(
    output_dir: Path, chapter: ChapterSpec, body: str
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / chapter.output_name
    out_path.write_text(format_chapter_markdown(chapter, body), encoding="utf-8")
    return out_path


def chapter_map_entry(chapter: ChapterSpec, dump_path: Path) -> dict:
    return {
        "chapter": chapter.number,
        "title": chapter.title,
        "start_page": chapter.start_page,
        "end_page": chapter.end_page,
        "dump_path": str(dump_path),
    }


def write_chapter_map(
    output_dir: Path,
    source_path: Path,
    chapters: list[ChapterSpec],
    dumps: list[Path],
) -> Path:
    payload = {
        "source": str(source_path),
        "chapters": [
            chapter_map_entry(chapter, dump_path)
            for chapter, dump_path in zip(chapters, dumps)
        ],
    }
    out_path = output_dir / GENERATED_MAP_NAME
    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return out_path


def dump_chapters(
    doc,
    output_dir: Path,
    chapters: list[ChapterSpec],
) -> list[Path]:
    dumps: list[Path] = []
    for chapter in chapters:
        body = extract_page_range_text(
            doc, chapter.start_page, chapter.end_page
        )
        if not body.strip():
            raise SystemExit(
                f"error: no extractable text for chapter {chapter.number} "
                f"(pages {chapter.start_page}-{chapter.end_page}); "
                "source may be image-only or need OCR"
            )
        dumps.append(write_chapter_dump(output_dir, chapter, body))
    return dumps


# Backwards-compatible aliases used in tests.
dump_with_toc = dump_chapters


def resolve_output_dir(
    root: Path, source_path: Path, slug: str | None, output_dir: str | None
) -> tuple[str, Path]:
    source_slug = (
        normalize_slug(slug) if slug else slugify_source_name(source_path.stem)
    )
    if output_dir:
        out = Path(output_dir)
        if not out.is_absolute():
            out = root / out
    else:
        out = (root / "incoming" / source_slug).resolve()
        if root.resolve() not in out.parents and out != root.resolve():
            raise SystemExit("error: resolved output directory escapes repo root")
    return source_slug, out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Dump PDF/EPUB sources into per-chapter plain markdown."
    )
    parser.add_argument(
        "source",
        help="Path to a PDF or EPUB file (relative to repo root or absolute)",
    )
    parser.add_argument(
        "--slug",
        help="Source slug for incoming/<slug>/ (default: derived from filename)",
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory (default: incoming/<slug>/)",
    )
    parser.add_argument(
        "--chapter-map",
        type=Path,
        help="JSON chapter map for sources without an embedded outline",
    )
    parser.add_argument(
        "--front-matter-only",
        action="store_true",
        help="Extract front matter only (no chapter dumps)",
    )
    parser.add_argument(
        "--front-matter-pages",
        type=int,
        default=40,
        help="Pages to include in front-matter extraction (default: 40)",
    )
    args = parser.parse_args()

    root = find_root(Path(__file__).resolve().parent)
    source_path = Path(args.source)
    if not source_path.is_absolute():
        source_path = root / source_path
    source_path = source_path.resolve()
    if not source_path.is_file():
        raise SystemExit(f"error: source file not found: {source_path}")

    source_slug, output_dir = resolve_output_dir(
        root, source_path, args.slug, args.output_dir
    )

    doc = open_document(source_path)
    total_pages = page_count(doc)

    if args.front_matter_only:
        output_dir.mkdir(parents=True, exist_ok=True)
        clear_generated_artifacts(output_dir)
        front_path = output_dir / GENERATED_FRONT_MATTER_NAME
        front_text = extract_front_matter(doc, args.front_matter_pages)
        if not front_text.strip():
            print(
                "warning: front matter has no extractable text "
                "(image-only pages?)",
                file=sys.stderr,
            )
        front_path.write_text(
            clean_paragraph_flow(front_text), encoding="utf-8"
        )
        print(f"source_slug: {source_slug}")
        print(f"pages: {total_pages}")
        print(f"front_matter: {front_path}")
        print("mode: front-matter-only")
        doc.close()
        return

    chapters: list[ChapterSpec]
    mode: str

    if args.chapter_map:
        map_path = resolve_repo_path(root, args.chapter_map)
        chapters = load_chapter_map(map_path, total_pages)
        mode = "chapter-map"
    else:
        toc = doc.get_toc(simple=True)
        chapters = chapters_from_toc(toc, total_pages)
        if chapters:
            mode = "toc"
        else:
            output_dir.mkdir(parents=True, exist_ok=True)
            clear_generated_artifacts(output_dir)
            front_path = output_dir / GENERATED_FRONT_MATTER_NAME
            front_text = extract_front_matter(doc, args.front_matter_pages)
            if not front_text.strip():
                print(
                    "warning: front matter has no extractable text "
                    "(image-only pages?)",
                    file=sys.stderr,
                )
            front_path.write_text(
                clean_paragraph_flow(front_text), encoding="utf-8"
            )
            print(f"source_slug: {source_slug}")
            print(f"pages: {total_pages}")
            print(f"front_matter: {front_path}")
            print("mode: no-outline")
            print(
                "next: provide a chapter map JSON and re-run with "
                "--chapter-map <path>"
            )
            doc.close()
            return

    output_dir.mkdir(parents=True, exist_ok=True)
    clear_generated_artifacts(output_dir)
    dumps = dump_chapters(doc, output_dir, chapters)
    doc.close()
    map_path = write_chapter_map(output_dir, source_path, chapters, dumps)

    print(f"source_slug: {source_slug}")
    print(f"pages: {total_pages}")
    print(f"chapters: {len(chapters)}")
    print(f"mode: {mode}")
    print(f"chapter_map: {map_path}")
    for chapter, dump_path in zip(chapters, dumps):
        try:
            rel = dump_path.relative_to(root)
            shown = str(rel)
        except ValueError:
            shown = str(dump_path)
        print(f"  {chapter.nn} {chapter.title} -> {shown}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
