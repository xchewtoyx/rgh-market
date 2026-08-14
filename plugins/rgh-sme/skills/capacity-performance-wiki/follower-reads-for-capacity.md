---
type: concept
title: Follower Reads for Read Capacity
description: Routing read-only traffic to replicas instead of the primary/leader trades a bounded amount of read staleness for read throughput and latency that scale with replica count rather than being capped by a single node.
sources:
  - title: "Patterns of Distributed Systems"
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 16, Follower Reads"
---

In a leader-replicated data system, sending every read to the leader caps total read capacity at whatever a single node can serve, even though the data is already fully replicated to every follower. **Follower reads** route read-only requests to a follower instead — nearest-region or least-loaded — taking that load off the leader entirely and adding read capacity that scales with the number of replicas rather than staying fixed at one node.

## The Cost: Bounded Staleness

Followers always lag the leader by some non-zero replication delay, even under strongly-consistent replication — the leader still has to send a message to the follower after a write is committed. Follower reads are only appropriate where the application can tolerate reading a value that is very recently but not immediately up to date. This makes the decision a per-endpoint trade rather than a system-wide switch: endpoints that need the absolute latest value stay pinned to the leader; endpoints that can tolerate a small lag move to followers.

A follower that has fallen unusually far behind (network partition, slow disk) should stop serving reads rather than silently return arbitrarily stale data — real systems cap acceptable staleness and exclude followers that exceed it from the read-routing pool, the same headroom-based exclusion principle as any pool member that's failing its health check.

## The Read-Your-Own-Writes Problem

A client that just wrote to the leader and immediately reads from a follower can see its own write disappear, because the follower hasn't caught up yet. The fix carries a real latency cost: the client attaches the version stamp from its write to the subsequent read, and the serving follower waits until it has caught up to at least that version (or times out) before answering. This converts an inconsistency bug into a bounded wait, but that wait is extra latency specifically for read-after-write access patterns — an application with heavy read-your-own-writes traffic recovers less of the leader's capacity gain than one whose reads and writes come from different, uncorrelated clients.

## Relationship to Capacity Planning

Follower reads are a capacity lever, not a durability one: they don't change how much data is retained or how failures are tolerated, only where read load lands. As such they compose with the same [N+M redundancy](n-plus-m-redundancy.md) sizing already done for failure tolerance — extra replicas provisioned for durability incidentally add read capacity too, but sizing replica count purely to add read throughput runs into the same non-linear cost as [quorum size vs. write throughput trade-off](quorum-size-throughput-tradeoff.md) if those replicas also participate in write quorums. A read-only follower that never votes in a write quorum avoids that cost entirely, which is why systems that want to scale read capacity aggressively often add non-voting read replicas rather than growing the voting replica set.
