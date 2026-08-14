---
type: concept
title: CAP Theorem
description: >
  When a network partition occurs, a replicated system must choose between
  linearizable consistency and availability — better read as "consistent or
  available when partitioned".
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 11"
---

# CAP Theorem

Formalized by Gilbert and Lynch after Brewer: in the presence of a network
partition, a system can preserve either [linearizability](linearizability.md)
or availability, not both. The popular "pick two of three" phrasing is
misleading — partitions are physical faults that *happen*, not a design
option. Better: **when partitioned, consistent or available (CP or AP)**.

- **CP behavior:** replicas that cannot reach the leader or a
  [quorum](truth-defined-by-majority.md) refuse to serve reads/writes,
  becoming unavailable to preserve the single-copy illusion.
- **AP behavior:** every replica keeps serving independently (as
  [multi-leader](multi-leader-replication.md) and
  [sloppy-quorum](sloppy-quorum-and-hinted-handoff.md) systems do), staying
  available but exposing stale reads and concurrent writes.

Cautions when applying it:

- The theorem's scope is narrow: one consistency model (linearizability), one
  fault type (partitions). It says nothing about network delay, dead nodes, or
  other trade-offs, and "availability" has a specific formal meaning that
  doesn't match every intuition. Treat it as one named trade-off, not a
  complete classification of systems.
- Each property is a **continuum**, not a binary — vendor "CP"/"AP" labels
  oversimplify, and real systems sit at different points per operation.
  Excessive latency in particular *functionally behaves like a partition*
  (clients time out either way), so the consistency-versus-latency trade-off
  matters on every request, not just during faults. When availability is the
  choice, [yield vs. harvest](yield-and-harvest.md) is a finer-grained frame
  than up/down.
- CAP "consistency" (linearizability) is unrelated to
  [ACID](acid-transactions.md) consistency (application invariants) — same
  word, different concepts.
- Even without partitions, linearizability costs latency proportional to
  network delay uncertainty — many systems choose weaker models for speed,
  not partition tolerance. [Causal ordering](causal-ordering.md) is the
  strongest model that avoids both the partition unavailability and the
  latency penalty.
