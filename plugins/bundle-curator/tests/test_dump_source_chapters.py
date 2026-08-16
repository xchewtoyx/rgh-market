"""Tests for scripts/dump-source-chapters.py."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pymupdf as fitz
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "dump-source-chapters.py"


def load_module():
    spec = importlib.util.spec_from_file_location("dump_source_chapters", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["dump_source_chapters"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


def make_pdf_with_toc(path: Path) -> None:
    doc = fitz.open()
    for i in range(1, 7):
        page = doc.new_page()
        page.insert_text((72, 72), f"Body text for page {i}.")
    doc.set_toc(
        [
            [1, "Front matter", 1],
            [2, "Chapter 1 First Topic", 2],
            [2, "Chapter 2 Second Topic", 4],
            [2, "Chapter 3 Third Topic", 6],
        ]
    )
    doc.save(path)
    doc.close()


def make_pdf_without_toc(path: Path, pages: int = 4) -> None:
    doc = fitz.open()
    for i in range(1, pages + 1):
        page = doc.new_page()
        page.insert_text((72, 72), f"Plain page {i} without outline.")
    doc.save(path)
    doc.close()


class TestCleanParagraphFlow:
    def test_simple_line_joining(self):
        raw = "This is a sentence\nthat was split\nacross lines."
        assert (
            mod.clean_paragraph_flow(raw)
            == "This is a sentence that was split across lines."
        )

    def test_hyphenation_repair(self):
        raw = "This is a distributed sys-\ntem that works."
        assert (
            mod.clean_paragraph_flow(raw)
            == "This is a distributed system that works."
        )

    def test_heading_preservation(self):
        raw = "# Heading\n\nSome paragraph text."
        assert mod.clean_paragraph_flow(raw) == "# Heading\n\nSome paragraph text."

    def test_paragraph_break_preservation(self):
        raw = "First paragraph ended.\n\nSecond paragraph starts with uppercase."
        assert (
            mod.clean_paragraph_flow(raw)
            == "First paragraph ended.\n\nSecond paragraph starts with uppercase."
        )

    def test_list_preservation(self):
        raw = "Here is a list:\n\n- Item 1\n- Item 2"
        assert mod.clean_paragraph_flow(raw) == "Here is a list:\n\n- Item 1\n- Item 2"

    def test_calibre_link_stripping(self):
        raw = "Reference [1](index.html#page_11) and [2](index.html#page_15) here."
        assert mod.clean_paragraph_flow(raw) == "Reference 1 and 2 here."


class TestSlugify:
    def test_unicode_title_gets_distinct_slug(self):
        assert mod.slugify_source_name("数据仓库") != "source"
        assert mod.slugify_source_name("数据仓库") == mod.slugify_source_name("数据仓库")
        assert mod.slugify_source_name("数据仓库") != mod.slugify_source_name("机器学习")


class TestChaptersFromToc:
    def test_parses_chapter_entries(self):
        toc = [
            [1, "Front matter", 1],
            [2, "Chapter 1 First Topic", 2],
            [2, "Chapter 2 Second Topic", 4],
            [2, "Chapter 3 Third Topic", 6],
        ]
        chapters = mod.chapters_from_toc(toc, total_pages=6)
        assert [ch.number for ch in chapters] == [1, 2, 3]
        assert chapters[0].start_page == 2
        assert chapters[0].end_page == 3
        assert chapters[1].start_page == 4
        assert chapters[1].end_page == 5
        assert chapters[2].start_page == 6
        assert chapters[2].end_page == 6


class TestChapterPlanValidation:
    def test_rejects_overlapping_ranges(self):
        chapters = [
            mod.ChapterSpec(1, "Ch 1", 1, 20),
            mod.ChapterSpec(2, "Ch 2", 20, 40),
        ]
        with pytest.raises(SystemExit, match="overlap"):
            mod.validate_chapter_plan(chapters, total_pages=40)

    def test_rejects_duplicate_numbers(self):
        chapters = [
            mod.ChapterSpec(1, "Ch 1", 1, 10),
            mod.ChapterSpec(1, "Ch 1 dup", 11, 20),
        ]
        with pytest.raises(SystemExit, match="duplicate"):
            mod.validate_chapter_plan(chapters, total_pages=20)

    def test_rejects_explicit_overlapping_end_page(self):
        drafts = [
            mod.ChapterSpecDraft(1, "Ch 1", 1, 20),
            mod.ChapterSpecDraft(2, "Ch 2", 20, 40),
        ]
        with pytest.raises(SystemExit, match="overlap"):
            mod.finalize_chapter_plan(drafts, total_pages=40)

    def test_last_chapter_may_omit_end_page(self):
        data = [
            {"chapter": 1, "title": "Ch 1", "start_page": 1, "end_page": 2},
            {"chapter": 2, "title": "Ch 2", "start_page": 3},
        ]
        chapters = mod.chapters_from_map(data, total_pages=5)
        assert chapters[1].end_page == 5


class TestSlugSafety:
    def test_rejects_path_like_slug(self, tmp_path: Path):
        root = tmp_path
        with pytest.raises(SystemExit, match="single directory name"):
            mod.resolve_output_dir(root, root / "book.pdf", "../../escape", None)


class TestTocBackMatter:
    def test_last_chapter_stops_before_appendix(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        doc = fitz.open()
        for i in range(1, 8):
            page = doc.new_page()
            page.insert_text((72, 72), f"Text on page {i}.")
        doc.set_toc(
            [
                [1, "Front matter", 1],
                [2, "Chapter 1 Topic", 2],
                [2, "Chapter 2 Topic", 4],
                [2, "Appendix A", 6],
            ]
        )
        doc.save(pdf)
        doc.close()

        doc = mod.open_document(pdf)
        chapters = mod.chapters_from_toc(doc.get_toc(simple=True), total_pages=7)
        doc.close()

        assert len(chapters) == 2
        assert chapters[1].end_page == 5

    def test_intermediate_chapter_stops_before_part_divider(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        doc = fitz.open()
        for i in range(1, 11):
            page = doc.new_page()
            page.insert_text((72, 72), f"Text on page {i}.")
        doc.set_toc(
            [
                [1, "Front matter", 1],
                [2, "Chapter 1 Topic", 2],
                [2, "Chapter 2 Topic", 4],
                [1, "Part II", 6],
                [2, "Chapter 3 Topic", 8],
            ]
        )
        doc.save(pdf)
        doc.close()

        doc = mod.open_document(pdf)
        chapters = mod.chapters_from_toc(doc.get_toc(simple=True), total_pages=10)
        doc.close()

        assert [ch.number for ch in chapters] == [1, 2, 3]
        assert chapters[1].end_page == 5


class TestChapterMapLoading:
    def test_rejects_empty_map(self):
        with pytest.raises(SystemExit, match="empty"):
            mod.chapters_from_map([], total_pages=10)

    def test_resolves_map_relative_to_repo_root(self, tmp_path: Path):
        root = tmp_path
        (root / "okf-core.toml").write_text("", encoding="utf-8")
        maps = root / "maps"
        maps.mkdir()
        map_file = maps / "map.json"
        map_file.write_text(
            json.dumps(
                [
                    {
                        "chapter": 1,
                        "title": "Only",
                        "start_page": 1,
                        "end_page": 1,
                    }
                ]
            ),
            encoding="utf-8",
        )
        chapters = mod.load_chapter_map(
            mod.resolve_repo_path(root, Path("maps/map.json")), total_pages=1
        )
        assert len(chapters) == 1


class TestDumpIntegration:
    def test_dump_from_embedded_toc(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        out = tmp_path / "out"
        make_pdf_with_toc(pdf)

        doc = mod.open_document(pdf)
        chapters = mod.chapters_from_toc(
            doc.get_toc(simple=True), mod.page_count(doc)
        )
        dumps = mod.dump_chapters(doc, out, chapters)
        doc.close()

        assert len(dumps) == 3
        assert (out / "01-raw.md").is_file()
        first = (out / "01-raw.md").read_text(encoding="utf-8")
        assert first.startswith("# Chapter 1 First Topic")
        assert "Body text for page 2" in first

    def test_dump_from_chapter_map_without_toc(self, tmp_path: Path):
        pdf = tmp_path / "scan.pdf"
        out = tmp_path / "out"
        make_pdf_without_toc(pdf, pages=5)

        chapter_map = tmp_path / "map.json"
        chapter_map.write_text(
            json.dumps(
                [
                    {
                        "chapter": 1,
                        "title": "Chapter 1 Intro",
                        "start_page": 1,
                        "end_page": 2,
                    },
                    {
                        "chapter": 2,
                        "title": "Chapter 2 Body",
                        "start_page": 3,
                        "end_page": 5,
                    },
                ]
            ),
            encoding="utf-8",
        )

        doc = mod.open_document(pdf)
        chapters = mod.load_chapter_map(chapter_map, total_pages=mod.page_count(doc))
        dumps = mod.dump_chapters(doc, out, chapters)
        doc.close()

        assert len(dumps) == 2
        second = (out / "02-raw.md").read_text(encoding="utf-8")
        assert "Plain page 3" in second
        assert "Plain page 5" in second

    def test_chapter_map_round_trip(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        out = tmp_path / "out"
        make_pdf_with_toc(pdf)

        doc = mod.open_document(pdf)
        chapters = mod.chapters_from_toc(
            doc.get_toc(simple=True), mod.page_count(doc)
        )
        dumps = mod.dump_chapters(doc, out, chapters)
        map_path = mod.write_chapter_map(out, pdf, chapters, dumps)
        doc.close()

        reloaded = mod.load_chapter_map(map_path, total_pages=6)
        assert [ch.number for ch in reloaded] == [1, 2, 3]

    def test_front_matter_includes_page_markers(self, tmp_path: Path):
        pdf = tmp_path / "scan.pdf"
        make_pdf_without_toc(pdf, pages=3)

        doc = mod.open_document(pdf)
        front = mod.extract_front_matter(doc, max_pages=2)
        doc.close()

        assert "## Page 1" in front
        assert "## Page 2" in front
        assert "## Page 3" not in front

    def test_clear_generated_artifacts_removes_stale_dumps(self, tmp_path: Path):
        out = tmp_path / "out"
        out.mkdir()
        stale = out / "01-raw.md"
        stale.write_text("stale", encoding="utf-8")
        (out / "chapter-map.json").write_text("{}", encoding="utf-8")

        mod.clear_generated_artifacts(out)

        assert not stale.exists()
        assert not (out / "chapter-map.json").exists()

    def test_empty_chapter_text_fails(self, tmp_path: Path):
        pdf = tmp_path / "blank.pdf"
        doc = fitz.open()
        doc.new_page()
        doc.save(pdf)
        doc.close()

        doc = mod.open_document(pdf)
        chapters = [
            mod.ChapterSpec(1, "Blank", 1, 1),
        ]
        with pytest.raises(SystemExit, match="no extractable text"):
            mod.dump_chapters(doc, tmp_path / "out", chapters)
        doc.close()
