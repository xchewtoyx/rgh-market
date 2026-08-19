#!/usr/bin/env python3
"""Bundle config resolution for rgh-mms (issues #175, #172, #327).

Two independent resolvers live in this module:

1. `resolve_detached_bundle` (issue #175/#172) — reads detached-mode
   dispositions out of `repos/<bundle>.yaml`, the legacy meta-registry. A
   bundle is *pinned* (the default) when the product repo carries
   `.agentic/harness.yaml` and that file is the authoritative contract, or
   *detached* when the product repo carries no harness files at all and the
   registry entry in this repo is the contract. See `repos/README.md`
   ("Resolution order") and
   `.agent-metrics/contracts/0025_detached_contract_mode.md`. Unchanged by
   issue #327 — this is the deferred-wave `repos/*.yaml` regime the
   layered resolver below does not touch (see `AGENTS.md`
   "`scripts/bundle_registry.py`").
2. `resolve_bundle_config` (issue #327) — the new four-layer resolver
   replacing `repos/README.md`'s three prose resolution-order variants:
   plugin per-platform defaults -> `~/.claude/rgh-mms.json` (user plugin
   config, keyed per bundle) -> committed in-repo `.claude/rgh-mms.json`
   -> optional uncommitted `.claude/rgh-mms.local.json`. See that
   function's docstring and `.agent-metrics/contracts/i324_repo_offboarding.md`.

Issue #172 wires `resolve_detached_bundle` into
`scripts/generate-adapters.py::resolve_default_clients` when an operator
supplies `--bundle` for a target with no product-side contract.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - same guard as validate-manifests.py
    yaml = None

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schema_validate import validate_contract  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REPOS_DIR = ROOT / "repos"

PINNED_MODE = "pinned"
DETACHED_MODE = "detached"
DEFAULT_MODE = PINNED_MODE

#: Registry keys that only a detached bundle may declare, because a pinned
#: bundle's product-side `.agentic/harness.yaml` already owns them.
DETACHED_ONLY_FIELDS = ("capabilities", "clients")


@dataclass(frozen=True)
class DetachedBundle:
    """Resolved contract for a bundle whose registry entry *is* the contract.

    `capabilities` and `clients` distinguish **absent** (`None` — the entry
    states no opinion) from **declared empty** (`()` — an explicit empty list,
    meaning reference-only for `clients`). Issue #172 needs exactly that
    distinction, so it is preserved here rather than normalized away.
    """

    bundle: str
    version: str
    manifest_path: Path
    profile: str | None = None
    capabilities: tuple[str, ...] | None = None
    clients: tuple[str, ...] | None = None


def manifest_mode(data: dict) -> str:
    """Return the declared harness mode, defaulting to `pinned`."""
    harness = data.get("harness")
    if not isinstance(harness, dict):
        return DEFAULT_MODE
    mode = harness.get("mode", DEFAULT_MODE)
    return mode if isinstance(mode, str) else DEFAULT_MODE


def _as_str_tuple(value: object) -> tuple[str, ...] | None:
    if not isinstance(value, list):
        return None
    return tuple(item for item in value if isinstance(item, str))


def resolve_detached_bundle(bundle: str, repos_dir: Path | None = None) -> DetachedBundle | None:
    """Return the detached contract for `bundle`, or `None`.

    `None` covers every "no detached opinion" case uniformly, so a caller
    never has to distinguish them or handle a raw exception: the manifest is
    absent, unreadable, not valid YAML, not a mapping, PyYAML is
    unavailable, the bundle is pinned (the default), or it claims
    `harness.mode: detached` without the `harness.version` that
    `scripts/validate-manifests.py` requires of a detached entry.
    """
    if yaml is None:
        return None
    directory = REPOS_DIR if repos_dir is None else repos_dir
    manifest_path = directory / f"{bundle}.yaml"
    if not manifest_path.is_file():
        return None
    try:
        data = yaml.safe_load(manifest_path.read_text())
    except (OSError, yaml.YAMLError) as exc:
        print(f"WARN: cannot read {manifest_path}: {exc}", file=sys.stderr)
        return None
    if not isinstance(data, dict):
        return None
    if manifest_mode(data) != DETACHED_MODE:
        return None
    harness = data.get("harness") or {}
    version = harness.get("version")
    if not isinstance(version, str) or not version.strip():
        return None
    profile = harness.get("profile")
    return DetachedBundle(
        bundle=bundle,
        version=version,
        manifest_path=manifest_path,
        profile=profile if isinstance(profile, str) else None,
        capabilities=_as_str_tuple(data.get("capabilities")),
        clients=_as_str_tuple(data.get("clients")),
    )


# --- Four-layer config resolver (issue #327) --------------------------------
#
# Precedence, lowest to highest: plugin per-platform defaults ->
# `~/.claude/rgh-mms.json` (operator-local, keyed per bundle) -> committed
# `<target>/.claude/rgh-mms.json` -> uncommitted `<target>/.claude/
# rgh-mms.local.json`. Replaces the three prose "Resolution order" variants
# in `repos/README.md` with one deterministic, invocable resolver. Hard
# cutover (2026-08-19 OWNER decision, issue #327): this resolver never falls
# back to `repos/<bundle>.yaml` / a product's `.agentic/harness.yaml` when
# the new layers are empty -- a bundle not yet onboarded through #339's
# onboarding flow simply resolves with no bundle-specific opinion beyond the
# platform defaults (see `configured` below), not a silent read of the
# legacy registry.

RGH_MMS_CONFIG_SCHEMA_PATH = ROOT / "schemas" / "rgh-mms-config.schema.json"
PLATFORM_DEFAULTS_DIR = ROOT / "platform-defaults"
DEFAULT_USER_CONFIG_PATH = Path.home() / ".claude" / "rgh-mms.json"
COMMITTED_CONFIG_RELATIVE = Path(".claude") / "rgh-mms.json"
LOCAL_CONFIG_RELATIVE = Path(".claude") / "rgh-mms.local.json"
DEFAULT_PLATFORM = "github"
KNOWN_PLATFORMS = ("github", "ado", "bitbucket")


class ConfigSchemaError(ValueError):
    """A present layer file fails validation against
    `schemas/rgh-mms-config.schema.json`, or is present but unreadable /
    unparsable / not a JSON object at its top level.

    Deliberately diverges from `resolve_detached_bundle`'s "no opinion ->
    `None`" convention above: a *missing* layer file is silently absent
    (contributes nothing), but a *present, malformed* one is a defect the
    operator or committer needs to fix, not a condition to degrade past
    quietly (issue #327 AC2: "resolver validates input files against it and
    fails loudly on schema violations"). Callers print `str(exc)` to stderr
    and exit non-zero.
    """


_CONFIG_SCHEMA_CACHE: dict | None = None


def _load_config_schema() -> dict:
    global _CONFIG_SCHEMA_CACHE
    if _CONFIG_SCHEMA_CACHE is None:
        _CONFIG_SCHEMA_CACHE = json.loads(RGH_MMS_CONFIG_SCHEMA_PATH.read_text(encoding="utf-8"))
    return _CONFIG_SCHEMA_CACHE


def _validate_fragment(data: dict, *, label: str) -> None:
    errors = validate_contract(data, _load_config_schema(), label)
    if errors:
        detail = "\n  - ".join(errors)
        raise ConfigSchemaError(f"{label} failed schema validation:\n  - {detail}")


def _deep_merge(base: dict, override: dict) -> dict:
    """Recursive merge: `override` wins per-key; nested dicts merge, not replace."""
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _load_json_object(path: Path, *, label: str) -> dict:
    """Return the parsed JSON object at `path`, or `{}` if `path` is absent.

    A *present* file that cannot be read, is not valid JSON, or does not
    parse to a JSON object at the top level raises `ConfigSchemaError`
    rather than degrading to `{}` -- see that class's docstring.
    """
    if not path.is_file():
        return {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigSchemaError(f"{label}: cannot read {path}: {exc}") from exc
    try:
        data = json.loads(text) if text.strip() else {}
    except json.JSONDecodeError as exc:
        raise ConfigSchemaError(f"{label}: {path} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigSchemaError(f"{label}: {path} must contain a JSON object at the top level")
    return data


def _load_validated_fragment(path: Path, *, label: str) -> dict:
    fragment = _load_json_object(path, label=label)
    if fragment:
        _validate_fragment(fragment, label=label)
    return fragment


def _load_user_config_fragment(bundle: str, user_config_path: Path) -> dict:
    """Extract and validate bundle's entry from the `~/.claude/rgh-mms.json`
    layer, shaped `{"bundles": {"<bundle-id>": {...fragment...}, ...}}`
    (keyed per bundle, per issue #327's AC1) -- unlike the committed/local
    layers below, which are already scoped to a single repo/bundle and so
    carry the fragment directly with no wrapper key.
    """
    label = str(user_config_path)
    data = _load_json_object(user_config_path, label=label)
    if not data:
        return {}
    bundles = data.get("bundles")
    if bundles is None:
        return {}
    if not isinstance(bundles, dict):
        raise ConfigSchemaError(f"{label}: 'bundles' must be a JSON object")
    fragment = bundles.get(bundle)
    if fragment is None:
        return {}
    if not isinstance(fragment, dict):
        raise ConfigSchemaError(f"{label}: bundles.{bundle} must be a JSON object")
    _validate_fragment(fragment, label=f"{label}#bundles.{bundle}")
    return fragment


def resolve_bundle_config(
    bundle: str,
    *,
    target_root: Path,
    platform: str | None = None,
    user_config_path: Path | None = None,
    plugin_defaults_dir: Path | None = None,
) -> dict:
    """Resolve `bundle`'s merged config across the four layers (issue #327).

    Precedence, lowest to highest:

    1. Plugin per-platform defaults -- `<plugin_defaults_dir>/<platform>.json`
       (default `PLATFORM_DEFAULTS_DIR`, i.e. `platform-defaults/` alongside
       this script's own root -- resolves correctly whether this module runs
       from the canonical rgh-mms checkout or from a packaged plugin tree,
       same `Path(__file__).resolve().parents[1]` trick `REPOS_DIR` above
       uses).
    2. `~/.claude/rgh-mms.json` (default `DEFAULT_USER_CONFIG_PATH`) --
       operator-local, keyed per bundle under a `bundles` map.
    3. `<target_root>/.claude/rgh-mms.json` -- committed in-repo settings,
       present only for a bundle that has opted in.
    4. `<target_root>/.claude/rgh-mms.local.json` -- uncommitted per-clone
       override, the successor to detached mode's `.git/info/exclude`
       bookkeeping (see `repos/README.md`).

    Every present layer file is independently validated against
    `schemas/rgh-mms-config.schema.json` (`ConfigSchemaError` on violation,
    propagated uncaught -- callers decide how to report it). Merging is a
    recursive per-key overlay (`_deep_merge`): a later layer's nested object
    only overrides the keys it actually sets, never the whole parent object.

    `platform` selects which per-platform defaults file layer 1 loads. When
    omitted, it is read from the deep-merged layers 2-4 (`platform` key),
    defaulting to `DEFAULT_PLATFORM` ("github") when none of them declare
    one either -- resolving platform's own defaults needs to know platform,
    which only the higher-precedence layers can declare, hence the
    two-pass shape: merge 2-4 first, pick platform, then prepend layer 1.

    The returned dict always carries `bundle` and `platform`, plus a
    resolver-computed `configured` flag: `True` when at least one of layers
    2-4 contributed any key for this bundle, `False` when nothing beyond the
    platform defaults applies. `configured` is not part of the schema (it
    describes the *resolution*, not a layer's content) -- callers use it the
    way `repos/<bundle>.yaml` `status: stub` used to gate a not-yet-onboarded
    bundle, since the new layers have no direct equivalent of that field
    (hard cutover, issue #327: an unmigrated bundle like this repo's own
    `rgh-mms` resolves with `configured: False` until #339/#331 land, not a
    silent read of the legacy registry).
    """
    user_path = user_config_path if user_config_path is not None else DEFAULT_USER_CONFIG_PATH
    defaults_dir = plugin_defaults_dir if plugin_defaults_dir is not None else PLATFORM_DEFAULTS_DIR

    user_fragment = _load_user_config_fragment(bundle, user_path)
    committed_fragment = _load_validated_fragment(
        target_root / COMMITTED_CONFIG_RELATIVE, label=str(target_root / COMMITTED_CONFIG_RELATIVE)
    )
    local_fragment = _load_validated_fragment(
        target_root / LOCAL_CONFIG_RELATIVE, label=str(target_root / LOCAL_CONFIG_RELATIVE)
    )

    overrides = _deep_merge(_deep_merge(user_fragment, committed_fragment), local_fragment)
    configured = bool(overrides)
    resolved_platform = platform or overrides.get("platform") or DEFAULT_PLATFORM

    defaults_path = defaults_dir / f"{resolved_platform}.json"
    plugin_defaults = _load_validated_fragment(
        defaults_path, label=f"platform-defaults/{resolved_platform}.json"
    )

    merged = _deep_merge(plugin_defaults, overrides)
    merged["bundle"] = bundle
    merged["platform"] = resolved_platform
    merged["configured"] = configured
    return merged


def _cli_resolve(args: argparse.Namespace) -> int:
    try:
        resolved = resolve_bundle_config(
            args.bundle,
            target_root=args.root,
            platform=args.platform,
            user_config_path=args.user_config,
        )
    except ConfigSchemaError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(resolved, indent=2, sort_keys=True))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Resolve the layered rgh-mms bundle config (issue #327)."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    resolve_parser = sub.add_parser(
        "resolve", help="Resolve and print the merged config for a bundle as JSON"
    )
    resolve_parser.add_argument("--bundle", required=True, help="Bundle id to resolve")
    resolve_parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Target repo root, for the committed/local config layers (default: cwd)",
    )
    resolve_parser.add_argument(
        "--platform",
        choices=KNOWN_PLATFORMS,
        default=None,
        help="Force which platform-defaults layer to use "
        "(default: read from resolved layers, else github)",
    )
    resolve_parser.add_argument(
        "--user-config",
        type=Path,
        default=None,
        help="Override ~/.claude/rgh-mms.json path (testing/advanced use)",
    )

    args = parser.parse_args(argv)
    if args.command == "resolve":
        return _cli_resolve(args)
    parser.error(f"unknown command {args.command!r}")
    return 2  # pragma: no cover - argparse.error already raises SystemExit


if __name__ == "__main__":
    raise SystemExit(main())
