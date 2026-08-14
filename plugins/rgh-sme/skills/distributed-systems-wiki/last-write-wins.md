---
type: concept
title: Last Write Wins (LWW)
description: >
  Conflict resolution that keeps only the write with the highest timestamp —
  convergent, but silently discards concurrent writes and is corrupted by
  clock skew.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 10"
---

# Last Write Wins (LWW)

Attach a timestamp to every write; when writes conflict, keep the one with the
highest timestamp and discard the others. Used as the default conflict
resolution in Cassandra and optionally in Riak.

LWW achieves convergence — every replica ends with the same value — at the cost
of **durability**: when several writes are
[concurrent](happens-before-and-concurrency.md), all of them were reported
successful to their clients, but only one survives. The loss is silent.

It gets worse with wall-clock timestamps: [clocks on different nodes are not
synchronized](unreliable-clocks.md), so a write that happened strictly *later*
can carry an *earlier* timestamp and be discarded in favor of stale data.
Clock skew turns "last" into an arbitrary choice — and wall-clock time can
outright run backward (NTP corrections, hardware faults, leap seconds; Google
smears leap seconds across the day precisely to keep time monotonic). The
risk concentrates where a write depends on previously *read* state,
especially across a partition — the read's basis may lose to an invisible
concurrent write.

LWW is only safe when lost updates are acceptable, or when the workload makes
conflicts impossible — e.g. giving every write a unique key (immutable values,
write-once). For anything else, prefer explicit
[conflict resolution](write-conflict-resolution.md) built on
[version vectors](version-vectors.md), which can distinguish a genuine
overwrite from a concurrent write that needs merging.
