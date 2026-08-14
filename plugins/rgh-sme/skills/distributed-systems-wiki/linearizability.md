---
type: concept
title: Linearizability
description: >
  The recency guarantee that a replicated system behaves as if there were a
  single copy of the data, with every operation atomic at one point in a
  single global timeline.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
---

# Linearizability

Also called atomic consistency or strong consistency. A linearizable system
appears to have **a single copy of the data**, with each operation (read,
write, compare-and-set on a single object) taking effect atomically at some
instant between its start and finish. The operational content is a **recency
guarantee**: as soon as any client's write completes — or any client *reads*
the new value — every subsequent read by anyone returns that value or newer.
Time never moves backward for any observer; there is one global order of
operations (a total order, unlike the partial order of
[causality](causal-ordering.md)).

## Not the same as serializability

- **[Serializability](serializability.md)** is a multi-object *transaction
  isolation* property: the outcome equals *some* serial order — possibly not
  the real-time order.
- **Linearizability** is a single-object *recency* property, saying nothing
  about transactions.
- Both together = strict serializability. Notably, serializable snapshot
  isolation is not linearizable: it deliberately reads from an older
  [consistent snapshot](snapshot-isolation.md).

## When you actually need it

1. **Locking and leader election** — a [distributed lock](distributed-locks.md)
   must be linearizable, or two nodes can both win and cause
   [split-brain](split-brain.md).
2. **Uniqueness and threshold constraints** enforced at write time — unique
   usernames, not selling more stock than exists — need a linearizable
   compare-and-set.
3. **Cross-channel timing dependencies** — when data flows through two
   channels (e.g. file storage plus a message queue announcing the file), a
   non-linearizable store lets the message overtake the write, and the
   consumer reads stale or missing data.

## Which architectures provide it

- Single-leader with reads from the leader: *potentially* (failover bugs and
  [zombie leaders](process-pauses.md) break it in practice).
- [Consensus](consensus.md)-based systems (ZooKeeper, etcd): yes.
- [Multi-leader](multi-leader-replication.md): no — concurrent writes on
  multiple nodes by design.
- [Leaderless](leaderless-replication.md): generally no, even with strict
  quorums — under variable network delay, concurrent readers can see a
  partially propagated write in opposite orders. (Linearizable quorum reads
  are possible only with synchronous read repair and read-before-write, at
  significant cost, and still not for compare-and-set.)

## The cost

See the [CAP theorem](cap-theorem.md) for the availability trade-off. Beyond
partitions, linearizability is *always* slow: response time of linearizable
reads and writes is provably proportional to the uncertainty of network
delays. This is why even multicore CPUs abandon linearizable memory (per-core
caches, store buffers) and why most systems that drop the guarantee do so for
performance, not fault tolerance. Weaker models like
[causal ordering](causal-ordering.md) capture much of the value without the
penalty.
