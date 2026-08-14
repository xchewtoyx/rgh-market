---
type: concept
title: Cross-Reference Field
description: >
  A string identifier field on one resource pointing at another, decoupled from
  the target's lifetime and validated only by client convention.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 13"
---

Resources reference each other with **cross-reference fields** — string
[resource identifiers](resource-identifier.md) (or URIs for external targets).
The field **name** conveys type and role (`authorId` on `Book`); the value is
just an id string.

**Dynamic targets:** when the referenced type varies, add a separate `targetType`
field alongside `targetId` (for example `api.example.com/Author` vs `Book`).

References are fully decoupled — no automatic lifecycle coupling. Consumers must
handle stale or dangling pointers after delete.

## Deletion semantics

When the referenced resource is deleted:

1. **Prohibit delete** while dependents exist — can deadlock on mutual references.
2. **Reset to zero value** — may require mass updates at scale.
3. **Allow dangling pointers** (recommended) — consistent, atomic deletes without
   side effects; clients validate references before use.

Option 3 aligns with [standard method contract](standard-method-contract.md) delete
rules and large fan-out realities.

## Reference vs inline value

Inlining the full related resource (pass-by-value) avoids a second get but bloats
responses, raises update ambiguity (change author via `UpdateBook` or `UpdateAuthor?`),
and risks stale embedded copies unless joined every read. Prefer references; clients
assemble graphs via multiple gets, [request bundle](request-bundle.md), or client-side
query layers.

Contrast [resource hierarchy vs cross-reference](resource-hierarchy-vs-cross-reference.md)
(path ownership vs field association) and [embedded entity vs linked information
holder](embedded-entity-vs-linked-information-holder.md) (message design, not just
foreign keys).

Fields holding copied foreign data omit the `Id` suffix; id-only pointers use it.
