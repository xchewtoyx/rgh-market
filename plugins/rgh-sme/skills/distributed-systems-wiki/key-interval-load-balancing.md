---
type: concept
title: Key Interval Load Balancing
description: >
  A replicated master dynamically assigns contiguous key ranges to worker
  machines and moves, splits, or merges them under load — partition
  rebalancing applied to a stateful stream-processing computation instead of
  a storage cluster.
sources:
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §7.1"
---

# Key Interval Load Balancing

A stream-processing computation that keeps per-key state faces the same
placement problem a partitioned datastore does: divide the keyspace so work
is spread across machines, and move that division when load shifts. MillWheel
solves it the same way [key-range partitioning](key-range-partitioning.md)
does for storage — a **replicated master** divides each computation's
keyspace into lexicographic **key intervals** that collectively cover every
possible key, and assigns each interval to exactly one machine.

Unlike a storage cluster's rebalancing (typically triggered by node count
changing), the master here watches live resource pressure — CPU load and
memory pressure reported by a standard process monitor — and reacts by
moving an interval to a less-loaded machine, or splitting/merging intervals
outright. This is [rebalancing](rebalancing-partitions.md)'s trigger
generalized from "the cluster changed shape" to "a machine is struggling
right now," continuous rather than event-driven.

## Recovering ownership cheaply

When a machine takes over a key interval — after a move, split, merge, or the
previous owner's failure — it does one full scan of the interval's metadata
in the backing store to rebuild its in-memory structures: the heap of
pending timers and the queue of checkpointed productions. After that initial
scan, the new owner *trusts* its in-memory state to stay consistent with the
backing store for as long as it holds the interval, and serves everything
from memory rather than re-querying storage per operation. This is only sound
because exactly one machine can be actively writing a given interval's state
at a time — the single-writer guarantee [fencing
tokens](fencing-tokens.md) (MillWheel's per-key **sequencer**) enforce across
a handoff, so a scan can never race a stale former owner's delayed write.

## Storage layout

Timers, pending productions, and persisted state for a given key all live in
the **same row** of a backing store offering atomic single-row updates
(Bigtable, Spanner). Colocating them means a key's full state transition —
advance a timer, emit a production, update persisted state — commits as one
atomic row write, without needing a distributed transaction to keep the
pieces in sync.
