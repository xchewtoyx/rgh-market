---
type: concept
title: Caching Tiers
description: >
  Memory-speed read tiers in front of a datastore: the population-strategy
  choices, the staleness/divergence risks each carries, and the thundering
  herd failure mode.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 12"
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 4"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Caching Tiers

A cache tier serves reads at RAM speed for data too large or too contended
for the primary datastore's own buffer cache. It is a *derived copy*, so
every design question is a replication question in disguise: how it is
populated determines how it diverges. A [content delivery
network](content-delivery-networks.md) is this same pattern turned into
globally distributed infrastructure, populated by regional demand rather
than pushed everywhere up front.

## Population strategies

- **Cache-after-persist:** write the database, then populate the cache (on
  the write path or lazily on read miss). Simplest; suits static or
  rarely-invalidated data. Staleness window between DB write and cache
  update.
- **Double-write:** write both cache and database from the application — a
  [dual write](dual-writes-problem.md), with exactly its race and
  partial-failure divergence problems; safe only with expensive validation
  machinery. Avoid.
- **Write-through (cache-first):** write the cache, persist to the database
  asynchronously. Fastest writes, but the cache now holds the *only* copy of
  recent writes — a cache crash loses data unless writes are logged for
  replay. The cache has become a leader with
  [async replication](synchronous-vs-asynchronous-replication.md), and needs
  the corresponding durability care.

A cleaner population path where infrastructure allows: feed the cache from
the database's [change stream](change-data-capture.md), making it an
ordinary derived follower with observable [lag](replication-lag.md).

## Failure modes

- **Thundering herd (dogpile / cache stampede):** a hot key expires (or a
  cold cache restarts) and all its readers miss simultaneously, stampeding
  the backing store with thousands of concurrent recomputations of the same
  result — a store sized on the assumption the cache absorbs that load
  collapses. Mitigate by staggering TTLs across nodes/keys, request
  coalescing (one fetch recomputes, the rest wait), or an intermediate
  proxy-cache tier that limits concurrent backing-store fetches.
- **Hidden hard dependency:** once SLOs are only achievable with the cache
  warm, the cache is a de facto critical tier and needs its own availability
  plan. Periodically test with the cache bypassed — in production, not
  staging — to learn whether the fallback path still works at all.
- **Invalidation bugs** serve stale data indefinitely; prefer designs where
  staleness is bounded (TTL, changelog-driven) over manual invalidation
  correctness.

## Provision the core for full load, the cache for latency

On [ephemeral compute instances](ephemeral-compute-instances.md), a local
cache is transient — capacity can vanish when workers are rescheduled. A
robust pattern: **size the cache to meet latency goals, but size the core
application path for total load** without the cache. When cache capacity is
lost, the uncached path still handles full traffic at higher latency instead
of collapsing — trading redundancy spend against the risk and cost of cache
loss. This is the same lesson as [hidden hard dependency](#failure-modes)
above, stated as a capacity-planning rule.
