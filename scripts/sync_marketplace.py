#!/usr/bin/env python3
"""Refresh Cloudsmith-backed plugin entries in .claude-plugin/marketplace.json.

For every plugin entry whose ``source.source`` is ``"archive"`` and whose
``source.url`` points at ``dl.cloudsmith.io``, this queries the Cloudsmith
packages API (anonymous read, no API key needed for a public repo) for the
newest package matching that plugin's name, and rewrites the entry's
``version``, ``source.url``, and ``source.sha256`` to match. Entries whose
Cloudsmith package can't be found are left untouched and reported as
warnings, so a transient API hiccup or a renamed package doesn't wipe out a
working marketplace entry.

The owner/repo/package-name triple is parsed from the entry's own existing
Cloudsmith URL, so no separate config file is needed: add a new plugin entry
pointing at any version of its Cloudsmith package, and future runs keep it
current.

Usage (from repo root, or any cwd -- script locates the root):
  scripts/sync_marketplace.py
  scripts/sync_marketplace.py --check   # exit 1 if the file would change
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable

CLOUDSMITH_URL_RE = re.compile(
    r"^https://dl\.cloudsmith\.io/public/(?P<owner>[^/]+)/(?P<repo>[^/]+)/raw/"
    r"names/(?P<name>[^/]+)/versions/(?P<version>[^/]+)/(?P<filename>[^/]+)$"
)

API_TEMPLATE = (
    "https://api.cloudsmith.io/v1/packages/{owner}/{repo}/"
    "?query=name:{name}&sort=-date&page_size=1"
)

Fetcher = Callable[[str, str, str], "dict | None"]


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


def sync_entry(entry: dict, fetch: Fetcher) -> bool:
    """Update `entry` in place from Cloudsmith. Return True if it changed."""
    source = entry.get("source")
    if not isinstance(source, dict) or source.get("source") != "archive":
        return False
    match = CLOUDSMITH_URL_RE.match(source.get("url", ""))
    if not match:
        return False

    package = fetch(match["owner"], match["repo"], match["name"])
    if package is None:
        return False

    new_url = package.get("cdn_url")
    new_sha256 = package.get("checksum_sha256")
    new_version = package.get("version")
    if not new_url or not new_sha256 or not new_version:
        print(
            f"warning: Cloudsmith package for {match['name']!r} is missing "
            f"cdn_url/checksum_sha256/version; leaving entry unchanged",
            file=sys.stderr,
        )
        return False

    changed = (
        source.get("url") != new_url
        or source.get("sha256") != new_sha256
        or entry.get("version") != new_version
    )
    source["url"] = new_url
    source["sha256"] = new_sha256
    entry["version"] = new_version
    return changed


def sync_marketplace(path: Path, fetch: Fetcher = fetch_latest_package) -> bool:
    """Sync every archive/Cloudsmith plugin entry in `path`. Return True if changed."""
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for entry in data.get("plugins", []):
        if sync_entry(entry, fetch):
            changed = True
            print(f"updated {entry['name']} -> {entry['version']}")
    if changed:
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--marketplace",
        type=Path,
        default=None,
        help="Path to marketplace.json (default: <repo>/.claude-plugin/marketplace.json)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if the file would change (CI guard; still writes the update)",
    )
    args = parser.parse_args()

    path = args.marketplace or (find_root(Path.cwd()) / ".claude-plugin" / "marketplace.json")
    changed = sync_marketplace(path)

    if not changed:
        print("marketplace.json is already up to date")
    if args.check and changed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
