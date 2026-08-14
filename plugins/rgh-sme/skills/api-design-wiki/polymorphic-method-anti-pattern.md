---
type: concept
title: Polymorphic Method Anti-Pattern
description: >
  A single custom method operating across unrelated resource types trades short-term
  convenience for lost per-type evolution flexibility.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 16"
---

A **polymorphic method** applies one operation signature across multiple distinct
resource types — for example `DeleteResource()` on a `"*/*"` URL pattern instead
of per-collection deletes. Deletion may appear type-agnostic, but resources differ
in [soft deletion](soft-deletion.md), [validate-only request](validate-only-request.md)
support, and side-effect rules.

Problems:

- Shared name and signature do not imply identical or permanently identical
  behavior across types.
- Assumes all targeted resources will evolve uniformly — rarely true as APIs age.
- Locks future divergence: one type needing different delete semantics forces a
  breaking change or awkward exceptions.

Prefer per-resource [standard method contract](standard-method-contract.md) or
[custom method](custom-method.md) endpoints. Use [polymorphic resource](polymorphic-resource.md)
when subtypes truly share one interface; do not generalize methods across unrelated
collections to save typing today.
