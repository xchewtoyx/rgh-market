"""Tests for scripts/select-watch-candidates.py."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "select-watch-candidates.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "select_watch_candidates", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["select_watch_candidates"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


def obs(title, core, fit=0.9, authors="X et al.", year=2023):
    return {
        "title": title,
        "authors": authors,
        "year": year,
        "bundle": "agentic-engineering",
        "citing_core": core,
        "citing_path": f"fleeting/{core}/01.md",
        "charter_fit": fit,
        "arxiv_id": None,
        "notes": "test",
    }


class TestSelectWatchCandidates(unittest.TestCase):
    def test_requires_min_cores(self):
        entries = [
            obs("Voyager Embodied Agent", "ai-engineering"),
            obs("Voyager Embodied Agent", "ai-engineering"),
        ]
        result = mod.select_candidates(
            entries,
            onboarded=set(),
            min_cores=2,
            min_charter_fit=0.7,
            limit=10,
        )
        self.assertEqual(result, [])

    def test_two_cores_survive(self):
        entries = [
            obs("Voyager: One", "ai-engineering", 0.9),
            obs("Voyager: Two", "memgpt-packer", 0.85),
        ]
        result = mod.select_candidates(
            entries,
            onboarded=set(),
            min_cores=2,
            min_charter_fit=0.7,
            limit=10,
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["core_count"], 2)
        self.assertEqual(
            set(result[0]["citing_cores"]),
            {"ai-engineering", "memgpt-packer"},
        )

    def test_onboarded_titles_dropped(self):
        entries = [
            obs("ReAct Synergizing Reasoning", "ai-engineering"),
            obs("ReAct Synergizing Reasoning", "memgpt-packer"),
        ]
        onboarded = {mod.normalize("ReAct Synergizing Reasoning")}
        result = mod.select_candidates(
            entries,
            onboarded=onboarded,
            min_cores=2,
            min_charter_fit=0.7,
            limit=10,
        )
        self.assertEqual(result, [])

    def test_charter_fit_threshold(self):
        entries = [
            obs("Some Paper", "ai-engineering", 0.5),
            obs("Some Paper", "react-yao", 0.4),
        ]
        result = mod.select_candidates(
            entries,
            onboarded=set(),
            min_cores=2,
            min_charter_fit=0.7,
            limit=10,
        )
        self.assertEqual(result, [])

    def test_sort_by_cores_then_fit(self):
        entries = [
            obs("Alpha Paper", "a", 0.95),
            obs("Alpha Paper", "b", 0.9),
            obs("Beta Paper", "a", 0.99),
            obs("Beta Paper", "b", 0.99),
            obs("Beta Paper", "c", 0.99),
        ]
        result = mod.select_candidates(
            entries,
            onboarded=set(),
            min_cores=2,
            min_charter_fit=0.7,
            limit=10,
        )
        self.assertEqual(
            [r["title"] for r in result], ["Beta Paper", "Alpha Paper"]
        )


if __name__ == "__main__":
    unittest.main()
