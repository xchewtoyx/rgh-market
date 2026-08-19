"""Tests for scripts/select-score-catchup-candidates.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "select-score-catchup-candidates.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "select_score_catchup_candidates", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["select_score_catchup_candidates"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


class TestBundleCandidates:
    def test_requires_unreviewed_and_landscape_tagged(self):
        unreviewed = {"a.md", "b.md", "c.md"}
        landscape_paths = {"a.md", "b.md"}
        rated_paths: set[str] = set()
        # only a.md and b.md are unreviewed AND landscape-tagged
        result = mod.bundle_candidates(unreviewed, landscape_paths, rated_paths)
        assert result == ["a.md", "b.md"]

    def test_already_rated_excluded_regardless_of_confidence(self):
        unreviewed = {"a.md", "b.md"}
        landscape_paths = {"a.md", "b.md"}
        rated_paths = {"a.md"}  # already scored, at any confidence
        result = mod.bundle_candidates(unreviewed, landscape_paths, rated_paths)
        assert result == ["b.md"]

    def test_reviewed_path_excluded_even_if_landscape_tagged(self):
        unreviewed = {"b.md"}  # a.md already reviewed, absent here
        landscape_paths = {"a.md", "b.md"}
        rated_paths: set[str] = set()
        result = mod.bundle_candidates(unreviewed, landscape_paths, rated_paths)
        assert result == ["b.md"]

    def test_no_landscape_entry_excludes(self):
        unreviewed = {"a.md"}
        landscape_paths: set[str] = set()
        rated_paths: set[str] = set()
        assert mod.bundle_candidates(unreviewed, landscape_paths, rated_paths) == []

    def test_sorted_alphabetically(self):
        unreviewed = {"z.md", "a.md", "m.md"}
        landscape_paths = {"z.md", "a.md", "m.md"}
        result = mod.bundle_candidates(unreviewed, landscape_paths, set())
        assert result == ["a.md", "m.md", "z.md"]

    def test_empty_intersection_returns_empty(self):
        assert mod.bundle_candidates(set(), set(), set()) == []


class TestLoadRatedPaths:
    def test_missing_file_returns_empty_set(self, tmp_path: Path):
        assert mod.load_rated_paths(tmp_path / "missing.jsonl") == set()

    def test_reads_paths_regardless_of_confidence(self, tmp_path: Path):
        ratings = tmp_path / "philosophy.jsonl"
        ratings.write_text(
            '{"path": "a.md", "bundle": "philosophy", "confidence": 0.1}\n'
            '{"path": "b.md", "bundle": "philosophy", "confidence": 0.95}\n',
            encoding="utf-8",
        )
        assert mod.load_rated_paths(ratings) == {"a.md", "b.md"}

    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        ratings = tmp_path / "philosophy.jsonl"
        ratings.write_text(
            '{"path": "a.md", "bundle": "philosophy", "confidence": 0.5}\n'
            "not valid json\n",
            encoding="utf-8",
        )
        assert mod.load_rated_paths(ratings) == {"a.md"}

    def test_missing_path_skipped(self, tmp_path: Path):
        ratings = tmp_path / "philosophy.jsonl"
        ratings.write_text(
            '{"bundle": "philosophy", "confidence": 0.9}\n', encoding="utf-8"
        )
        assert mod.load_rated_paths(ratings) == set()


class TestLandscapePathsForBundle:
    def test_returns_paths_with_bundle_in_list(self):
        overlap = {
            "a.md": ["philosophy", "mindset"],
            "b.md": ["mindset"],
            "c.md": [],
        }
        assert mod.landscape_paths_for_bundle(overlap, "philosophy") == {"a.md"}

    def test_no_matches_returns_empty(self):
        overlap = {"a.md": ["mindset"]}
        assert mod.landscape_paths_for_bundle(overlap, "philosophy") == set()


class TestBundlePriorityKey:
    def test_more_candidates_sorts_first(self):
        results = [
            {"bundle": "a", "count": 2},
            {"bundle": "b", "count": 5},
        ]
        results.sort(key=mod.bundle_priority_key)
        assert [r["bundle"] for r in results] == ["b", "a"]

    def test_tie_on_count_breaks_by_slug(self):
        results = [
            {"bundle": "zebra", "count": 3},
            {"bundle": "alpha", "count": 3},
        ]
        results.sort(key=mod.bundle_priority_key)
        assert [r["bundle"] for r in results] == ["alpha", "zebra"]


class TestSelectReadyBundles:
    def test_end_to_end_two_bundles(self, tmp_path: Path):
        root = tmp_path
        fleeting = root / "fleeting" / "src"
        fleeting.mkdir(parents=True)
        (fleeting / "01-a.md").write_text("", encoding="utf-8")
        (fleeting / "02-b.md").write_text("", encoding="utf-8")
        (fleeting / "03-c.md").write_text("", encoding="utf-8")
        (fleeting / "04-d.md").write_text("", encoding="utf-8")

        (root / "curation").mkdir()
        (root / "curation" / "philosophy.txt").write_text(
            "fleeting/src/04-d.md\n", encoding="utf-8"
        )

        (root / "landscape").mkdir()
        (root / "landscape" / "overlap.jsonl").write_text(
            '{"path": "fleeting/src/01-a.md", "bundles": ["philosophy"]}\n'
            '{"path": "fleeting/src/02-b.md", "bundles": ["mindset"]}\n'
            '{"path": "fleeting/src/03-c.md", "bundles": ["mindset"]}\n',
            encoding="utf-8",
        )

        (root / "ratings").mkdir()
        (root / "ratings" / "philosophy.jsonl").write_text(
            '{"path": "fleeting/src/01-a.md", "bundle": "philosophy", '
            '"confidence": 0.4}\n',
            encoding="utf-8",
        )
        # mindset has no ratings file at all yet -- both notes unscored

        results = mod.select_ready_bundles(
            root, ["philosophy", "mindset", "telemetry-state"]
        )
        # philosophy's only landscape-tagged note is already rated -> not ready
        assert [r["bundle"] for r in results] == ["mindset"]
        assert results[0]["candidates"] == [
            "fleeting/src/02-b.md",
            "fleeting/src/03-c.md",
        ]
        assert results[0]["count"] == 2

    def test_no_ready_bundles_returns_empty_list(self, tmp_path: Path):
        root = tmp_path
        (root / "fleeting").mkdir()
        assert mod.select_ready_bundles(root, ["philosophy"]) == []


class TestLoadLandscapeOverlap:
    def test_missing_file_returns_empty_dict(self, tmp_path: Path):
        assert mod.load_landscape_overlap(tmp_path / "missing.jsonl") == {}

    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "a.md", "bundles": ["philosophy"]}\n' "not valid json\n",
            encoding="utf-8",
        )
        assert mod.load_landscape_overlap(overlap) == {"a.md": ["philosophy"]}


class TestLoadLedgerPaths:
    def test_ignores_comments_and_blank_lines(self, tmp_path: Path):
        ledger = tmp_path / "domain.txt"
        ledger.write_text(
            "# comment\n\nfleeting/a.md\nfleeting/b.md\n", encoding="utf-8"
        )
        assert mod.load_ledger_paths(ledger) == {"fleeting/a.md", "fleeting/b.md"}

    def test_missing_ledger_returns_empty_set(self, tmp_path: Path):
        assert mod.load_ledger_paths(tmp_path / "missing.txt") == set()


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
