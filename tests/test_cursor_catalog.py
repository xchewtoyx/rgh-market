import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import cursor_catalog  # noqa: E402


def write_plugin(root: Path, name: str, skills: list[str], agents: list[str] | None = None) -> Path:
    plugin_dir = root / "plugins" / name
    plugin_dir.mkdir(parents=True)
    (plugin_dir / "plugin.json").write_text(
        json.dumps({"name": name, "version": "0.1.0"}), encoding="utf-8"
    )
    for skill in skills:
        skill_dir = plugin_dir / "skills" / skill
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: {skill}\ndescription: test\n---\n", encoding="utf-8"
        )
    for agent in agents or []:
        agent_dir = plugin_dir / "agents"
        agent_dir.mkdir(parents=True, exist_ok=True)
        (agent_dir / f"{agent}.md").write_text(
            f"---\nname: {agent}\ndescription: test\n---\n", encoding="utf-8"
        )
    return plugin_dir


def claude_marketplace() -> dict:
    return {
        "name": "rgh-plugins",
        "owner": {"name": "Russell Heilling", "url": "https://github.com/xchewtoyx"},
        "description": "Test market",
        "plugins": [
            {
                "name": "rgh-sme",
                "displayName": "rgh-sme",
                "description": "SME wikis",
                "version": "0.1.1",
                "author": {"name": "Russell Heilling", "url": "https://github.com/xchewtoyx"},
                "homepage": "https://github.com/xchewtoyx/rgh-sme",
                "repository": "https://github.com/xchewtoyx/rgh-sme",
                "license": "MIT",
                "keywords": ["wiki"],
                "category": "knowledge",
                "strict": False,
                "source": "./plugins/rgh-sme",
            }
        ],
    }


def test_claude_to_cursor_marketplace_drops_claude_fields_and_rewrites_source(tmp_path):
    write_plugin(tmp_path, "rgh-sme", ["wiki-router", "observability-wiki"])
    cursor = cursor_catalog.claude_to_cursor_marketplace(claude_marketplace(), tmp_path / "plugins")

    assert cursor["name"] == "rgh-plugins"
    assert cursor["owner"] == {"name": "Russell Heilling"}
    assert "url" not in cursor["owner"]
    assert cursor["metadata"]["pluginRoot"] == "plugins"
    entry = cursor["plugins"][0]
    assert entry["source"] == "rgh-sme"
    assert entry["name"] == "rgh-sme"
    assert "strict" not in entry
    assert "displayName" not in entry
    assert entry["author"] == {"name": "Russell Heilling"}
    assert entry["skills"] == "skills"
    assert "agents" not in entry


def test_cursor_marketplace_includes_agents_when_present(tmp_path):
    write_plugin(tmp_path, "rgh-sme", ["research"], agents=["planner"])
    cursor = cursor_catalog.claude_to_cursor_marketplace(claude_marketplace(), tmp_path / "plugins")
    assert cursor["plugins"][0]["agents"] == "agents"


def test_install_catalog_includes_archive_and_skill_inventory(tmp_path):
    plugin_dir = write_plugin(tmp_path, "rgh-sme", ["wiki-router"])
    (plugin_dir / cursor_catalog.STAMP_FILENAME).write_text(
        json.dumps(
            {
                "owner": "chewcorp-kl2f",
                "repo": "xchewtoyx",
                "name": "rgh-sme",
                "version": "0.1.1",
                "sha256": "abc",
                "source_url": "https://example.test/rgh-sme.zip",
            }
        ),
        encoding="utf-8",
    )

    catalog = cursor_catalog.build_install_catalog(claude_marketplace(), tmp_path / "plugins")
    entry = catalog["plugins"][0]
    assert entry["source"] == "plugins/rgh-sme"
    assert entry["skills"] == ["wiki-router"]
    assert entry["archive"] == {
        "url": "https://example.test/rgh-sme.zip",
        "sha256": "abc",
        "version": "0.1.1",
    }
    assert entry["git"]["path"] == "plugins/rgh-sme"


def test_write_cursor_artifacts_and_check(tmp_path):
    (tmp_path / ".claude-plugin").mkdir()
    (tmp_path / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps(claude_marketplace(), indent=2) + "\n", encoding="utf-8"
    )
    write_plugin(tmp_path, "rgh-sme", ["wiki-router"])

    changed = cursor_catalog.write_cursor_artifacts(tmp_path)
    assert changed["marketplace"] is True
    assert changed["catalog"] is True
    assert changed["sidecars"] is True
    assert cursor_catalog.artifacts_are_current(tmp_path)

    changed_again = cursor_catalog.write_cursor_artifacts(tmp_path)
    assert changed_again == {"marketplace": False, "catalog": False, "sidecars": False}

    market = json.loads((tmp_path / ".cursor-plugin" / "marketplace.json").read_text())
    sidecar = json.loads(
        (tmp_path / "plugins" / "rgh-sme" / ".cursor-plugin" / "plugin.json").read_text()
    )
    assert market["plugins"][0]["source"] == "rgh-sme"
    assert sidecar["name"] == "rgh-sme"
    assert sidecar["skills"] == "skills"


def test_committed_repo_catalogs_are_current():
    root = Path(__file__).resolve().parent.parent
    assert (root / ".claude-plugin" / "marketplace.json").is_file()
    assert cursor_catalog.artifacts_are_current(root)
