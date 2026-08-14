---
type: concept
title: Map Field Bounds and Defaults
description: >
  Rules for predefined struct grouping versus dynamic string-key maps,
  including UTF-8 key normalization, size bounds, and null-vs-empty semantics.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

Two keyed shapes appear on the wire:

**Predefined schema grouping** — related fields grouped into a nested object
(for example `securityConfig: SecurityConfig` on a chat room). Use when fields
are thematically related. If fields are meaningful independently of the parent,
consider a [singleton sub-resource](singleton-sub-resource.md) instead.

**Dynamic string-key map** — arbitrary keys per instance (for example
`ingredientAmounts: Map<string,string>` on a grocery item). Use when enumerating
every possible key in schema is impractical.

Map keys should be **strings**, UTF-8, Unicode Normalization Form C — keys act
as identifiers; numeric keys inherit precision issues.

**Bounds:** predefined structs need no field-count cap (schema is the boundary).
Dynamic maps need max key count plus key size (~100 chars) and value size (~500
chars) limits; optionally cap total characters across the map when value sizes
vary wildly — discouraged except when necessary.

**Defaults:** `{}` vs `null` is distinguishable — `null` means "provider picks
best default"; `{}` means explicitly empty. Unlike [atomic list fields](atomic-list-field.md),
empty maps can carry intentional meaning alongside null defaults.

See [missing versus null policy](missing-versus-null-policy.md) for broader
default conventions.
