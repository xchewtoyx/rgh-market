"""Tests for scripts/curation-progress.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "curation-progress.py"


def load_module():
    spec = importlib.util.spec_from_file_location("curation_progress", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["curation_progress"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


def entry(path: str, confidence: float, bundle: str = "philosophy") -> dict:
    return {"path": path, "bundle": bundle, "confidence": confidence}


class TestPendingRatingsStats:
    def test_max_and_high_count_for_pending_only(self):
        # Threshold comparison is >= here (matching the selectors' "at or
        # above" gating), so the boundary value 0.7 counts as high too --
        # unlike select-focused-candidates.py's walk-stop, this is a
        # preview count, not a gate, so it should agree with what a
        # selector run would actually pick up.
        pending = {"a.md", "b.md", "c.md", "unscored.md"}
        entries = [
            entry("a.md", 0.95),
            entry("b.md", 0.69),
            entry("c.md", 0.7),
            entry("curated.md", 0.99),
        ]
        max_confidence, high_count = mod.pending_ratings_stats(entries, pending)
        assert max_confidence == 0.95
        assert high_count == 2

    def test_duplicate_paths_keep_highest_confidence(self):
        pending = {"a.md"}
        entries = [entry("a.md", 0.6), entry("a.md", 0.85), entry("a.md", 0.75)]
        max_confidence, high_count = mod.pending_ratings_stats(entries, pending)
        assert max_confidence == 0.85
        assert high_count == 1

    def test_empty_ratings_returns_dash_values(self):
        max_confidence, high_count = mod.pending_ratings_stats([], {"a.md"})
        assert max_confidence is None
        assert high_count == 0

    def test_ignores_invalid_confidence(self):
        pending = {"a.md", "b.md"}
        entries = [
            {"path": "a.md", "bundle": "philosophy", "confidence": "high"},
            entry("b.md", 0.8),
        ]
        max_confidence, high_count = mod.pending_ratings_stats(entries, pending)
        assert max_confidence == 0.8
        assert high_count == 1

    def test_below_threshold_not_counted_as_high(self):
        pending = {"a.md"}
        entries = [entry("a.md", 0.69)]
        max_confidence, high_count = mod.pending_ratings_stats(entries, pending)
        assert max_confidence == 0.69
        assert high_count == 0
