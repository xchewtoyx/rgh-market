"""Tests for scripts/select-catchup-candidates.py."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "select-catchup-candidates.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "select_catchup_candidates", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["select_catchup_candidates"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


def rating(path, confidence, bundle="philosophy"):
    return {"path": path, "bundle": bundle, "confidence": confidence}


class TestBundleCandidates:
    def test_requires_all_three_sets(self):
        unreviewed = {"a.md", "b.md", "c.md"}
        landscape_paths = {"a.md", "b.md"}
        rated = {"a.md": 0.9, "c.md": 0.95}
        # only a.md is in all three sets
        result = mod.bundle_candidates(unreviewed, landscape_paths, rated)
        assert result == [("a.md", 0.9)]

    def test_sorted_descending_by_confidence(self):
        unreviewed = {"a.md", "b.md"}
        landscape_paths = {"a.md", "b.md"}
        rated = {"a.md": 0.7, "b.md": 0.95}
        result = mod.bundle_candidates(unreviewed, landscape_paths, rated)
        assert result == [("b.md", 0.95), ("a.md", 0.7)]

    def test_reviewed_path_excluded_even_if_landscape_and_rated(self):
        # simulate: "a.md" already reviewed, so absent from unreviewed
        unreviewed = {"b.md"}
        landscape_paths = {"a.md", "b.md"}
        rated = {"a.md": 0.9, "b.md": 0.9}
        result = mod.bundle_candidates(unreviewed, landscape_paths, rated)
        assert result == [("b.md", 0.9)]

    def test_no_landscape_entry_excludes_even_if_rated(self):
        unreviewed = {"a.md"}
        landscape_paths: set[str] = set()
        rated = {"a.md": 0.9}
        assert mod.bundle_candidates(unreviewed, landscape_paths, rated) == []

    def test_empty_intersection_returns_empty(self):
        assert mod.bundle_candidates(set(), set(), {}) == []


class TestRatedAtOrAbove:
    def test_filters_below_threshold(self):
        entries = [rating("a.md", 0.9), rating("b.md", 0.5)]
        assert mod.rated_at_or_above(entries, 0.7) == {"a.md": 0.9}

    def test_boundary_value_included(self):
        entries = [rating("a.md", 0.7)]
        assert mod.rated_at_or_above(entries, 0.7) == {"a.md": 0.7}

    def test_duplicate_path_keeps_highest_confidence(self):
        entries = [rating("a.md", 0.7), rating("a.md", 0.95), rating("a.md", 0.8)]
        assert mod.rated_at_or_above(entries, 0.7) == {"a.md": 0.95}

    def test_ignores_malformed_confidence(self):
        entries = [
            {"path": "a.md", "bundle": "philosophy", "confidence": "high"},
            rating("b.md", 0.8),
        ]
        assert mod.rated_at_or_above(entries, 0.7) == {"b.md": 0.8}

    def test_missing_path_skipped(self):
        entries = [{"bundle": "philosophy", "confidence": 0.9}]
        assert mod.rated_at_or_above(entries, 0.7) == {}


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
    def test_higher_max_confidence_sorts_first(self):
        results = [
            {"bundle": "a", "count": 1, "max_confidence": 0.7},
            {"bundle": "b", "count": 1, "max_confidence": 0.9},
        ]
        results.sort(key=mod.bundle_priority_key)
        assert [r["bundle"] for r in results] == ["b", "a"]

    def test_tie_on_confidence_breaks_by_count(self):
        results = [
            {"bundle": "a", "count": 1, "max_confidence": 0.9},
            {"bundle": "b", "count": 5, "max_confidence": 0.9},
        ]
        results.sort(key=mod.bundle_priority_key)
        assert [r["bundle"] for r in results] == ["b", "a"]

    def test_tie_on_confidence_and_count_breaks_by_slug(self):
        results = [
            {"bundle": "zebra", "count": 1, "max_confidence": 0.9},
            {"bundle": "alpha", "count": 1, "max_confidence": 0.9},
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

        (root / "curation").mkdir()
        (root / "curation" / "philosophy.txt").write_text(
            "fleeting/src/03-c.md\n", encoding="utf-8"
        )

        (root / "landscape").mkdir()
        (root / "landscape" / "overlap.jsonl").write_text(
            '{"path": "fleeting/src/01-a.md", "bundles": ["philosophy"]}\n'
            '{"path": "fleeting/src/02-b.md", "bundles": ["mindset"]}\n',
            encoding="utf-8",
        )

        (root / "ratings").mkdir()
        (root / "ratings" / "philosophy.jsonl").write_text(
            '{"path": "fleeting/src/01-a.md", "bundle": "philosophy", '
            '"confidence": 0.9}\n',
            encoding="utf-8",
        )
        (root / "ratings" / "mindset.jsonl").write_text(
            '{"path": "fleeting/src/02-b.md", "bundle": "mindset", '
            '"confidence": 0.85}\n',
            encoding="utf-8",
        )

        results = mod.select_ready_bundles(
            root, ["philosophy", "mindset", "telemetry-state"], 0.7
        )
        # philosophy's max_confidence (0.9) outranks mindset's (0.85)
        assert [r["bundle"] for r in results] == ["philosophy", "mindset"]
        assert results[0]["candidates"] == ["fleeting/src/01-a.md"]
        assert results[0]["max_confidence"] == 0.9
        assert results[1]["candidates"] == ["fleeting/src/02-b.md"]

    def test_no_ready_bundles_returns_empty_list(self, tmp_path: Path):
        root = tmp_path
        (root / "fleeting").mkdir()
        assert mod.select_ready_bundles(root, ["philosophy"], 0.7) == []


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

    def test_missing_bundles_key_not_recorded(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text('{"path": "a.md"}\n', encoding="utf-8")
        assert mod.load_landscape_overlap(overlap) == {}


class TestLoadRatings:
    def test_missing_file_returns_empty_list(self, tmp_path: Path):
        assert mod.load_ratings(tmp_path / "missing.jsonl") == []

    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        ratings = tmp_path / "philosophy.jsonl"
        ratings.write_text(
            '{"path": "a.md", "bundle": "philosophy", "confidence": 0.9}\n'
            "not valid json\n",
            encoding="utf-8",
        )
        assert len(mod.load_ratings(ratings)) == 2


class TestLoadLedgerPaths:
    def test_ignores_comments_and_blank_lines(self, tmp_path: Path):
        ledger = tmp_path / "domain.txt"
        ledger.write_text(
            "# comment\n\nfleeting/a.md\nfleeting/b.md\n", encoding="utf-8"
        )
        assert mod.load_ledger_paths(ledger) == {"fleeting/a.md", "fleeting/b.md"}

    def test_missing_ledger_returns_empty_set(self, tmp_path: Path):
        assert mod.load_ledger_paths(tmp_path / "missing.txt") == set()


class TestMinConfidenceType:
    def test_accepts_value_within_range(self):
        assert mod.min_confidence_type("0.8") == 0.8

    def test_rejects_nan(self):
        with pytest.raises(argparse.ArgumentTypeError):
            mod.min_confidence_type("nan")

    def test_rejects_value_above_one(self):
        with pytest.raises(argparse.ArgumentTypeError):
            mod.min_confidence_type("1.5")


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
