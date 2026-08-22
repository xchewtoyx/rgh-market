#!/usr/bin/env python3
"""Generate Cursor-facing catalogs from the Claude marketplace.

Claude Code reads `.claude-plugin/marketplace.json`. Cursor Team Marketplace
import and `agent plugin marketplace add` read `.cursor-plugin/marketplace.json`
instead — same plugins, different catalog schema and source paths.

This module is the single translation step:

- `.cursor-plugin/marketplace.json` — Cursor multi-plugin repo catalog
  (https://cursor.com/docs/reference/plugins.md#cursor-multi-plugin-repositories)
- `.cursor-plugin/catalog.json` — install metadata for Cloud Agents
  (archive URLs, checksums, skill/agent inventories)
- `plugins/<name>/.cursor-plugin/plugin.json` — per-plugin Cursor sidecar so
  Team Marketplace resolution finds a Cursor manifest without rewriting the
  Agent Plugins `plugin.json` that Cloudsmith vendors.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

DEFAULT_MARKET_REPO = "https://github.com/xchewtoyx/rgh-market"
DEFAULT_CATALOG_URL = (
    "https://raw.githubusercontent.com/xchewtoyx/rgh-market/main/"
    ".cursor-plugin/catalog.json"
)
CURSOR_SIDECAR_DIR = ".cursor-plugin"
MARKETPLACE_FILENAME = "marketplace.json"
CATALOG_FILENAME = "catalog.json"
PLUGIN_MANIFEST = "plugin.json"
STAMP_FILENAME = ".cloudsmith-source.json"

CURSOR_ENTRY_FIELDS = (
    "name",
    "description",
    "version",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "logo",
    "category",
    "tags",
)


def dumps(data: Any) -> str:
    return json.dumps(data, indent=2) + "\n"


def write_json(path: Path, data: Any) -> bool:
    """Write pretty JSON. Return True if the file content changed."""
    text = dumps(data)
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def list_component_dirs(plugin_dir: Path, folder: str, required_file: str | None) -> list[str]:
    root = plugin_dir / folder
    if not root.is_dir():
        return []
    names: list[str] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        if required_file and not (child / required_file).is_file():
            continue
        names.append(child.name)
    return names


def list_component_files(plugin_dir: Path, folder: str, suffixes: tuple[str, ...]) -> list[str]:
    root = plugin_dir / folder
    if not root.is_dir():
        return []
    names: list[str] = []
    for child in sorted(root.iterdir()):
        if child.is_file() and child.suffix.lower() in suffixes:
            names.append(child.stem)
    return names


def discover_components(plugin_dir: Path) -> dict[str, list[str]]:
    """Inventory skills (SKILL.md dirs) and agents (markdown files)."""
    skills = list_component_dirs(plugin_dir, "skills", "SKILL.md")
    agents = list_component_files(plugin_dir, "agents", (".md", ".mdc", ".markdown"))
    return {"skills": skills, "agents": agents}


def cursor_author(author: Any) -> dict[str, str] | None:
    """Cursor author objects accept name + optional email, not url."""
    if not isinstance(author, dict) or not author.get("name"):
        return None
    mapped = {"name": author["name"]}
    if author.get("email"):
        mapped["email"] = author["email"]
    return mapped


def plugin_source_name(entry: dict) -> str:
    """Turn Claude `./plugins/rgh-sme` (or any path) into a Cursor source name."""
    source = entry.get("source") or entry.get("name") or ""
    if isinstance(source, dict):
        source = source.get("path") or entry.get("name") or ""
    return Path(str(source)).name


def cursor_plugin_entry(entry: dict, plugin_dir: Path | None) -> dict[str, Any]:
    out: dict[str, Any] = {"name": entry["name"], "source": plugin_source_name(entry)}
    for key in CURSOR_ENTRY_FIELDS:
        if key in ("name", "author"):
            continue
        if key in entry and entry[key] not in (None, "", []):
            out[key] = entry[key]
    author = cursor_author(entry.get("author"))
    if author:
        out["author"] = author
    if plugin_dir is not None:
        components = discover_components(plugin_dir)
        if components["skills"]:
            out["skills"] = "skills"
        if components["agents"]:
            out["agents"] = "agents"
    return out


def claude_to_cursor_marketplace(claude: dict, plugins_dir: Path) -> dict[str, Any]:
    owner = claude.get("owner") or {}
    cursor_owner = {"name": owner.get("name") or "unknown"}
    if owner.get("email"):
        cursor_owner["email"] = owner["email"]

    plugins: list[dict[str, Any]] = []
    for entry in claude.get("plugins", []):
        name = plugin_source_name(entry)
        plugin_dir = plugins_dir / name
        plugins.append(cursor_plugin_entry(entry, plugin_dir if plugin_dir.is_dir() else None))

    marketplace: dict[str, Any] = {
        "name": claude.get("name") or "rgh-plugins",
        "owner": cursor_owner,
        "metadata": {
            "description": claude.get("description")
            or "Zettelkasten-style Agent Plugins wiki bundles",
            "pluginRoot": "plugins",
        },
        "plugins": plugins,
    }
    return marketplace


def install_catalog_entry(entry: dict, plugin_dir: Path, market_repo: str) -> dict[str, Any]:
    components = discover_components(plugin_dir) if plugin_dir.is_dir() else {
        "skills": [],
        "agents": [],
    }
    out: dict[str, Any] = {
        "name": entry["name"],
        "description": entry.get("description") or "",
        "version": entry.get("version"),
        "source": f"plugins/{plugin_source_name(entry)}",
        "homepage": entry.get("homepage"),
        "repository": entry.get("repository"),
        "license": entry.get("license"),
        "keywords": entry.get("keywords") or [],
        "category": entry.get("category"),
        "skills": components["skills"],
        "agents": components["agents"],
        "git": {"url": market_repo, "path": f"plugins/{plugin_source_name(entry)}"},
    }
    stamp_path = plugin_dir / STAMP_FILENAME
    if stamp_path.is_file():
        stamp = load_json(stamp_path)
        url = stamp.get("source_url")
        sha256 = stamp.get("sha256")
        if url and sha256:
            out["archive"] = {
                "url": url,
                "sha256": sha256,
                "version": stamp.get("version") or entry.get("version"),
            }
    return {k: v for k, v in out.items() if v not in (None,)}


def build_install_catalog(
    claude: dict,
    plugins_dir: Path,
    market_repo: str = DEFAULT_MARKET_REPO,
) -> dict[str, Any]:
    plugins = [
        install_catalog_entry(entry, plugins_dir / plugin_source_name(entry), market_repo)
        for entry in claude.get("plugins", [])
    ]
    return {
        "name": claude.get("name") or "rgh-plugins",
        "description": claude.get("description")
        or "Zettelkasten-style Agent Plugins wiki bundles",
        "repository": market_repo,
        "catalog_url": DEFAULT_CATALOG_URL,
        "plugins": plugins,
    }


def cursor_sidecar_manifest(entry: dict, plugin_dir: Path) -> dict[str, Any]:
    """Thin Cursor Plugin manifest derived from the marketplace entry + layout."""
    manifest: dict[str, Any] = {"name": entry["name"]}
    if entry.get("description"):
        manifest["description"] = entry["description"]
    if entry.get("version"):
        manifest["version"] = entry["version"]
    author = cursor_author(entry.get("author"))
    if author:
        manifest["author"] = author
    if entry.get("homepage"):
        manifest["homepage"] = entry["homepage"]
    if entry.get("repository"):
        manifest["repository"] = entry["repository"]
    if entry.get("license"):
        manifest["license"] = entry["license"]
    if entry.get("keywords"):
        manifest["keywords"] = entry["keywords"]
    components = discover_components(plugin_dir)
    if components["skills"]:
        manifest["skills"] = "skills"
    if components["agents"]:
        manifest["agents"] = "agents"
    return manifest


def write_plugin_sidecars(claude: dict, plugins_dir: Path) -> list[str]:
    changed: list[str] = []
    for entry in claude.get("plugins", []):
        name = plugin_source_name(entry)
        plugin_dir = plugins_dir / name
        if not plugin_dir.is_dir():
            continue
        sidecar = plugin_dir / CURSOR_SIDECAR_DIR / PLUGIN_MANIFEST
        if write_json(sidecar, cursor_sidecar_manifest(entry, plugin_dir)):
            changed.append(name)
    return changed


def write_cursor_artifacts(
    root: Path,
    market_repo: str = DEFAULT_MARKET_REPO,
) -> dict[str, bool]:
    """Regenerate Cursor catalogs and sidecars. Values are True when a file changed."""
    claude_path = root / ".claude-plugin" / MARKETPLACE_FILENAME
    if not claude_path.is_file():
        raise FileNotFoundError(f"missing {claude_path}")
    claude = load_json(claude_path)
    plugins_dir = root / "plugins"
    cursor_dir = root / CURSOR_SIDECAR_DIR

    marketplace = claude_to_cursor_marketplace(claude, plugins_dir)
    catalog = build_install_catalog(claude, plugins_dir, market_repo)
    changed = {
        "marketplace": write_json(cursor_dir / MARKETPLACE_FILENAME, marketplace),
        "catalog": write_json(cursor_dir / CATALOG_FILENAME, catalog),
        "sidecars": bool(write_plugin_sidecars(claude, plugins_dir)),
    }
    return changed


def artifacts_are_current(root: Path, market_repo: str = DEFAULT_MARKET_REPO) -> bool:
    """True when committed Cursor artifacts match a fresh generation."""
    claude = load_json(root / ".claude-plugin" / MARKETPLACE_FILENAME)
    plugins_dir = root / "plugins"
    cursor_dir = root / CURSOR_SIDECAR_DIR
    expected_market = dumps(claude_to_cursor_marketplace(claude, plugins_dir))
    expected_catalog = dumps(build_install_catalog(claude, plugins_dir, market_repo))
    market_path = cursor_dir / MARKETPLACE_FILENAME
    catalog_path = cursor_dir / CATALOG_FILENAME
    if not market_path.is_file() or not catalog_path.is_file():
        return False
    if market_path.read_text(encoding="utf-8") != expected_market:
        return False
    if catalog_path.read_text(encoding="utf-8") != expected_catalog:
        return False
    for entry in claude.get("plugins", []):
        name = plugin_source_name(entry)
        plugin_dir = plugins_dir / name
        if not plugin_dir.is_dir():
            continue
        sidecar = plugin_dir / CURSOR_SIDECAR_DIR / PLUGIN_MANIFEST
        if not sidecar.is_file():
            return False
        if sidecar.read_text(encoding="utf-8") != dumps(cursor_sidecar_manifest(entry, plugin_dir)):
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Marketplace repo root (default: parent of this script's directory)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if committed Cursor artifacts are stale (does not write)",
    )
    parser.add_argument(
        "--repo",
        default=DEFAULT_MARKET_REPO,
        help=f"Canonical git URL recorded in catalog.json (default: {DEFAULT_MARKET_REPO})",
    )
    args = parser.parse_args()
    root = (args.root or Path(__file__).resolve().parent.parent).resolve()

    if args.check:
        if artifacts_are_current(root, args.repo):
            print("Cursor catalogs are up to date")
            return
        print("error: Cursor catalogs are stale; run scripts/cursor_catalog.py", file=sys.stderr)
        raise SystemExit(1)

    changed = write_cursor_artifacts(root, args.repo)
    if any(changed.values()):
        parts = [name for name, did in changed.items() if did]
        print("updated " + ", ".join(parts))
    else:
        print("Cursor catalogs are already up to date")


if __name__ == "__main__":
    main()
