import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_marketplace  # noqa: E402


def make_entry(name: str, version: str) -> dict:
    return {
        "name": name,
        "version": version,
        "strict": False,
        "source": {
            "source": "archive",
            "url": (
                f"https://dl.cloudsmith.io/public/chewcorp-kl2f/xchewtoyx/raw/"
                f"names/{name}/versions/{version}/{name}-{version}.zip"
            ),
            "sha256": "0" * 64,
        },
    }


def fake_fetch(new_version: str, new_sha256: str):
    def fetch(owner: str, repo: str, name: str):
        assert owner == "chewcorp-kl2f"
        assert repo == "xchewtoyx"
        return {
            "name": name,
            "version": new_version,
            "cdn_url": (
                f"https://dl.cloudsmith.io/public/{owner}/{repo}/raw/"
                f"names/{name}/versions/{new_version}/{name}-{new_version}.zip"
            ),
            "checksum_sha256": new_sha256,
        }

    return fetch


def test_sync_entry_updates_on_new_version():
    entry = make_entry("rgh-sme", "0.1.0")
    changed = sync_marketplace.sync_entry(entry, fake_fetch("0.1.1", "a" * 64))
    assert changed is True
    assert entry["version"] == "0.1.1"
    assert entry["source"]["sha256"] == "a" * 64
    assert entry["source"]["url"].endswith("rgh-sme-0.1.1.zip")


def test_sync_entry_no_change_when_already_current():
    entry = make_entry("rgh-sme", "0.1.1")
    same_sha = "0" * 64
    changed = sync_marketplace.sync_entry(entry, fake_fetch("0.1.1", same_sha))
    assert changed is False


def test_sync_entry_ignores_non_archive_source():
    entry = {
        "name": "other-plugin",
        "source": {"source": "github", "repo": "owner/repo"},
    }
    changed = sync_marketplace.sync_entry(entry, fake_fetch("9.9.9", "f" * 64))
    assert changed is False


def test_sync_entry_leaves_entry_when_package_missing():
    entry = make_entry("rgh-sme", "0.1.0")
    before = json.dumps(entry)
    changed = sync_marketplace.sync_entry(entry, lambda owner, repo, name: None)
    assert changed is False
    assert json.dumps(entry) == before


def test_sync_marketplace_writes_file_only_when_changed(tmp_path):
    path = tmp_path / "marketplace.json"
    data = {"name": "rgh-plugins", "plugins": [make_entry("rgh-sme", "0.1.0")]}
    path.write_text(json.dumps(data), encoding="utf-8")

    changed = sync_marketplace.sync_marketplace(path, fetch=fake_fetch("0.1.1", "b" * 64))

    assert changed is True
    written = json.loads(path.read_text(encoding="utf-8"))
    assert written["plugins"][0]["version"] == "0.1.1"


def test_sync_marketplace_no_write_when_up_to_date(tmp_path):
    path = tmp_path / "marketplace.json"
    entry = make_entry("rgh-sme", "0.1.1")
    data = {"name": "rgh-plugins", "plugins": [entry]}
    path.write_text(json.dumps(data), encoding="utf-8")
    mtime_before = path.stat().st_mtime_ns

    same_sha = entry["source"]["sha256"]
    changed = sync_marketplace.sync_marketplace(path, fetch=fake_fetch("0.1.1", same_sha))

    assert changed is False
    assert path.stat().st_mtime_ns == mtime_before
