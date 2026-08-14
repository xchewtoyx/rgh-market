---
type: concept
title: Relational Warehouse Anti-Patterns
description: >
  Three ways a "data warehouse" build ends up delivering none of a real
  warehouse's benefits — copying tables verbatim, unioning sources instead of
  modeling them, and letting scope creep from an ad hoc request.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 4"
---

Something can carry the name "data warehouse" and still fail to deliver what
[a real relational data warehouse](data-warehouse-architecture.md) is for.
Three recurring ways that happens:

- **The DW prefix**: copying a source database's tables unmodified into a
  differently-named schema (`Finance` becomes `DW_Finance`) and reporting off
  those tables directly. This produces a warehouse in name only — the tables
  are still shaped for operational CRUD, not for read-heavy analytical
  access, so none of the read-performance or data-modeling benefit a genuine
  analytical layer provides ever materializes. It looks like progress because
  reports now point at something called a warehouse, while the actual
  problem (source-shaped tables driving analytical queries) is unchanged.
- **Views with unions instead of modeling**: when the same entity exists
  across multiple sources (`CustomerSource1`, `CustomerSource2`,
  `CustomerSource3`), stitching them together with a SQL `VIEW` that unions
  the rows, rather than actually modeling and merging them into one
  genuinely integrated table. This skips the real work — a data model that
  fits all sources' shapes, and usually
  [master data management](master-data-management.md) to deduplicate and
  reconcile records that represent the same real-world entity differently
  across systems. A union view looks like integration but leaves every
  downstream consumer to rediscover and work around the sources' actual
  inconsistencies themselves.
- **The dumping ground**: standing up a warehouse quickly to satisfy one
  user's one-off request, then expanding it piecemeal as more requests
  arrive, with no design pass ever happening. Each individual addition seems
  reasonable in isolation, but the result is a jumbled structure nobody
  designed for the actual range of sources and users it now serves. The
  fix is at the first request: assess honestly whether it's genuinely a
  one-off or the start of something that will grow into an
  enterprise-scale warehouse, and if it's the latter, take the up-front
  design time before building rather than after the structure has already
  calcified around ad hoc decisions.

All three share the same root cause: skipping the modeling and design work a
warehouse is supposed to do, while still calling the result a warehouse. A
system exhibiting any of these anti-patterns needs the modeling work it
skipped, not a different storage technology — swapping the underlying
platform won't fix a structure that was never actually designed.
