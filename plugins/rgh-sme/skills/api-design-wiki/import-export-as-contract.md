---
type: concept
title: Import and Export as Contract
description: >
  Custom methods that move bulk data directly between an API and external storage,
  with separate transport and serialization config, distinct from backup/restore.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 23"
---

**Import** and **export** [custom methods](custom-method.md) move bulk data
**directly between the API and remote storage**, bypassing an application server
that would otherwise read bytes, parse resources, and call standard or
[batch operations](batch-operations.md). They return
[long-running operations](long-running-operation.md) when work is slow:

```text
POST /{parent=chatRooms/*}/messages:export
POST /{parent=chatRooms/*}/messages:import
```

Import is not limited to collections — for example `ImportTrainingData` into a
single `VirtualAssistant` resource. When [resource revision](resource-revision.md)
would need hierarchy-aware snapshots, export can still capture one resource type
at a time with clearer scope than inline revision storage.

## Not backup or restore

Export reads a collection over nonzero time without exclusive locks. Unless the
storage layer offers snapshots, the result is a **smear** — resources that never
coexisted at one instant. Backup implies a consistent snapshot with full identity
metadata; export is ordinary retrieval routed to external storage. Import/export
**ignore user-specified ids on import** when the API does not support client-chosen
ids (the general recommendation in [resource identifier](resource-identifier.md)) —
equivalent to [batch create](batch-operations.md) on parsed rows. Re-importing the
same file can duplicate resources by design.

Restrict import/export to **one resource type** with **no children** — leaf
resources useful on their own (messages under a chat room), not whole parent graphs.
Multi-type or nested export shifts intent toward backup/restore and different
guarantees.

## Configuration separation

Two orthogonal concerns:

1. **Transport** — generic `DataSource` (import) and `DataDestination` (export)
   interfaces: which storage system and how to connect.
2. **Transformation** — per-resource `InputConfig` / `OutputConfig`: serialization
   (newline-delimited JSON, CSV, TSV), compression, encryption, file splitting.

Keep source and destination interfaces **separate** even when fields overlap (S3
glob on read versus prefix on write) so each can evolve independently. Use a
`type` discriminator with per-system extensions (for example `S3DataSource`) —
not one flat schema with ambiguous required fields.

## Filtering

**Export:** support a [list filter](list-filter.md) on the export request (not
inside `OutputConfig`) — selection happens before byte conversion, like list.

**Import:** do **not** support filtering incoming bytes; that would require full
deserialize plus business logic on fields that may not exist until create (for
example `createTime`). Users filter or transform files before import.

## Failures and deduplication

**Export** failures are generally safe to retry; each attempt is independent and
consistency is already best-effort. Leave partial exports in place — the API may
lack delete permission on external storage by design.

**Import** retries risk duplicates after partial success. Prefer a per-record
**importRequestId** cached server-side (ties to
[request deduplication and idempotency keys](request-deduplication-and-idempotency-keys.md));
optionally inject ids during export via `OutputConfig` for safe re-import. Validation
failures belong in the LRO result, not silent retry.

Distinct from casual [request bundles](request-bundle.md) on single entities.
