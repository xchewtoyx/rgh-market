---
type: concept
title: Real-Time Partition Pattern
description: >
  Extending a static, heavily-indexed warehouse fact table's history to the
  current instant with a separate, lightly-indexed hot partition that gets
  merged in and reset on the next full load.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 20"
---

A warehouse fact table optimized for query performance is normally heavily
indexed and backed by [aggregates](aggregate-table-load-consistency.md) —
exactly the properties that make it slow and disruptive to keep continuously
open for a trickle of incoming rows. The real-time partition pattern
resolves this by physically and administratively separating "today's
still-forming data" from "yesterday-and-earlier's settled data":

- The **real-time partition** holds only activity since the last regular
  (typically midnight) load, ideally as a true physical partition of the
  fact table sharing its dimensional structure. It's indexed as lightly as
  possible — ideally not indexed at all — so rows can be continuously
  dribbled in without index-maintenance overhead blocking the load, and it's
  small enough to pin entirely in memory, which is what keeps queries against
  it responsive despite the missing indexes.
- The **static fact table** stays exactly as heavily indexed and
  aggregate-supported as it would be without any real-time requirement at
  all, since it never has to absorb continuous small writes.
- At the point the static table's next regular load runs, the real-time
  partition's accumulated rows get merged into it as the newest slice of
  history, and the partition resets to empty — for a transaction-grain fact
  table this repeats every load cycle; for a periodic-snapshot fact table,
  the partition is the "hot rolling" current period, merged in wholesale as
  the newest period once it closes.

This is the concrete mechanism that makes an [intra-day latency
tier](latency-tier-triage.md) commitment deliverable without redesigning the
whole warehouse around continuous ingestion — only a narrow, disposable slice
of the fact table takes on real-time-write characteristics, while the bulk
of the table keeps its normal, query-optimized shape. The pattern hasn't
proven necessary for accumulating-snapshot fact tables, since their
[destructive-update load mechanics](accumulating-snapshot-load-mechanics.md)
already handle continuous change to a small number of in-flight rows without
needing a separate hot partition.
