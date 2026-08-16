"""Tests for scripts/list-bundles-for-paths.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "list-bundles-for-paths.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "list_bundles_for_paths", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["list_bundles_for_paths"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


class TestBundlesForPaths:
    def test_returns_union_sorted_and_deduplicated(self):
        overlap = {
            "a.md": ["philosophy", "mindset"],
            "b.md": ["mindset", "capacity-load"],
        }
        result = mod.bundles_for_paths(["a.md", "b.md"], overlap)
        assert result == ["capacity-load", "mindset", "philosophy"]

    def test_path_with_empty_bundles_contributes_nothing(self):
        overlap = {"a.md": []}
        assert mod.bundles_for_paths(["a.md"], overlap) == []

    def test_unmapped_path_contributes_nothing(self):
        overlap = {"b.md": ["philosophy"]}
        result = mod.bundles_for_paths(["a.md", "b.md"], overlap)
        assert result == ["philosophy"]

    def test_empty_path_list_returns_empty(self):
        assert mod.bundles_for_paths([], {"a.md": ["philosophy"]}) == []


class TestFilterKnownBundles:
    def test_splits_known_and_unknown_by_folder_existence(
        self, tmp_path: Path
    ):
        (tmp_path / "philosophy").mkdir()
        known, unknown = mod.filter_known_bundles(
            ["philosophy", "not-a-real-bundle"], tmp_path
        )
        assert known == ["philosophy"]
        assert unknown == ["not-a-real-bundle"]

    def test_all_known_returns_empty_unknown_list(self, tmp_path: Path):
        (tmp_path / "mindset").mkdir()
        known, unknown = mod.filter_known_bundles(["mindset"], tmp_path)
        assert known == ["mindset"]
        assert unknown == []


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

    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": ["philosophy"]}\n'
            "not valid json\n",
            encoding="utf-8",
        )
        assert mod.load_overlap(overlap) == {"a.md": ["philosophy"]}


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
