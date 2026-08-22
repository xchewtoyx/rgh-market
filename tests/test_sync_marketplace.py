import hashlib
import io
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_marketplace  # noqa: E402


def make_zip_bytes(files: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, content in files.items():
            zf.writestr(name, content)
    return buf.getvalue()


def make_stamp(tmp_path: Path, name: str, version: str, sha256: str) -> Path:
    plugin_dir = tmp_path / "plugins" / name
    plugin_dir.mkdir(parents=True)
    stamp = {
        "owner": "chewcorp-kl2f",
        "repo": "xchewtoyx",
        "name": name,
        "version": version,
        "sha256": sha256,
    }
    (plugin_dir / sync_marketplace.STAMP_FILENAME).write_text(json.dumps(stamp), encoding="utf-8")
    return plugin_dir


def fake_fetch(new_version: str, new_sha256: str, new_url: str = "https://dl.cloudsmith.io/x.zip"):
    def fetch(owner: str, repo: str, name: str):
        assert owner == "chewcorp-kl2f"
        assert repo == "xchewtoyx"
        return {"name": name, "version": new_version, "checksum_sha256": new_sha256, "cdn_url": new_url}

    return fetch


def test_sync_plugin_dir_extracts_new_version(tmp_path):
    zip_bytes = make_zip_bytes({"plugin.json": "{}", "skills/foo-wiki/SKILL.md": "hi"})
    sha256 = hashlib.sha256(zip_bytes).hexdigest()
    plugin_dir = make_stamp(tmp_path, "rgh-sme", "0.1.0", "0" * 64)

    new_version = sync_marketplace.sync_plugin_dir(
        plugin_dir, fake_fetch("0.1.1", sha256), lambda url: zip_bytes
    )

    assert new_version == "0.1.1"
    assert (plugin_dir / "plugin.json").read_text() == "{}"
    assert (plugin_dir / "skills" / "foo-wiki" / "SKILL.md").read_text() == "hi"
    stamp = json.loads((plugin_dir / sync_marketplace.STAMP_FILENAME).read_text())
    assert stamp["version"] == "0.1.1"
    assert stamp["sha256"] == sha256
    assert "synced_at" in stamp


def test_sync_plugin_dir_no_change_when_sha_matches(tmp_path):
    sha256 = "a" * 64
    plugin_dir = make_stamp(tmp_path, "rgh-sme", "0.1.1", sha256)

    calls = []
    new_version = sync_marketplace.sync_plugin_dir(
        plugin_dir, fake_fetch("0.1.1", sha256), lambda url: calls.append(url) or b""
    )

    assert new_version is None
    assert calls == []  # never downloaded -- sha256 already matched


def test_sync_plugin_dir_rejects_checksum_mismatch(tmp_path):
    plugin_dir = make_stamp(tmp_path, "rgh-sme", "0.1.0", "0" * 64)
    (plugin_dir / "keepme.txt").write_text("still here")

    new_version = sync_marketplace.sync_plugin_dir(
        plugin_dir, fake_fetch("0.1.1", "b" * 64), lambda url: b"not the right bytes"
    )

    assert new_version is None
    assert (plugin_dir / "keepme.txt").read_text() == "still here"  # untouched
    stamp = json.loads((plugin_dir / sync_marketplace.STAMP_FILENAME).read_text())
    assert stamp["version"] == "0.1.0"  # stamp untouched too


def test_sync_plugin_dir_clears_stale_files(tmp_path):
    plugin_dir = make_stamp(tmp_path, "rgh-sme", "0.1.0", "0" * 64)
    (plugin_dir / "removed-in-new-version.md").write_text("stale")
    sidecar = plugin_dir / ".cursor-plugin" / "plugin.json"
    sidecar.parent.mkdir()
    sidecar.write_text('{"name":"rgh-sme"}\n', encoding="utf-8")

    zip_bytes = make_zip_bytes({"plugin.json": "{}"})
    sha256 = hashlib.sha256(zip_bytes).hexdigest()

    sync_marketplace.sync_plugin_dir(plugin_dir, fake_fetch("0.1.1", sha256), lambda url: zip_bytes)

    assert not (plugin_dir / "removed-in-new-version.md").exists()
    assert (plugin_dir / sync_marketplace.STAMP_FILENAME).exists()  # stamp itself survives
    assert sidecar.is_file()  # Cursor sidecar is marketplace metadata, not package content


def test_sync_plugin_dir_missing_stamp_is_skipped(tmp_path):
    plugin_dir = tmp_path / "plugins" / "no-stamp"
    plugin_dir.mkdir(parents=True)

    new_version = sync_marketplace.sync_plugin_dir(
        plugin_dir, fake_fetch("9.9.9", "f" * 64), lambda url: b""
    )

    assert new_version is None


def test_update_marketplace_version(tmp_path):
    path = tmp_path / "marketplace.json"
    data = {
        "name": "rgh-plugins",
        "plugins": [
            {"name": "rgh-sme", "version": "0.1.0", "source": "./plugins/rgh-sme"},
            {"name": "rgh-pre", "version": "0.1.0", "source": "./plugins/rgh-pre"},
        ],
    }
    path.write_text(json.dumps(data), encoding="utf-8")

    sync_marketplace.update_marketplace_version(path, "rgh-sme", "0.1.1")

    written = json.loads(path.read_text())
    assert written["plugins"][0]["version"] == "0.1.1"
    assert written["plugins"][1]["version"] == "0.1.0"  # untouched


def test_sync_marketplace_end_to_end(tmp_path):
    (tmp_path / ".claude-plugin").mkdir()
    marketplace_path = tmp_path / ".claude-plugin" / "marketplace.json"
    marketplace_path.write_text(
        json.dumps(
            {
                "name": "rgh-plugins",
                "plugins": [{"name": "rgh-sme", "version": "0.1.0", "source": "./plugins/rgh-sme"}],
            }
        ),
        encoding="utf-8",
    )
    zip_bytes = make_zip_bytes({"plugin.json": "{}"})
    sha256 = hashlib.sha256(zip_bytes).hexdigest()
    make_stamp(tmp_path, "rgh-sme", "0.1.0", "0" * 64)

    changed, cursor_changed = sync_marketplace.sync_marketplace(
        tmp_path, fetch=fake_fetch("0.1.1", sha256), download=lambda url: zip_bytes
    )

    assert changed == ["rgh-sme"]
    assert cursor_changed["marketplace"] is True
    written = json.loads(marketplace_path.read_text())
    assert written["plugins"][0]["version"] == "0.1.1"
    cursor_market = json.loads((tmp_path / ".cursor-plugin" / "marketplace.json").read_text())
    assert cursor_market["plugins"][0]["version"] == "0.1.1"
    assert (tmp_path / "plugins" / "rgh-sme" / ".cursor-plugin" / "plugin.json").is_file()
