---
type: concept
title: Versioned Value
description: >
  Storing every update to a key under a new monotonic version instead of
  overwriting in place, so clients can address a specific point in a key's
  history and readers never block writers.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 17, Versioned Value"
---

# Versioned Value

A different problem from [version vectors](version-vectors.md): this is a
single, monotonically increasing version number per key in a
[leader-based](leader-election.md) system (not per-replica counters for
detecting concurrent writes in a leaderless one). Every write becomes a
fresh append under a new version rather than an in-place mutation — nothing
is ever overwritten — and a client can read a historical value by specifying
the version it wants, or the latest by default.

The version counter ties directly into
[state machine replication](state-machine-replication.md): a leader
replicates a write via its [write-ahead log](write-ahead-log.md), and once
the entry crosses the [high water mark](high-water-mark.md) and is applied,
the underlying store bumps its version counter once per applied write and
keys the resulting value by (logical key, version).

## Storage encoding

Because append-only writes are what make non-blocking reads possible (see
[snapshot isolation and MVCC](snapshot-isolation.md) for why readers never
blocking writers matters), the version has to be encoded so that lookups
stay efficient. The common technique: append the version as a **suffix** to
the logical key, so keys sort first by logical key and then by version —
compatible with any sorted-key storage engine (RocksDB, BoltDB — both used
by real systems: etcd on BoltDB, CockroachDB historically on a RocksDB
derivative). A point read for "the value as of version N" becomes a
floor/predecessor lookup: the largest stored version at or before N (a key
with stored versions 1, 2, 3, 5 answers a read at version 4 with the value
stored at version 3). Storage engines that already sort keys internally
typically expose a custom-comparator hook so versioned keys sort correctly
at the engine level rather than needing a wrapper structure. Reading a
*range* of versions (not just a point) needs a secondary index from logical
key to the list of versions it has, kept alongside the main store.

## What it enables

- **[Follower reads](follower-reads.md)** use the version returned on write
  as a causality token: a client's later read carries that version, and the
  serving replica waits until its own applied version has caught up before
  answering.
- **[State watch](state-watch.md)** consumers that need every change from a
  given point onward, not just the latest value, read a version range rather
  than a single point.
- Snapshot isolation and MVCC transaction semantics fall out naturally once
  values are versioned this way — see [snapshot isolation and
  MVCC](snapshot-isolation.md) for the transaction-visibility rules built on
  top.

Real systems: etcd3's MVCC backend uses a single incrementing integer as the
version; MongoDB and CockroachDB instead key their MVCC backend by a [hybrid
clock](hybrid-clock.md) timestamp rather than a plain integer, letting the
version double as a causally meaningful point in time rather than an
opaque counter.
