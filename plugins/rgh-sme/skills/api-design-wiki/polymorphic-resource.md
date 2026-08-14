---
type: concept
title: Polymorphic Resource
description: >
  One resource type whose wire shape varies by an explicit type field, letting
  standard methods apply uniformly across subtypes without duplicating endpoints.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 16"
---

A **polymorphic resource** exposes a generic interface (for example `Message`)
plus an explicit **type** field naming the concrete subtype (`text`, `photo`,
`video`). Standard and custom methods on that resource behave polymorphically
without method-level branching — a `CountShapeSides` custom method on `Shape`
returns 3 for triangles and 4 for squares from field values alone.

**When to unify:** ask whether [standard methods](standard-method-contract.md)
behave identically across subtypes and whether clients must **list mixed subtypes
in one response** — chat messages interleaved by time need one `Message` resource;
a `Broadcast` that differs in membership and directionality should stay separate
even if it superficially resembles `ChatRoom`.

**Type field:** use a plain [string instead of enumeration](string-instead-of-enumeration.md)
with server-side validation of allowed values — easier evolution and pairs with
[list filter](list-filter.md) (`type = "text"`). Changing a resource's type after
creation is technically possible but **discouraged** — dependents may assume the
original type.

**Data shape** (in increasing field reuse):

1. Superset of optional dedicated fields per type (`text?`, `photoUri?`, …).
2. One reused field whose meaning depends on `type` (for example `content`).
3. A union-typed field (for example `content: string | Media`) when subtypes need
   structured payloads.

Abstract only as far as it stays practical — `Message` can share `content`; `Shape`
should use a `dimension` union (`SquareDimension`, `CircleDimension`, …) because
field names carry meaning (`length` vs `radius` vs `base`/`height`).

**Validation:** rules differ by `type` — `content` must be arbitrary text for
`text` but a valid URI for `photo`. For irrelevant but well-formed extra fields
(square with both `radius` and `length`), validate required fields for the given
type and **silently discard** irrelevant input, consistent with
[field mask unknown path tolerance](field-mask-unknown-path-tolerance.md).

Trade-off: unifying too eagerly locks representation and complicates later
[backward compatibility](backward-compatibility-policy.md). Prefer polymorphic
resources over [polymorphic method anti-pattern](polymorphic-method-anti-pattern.md)
when behavior may diverge across types over time.
