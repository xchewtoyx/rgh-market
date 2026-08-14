---
type: concept
title: Write-Ahead Log
description: >
  Persisting every state change as an append-only log entry before applying
  it in memory, so a crashed process can replay the log to recover exactly
  the state it had promised.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 3, Write-Ahead Log"
---

# Write-Ahead Log

A single server needs durability without relying on its storage engine's own
data structures being safely flushed to disk: once it has agreed to perform
an action, it must still perform it after a crash and restart, even though a
restart wipes all in-memory state. The fix is to write every state change to
a sequential, append-only log file (also called a **commit log**) *before*
applying it to in-memory structures. Because the log write happens first, a
handler can acknowledge the caller as soon as the entry is durable — the
in-memory update is a formality that a restart can always reconstruct by
replaying the log from the start (or from a snapshot — see [low water
mark](low-water-mark.md)).

Each entry gets a unique, monotonically increasing index. That index is what
makes later machinery possible: [segmented log](segmented-log.md) splits the
file by index ranges, [low water mark](low-water-mark.md) discards entries
before a safe index, and a [replicated log](state-machine-replication.md)
ships entries by index to followers. A write-ahead log is what makes
replication *valid* rather than just recovery: a known starting state plus a
linear sequence of logged changes fully determines the ending state, so
replaying the same entries on another node reproduces the same state.

## Implementation considerations

- **Flush trade-off.** Flushing every write to physical media before
  acknowledging gives the strongest durability guarantee but is a severe
  throughput bottleneck; delayed/async flushing trades durability risk (losing
  unflushed entries on crash) for throughput. Real implementations mitigate
  this with batching. [Write buffering](write-buffering-for-latency.md) takes
  this further in a replicated store: buffer writes per-node and lean on the
  replica quorum, rather than the log's own flush cadence, to bound the risk.
- **Corruption detection.** Entries are typically written with CRC checksums,
  validated on read, to detect corrupted log files — a cheap defense against
  the kind of silent bit-flip corruption discussed under [Byzantine
  faults](byzantine-faults.md).
- **Duplicates on retry.** Because the log is append-only, a client retrying
  after a communication failure can produce duplicate entries. If the
  resulting state structure makes repeated identical updates naturally
  idempotent (e.g. a last-write-wins map), nothing special is needed;
  otherwise the system needs explicit per-request deduplication (see
  [idempotency](idempotency.md)).
- **Single-threaded writer.** Log writes are commonly funneled through one
  dedicated thread — a [singular update queue](singular-update-queue.md) —
  so the log's append order matches the order updates were decided in,
  without locking.

## Versus event sourcing

Both use a log of changes, and an [event-sourced](event-sourcing.md) system
effectively treats its log as a write-ahead log when synchronizing other
systems from it. But event sourcing goes further: the log itself is the
**persistent source of truth**, retained indefinitely, supporting
reconstruction of state at any past point. A plain write-ahead log's entries
exist only to support crash recovery and can be discarded once fully applied
and safely past the [low water mark](low-water-mark.md).

Real systems: ZooKeeper and Raft/etcd implementations use WAL-style logging
for their own consensus state; Kafka's storage layer and conventional
database commit logs (including NoSQL stores such as Cassandra) follow the
same append-and-replay structure.
