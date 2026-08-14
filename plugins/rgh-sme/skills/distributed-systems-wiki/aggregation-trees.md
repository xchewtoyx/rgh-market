---
type: concept
title: Aggregation Trees
description: >
  A hierarchical alternative to flat scatter/gather — parent nodes merge and
  rank leaf results at each level, bounding fan-in and spreading aggregation
  work instead of concentrating it at one coordinator.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 1"
---

# Aggregation Trees

Flat [scatter/gather](partitioned-secondary-indexes.md) sends a query to
every relevant partition and merges all replies at one coordinator — fine
until the partition count and per-reply size both grow, at which point that
single coordinator becomes a fan-in bottleneck. The **aggregation tree**
(a.k.a. server tree) pattern restructures this as a hierarchy instead of a
flat fan-out: a root receives the query, forwards it to a layer of parent
nodes, which forward to leaf nodes each holding one shard of a corpus too
large for one machine — the classic example is splitting a search index's
terms or documents across leaves the way an encyclopedia's volumes get
split among readers searching in parallel.

Results flow back up the same hierarchy, but each **parent aggregates before
forwarding** rather than just relaying: it merges, sorts, and truncates
(e.g. keeps only the top 50) what its own children returned before passing
that smaller result set further up. This differs from flat scatter/gather
in where the aggregation work happens — spread across each tree level
instead of concentrated at one coordinator — and it bounds fan-in at every
node to (branching factor) replies rather than (total leaf count) replies.

Consequences and knobs:

- **Latency budgets still apply, level by level.** A node that hasn't heard
  back from all its children by its own deadline returns the best partial
  result it has rather than blocking the whole query — the same
  [trade harvest for yield](yield-and-harvest.md) move flat fan-out makes,
  just applicable independently at each tree level.
- **More leaves** shrinks the per-leaf shard (finer partitioning) or adds
  room for shard replication at the leaves for availability; **more parents
  per level** adds sort/rank capacity; **more levels** widens total fanout
  for corpora too large for a two-level tree.
- **Redundant, load-balanced nodes per level** give both spare capacity and
  a place to route around a failed node at that level, same as any
  [load-balanced replica pool](datacenter-load-balancing.md).
- **Caching at parent levels** is more effective the deeper the tree, since
  a parent sees the same repeated sub-queries from many downstream paths.

The same tail-latency compounding that afflicts flat
[fan-out](fan-out.md) still applies here — each level of the tree adds
another point where one slow child can gate its parent's response — but
per-level aggregation and per-level deadlines are exactly the mitigation:
they cap how much of that compounding effect propagates past any one level
instead of letting the slowest leaf in the *entire* corpus gate the root.
