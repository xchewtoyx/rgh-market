"""Tests for scripts/list-landscape-unmapped.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "list-landscape-unmapped.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "list_landscape_unmapped", SCRIPT
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["list_landscape_unmapped"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


class TestUnmappedPaths:
    def test_returns_paths_not_in_mapped_set_sorted(self):
        fleeting = {"fleeting/b.md", "fleeting/a.md", "fleeting/c.md"}
        mapped = {"fleeting/b.md"}
        assert mod.unmapped_paths(fleeting, mapped) == [
            "fleeting/a.md",
            "fleeting/c.md",
        ]

    def test_all_mapped_returns_empty(self):
        fleeting = {"fleeting/a.md"}
        mapped = {"fleeting/a.md"}
        assert mod.unmapped_paths(fleeting, mapped) == []

    def test_no_fleeting_paths_returns_empty(self):
        assert mod.unmapped_paths(set(), {"fleeting/a.md"}) == []


class TestLoadMappedPaths:
    def test_missing_file_returns_empty_set(self, tmp_path: Path):
        assert mod.load_mapped_paths(tmp_path / "missing.jsonl") == set()

    def test_reads_path_keys_from_each_line(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "fleeting/a.md", "bundles": ["philosophy"]}\n'
            '{"path": "fleeting/b.md", "bundles": []}\n',
            encoding="utf-8",
        )
        assert mod.load_mapped_paths(overlap) == {
            "fleeting/a.md",
            "fleeting/b.md",
        }

    def test_skips_malformed_json_lines_without_raising(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "fleeting/a.md", "bundles": []}\n'
            "not valid json\n",
            encoding="utf-8",
        )
        assert mod.load_mapped_paths(overlap) == {"fleeting/a.md"}

    def test_skips_entries_missing_path(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"bundles": ["philosophy"]}\n'
            '{"path": "fleeting/a.md", "bundles": []}\n',
            encoding="utf-8",
        )
        assert mod.load_mapped_paths(overlap) == {"fleeting/a.md"}

    def test_blank_lines_are_ignored(self, tmp_path: Path):
        overlap = tmp_path / "overlap.jsonl"
        overlap.write_text(
            '{"path": "fleeting/a.md", "bundles": []}\n\n   \n',
            encoding="utf-8",
        )
        assert mod.load_mapped_paths(overlap) == {"fleeting/a.md"}


class TestLoadFleetingPaths:
    def test_lists_markdown_files_relative_to_root(self, tmp_path: Path):
        root = tmp_path / "repo"
        fleeting = root / "fleeting" / "domain"
        fleeting.mkdir(parents=True)
        (fleeting / "01-note.md").write_text("", encoding="utf-8")
        (fleeting / "not-markdown.txt").write_text("", encoding="utf-8")
        assert mod.load_fleeting_paths(root) == {
            "fleeting/domain/01-note.md"
        }

    def test_top_level_file_directly_under_fleeting_excluded(
        self, tmp_path: Path
    ):
        # fleeting/ is a folder-per-source layout; a stray file at its top
        # level (e.g. a README) is never itself a literature note.
        root = tmp_path / "repo"
        fleeting = root / "fleeting"
        source = fleeting / "domain"
        source.mkdir(parents=True)
        (source / "01-note.md").write_text("", encoding="utf-8")
        (fleeting / "README.md").write_text("", encoding="utf-8")
        assert mod.load_fleeting_paths(root) == {
            "fleeting/domain/01-note.md"
        }

    def test_missing_fleeting_dir_raises(self, tmp_path: Path):
        try:
            mod.load_fleeting_paths(tmp_path)
        except SystemExit as exc:
            assert "fleeting/" in str(exc)
        else:
            raise AssertionError("expected SystemExit")


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
