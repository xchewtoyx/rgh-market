---
type: concept
title: Synchronous vs. Asynchronous Replication
description: >
  The trade-off between waiting for follower confirmation on every write
  (durability, but blocked by any slow follower) and confirming immediately
  (responsive, but recent writes are lost if the leader dies).
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Synchronous vs. Asynchronous Replication

In [single-leader replication](single-leader-replication.md), the leader must
choose whether to wait for followers before confirming a write to the client:

- **Synchronous:** the leader waits for the follower to confirm it received the
  write before reporting success. Guarantees the follower has an up-to-date
  copy, so no data is lost on leader crash — but if the synchronous follower is
  down or slow, *all writes block*. For this reason fully synchronous
  replication (every follower synchronous) is impractical: any single node
  outage halts the system.
- **Semi-synchronous:** exactly one follower is synchronous, the rest
  asynchronous. If the synchronous follower stalls, an asynchronous one is
  promoted to synchronous. Guarantees an up-to-date copy exists on at least two
  nodes.
- **Asynchronous:** the leader confirms immediately without waiting for any
  follower. The system stays responsive and keeps accepting writes even if all
  followers fall behind — but writes that were confirmed to clients and not yet
  replicated are **lost if the leader fails**, a durability violation that
  surfaces during [failover](leader-failover.md).

Asynchronous replication is the widespread default, especially with many
followers or geographic distribution. Its cost is [replication
lag](replication-lag.md): followers serve stale reads, producing the anomalies
that read-consistency guarantees exist to contain.

This sync/semi-sync/async spectrum is a specific instance of a general
pattern — see [redundant spare tiers](redundant-spare-tiers.md) for how the
same hot/warm/cold tradeoff between standby freshness and runtime cost shows
up for any component with a standby, not just database leaders.
