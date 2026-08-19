"""Tests for scripts/select-focused-candidates.py."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "select-focused-candidates.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "select_focused_candidates", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["select_focused_candidates"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


def entry(path, confidence, bundle="philosophy"):
    return {"path": path, "bundle": bundle, "confidence": confidence}


class TestSelectCandidatesSortAndThreshold:
    def test_descending_sort_and_threshold_walk_stop(self):
        entries = [
            entry("a.md", 0.65),
            entry("b.md", 0.9),
            entry("c.md", 0.75),
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["b.md", "c.md"]

    def test_all_below_threshold_returns_empty(self):
        entries = [entry("a.md", 0.5), entry("b.md", 0.6)]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == []

    def test_all_at_or_above_threshold_returns_all_sorted(self):
        entries = [entry("a.md", 0.7), entry("b.md", 0.95), entry("c.md", 0.8)]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["b.md", "c.md", "a.md"]


class TestAlreadyCuratedFiltering:
    def test_already_curated_paths_filtered_out(self):
        entries = [entry("a.md", 0.95), entry("b.md", 0.9)]
        result = mod.select_candidates(
            entries, curated_paths={"a.md"}, min_confidence=0.7
        )
        assert result == ["b.md"]

    def test_curated_high_confidence_path_does_not_shift_threshold_walk(self):
        # If the curated filter ran after the threshold walk instead of
        # before, a curated high-confidence entry could still influence
        # ordering. Filtering first means only b/c/d are ever considered.
        entries = [
            entry("curated.md", 0.99),
            entry("b.md", 0.9),
            entry("c.md", 0.75),
            entry("d.md", 0.65),
        ]
        result = mod.select_candidates(
            entries, curated_paths={"curated.md"}, min_confidence=0.7
        )
        assert result == ["b.md", "c.md"]


class TestShortCircuit:
    def test_short_circuits_on_first_sub_threshold_value(self):
        entries = [
            entry("high.md", 0.9),
            entry("mid.md", 0.75),
            entry("boundary.md", 0.65),  # first sub-threshold entry
            entry("very-low.md", 0.1),
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["high.md", "mid.md"]

    def test_malformed_entries_after_cutoff_do_not_break_run(self):
        # Two malformed entries (non-numeric confidence with no path; a
        # bare confidence with no path or bundle at all) sit below the
        # first sub-threshold entry once sorted. If the walk scanned past
        # the cutoff and tried to use their data, this would raise
        # (TypeError comparing str/float, or a KeyError on 'path'). It
        # must not: the break happens at "boundary.md" and the malformed
        # entries are never inspected beyond their (-inf) sort key.
        entries = [
            entry("high.md", 0.9),
            entry("boundary.md", 0.65),  # first sub-threshold (T=0.7)
            {"bundle": "philosophy", "confidence": "not-a-number"},
            {"confidence": 0.05},
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["high.md"]

    def test_non_numeric_confidence_sorts_last_without_crashing(self):
        entries = [
            entry("high.md", 0.9),
            {"path": "bad.md", "bundle": "philosophy", "confidence": "oops"},
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.0
        )
        assert result == ["high.md"]

    def test_entry_missing_path_above_threshold_is_skipped_not_crashed(self):
        entries = [
            entry("high.md", 0.9),
            {"bundle": "philosophy", "confidence": 0.85},  # no path field
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["high.md"]


class TestSortKey:
    def test_missing_confidence_is_negative_infinity(self):
        assert mod.sort_key({}) == float("-inf")

    def test_bool_confidence_is_not_treated_as_numeric(self):
        # bool is a subclass of int in Python; guard against True/False
        # silently sorting as 1.0/0.0 confidence.
        assert mod.sort_key({"confidence": True}) == float("-inf")

    def test_nan_confidence_sorts_as_negative_infinity(self):
        # float('nan') passes isinstance(value, (int, float)), so without an
        # explicit finiteness check it would sort as NaN, not -inf.
        assert mod.sort_key({"confidence": float("nan")}) == float("-inf")

    def test_inf_confidence_sorts_as_negative_infinity(self):
        # +inf is numeric and would otherwise sort/select as the highest
        # possible confidence (`inf < x` is correctly False, so unlike NaN
        # it has no comparison-bypass bug) -- but a confidence outside a
        # sane range is not a real score, so `math.isfinite` excludes it the
        # same as any other unusable value.
        assert mod.sort_key({"confidence": float("inf")}) == float("-inf")


class TestNonFiniteConfidenceGate:
    def test_nan_confidence_entry_is_dropped_not_selected(self):
        # nan < min_confidence is always False (NaN never compares true
        # either way), so a NaN-confidence entry must not slip past the
        # threshold walk the way it would if sort_key returned NaN as-is.
        entries = [
            entry("high1.md", 0.95),
            entry("nan.md", float("nan")),
            entry("high2.md", 0.9),
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["high1.md", "high2.md"]
        assert "nan.md" not in result

    def test_inf_confidence_entry_is_dropped_not_selected(self):
        # Pre-fix, a literal +inf confidence sorted to the top and was
        # selected as the single highest-confidence candidate. Post-fix it
        # must fall back to -inf and be dropped, same as NaN -- not merely
        # excluded from the result count, but genuinely absent while the
        # next-highest legitimate entry still gets selected in its place.
        entries = [
            entry("high1.md", 0.95),
            entry("inf.md", float("inf")),
            entry("high2.md", 0.9),
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["high1.md", "high2.md"]
        assert "inf.md" not in result


class TestDuplicatePathDedup:
    def test_duplicate_path_deduped_keeping_highest_confidence_occurrence(self):
        entries = [
            entry("dup.md", 0.99),
            entry("other.md", 0.9),
            entry("dup.md", 0.85),
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["dup.md", "other.md"]
        assert result.count("dup.md") == 1

    def test_dedup_keeps_sorted_first_occurrence_not_original_list_order(self):
        # The lower-confidence "dup.md" entry appears first in `entries`,
        # but the walk runs over the sorted-descending order, so the 0.95
        # occurrence is inspected (and kept) before the 0.8 one. This
        # confirms dedup is applied during the walk over sorted entries,
        # not by naively keeping whichever occurrence came first in the
        # input list.
        entries = [
            entry("dup.md", 0.8),
            entry("dup.md", 0.95),
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["dup.md"]

    def test_duplicate_above_threshold_does_not_break_the_walk(self):
        # A naive fix that `break`s (instead of `continue`s) on a
        # duplicate would silently truncate the walk right there, dropping
        # legitimate later candidates like "other.md" -- and would also
        # never reach "boundary.md" to prove the short-circuit still
        # works. Duplicates must be skipped without disturbing the walk.
        entries = [
            entry("dup.md", 0.95),
            entry("dup.md", 0.9),
            entry("other.md", 0.8),
            entry("boundary.md", 0.65),  # first sub-threshold entry (T=0.7)
        ]
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["dup.md", "other.md"]


class TestMinConfidenceType:
    def test_accepts_value_within_range(self):
        assert mod.min_confidence_type("0.8") == 0.8

    def test_accepts_boundary_values(self):
        assert mod.min_confidence_type("0") == 0.0
        assert mod.min_confidence_type("1") == 1.0

    def test_rejects_nan(self):
        # The exact footgun this guards against: plain `type=float` on
        # argparse accepts "nan", and `confidence < nan` is always False,
        # so the threshold walk in `select_candidates` would never see a
        # sub-threshold entry and never stop -- possibly selecting
        # unintended entries. Must be rejected at parse time instead.
        with pytest.raises(argparse.ArgumentTypeError, match="finite"):
            mod.min_confidence_type("nan")

    def test_rejects_infinity(self):
        with pytest.raises(argparse.ArgumentTypeError, match="finite"):
            mod.min_confidence_type("inf")

    def test_rejects_value_above_one(self):
        with pytest.raises(argparse.ArgumentTypeError, match=r"\[0, 1\]"):
            mod.min_confidence_type("1.5")

    def test_rejects_negative_value(self):
        with pytest.raises(argparse.ArgumentTypeError, match=r"\[0, 1\]"):
            mod.min_confidence_type("-0.1")

    def test_rejects_non_numeric_string(self):
        with pytest.raises(
            argparse.ArgumentTypeError, match="invalid float"
        ):
            mod.min_confidence_type("not-a-number")


class TestLoadRatings:
    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        ratings = tmp_path / "philosophy.jsonl"
        ratings.write_text(
            '{"path": "a.md", "bundle": "philosophy", "confidence": 0.9}\n'
            "not valid json\n",
            encoding="utf-8",
        )
        entries = mod.load_ratings(ratings)
        assert len(entries) == 2
        result = mod.select_candidates(
            entries, curated_paths=set(), min_confidence=0.7
        )
        assert result == ["a.md"]

    def test_missing_file_returns_empty_list(self, tmp_path: Path):
        assert mod.load_ratings(tmp_path / "missing.jsonl") == []

    def test_blank_lines_are_ignored(self, tmp_path: Path):
        ratings = tmp_path / "philosophy.jsonl"
        ratings.write_text(
            '{"path": "a.md", "bundle": "philosophy", "confidence": 0.9}\n'
            "\n"
            "   \n",
            encoding="utf-8",
        )
        assert len(mod.load_ratings(ratings)) == 1


class TestLoadLedgerPaths:
    def test_ignores_comments_and_blank_lines(self, tmp_path: Path):
        ledger = tmp_path / "domain.txt"
        ledger.write_text(
            "# comment\n\nfleeting/a.md\nfleeting/b.md\n", encoding="utf-8"
        )
        assert mod.load_ledger_paths(ledger) == {
            "fleeting/a.md",
            "fleeting/b.md",
        }

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
