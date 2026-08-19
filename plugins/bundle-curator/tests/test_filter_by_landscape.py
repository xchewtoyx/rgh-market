"""Tests for scripts/filter-by-landscape.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "filter-by-landscape.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "filter_by_landscape", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["filter_by_landscape"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


class TestFilterCandidates:
    def test_keeps_paths_whose_entry_lists_the_domain(self):
        overlap = {"a.md": ["philosophy", "mindset"]}
        result = mod.filter_candidates(["a.md"], overlap, "philosophy")
        assert result == ["a.md"]

    def test_drops_paths_whose_entry_excludes_the_domain(self):
        overlap = {"a.md": ["mindset"]}
        result = mod.filter_candidates(["a.md"], overlap, "philosophy")
        assert result == []

    def test_drops_paths_with_an_empty_bundles_list(self):
        overlap = {"a.md": []}
        result = mod.filter_candidates(["a.md"], overlap, "philosophy")
        assert result == []

    def test_fails_open_for_paths_with_no_cache_entry(self):
        overlap = {"b.md": ["philosophy"]}
        result = mod.filter_candidates(
            ["a.md", "b.md"], overlap, "philosophy"
        )
        assert result == ["a.md", "b.md"]

    def test_preserves_input_order(self):
        overlap = {
            "a.md": ["philosophy"],
            "c.md": ["philosophy"],
        }
        result = mod.filter_candidates(
            ["a.md", "b.md", "c.md"], overlap, "philosophy"
        )
        assert result == ["a.md", "b.md", "c.md"]


class TestLoadOverlap:
    def test_missing_file_returns_empty_dict(self, tmp_path: Path):
        assert mod.load_overlap(tmp_path / "missing.jsonl") == {}

    def test_reads_path_and_bundles(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": ["philosophy", "mindset"]}\n',
            encoding="utf-8",
        )
        assert mod.load_overlap(overlap) == {
            "a.md": ["philosophy", "mindset"]
        }

    def test_empty_bundles_list_is_recorded_as_mapped(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text('{"path": "a.md", "bundles": []}\n', encoding="utf-8")
        assert mod.load_overlap(overlap) == {"a.md": []}

    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": ["philosophy"]}\n'
            "not valid json\n",
            encoding="utf-8",
        )
        assert mod.load_overlap(overlap) == {"a.md": ["philosophy"]}

    def test_missing_bundles_key_is_not_recorded_as_mapped(
        self, tmp_path: Path
    ):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text('{"path": "a.md"}\n', encoding="utf-8")
        assert mod.load_overlap(overlap) == {}

    def test_non_list_bundles_is_not_recorded_as_mapped(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": "philosophy"}\n',
            encoding="utf-8",
        )
        assert mod.load_overlap(overlap) == {}

    def test_non_string_bundle_entries_are_dropped(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": ["philosophy", 3, null]}\n',
            encoding="utf-8",
        )
        assert mod.load_overlap(overlap) == {"a.md": ["philosophy"]}

    def test_later_line_overrides_earlier_for_same_path(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": ["philosophy"]}\n'
            '{"path": "a.md", "bundles": ["mindset"]}\n',
            encoding="utf-8",
        )
        assert mod.load_overlap(overlap) == {"a.md": ["mindset"]}

    def test_blank_lines_are_ignored(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": []}\n\n   \n', encoding="utf-8"
        )
        assert mod.load_overlap(overlap) == {"a.md": []}


class TestReadCandidatePaths:
    def test_strips_and_drops_blank_lines(self):
        stream = iter(["a.md\n", "\n", "  \n", "b.md\n"])
        assert mod.read_candidate_paths(stream) == ["a.md", "b.md"]


class TestFindRoot:
    def test_resolves_repo_root_containing_okf_core_toml(self, tmp_path: Path):
        root = tmp_path / "repo"
        nested = root / "scripts"
        nested.mkdir(parents=True)
        (root / "okf-core.toml").write_text("", encoding="utf-8")
        assert mod.find_root(nested) == root

    def test_missing_okf_core_toml_raises(self, tmp_path: Path):
        try:
            mod.find_root(tmp_path)
        except SystemExit as exc:
            assert "okf-core.toml" in str(exc)
        else:
            raise AssertionError("expected SystemExit")
