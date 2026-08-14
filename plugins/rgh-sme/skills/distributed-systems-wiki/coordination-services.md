---
type: concept
title: Coordination Services
description: >
  ZooKeeper/etcd-style replicated in-memory key-value stores exposing
  consensus as linearizable primitives: locks, leases, leader election,
  membership, and watches.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer et al.), ch. 23"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 25, Consistent Core"
---

# Coordination Services

ZooKeeper and etcd are small, in-memory, replicated key-value stores built on
[consensus](consensus.md) protocols (Zab and Raft respectively — i.e.
[total order broadcast](total-order-broadcast.md)). Their point is to let the
rest of the infrastructure "outsource" consensus rather than implement it.
They hold small, slow-changing coordination *metadata* — never application
data.

What they package together:

- **Linearizable atomic operations:** compare-and-set gives
  [distributed locks and leases](distributed-locks.md).
- **Total ordering of operations:** every operation gets a monotonically
  increasing id (ZooKeeper's `zxid`) — ready-made
  [fencing tokens](fencing-tokens.md).
- **Failure detection:** ephemeral nodes are deleted automatically when a
  client's heartbeat session dies, releasing its locks and roles.
- **Change notifications ([watches](state-watch.md)):** clients subscribe to
  key changes instead of polling — how peers learn about new leaders or
  membership changes.

Typical uses: leader election for single-leader systems
(avoiding [failover](leader-failover.md) hand-rolling), work/partition
assignment ("which node owns which shard") — [Kafka's consumer group
rebalancing](consumer-group-rebalancing.md) is a concrete instance, using
ephemeral registries and watches to let every consumer compute the same
assignment without a master — service discovery, and
[membership](membership-services.md) — agreeing which nodes are currently
alive. The pattern scales because consensus runs among a fixed small ensemble
(3 or 5 nodes) while thousands of clients merely read from it.

Google's **Chubby** is the archetype (and ZooKeeper's inspiration): a lock
service running Paxos over five replicas, granting clients time-bounded
leases kept alive by heartbeats. It provides leader election for cluster
managers (Borgmaster), master-location discovery, and storage for small
configuration metadata — the same holds-critical-state-so-nothing-else-has-to
role ZooKeeper and etcd play elsewhere.

## Why a small dedicated cluster ("Consistent Core")

Running full quorum-based [consensus](consensus.md) at the scale of an
entire data cluster degrades throughput badly — see [consensus](consensus.md)'s
note on throughput falling faster than cluster size grows. The pattern
that avoids this: run consensus on only a small, dedicated 3–5 node
ensemble (sometimes named a **Consistent Core**), giving it linearizability
and fault tolerance, and have a much larger data cluster delegate
coordination decisions to it rather than ever running quorum consensus at
data-cluster scale. Because the *entire* dependent cluster's correctness
rests on this small ensemble, subtle liveness bugs there are unusually
serious — a 2020 Cloudflare outage traced back to a partitioned node
continuously triggering Raft elections without adequate safeguards.

Keys are commonly namespaced hierarchically (`/servers/1`, `/tasks/task1`),
and a read typically fetches everything under a prefix at once — e.g.
reading `/servers` to learn full cluster membership in one call. This is why
ZooKeeper and Chubby expose a filesystem-like interface, while etcd3 instead
exposes a flat key space with range reads.

### Getting to the leader, and what followers can safely answer

A follower can safely serve reads that only need
[serializability](serializability.md) (a client's own view of order is
preserved, but may lag true latest state) — acceptable for metadata reads
that tolerate brief staleness — but an operation like a
[lease](distributed-locks.md) grant needs true
[linearizability](linearizability.md) and must go through the leader. Two
approaches route clients there: followers can redirect to the current
leader (ZooKeeper, etcd — useful since these systems also let followers
serve plain reads, so clients need a way to route only the strict
operations correctly), or any server can transparently forward to the
leader internally so clients never need leader-awareness logic at all.
Either way, a transient "no leader yet, election in progress" response just
means retry against another server. Duplicate requests from a client retry
after failover are handled the same way as anywhere else in a [replicated
log](replicated-log.md): via [idempotency](idempotency.md).
