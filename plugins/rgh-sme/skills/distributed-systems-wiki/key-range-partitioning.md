---
type: concept
title: Key-Range Partitioning
description: >
  Assigning continuous ranges of sorted keys to partitions — efficient range
  scans, but monotonically increasing keys create write hot spots.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 20, Key-Range Partitions"
---

# Key-Range Partitioning

Assign each [partition](partitioning.md) a continuous range of keys, like
encyclopedia volumes (A–B, C–D, …). Boundaries are *not* evenly spaced in key
space — they adapt to the data distribution so partitions hold similar
volumes, set manually or [automatically](rebalancing-partitions.md). Within a
partition, keys are kept sorted.

- **Strength:** range queries on the key are efficient — adjacent keys live
  together, and a scan touches one or few partitions. Natural for
  time-series fetches like "all readings from this month". Used by HBase,
  RethinkDB, earlier MongoDB.
- **Weakness:** access patterns correlated with key order concentrate load.
  The classic case is a **monotonically increasing key** (timestamp,
  auto-increment id): every current write lands in the partition owning
  "now" — a pure write [hot spot](hot-spots-and-skew.md) while other
  partitions idle.
- **Mitigation:** prefix the key with something that distributes, e.g.
  `(sensor_id, timestamp)` instead of `(timestamp)` — writes spread across
  sensors, and per-sensor time ranges stay scannable. The cost: queries
  across *all* sensors for a time range must now query every partition.

The alternative that trades away range scans for uniform load is
[hash partitioning](hash-partitioning.md).

## Auto-splitting when ranges aren't known upfront

Rather than choosing split points from a known key distribution, a system
can start with one partition spanning the entire key space and split
dynamically as it grows: each node periodically scans its own partitions,
and one crossing a configured size threshold triggers a split at an
approximate middle key. Scanning a whole partition just to size it and find
its midpoint is expensive, so production systems avoid it — some track
size-and-key metadata directly to skip the scan, others (which run one
storage-engine instance per partition) approximate the midpoint from
storage-file metadata instead of the actual data. The split itself goes
through the same coordinator-and-[replicated-log](replicated-log.md)
mechanics as [fixed-partition](fixed-partitions.md) assignment: the
coordinator persists the split, instructs the hosting node to physically
divide its data, waits for acknowledgment, then marks the new partition
online — and bumps a per-partition [generation
clock](generation-clock.md) specifically so a client holding a stale cached
partition table gets rejected and forced to refresh, rather than silently
querying the wrong node with a now-wrong range. Pure size-based splitting has
a cold-start problem — everything hits the single initial partition until
the first split propagates, no matter how many other nodes sit idle — which
is why some systems (CockroachDB, YugabyteDB) also trigger splits on load
signals like request rate, not size alone. [Key interval load
balancing](key-interval-load-balancing.md) takes the load-triggered variant
further still, continuously moving, splitting, and merging ranges in
response to live CPU/memory pressure rather than a size threshold — the same
idea applied to a stateful stream-processing computation instead of a
storage partition.
