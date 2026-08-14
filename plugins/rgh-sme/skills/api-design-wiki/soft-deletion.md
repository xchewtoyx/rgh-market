---
type: concept
title: Soft Deletion
description: >
  Repurposing standard delete to mark resources deleted while keeping them
  recoverable, with list filtering and output-only deleted flags.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 25"
---

**Soft deletion** is the API analogue of a recycle bin: mark a resource deleted
and hide it from normal views while keeping it recoverable — protecting against
accidental bulk deletes at scale.

**Deleted designation:**

- **Boolean `deleted`** (preferred default) — output only; standard update and
  field masks must **silently ignore** attempts to set it. Only standard delete
  (`false`→`true`) and [undelete custom method](undelete-custom-method.md)
  (`true`→`false`) change it.
- **State enum** — if the resource already has a life-cycle state machine, a
  `deleted` state is possible but undelete target state is ambiguous. Prefer
  keeping normal life-cycle state **and** an orthogonal `deleted` boolean.

**Standard method changes:**

- **Get** — returns the resource even when soft-deleted (no 404). Callers with
  a specific id may be checking deletion status.
- **List** — excludes soft-deleted by default; add `includeDeleted?: boolean`
  to opt in. Keep separate from `filter` — `includeDeleted` **enlarges** the
  candidate set; `filter` **narrows** it. To list only deleted items:
  `includeDeleted: true` plus `filter: "deleted: true"`.
- **Delete** — marks deleted and **returns the modified resource** (not void).
  Delete on an already-soft-deleted resource → error (412 Precondition Failed)
  — preserves whether *this request* caused deletion vs resource already deleted.

**Expiration:** optional `expireTime` set at soft-delete per policy (for example
+30 days); reset on undelete. Fixed at delete time so policy changes affect
only newly deleted resources. Purge when `deleted && expireTime <= now`.

**Referential integrity:** apply the same rules as hard delete (restrict, cascade,
ignore) even though references still resolve — simplifies restore vs special-casing
the soft-deleted window.

**Versioning:** retrofitting soft delete is a [backward compatibility](backward-compatibility-policy.md)
judgment — short expiration on non-critical data may be acceptable; indefinite
retention or regulated exact-delete requirements may force a major bump or skip
soft delete entirely.

Batch delete inherits soft-delete behavior; add batch expunge when bulk permanent
removal is needed. See [expunge custom method](expunge-custom-method.md) for
hard removal and regulatory trade-offs.

[Master data holders](master-data-holder.md) favor soft delete when inbound
references exist. Evolution-safe when clients must not reuse
[resource identifiers](resource-identifier.md).
