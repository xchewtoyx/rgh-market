#!/usr/bin/env python3
"""Vendor Cloudsmith-published plugin packages into plugins/<name>/ and keep
.claude-plugin/marketplace.json's version field current.

Claude Code's stable CLI installer (verified against 2.1.223) only supports
`github`, `url` (git), and `git-subdir` plugin sources -- not the `archive`
(HTTPS zip + sha256) source type these packages were originally published
under. Rather than wait for that to land everywhere, each marketplace.json
plugin entry points at a `./plugins/<name>` path *inside this repo*, and
this script is what keeps that vendored copy in sync with the newest
package Cloudsmith has: it downloads the zip, verifies its sha256 against
what the Cloudsmith API reports, and extracts it over the vendored
directory. Cloudsmith stays the authoritative artifact store; this repo
just mirrors the latest release so every Claude Code version -- not only
ones with archive support -- can install straight from git.

Each plugins/<name>/ directory carries a `.cloudsmith-source.json` stamp
recording where it's vendored from (Cloudsmith owner/repo/package name) and
what was last synced (version, sha256, source URL, timestamp). To vendor a
new plugin, create plugins/<name>/.cloudsmith-source.json with those three
coordinates, add a matching entry to marketplace.json's plugins[], and the
next sync run populates the directory and its version.

Usage (from repo root, or any cwd -- script locates the root):
  scripts/sync_marketplace.py
  scripts/sync_marketplace.py --check   # exit 1 if anything would change
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

API_TEMPLATE = (
    "https://api.cloudsmith.io/v1/packages/{owner}/{repo}/"
    "?query=name:{name}&sort=-date&page_size=1"
)

STAMP_FILENAME = ".cloudsmith-source.json"

Fetcher = Callable[[str, str, str], "dict | None"]
Downloader = Callable[[str], bytes]


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".claude-plugin" / "marketplace.json").is_file():
            return candidate
    raise SystemExit(f"error: could not find .claude-plugin/marketplace.json above {start}")


def fetch_latest_package(owner: str, repo: str, name: str) -> dict | None:
    """Return the newest Cloudsmith package dict matching `name`, or None."""
    url = API_TEMPLATE.format(owner=owner, repo=repo, name=name)
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            payload = json.load(resp)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"warning: Cloudsmith API request failed for {name}: {exc}", file=sys.stderr)
        return None
    if isinstance(payload, dict):
        # Cloudsmith returns a JSON array of error strings for bad requests.
        print(f"warning: unexpected Cloudsmith API response for {name}: {payload}", file=sys.stderr)
        return None
    matches = [p for p in payload if p.get("name") == name]
    if not matches:
        print(f"warning: no Cloudsmith package named {name!r} in {owner}/{repo}", file=sys.stderr)
        return None
    return matches[0]


def download_bytes(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as resp:
        return resp.read()


def _clear_dir(path: Path) -> None:
    """Remove everything under `path` except the stamp file."""
    for entry in path.iterdir():
        if entry.name == STAMP_FILENAME:
            continue
        if entry.is_dir():
            shutil.rmtree(entry)
        else:
            entry.unlink()


def sync_plugin_dir(plugin_dir: Path, fetch: Fetcher, download: Downloader) -> str | None:
    """Vendor the newest Cloudsmith package into `plugin_dir` if it changed.

    Returns the new version string on a successful update, else None.
    """
    stamp_path = plugin_dir / STAMP_FILENAME
    if not stamp_path.is_file():
        print(f"warning: no {STAMP_FILENAME} in {plugin_dir}; skipping", file=sys.stderr)
        return None
    stamp = json.loads(stamp_path.read_text(encoding="utf-8"))
    owner, repo, name = stamp.get("owner"), stamp.get("repo"), stamp.get("name")
    if not owner or not repo or not name:
        print(f"warning: {stamp_path} missing owner/repo/name; skipping", file=sys.stderr)
        return None

    package = fetch(owner, repo, name)
    if package is None:
        return None

    new_version = package.get("version")
    new_sha256 = package.get("checksum_sha256")
    new_url = package.get("cdn_url")
    if not new_version or not new_sha256 or not new_url:
        print(
            f"warning: Cloudsmith package for {name!r} is missing "
            f"version/checksum_sha256/cdn_url; skipping",
            file=sys.stderr,
        )
        return None

    if stamp.get("sha256") == new_sha256:
        return None  # already vendoring the newest package

    data = download(new_url)
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != new_sha256:
        print(
            f"warning: downloaded {name} archive sha256 {actual_sha256} does not match "
            f"Cloudsmith-reported {new_sha256}; leaving vendored copy unchanged",
            file=sys.stderr,
        )
        return None

    with tempfile.TemporaryDirectory() as tmp:
        archive_path = Path(tmp) / "package.zip"
        archive_path.write_bytes(data)
        with zipfile.ZipFile(archive_path) as zf:
            _clear_dir(plugin_dir)
            zf.extractall(plugin_dir)

    stamp.update(
        version=new_version,
        sha256=new_sha256,
        source_url=new_url,
        synced_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
    stamp_path.write_text(json.dumps(stamp, indent=2) + "\n", encoding="utf-8")
    return new_version


def update_marketplace_version(marketplace_path: Path, name: str, version: str) -> None:
    data = json.loads(marketplace_path.read_text(encoding="utf-8"))
    for entry in data.get("plugins", []):
        if entry.get("name") == name:
            entry["version"] = version
            break
    marketplace_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sync_marketplace(
    root: Path,
    fetch: Fetcher = fetch_latest_package,
    download: Downloader = download_bytes,
) -> list[str]:
    """Sync every plugins/<name>/ directory under `root`. Return names that changed."""
    marketplace_path = root / ".claude-plugin" / "marketplace.json"
    plugins_dir = root / "plugins"
    changed: list[str] = []
    for plugin_dir in sorted(p for p in plugins_dir.iterdir() if p.is_dir()):
        new_version = sync_plugin_dir(plugin_dir, fetch, download)
        if new_version:
            update_marketplace_version(marketplace_path, plugin_dir.name, new_version)
            changed.append(plugin_dir.name)
            print(f"updated {plugin_dir.name} -> {new_version}")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Marketplace repo root (default: located from cwd via .claude-plugin/marketplace.json)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if anything would change (CI guard; still writes the update)",
    )
    args = parser.parse_args()

    root = args.root or find_root(Path.cwd())
    changed = sync_marketplace(root)

    if not changed:
        print("plugins are already up to date")
    if args.check and changed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
