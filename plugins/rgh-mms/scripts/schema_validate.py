#!/usr/bin/env python3
"""Shared hand-rolled JSON-Schema-subset validator primitives (issue #208).

Extracted from `scripts/validate-manifests.py`'s original `_check_required`,
`_check_closed`, and `_check_item_enum` so `scripts/generate-adapters.py`
(`validate_contract`, below) can validate `.agentic/harness.yaml` contracts
against `schemas/harness-contract.schema.json` without duplicating the
validation logic. `validate-manifests.py` now imports and calls these
functions instead of defining its own copies; its own behavior against
`schemas/repo-registry.schema.json` is unchanged (see
`tests/test_validate_manifests.py`).

This module intentionally implements only the small subset of JSON Schema
draft 2020-12 actually used by the two schemas in this repo: `type`,
`required`, `additionalProperties: false` closure (recursed through nested
`object`-typed subschemas only), `pattern`, `enum` (including `items.enum`
for scalar array members), and `const`. It is not a general validator and
does not attempt to be one.

`const` has no analog in `schemas/repo-registry.schema.json` today; it was
added here for `schemas/harness-contract.schema.json`'s
`schema_version: {"type": "integer", "const": 1}`, which issue #91-era code
parsed but never checked (a dead field until issue #208 read it).
"""

from __future__ import annotations

import re


def check_item_enum(values: list, subschema: dict, path: str) -> list[str]:
    """Validate `items.enum` for an array of scalars, reporting `path[index]`.

    Partial answer to open question 2 of
    `.agent-metrics/contracts/0019_validate_manifests_additionalproperties.md`,
    which deferred array-item traversal for want of an index-aware path
    convention: this establishes that convention for scalar enum members
    only. Object *closure* recursion into array items (`runtime_agents.items`)
    stays out of scope, so the gap 0019 documented is narrowed, not closed.

    Added for `capabilities` / `clients` (issue #175), whose members feed
    real behavior, so a typo must fail rather than pass silently.
    """
    item_schema = subschema.get("items")
    if not isinstance(item_schema, dict):
        return []
    item_enum = item_schema.get("enum")
    if not item_enum:
        return []
    return [
        f"{path}[{index}]: must be one of {item_enum}"
        for index, item in enumerate(values)
        if item not in item_enum
    ]


def _check_properties(
    obj: dict, schema: dict, path: str, errors: list[str], *, enforce_required: bool
) -> None:
    """Shared per-level walk behind `check_required` and `check_constraints`.

    `enforce_required=True` reproduces `validate-manifests.py`'s original
    `_check_required` byte for byte (required-field check at this level,
    then type/pattern/enum/const checks, recursing with the same flag).
    `enforce_required=False` runs only the type/pattern/enum/const checks —
    used for contract validation (`validate_contract`), which must not
    newly require any field beyond what
    `policy/mission-boundaries.md` already treats as required (the harness
    version pin): "Nothing beyond the harness version pin is ever
    schema-required of a product repo." Skipping `required` here means an
    otherwise-valid contract that omits an optional block (e.g. no
    `harness:` at all, common in reference-only test fixtures) is not
    penalized for it — only fields the contract *does* declare get
    correctness-checked.
    """
    if enforce_required:
        for key in schema.get("required", []):
            if key not in obj:
                errors.append(f"{path}: missing required field '{key}'")
    props = schema.get("properties", {})
    for key, subschema in props.items():
        if key not in obj:
            continue
        val = obj[key]
        expected = subschema.get("type")
        if expected == "object" and isinstance(val, dict):
            _check_properties(
                val,
                subschema,
                f"{path}.{key}" if path else key,
                errors,
                enforce_required=enforce_required,
            )
        elif expected == "string" and not isinstance(val, str):
            errors.append(f"{path}.{key}: expected string")
        elif expected == "boolean" and not isinstance(val, bool):
            errors.append(f"{path}.{key}: expected boolean")
        elif expected == "array":
            if not isinstance(val, list):
                errors.append(f"{path}.{key}: expected array")
            else:
                errors.extend(check_item_enum(val, subschema, f"{path}.{key}" if path else key))
        pattern = subschema.get("pattern")
        if pattern and isinstance(val, str):
            if not re.fullmatch(pattern, val):
                errors.append(f"{path}.{key}: does not match pattern {pattern}")
        enum = subschema.get("enum")
        if enum and val not in enum:
            errors.append(f"{path}.{key}: must be one of {enum}")
        if "const" in subschema and val != subschema["const"]:
            errors.append(f"{path}.{key}: must equal {subschema['const']!r} (got {val!r})")


def check_required(obj: dict, schema: dict, path: str = "") -> list[str]:
    """Required-field + type/pattern/enum/const checks, recursed through
    nested objects. This is `validate-manifests.py`'s original
    `_check_required`, unchanged in behavior for `schemas/repo-
    registry.schema.json` (which declares no `const` keys, so the new
    `const` check never fires there)."""
    errors: list[str] = []
    _check_properties(obj, schema, path, errors, enforce_required=True)
    return errors


def check_constraints(obj: dict, schema: dict, path: str = "") -> list[str]:
    """Type/pattern/enum/const checks only — never `required` — recursed
    through nested objects. See `_check_properties`'s docstring for why
    contract validation (`validate_contract`) uses this instead of
    `check_required`."""
    errors: list[str] = []
    _check_properties(obj, schema, path, errors, enforce_required=False)
    return errors


def check_closed(obj: dict, schema: dict, path: str, errors: list[str]) -> None:
    """Enforce `additionalProperties: false` recursively wherever declared.

    Recurses only into `object`-typed subschemas reachable through
    `properties`, mirroring `check_required`'s traversal and dotted-path
    convention (`f"{path}.{key}"`). Array-item schemas (e.g.
    `runtime_agents.items`) are deliberately not recursed into: no manifest
    field currently reads array items closure, and closing the loop there
    would need its own index-aware path convention (`runtime_agents[0].foo`)
    that no other check in this module uses yet. See
    `.agent-metrics/contracts/0019_validate_manifests_additionalproperties.md`
    open question 2.
    """
    if not isinstance(obj, dict) or not isinstance(schema, dict):
        return
    props = schema.get("properties", {})
    if schema.get("additionalProperties") is False:
        for key in obj:
            if key not in props:
                errors.append(f"{path}.{key}: not declared in schema (additionalProperties: false)")
    for key, subschema in props.items():
        if key not in obj:
            continue
        val = obj[key]
        if subschema.get("type") == "object" and isinstance(val, dict):
            check_closed(val, subschema, f"{path}.{key}" if path else key, errors)


def validate_contract(data: dict, schema: dict, label: str = "contract") -> list[str]:
    """Validate a parsed `.agentic/harness.yaml` mapping against `schema`
    (`schemas/harness-contract.schema.json`) (issue #208).

    Returns a list of human-readable error strings, each naming the
    offending field via a dotted path rooted at `label`; an empty list means
    the contract is schema-valid. Checks unknown top-level/nested keys
    (`check_closed`) and type/pattern/enum/`const` correctness
    (`check_constraints`) — deliberately **not** `required`-field
    enforcement (see `_check_properties`'s docstring). `data` must already
    be a parsed mapping: `generate-adapters.py::load_contract` keeps the
    unreadable/unparsable-YAML/non-mapping degrade-to-`None` path entirely
    separate from this function, which only ever sees an already-valid
    mapping.
    """
    errors: list[str] = list(check_constraints(data, schema, label))
    check_closed(data, schema, label, errors)
    return errors
