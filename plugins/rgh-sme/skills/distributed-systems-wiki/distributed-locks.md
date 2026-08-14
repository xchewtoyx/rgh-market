---
type: concept
title: Distributed Locks and Leases
description: >
  Mutual exclusion across nodes via time-limited leases from a linearizable
  service — only safe when paired with receiver-side fencing.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 26, Lease"
---

# Distributed Locks and Leases

Ensuring only one node at a time performs some action — being leader, writing
a file, processing a partition. Because the holder may crash, distributed
locks are granted as **leases**: time-limited and renewed by heartbeat, so a
dead holder's lock frees itself.

Requirements that make this harder than it looks:

- The lock service must be [linearizable](linearizability.md) — everyone must
  agree on the single current holder — which is why locks are built on
  [coordination services](coordination-services.md) (ZooKeeper ephemeral
  nodes, etcd leases) rather than on eventually consistent stores.
- **Holding a lease proves nothing at the moment of use.** A
  [process pause](process-pauses.md) or network delay between checking the
  lease and acting can outlive the lease — the zombie-holder bug. Safe designs
  therefore require the *protected resource* to verify
  [fencing tokens](fencing-tokens.md); the lock service alone cannot make the
  system safe.
- Expiry timing inherits all the problems of
  [timeouts](timeouts-and-failure-detection.md) and
  [clocks](unreliable-clocks.md): too aggressive and live holders are
  dispossessed, too lax and recovery stalls.

Locks and leases are the building block of [leader
election](leader-failover.md), and misuse of them without fencing is one of
the most common real-world distributed-systems bugs.

## Expiration is itself a consensus decision

Inside a [coordination service](coordination-services.md), a lease's state
replicates to every node in the small consensus ensemble, but only the
current leader actively tracks the expiration timer against its own
[monotonic clock](unreliable-clocks.md) — followers run a no-op tracker
rather than deciding independently off their own uncoordinated clocks. When
the leader's timer fires, it removes the lease locally first, then proposes
an "expire lease" command through the [replicated
log](replicated-log.md) so every follower learns about it the same way any
other committed state change propagates — expiration is a committed event,
not a side effect any single node acts on unilaterally. A newly elected
leader refreshes every lease it knows about as one of its first actions,
which is deliberate rather than a bug: it buys a legitimate holder time to
notice the leadership change and reconnect before treating a transition it
hasn't detected yet as a lost lease.

A common way to attach a lease to a piece of data — ZooKeeper's ephemeral
node is exactly this — is to tie a specific key's lifetime to the lease: when
the lease expires, every key attached to it is removed automatically, and
[state watch](state-watch.md) subscribers are notified of the removal. This
is the standard building block for cluster-node failure detection: a node
registers a lease, attaches a self-identifying key to it, and keeps
renewing; if the node dies, the lease lapses, the key disappears, and
whatever was watching that key learns the node is gone — no separate failure
protocol needed. Practical heartbeat-interval guidance converges across
real systems on renewing at roughly half the lease TTL, giving two renewal
attempts within one TTL window as a safety margin against a single missed
heartbeat (ZooKeeper: ~3.3s heartbeats against a 10s session timeout;
Kafka's newer group-membership design: 3s heartbeats against an 18s lease).
