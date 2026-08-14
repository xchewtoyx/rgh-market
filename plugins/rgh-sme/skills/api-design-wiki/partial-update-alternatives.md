---
type: concept
title: Partial Update Alternatives
description: >
  JSON Patch and JSON Merge Patch as richer or simpler alternatives to explicit
  field masks for partial document mutation.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 8"
---

Besides [field masks](field-mask.md), two RFC-standard partial-update styles
appear in practice:

**JSON Patch (RFC 6902)** — sequential operations (test, copy, move, add,
remove) applied to a document. Supports copying between fields without a prior
read and indexed array edits with `test` preconditions. Richer than masks; more
complex for clients to author.

**JSON Merge Patch (RFC 7396)** — closer to implicit field-mask semantics: infer
updates from a partial document. Inherits the same null-vs-absent ambiguity for
dynamic structures ([field mask map key removal](field-mask-map-key-removal.md)).
Recurses into nested objects but **not** into arrays, which surprises consumers
with list-shaped fields ([atomic list fields](atomic-list-field.md) should stay
wholly replaced anyway).

Field masks stay simple to learn yet precise enough for most API partial
retrieval and update needs; choose Patch variants when operation lists or
cross-field copies justify the complexity.
