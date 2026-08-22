import hashlib
import io
import json
import sys
import tarfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import install_cursor_plugins  # noqa: E402


def make_zip_bytes(files: dict[str, str]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, content in files.items():
            zf.writestr(name, content)
    return buf.getvalue()


def make_tarball_bytes(prefix: str, files: dict[str, str]) -> bytes:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for name, content in files.items():
            data = content.encode("utf-8")
            info = tarfile.TarInfo(name=f"{prefix}/{name}")
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))
    return buf.getvalue()


def catalog_for(name: str, **extra) -> dict:
    entry = {
        "name": name,
        "description": "test plugin",
        "version": "0.1.1",
        "source": f"plugins/{name}",
        "skills": ["wiki-router"],
        "agents": [],
        "git": {"url": "https://github.com/xchewtoyx/rgh-market", "path": f"plugins/{name}"},
    }
    entry.update(extra)
    return {"name": "rgh-plugins", "plugins": [entry]}


def test_install_from_local_repo_flattens_skills(tmp_path, monkeypatch):
    root = tmp_path / "market"
    plugin = root / "plugins" / "rgh-sme"
    skill = plugin / "skills" / "wiki-router"
    skill.mkdir(parents=True)
    (plugin / "plugin.json").write_text('{"name":"rgh-sme"}', encoding="utf-8")
    (skill / "SKILL.md").write_text("---\nname: wiki-router\ndescription: x\n---\n", encoding="utf-8")
    catalog_path = root / ".cursor-plugin" / "catalog.json"
    catalog_path.parent.mkdir(parents=True)
    catalog_path.write_text(json.dumps(catalog_for("rgh-sme")), encoding="utf-8")

    plugins_dir = tmp_path / "dest-plugins"
    skills_dir = tmp_path / "dest-skills"
    rc = install_cursor_plugins.main(
        [
            "--root",
            str(root),
            "--catalog",
            str(catalog_path),
            "--plugins-dir",
            str(plugins_dir),
            "--skills-dir",
            str(skills_dir),
            "rgh-sme",
        ]
    )
    assert rc == 0
    assert (plugins_dir / "rgh-sme" / "skills" / "wiki-router" / "SKILL.md").is_file()
    assert (plugins_dir / "rgh-sme" / ".cursor-plugin" / "plugin.json").is_file()
    assert (skills_dir / "rgh-sme" / "wiki-router" / "SKILL.md").is_file()


def test_install_from_archive_verifies_sha256(tmp_path):
    zip_bytes = make_zip_bytes(
        {
            "plugin.json": '{"name":"rgh-sme"}',
            "skills/wiki-router/SKILL.md": "---\nname: wiki-router\ndescription: x\n---\n",
        }
    )
    sha256 = hashlib.sha256(zip_bytes).hexdigest()
    catalog = catalog_for(
        "rgh-sme",
        archive={"url": "https://example.test/rgh-sme.zip", "sha256": sha256, "version": "0.1.1"},
    )
    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps(catalog), encoding="utf-8")

    def download(url: str) -> bytes:
        assert url == "https://example.test/rgh-sme.zip"
        return zip_bytes

    plugins_dir = tmp_path / "plugins"
    rc = install_cursor_plugins.main(
        [
            "--catalog",
            str(catalog_path),
            "--plugins-dir",
            str(plugins_dir),
            "--plugins-only",
            "rgh-sme",
        ],
        download=download,
    )
    assert rc == 0
    assert (plugins_dir / "rgh-sme" / "plugin.json").is_file()


def test_install_rejects_checksum_mismatch(tmp_path):
    catalog = catalog_for(
        "rgh-sme",
        archive={"url": "https://example.test/rgh-sme.zip", "sha256": "0" * 64, "version": "0.1.1"},
    )
    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps(catalog), encoding="utf-8")

    try:
        install_cursor_plugins.main(
            [
                "--catalog",
                str(catalog_path),
                "--plugins-dir",
                str(tmp_path / "plugins"),
                "--plugins-only",
                "rgh-sme",
            ],
            download=lambda url: b"nope",
        )
    except SystemExit as exc:
        assert exc.code != 0
        assert "sha256" in str(exc)
    else:
        raise AssertionError("expected checksum mismatch to abort")


def test_install_from_github_tarball_subdir(tmp_path):
    tarball = make_tarball_bytes(
        "rgh-market-main",
        {
            "plugins/bundle-curator/plugin.json": '{"name":"bundle-curator"}',
            "plugins/bundle-curator/skills/curate/SKILL.md": "---\nname: curate\ndescription: x\n---\n",
        },
    )
    catalog = catalog_for(
        "bundle-curator",
        skills=["curate"],
        source="plugins/bundle-curator",
        git={"url": "https://github.com/xchewtoyx/rgh-market", "path": "plugins/bundle-curator"},
    )
    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
    skills_dir = tmp_path / "skills"

    rc = install_cursor_plugins.main(
        [
            "--catalog",
            str(catalog_path),
            "--skills-dir",
            str(skills_dir),
            "--skills-only",
            "--tarball-url",
            "https://example.test/main.tar.gz",
            "bundle-curator",
        ],
        download=lambda url: tarball,
    )
    assert rc == 0
    assert (skills_dir / "bundle-curator" / "curate" / "SKILL.md").is_file()


def test_list_and_unknown_plugin(tmp_path, capsys):
    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps(catalog_for("rgh-sme")), encoding="utf-8")

    assert install_cursor_plugins.main(["--catalog", str(catalog_path), "--list"]) == 0
    assert "rgh-sme" in capsys.readouterr().out

    assert (
        install_cursor_plugins.main(["--catalog", str(catalog_path), "does-not-exist"]) == 1
    )
