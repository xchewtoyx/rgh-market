---
type: concept
title: Schema Evolution for Wide Events
description: As arbitrarily wide events accumulate more and more distinct attribute keys over an application's lifetime, naive column-per-attribute storage stops scaling; flexible-map columns trade query efficiency for schema flexibility, and newer auto-promoting typed-blob columns try to get both.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
---

An [arbitrarily wide event](wide-event-attribute-checklist.md) can accumulate hundreds of distinct attribute keys over an application's lifetime, and new keys keep appearing as instrumentation grows. Three approaches to storing this, trading off differently:

- **Naive column-per-attribute** — each attribute gets its own physical column. Fast to query, but doesn't scale as the number of distinct keys grows unbounded; adding a column for every new attribute becomes untenable.
- **A generic map/key-value column** (e.g. `Map(String, String)`) — flexible, since any new key just becomes a new map entry with no schema change. Costs I/O: reading even one key out of a map column typically requires reading all of that row's map keys and values, and map keys generally can't participate in a primary/sort key the way a real column can — so this should be used sparingly, for genuinely long-tail low-value attributes.
- **Auto-promoting typed columns** (e.g. ClickHouse's `JSON` type) — automatically promotes frequently-seen fields into real, efficient columns while storing rarer fields in a typed blob, removing the need to manually manage the column/map split as usage patterns shift over time.

This is one of the concrete engineering problems that falls out of committing to [high dimensionality](dimensionality.md) as a first-class property of the data model rather than an edge case — see also [time-partitioned columnar storage](time-partitioned-columnar-storage.md) for how these column layouts fit into the broader storage architecture.
