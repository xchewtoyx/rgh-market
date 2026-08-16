#!/usr/bin/env python3
"""Domain-slug list, derived from okf-core.toml.

The single source of truth for which domain bundles exist. Scripts that need
the full domain list (scripts/curation-progress.py,
scripts/select-catchup-candidates.py, scripts/select-score-catchup-candidates.py,
scripts/build-plugin.py) import `load_domains` from here instead of carrying
their own hardcoded copy -- adding a domain then means editing okf-core.toml
and nothing else in scripts/.

Usage as a library:
    from domains import load_domains
    DOMAINS = load_domains(root)

Usage from the command line (debugging / shell scripts):
    python3 scripts/domains.py            # one slug per line, declaration order
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import tomllib  # Python >= 3.11
except ModuleNotFoundError:  # pragma: no cover - exercised only on old interpreters
    tomllib = None  # type: ignore[assignment]

_BUNDLE_HEADER = re.compile(r"^\[bundles\.([A-Za-z0-9_-]+)\]\s*$")


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "okf-core.toml").is_file():
            return candidate
    raise SystemExit(f"error: could not find okf-core.toml above {start}")


def _load_domains_tomllib(config_path: Path) -> list[str]:
    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    bundles = data.get("bundles", {})
    if not isinstance(bundles, dict):
        return []
    return list(bundles.keys())


def _load_domains_regex(config_path: Path) -> list[str]:
    """Fallback for interpreters without tomllib (< 3.11): scan for
    `[bundles.<slug>]` headers in file order. Good enough for this file's
    narrow, hand-authored shape; not a general TOML parser.
    """
    domains: list[str] = []
    for line in config_path.read_text(encoding="utf-8").splitlines():
        match = _BUNDLE_HEADER.match(line.strip())
        if match:
            domains.append(match.group(1))
    return domains


def load_domains(root: Path) -> list[str]:
    """Return domain slugs declared in okf-core.toml, in declaration order."""
    config_path = root / "okf-core.toml"
    if not config_path.is_file():
        raise SystemExit(f"error: okf-core.toml not found at {config_path}")
    if tomllib is not None:
        domains = _load_domains_tomllib(config_path)
    else:
        domains = _load_domains_regex(config_path)
    if not domains:
        raise SystemExit(
            f"error: no [bundles.<slug>] entries found in {config_path}"
        )
    return domains


def main() -> None:
    root = find_root(Path.cwd())
    for domain in load_domains(root):
        print(domain)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
