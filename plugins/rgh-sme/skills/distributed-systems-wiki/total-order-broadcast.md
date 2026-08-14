---
type: concept
title: Total Order Broadcast
description: >
  A protocol delivering every message to every node exactly once and in the
  same order — equivalent to consensus, and the foundation of state machine
  replication.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

# Total Order Broadcast

Also called atomic broadcast. A messaging protocol with two safety
properties:

1. **Reliable delivery:** no message is lost — delivered to one node,
   delivered to all.
2. **Totally ordered delivery:** every node receives the messages in the same
   order, and the order is fixed permanently at delivery time (no retroactive
   insertion).

This is exactly what [state machine replication](state-machine-replication.md)
needs: feed every replica the same deterministic operations in the same order
and they stay identical — which is what a database replication log is. Unlike
[Lamport timestamps](lamport-timestamps.md), the order is known *when each
message is delivered*, so nodes can act on it immediately.

## Linearizable operations from a log

Total order broadcast turns an append-only log into
[linearizable](linearizability.md) compare-and-set: to claim a unique value,
append a tentative claim message; wait until the log delivers your message
back to you; if yours is the **first** claim for that key in the log, commit —
otherwise abort. Every node reaches the same verdict because everyone sees the
same order. (This gives linearizable writes; linearizable *reads* need an
extra step, e.g. appending a marker message and reading at its log position,
or reading from a synchronously updated replica.)

## Equivalence to consensus

Total order broadcast is equivalent to repeated rounds of
[consensus](consensus.md): each delivery slot is one consensus decision on
"which message comes next". Solve either and you have solved the other —
which is why ZooKeeper (Zab) and etcd (Raft) implement total order broadcast
as their core, and why practical consensus algorithms are used as replicated
logs rather than one-shot decisions.

## Limits of total ordering

A total order requires funneling every event through a single sequencing
point (the leader), so its throughput is bounded by one node. At scale the
order fragments: [partitions](partitioning.md) each keep their own order
with none between them; geographically separate datacenters, offline mobile
clients, and independently deployed microservices each maintain separate
orders no one arbitrates. Beyond a single consensus domain, the achievable
guarantee is [causal ordering](causal-ordering.md) — tracked explicitly with
logical timestamps and references to prior state, not global sequencing.
