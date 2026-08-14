---
type: concept
title: Scale-Up vs. Scale-Out
description: >
  Bigger machine versus shared-nothing cluster — and why the real dividing
  line is state: stateless tiers distribute trivially, stateful data systems
  buy every distribution problem at once.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 1"
---

# Scale-Up vs. Scale-Out

Both directions are, at bottom, ways of giving a workload more of the same
[four physical resources](physical-resource-limits.md) — CPU, memory,
network, disk — that bound any single server. Two ways to cope with load:
**vertical scaling** (a bigger machine) and
**horizontal scaling** (a shared-nothing cluster of smaller ones). Big
machines are simpler but cost superlinearly and hit a ceiling; clusters
scale further and enable geographic distribution, and pragmatic
architectures mix both (a few decent machines beat many tiny ones).
Elastic auto-scaling helps with unpredictable load but adds operational
surprise; manually planned scaling is simpler and more predictable.

The decision hinge is **state**:

- **Stateless services** distribute trivially — any node can serve any
  request; add nodes behind a load balancer.
- **Stateful data systems** are where distribution's real costs live:
  moving data means [partitioning](partitioning.md) with its
  [rebalancing](rebalancing-partitions.md) and
  [hot spots](hot-spots-and-skew.md), replication with its
  [lag anomalies](replication-lag.md) and
  [conflicts](write-conflict-resolution.md), plus
  [consensus](consensus.md) for anything requiring agreement — all under
  [partial failure](partial-failure.md).

Hence the standing heuristic: keep state concentrated in as few specialized
systems as possible (databases, [logs](log-based-messaging.md),
[caches](caching-tiers.md)) and keep everything else stateless; and scale a
database up until scaling out is *forced* by load, not fashion. When it is
forced, choose the distribution machinery per the actual bottleneck — read
volume, write volume, or dataset size point at
[replication](single-leader-replication.md), [partitioning](partitioning.md),
or both. There is no generic scalable architecture: it's built from these
blocks around *your* load parameters — and which parameter dominates (reads,
writes, [fan-out](fan-out.md), working-set size) is the first thing to
establish.
