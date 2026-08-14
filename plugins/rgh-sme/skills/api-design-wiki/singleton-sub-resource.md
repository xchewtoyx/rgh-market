---
type: concept
title: Singleton Sub-Resource
description: >
  A per-parent child endpoint with exactly one instance, split out for size,
  security, or update volatility while keeping get and update semantics.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 12"
---

A **singleton sub-resource** moves a conceptually inherent component off the
parent into an isolated child with a fixed sub-path (`drivers/1/location`) when
inline fields are impractical:

- **Size/complexity** — ACLs, binary payloads (S3 metadata vs data RPC)
- **Security** — sensitive slice with different access than the parent
- **Volatility** — frequently updated slice (driver location vs license plate)
  causing write contention on the parent

**Standard methods:**

| Method | Behavior |
| --- | --- |
| Get | Like a separate resource — own id under parent |
| Update | Partial update like any resource |
| Create | **Not supported** — exists when parent exists (property semantics) |
| Delete | **Not supported** — cascades when parent deletes |
| List | n/a — exactly one instance |

Cannot atomically create parent and initialize singleton data in one call —
isolation is intentional. Provide sensible defaults at parent creation; add a
**reset** [custom method](custom-method.md) restoring creation-time defaults.

**Hierarchy rules:** must have a **full resource** parent (not another singleton);
never at API root (global singleton = global lock). During parent
[soft deletion](soft-deletion.md) or delete [long-running operation](long-running-operation.md),
sub-resource persists until parent removal completes.

**Trade-off:** loses atomic parent+child updates — acceptable when size, security,
or volatility motivated the split. Contrast inline grouping in
[map field bounds and defaults](map-field-bounds-and-defaults.md) and
[resource hierarchy vs cross-reference](resource-hierarchy-vs-cross-reference.md).

Idempotent safe reads may use GET on the sub-path; mutating work stays POST on
[custom methods](custom-method.md) when not a simple update.
