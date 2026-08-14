---
type: concept
title: Stale-Leader Read Hazard
description: >
  Serving reads directly from a leader's local state to skip replication
  overhead is unsafe when the leader has been silently partitioned away and
  doesn't yet know it was deposed.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 9, Replicated Log"
---

# Stale-Leader Read Hazard

Because writes are rarer and more latency-tolerant than reads in most
datastores, popular [replicated log](replicated-log.md) implementations
(etcd/Raft, ZooKeeper) serve reads directly from local key-value state,
skipping the replication round trip entirely. This reintroduces exactly the
stale-read hazard a leader-based design exists to prevent, specifically when
a leader is silently partitioned from the rest of the cluster and doesn't
yet know it has been deposed: it still believes itself to be leader, a real
new leader elsewhere accepts a genuinely new write, and a client reading from
the stale, partitioned "leader" gets the old value — despite talking to a
node that thinks it is authoritative. This is not hypothetical: both etcd and
Consul shipped this bug before fixing it, and ZooKeeper documents the
limitation explicitly rather than closing it.

## Mitigations

- **Heartbeat-gated reads.** Before answering a read, the leader first
  confirms via a fresh [heartbeat](heartbeat.md) round trip that it can still
  reach a quorum of followers, and only then serves the read (Raft's
  documented approach). Cost: an extra network round trip on every read,
  which is expensive for geographically distributed clusters.
- **Leader lease.** The leader tracks, per follower, the last time it got a
  successful response, and only serves reads if it has confirmed quorum
  reachability within a rolling `leaderLeaseTimeout` window — avoiding a
  round trip on the common-case read at the cost of relying on
  [monotonic clocks](unreliable-clocks.md) and bounded clock drift across the
  cluster. This only works if paired with a companion rule: follower
  election timeouts must be kept *longer* than the leader's lease timeout,
  and a follower must refuse to vote for anyone while it still tracks a
  known-live leader — together these ensure no second leader can be elected
  while the first still believes its lease is valid. YugabyteDB, etcd, and
  Consul all implement leader leases for this reason; the underlying
  [lease](distributed-locks.md) concept is the same time-bounded-ownership
  idea used for cluster membership, just held by the leader over its own
  role rather than granted to it by an external store.

The same freshness problem, approached from the follower side instead of the
leader side, is what [follower reads](follower-reads.md) has to solve when
routing reads away from the leader on purpose rather than by accident.
