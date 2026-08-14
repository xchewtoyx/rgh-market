---
type: concept
title: Field Mask
description: >
  A dotted-path list selecting which resource fields to return on get or apply on
  update, minimizing transfer without becoming a general query language.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 8"
---

A **field mask** names which fields participate in partial retrieval or partial
update — a collection of string paths on the resource.

**Motivation:** standard get returns whole resources; standard replace requires
whole bodies — wasteful for large resources and risky when clients hold stale
schemas (replace nulls out fields the client never knew existed). Field masks
enable fine-grained read and write intent.

## Transport

Field masks cannot live in GET bodies (often stripped) or inside PATCH bodies
(the body must remain pure resource representation). Use **query parameters**,
repeating the same name: `?fieldMask=title&fieldMask=description` — not comma-
separated lists (commas collide with dotted paths and map keys). Both get and
update request types carry `fieldMask: string[]`.

## Path syntax

Rules for nested static fields and dynamic maps:

1. Dot (`.`) separates path segments.
2. Asterisk (`*`) selects all fields of a nested message or all map entries.
3. Map keys are strings.
4. Keys that are not bare literals (numeric-looking, containing `.` or `*`) are
   quoted in backticks.
5. A literal backtick in a key is escaped as two backticks.

Examples on `ChatRoom`: `"loggingConfig.maxSizeMb"`, `"loggingConfig.*"`,
`` "settings.`1234`" ``, `` "settings.`test.value`" `` (key with embedded dot),
`"settings.test.value"` (true nesting into sub-object at key `test`).

## Repeated fields

Do **not** address array items by numeric index — indices shift on reorder.
For retrieval, `"administrators.*.name"` selects `name` from every element.
For update, repeated fields must be replaced **wholly** — partial per-index
update is unsafe without stable ordering guarantees. Prefer map fields with stable
keys or sub-resource collections when per-item addressing is needed.

## Defaults

**Standard get:** unset mask returns the complete field set. Exception: exceptionally
large fields may be excluded by default but require explicit opt-in — document each.
Use `"*"` to force every field including excluded or newly added ones.

**Standard update:** defaulting to all fields would equal replace — updates use
[implicit field mask inference](implicit-field-mask-inference.md) from the body when
no explicit mask is sent.

Unknown paths are tolerated — see
[field mask unknown path tolerance](field-mask-unknown-path-tolerance.md).

Field masks minimize transfer; they are **not** a join/query layer. Rich relational
reads belong in purpose-built APIs, not standard get. If partial retrieval is adopted,
apply it **consistently** across resources.

See [partial update alternatives](partial-update-alternatives.md) for JSON Patch
comparisons.
