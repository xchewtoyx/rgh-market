---
type: concept
title: Copy and Move Custom Methods
description: >
  POST custom methods that duplicate or relocate resources when identifiers and
  parents are otherwise immutable under standard update.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 17"
---

[Resource identifiers](resource-identifier.md) and hierarchy are treated as
fixed under standard update — yet users misplace resources, need duplicates, or
must rename or reparent. **Copy** and **move** are [custom methods](custom-method.md)
on the source resource, POST-bound, returning the new or relocated resource:

```text
POST /{id=chatRooms/*/messages/*}:move
POST /{id=chatRooms/*}:copy
```

## Identifiers

Follow create's id policy: if clients cannot choose ids on create, copy must not
become a loophole (create elsewhere, copy with chosen id). Copy accepts source
`id`, optional `destinationId` when user ids are supported, and `destinationParent`
(may equal the source parent). Blank `destinationId` means server-generated.
Taken destination id → **409 Conflict**, not silent fallback.

**Move** combines reparenting and rename via one `destinationId` (full new path
when user ids exist; parent segment changes when reparenting). Top-level
resources with server-only ids cannot move — omit move entirely.

## Children, references, and external data

Copy and move **include child resources** by default, rewriting child ids under
the new parent — otherwise behavior diverges from the source unpredictably.

**Move:** update referential fields on non-child resources that point at moved
ids (cascade like relational FK updates) — complex and a reason to avoid move
unless necessary.

**Copy:** whether to duplicate related non-child resources is a product decision
(for example share one review report across two messages vs duplicate members).

External URIs and off-API links cannot stay consistent — do not promise lifetime
for internet-wide references.

For blob-backed resources: **move** relocates metadata only; **copy** prefers
**copy-on-write** (reference first, split bytes on first diverging write).

## Inherited metadata

When destination parent policy conflicts with copied/moved data (message length
vs room cap), **reject the whole operation** with a clear error — do not leave
violating resources or silently truncate.

## Atomicity

Prefer storage snapshots or transactions so copy reflects a consistent source
view; without that, accept a time **smear** like [import and export as contract](import-export-as-contract.md).
Global write locks during copy are a DoS vector — avoid.

Move risks **clobbering concurrent updates** to reference rows if not transactional;
"ignore inconsistency" is worse than for copy. Favor copy when duplication is the
real need; need to move often signals bad hierarchy or
[hierarchical resource identifier](hierarchical-resource-identifier.md) choices.
