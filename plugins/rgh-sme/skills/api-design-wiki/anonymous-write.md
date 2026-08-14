---
type: concept
title: Anonymous Write
description: >
  A collection-scoped custom write method that ingests non-addressable entries
  for aggregate-only access instead of creating individually retrievable resources.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 20"
---

Not every datum fits the [standard method contract](standard-method-contract.md):
analytical time-series, log lines, and dashboard metrics are consumed as
**aggregates** (counts, averages) rather than by individual id. Many analytical
stores (BigQuery, InfluxDB) do not assign stable ids to each point. Modeling every
point as a full resource via create scales poorly — high volume, no meaningful
per-item lifecycle.

## Write versus create

Use a [custom method](custom-method.md) named **write** (and **batchWrite** when
needed) when data is **one-way**: inserted, never individually read, updated, or
deleted. The payload uses **entry** instead of **resource** — entries are
resource-like shapes but **anonymous** (no unique id, not addressable). Example:

```ts
interface WriteChatRoomStatEntryRequest {
  parent: string;
  entry: ChatRoomStatEntry;
}
```

Bind write to the **collection**, not the parent resource — for example
`POST /chatRooms/1/statEntries:write`, not `/chatRooms/1:writeStatEntry`. Even
when the collection is not a true set of addressable resources, collection
targeting keeps room for later collection-level methods ([batch operations](batch-operations.md),
[purge](purge-custom-method.md)). See [custom method targeting](custom-method-targeting.md).

## Return type and consistency

Write returns **void** — only success or error status. There is no meaningful
resource to return because the result joins an anonymous collection or updates a
streaming aggregate.

Standard create is expected to be immediately readable after success (or an
[LRO](long-running-operation.md) when visibility is delayed). Write breaks that
contract: aggregates cannot distinguish "my entry" from concurrent writers, so
there is no per-entry read-your-writes guarantee. **Eventual consistency** is
acceptable — return immediately before the entry appears in aggregates, matching
batched analytics pipelines.

Do **not** return an LRO per write: without an entry id you cannot track
pipeline visibility, and per-call Operation resources recreate the storage overhead
write exists to avoid. If clients need an acceptance signal, prefer **HTTP 202
Accepted** over 200 OK. When duplicate entries matter, apply
[request deduplication and idempotency keys](request-deduplication-and-idempotency-keys.md).

## Scope

The pattern is narrow — almost exclusively **analytical ingestion** alongside
otherwise resource-oriented APIs. Standard create on full resources remains valid
when per-item addressability and lifecycle matter.
