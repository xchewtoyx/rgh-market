#!/usr/bin/env python3
"""Install rgh-market plugins where Cursor Cloud Agents can load them.

Cloud Agents do not inherit plugins installed on a laptop. They discover:

- project skills at `.cursor/skills/` (and `.agents/skills/`) in the clone
- VM-global skills at `~/.cursor/skills/` (typically populated by an
  environment `install` script)
- local plugins at `~/.cursor/plugins/local/<name>/`

This script installs selected plugins as Cursor plugins (skills + agents)
and, by default, also flattens each skill tree under the skills destination
so Cloud Agents pick them up even if plugin discovery is unavailable.

Typical Cloud Agent environment.json:

    {
      "install": "curl -fsSL https://raw.githubusercontent.com/xchewtoyx/rgh-market/main/scripts/install_cursor_plugins.py | python3 - --all"
    }

From a clone of this repo:

    python3 scripts/install_cursor_plugins.py --all
    python3 scripts/install_cursor_plugins.py rgh-sme rgh-pre
    python3 scripts/install_cursor_plugins.py --project --skills-only rgh-sme
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import shutil
import sys
import tarfile
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Any, Callable

# Allow `python3 scripts/install_cursor_plugins.py` and `python3 -` (curl | python).
_SCRIPT_DIR = Path(__file__).resolve().parent if "__file__" in globals() else None
if _SCRIPT_DIR is not None and str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

try:
    import cursor_catalog
except ImportError:  # piped via curl — catalog helpers are inlined below as fallbacks
    cursor_catalog = None  # type: ignore[assignment]

DEFAULT_MARKET_REPO = "https://github.com/xchewtoyx/rgh-market"
DEFAULT_CATALOG_URL = (
    "https://raw.githubusercontent.com/xchewtoyx/rgh-market/main/"
    ".cursor-plugin/catalog.json"
)
DEFAULT_GITHUB_TARBALL = (
    "https://codeload.github.com/xchewtoyx/rgh-market/tar.gz/refs/heads/main"
)

Downloader = Callable[[str], bytes]


def download_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "rgh-market-cursor-install"})
    with urllib.request.urlopen(request, timeout=120) as resp:
        return resp.read()


def load_json_bytes(data: bytes) -> Any:
    return json.loads(data.decode("utf-8"))


def find_repo_root(start: Path) -> Path | None:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".cursor-plugin" / "catalog.json").is_file():
            return candidate
        if (candidate / ".claude-plugin" / "marketplace.json").is_file():
            return candidate
    return None


def load_catalog(
    catalog: str | None,
    repo_root: Path | None,
    download: Downloader,
) -> dict[str, Any]:
    if catalog:
        path = Path(catalog)
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
        return load_json_bytes(download(catalog))
    if repo_root is not None:
        local = repo_root / ".cursor-plugin" / "catalog.json"
        if local.is_file():
            return json.loads(local.read_text(encoding="utf-8"))
        if cursor_catalog is not None:
            claude = json.loads(
                (repo_root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
            )
            return cursor_catalog.build_install_catalog(claude, repo_root / "plugins")
    return load_json_bytes(download(DEFAULT_CATALOG_URL))


def plugin_index(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {entry["name"]: entry for entry in catalog.get("plugins", []) if entry.get("name")}


def extract_zip(data: bytes, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        zf.extractall(dest)


def extract_git_subdir(data: bytes, subdir: str, dest: Path) -> None:
    """Extract `<anything>/<subdir>/...` from a GitHub-style tarball into dest."""
    wanted = subdir.strip("/") + "/"
    dest.mkdir(parents=True, exist_ok=True)
    found = False
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        for member in tf.getmembers():
            parts = Path(member.name).parts
            if len(parts) < 2:
                continue
            rel = "/".join(parts[1:])  # drop the repo-name-ref prefix
            if rel == subdir.rstrip("/") or rel.startswith(wanted):
                found = True
                if member.isdir():
                    continue
                suffix = rel[len(wanted) :] if rel.startswith(wanted) else ""
                if not suffix:
                    continue
                target = dest / suffix
                target.parent.mkdir(parents=True, exist_ok=True)
                extracted = tf.extractfile(member)
                if extracted is None:
                    continue
                target.write_bytes(extracted.read())
    if not found:
        raise SystemExit(f"error: tarball did not contain {subdir!r}")


def copy_plugin_tree(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        src,
        dest,
        ignore=shutil.ignore_patterns(".cloudsmith-source.json", "__pycache__", "*.pyc"),
    )


def write_cursor_sidecar(dest: Path, entry: dict[str, Any]) -> None:
    manifest: dict[str, Any] = {"name": entry["name"]}
    if entry.get("description"):
        manifest["description"] = entry["description"]
    if entry.get("version"):
        manifest["version"] = entry["version"]
    if (dest / "skills").is_dir():
        manifest["skills"] = "skills"
    if (dest / "agents").is_dir():
        manifest["agents"] = "agents"
    sidecar = dest / ".cursor-plugin" / "plugin.json"
    sidecar.parent.mkdir(parents=True, exist_ok=True)
    sidecar.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def flatten_skills(plugin_dest: Path, skills_dest: Path, plugin_name: str) -> list[str]:
    """Copy skills/<name>/ to skills_dest/<plugin_name>/<name>/ to avoid collisions."""
    installed: list[str] = []
    skills_root = plugin_dest / "skills"
    if not skills_root.is_dir():
        return installed
    plugin_skills = skills_dest / plugin_name
    if plugin_skills.exists():
        shutil.rmtree(plugin_skills)
    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        if not (skill_dir / "SKILL.md").is_file():
            continue
        target = plugin_skills / skill_dir.name
        shutil.copytree(skill_dir, target)
        installed.append(f"{plugin_name}/{skill_dir.name}")
    return installed


def materialize_plugin(
    entry: dict[str, Any],
    staging: Path,
    repo_root: Path | None,
    download: Downloader,
    tarball_url: str,
) -> Path:
    name = entry["name"]
    dest = staging / name
    local_src = None
    if repo_root is not None:
        candidate = repo_root / entry.get("source", f"plugins/{name}")
        if candidate.is_dir() and (
            (candidate / "plugin.json").is_file() or (candidate / "skills").is_dir()
        ):
            local_src = candidate
    if local_src is not None:
        copy_plugin_tree(local_src, dest)
        return dest

    archive = entry.get("archive") or {}
    if archive.get("url"):
        data = download(archive["url"])
        expected = archive.get("sha256")
        if expected:
            actual = hashlib.sha256(data).hexdigest()
            if actual != expected:
                raise SystemExit(
                    f"error: {name} archive sha256 {actual} != catalog {expected}"
                )
        if dest.exists():
            shutil.rmtree(dest)
        extract_zip(data, dest)
        return dest

    git = entry.get("git") or {}
    subdir = git.get("path") or f"plugins/{name}"
    data = download(tarball_url)
    if dest.exists():
        shutil.rmtree(dest)
    extract_git_subdir(data, subdir, dest)
    return dest


def install_plugin(
    entry: dict[str, Any],
    repo_root: Path | None,
    plugins_dir: Path | None,
    skills_dir: Path | None,
    download: Downloader,
    tarball_url: str,
) -> dict[str, Any]:
    name = entry["name"]
    with tempfile.TemporaryDirectory(prefix=f"rgh-market-{name}-") as tmp:
        staged = materialize_plugin(entry, Path(tmp), repo_root, download, tarball_url)
        write_cursor_sidecar(staged, entry)
        result: dict[str, Any] = {"name": name, "version": entry.get("version"), "skills": []}
        if plugins_dir is not None:
            target = plugins_dir / name
            copy_plugin_tree(staged, target)
            write_cursor_sidecar(target, entry)
            result["plugin"] = str(target)
        if skills_dir is not None:
            source = (plugins_dir / name) if plugins_dir is not None else staged
            result["skills"] = flatten_skills(source, skills_dir, name)
        return result


def default_plugins_dir() -> Path:
    return Path.home() / ".cursor" / "plugins" / "local"


def default_skills_dir() -> Path:
    return Path.home() / ".cursor" / "skills"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "plugins",
        nargs="*",
        help="Plugin names to install (from the catalog). Omit and pass --all to install every entry.",
    )
    parser.add_argument("--all", action="store_true", help="Install every plugin in the catalog")
    parser.add_argument("--list", action="store_true", help="Print catalog entries and exit")
    parser.add_argument(
        "--catalog",
        default=None,
        help="Local catalog.json path or HTTPS URL (default: repo file, else GitHub raw)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="rgh-market checkout to copy plugins from (default: locate from cwd)",
    )
    parser.add_argument(
        "--plugins-dir",
        type=Path,
        default=None,
        help=f"Cursor local-plugin destination (default: {default_plugins_dir()})",
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=None,
        help=f"Flattened-skill destination (default: {default_skills_dir()})",
    )
    parser.add_argument(
        "--project",
        action="store_true",
        help="Install into the current repo: .cursor/plugins and .cursor/skills",
    )
    parser.add_argument(
        "--skills-only",
        action="store_true",
        help="Only flatten skills; do not write ~/.cursor/plugins/local",
    )
    parser.add_argument(
        "--plugins-only",
        action="store_true",
        help="Only install plugin trees; do not flatten skills",
    )
    parser.add_argument(
        "--tarball-url",
        default=DEFAULT_GITHUB_TARBALL,
        help="GitHub tarball used when a plugin has no Cloudsmith archive",
    )
    return parser.parse_args(argv)


def resolve_destinations(args: argparse.Namespace) -> tuple[Path | None, Path | None]:
    if args.project:
        plugins_dir = Path(".cursor") / "plugins"
        skills_dir = Path(".cursor") / "skills"
    else:
        plugins_dir = args.plugins_dir or default_plugins_dir()
        skills_dir = args.skills_dir or default_skills_dir()
    if args.plugins_dir is not None:
        plugins_dir = args.plugins_dir
    if args.skills_dir is not None:
        skills_dir = args.skills_dir
    if args.skills_only:
        plugins_dir = None
    if args.plugins_only:
        skills_dir = None
    if plugins_dir is None and skills_dir is None:
        raise SystemExit("error: nothing to install (--skills-only and --plugins-only together)")
    return plugins_dir, skills_dir


def main(argv: list[str] | None = None, download: Downloader = download_bytes) -> int:
    args = parse_args(argv)
    # An explicit --catalog is fetch instructions; do not also copy from cwd
    # unless the caller named a checkout with --root.
    if args.root is not None:
        repo_root = args.root.resolve()
    elif args.catalog is None:
        repo_root = find_repo_root(Path.cwd())
    else:
        repo_root = None
    try:
        catalog = load_catalog(args.catalog, repo_root, download)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"error: could not load catalog: {exc}", file=sys.stderr)
        return 1

    index = plugin_index(catalog)
    if args.list:
        for name, entry in index.items():
            skills = entry.get("skills") or []
            version = entry.get("version") or "?"
            print(f"{name} {version}  ({len(skills)} skills)")
        return 0

    selected = list(index) if args.all else list(args.plugins)
    if not selected:
        print("error: name one or more plugins, or pass --all / --list", file=sys.stderr)
        return 1
    missing = [name for name in selected if name not in index]
    if missing:
        known = ", ".join(index) or "(none)"
        print(f"error: unknown plugin(s): {', '.join(missing)}. Known: {known}", file=sys.stderr)
        return 1

    plugins_dir, skills_dir = resolve_destinations(args)
    if plugins_dir is not None:
        plugins_dir.mkdir(parents=True, exist_ok=True)
    if skills_dir is not None:
        skills_dir.mkdir(parents=True, exist_ok=True)

    for name in selected:
        result = install_plugin(
            index[name],
            repo_root,
            plugins_dir,
            skills_dir,
            download,
            args.tarball_url,
        )
        skill_note = f", {len(result['skills'])} skills" if result["skills"] else ""
        dest = result.get("plugin") or (str(skills_dir) if skills_dir else "")
        print(f"installed {result['name']} {result.get('version') or ''} -> {dest}{skill_note}".rstrip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
