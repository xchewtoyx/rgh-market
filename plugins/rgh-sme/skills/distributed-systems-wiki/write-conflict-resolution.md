---
type: concept
title: Write Conflict Resolution
description: >
  Strategies for handling concurrent writes to the same data in multi-leader
  and leaderless systems: avoidance, convergent rules, sibling merging, and
  automatic merge algorithms.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §2.3"
---

# Write Conflict Resolution

[Multi-leader](multi-leader-replication.md) and
[leaderless](leaderless-replication.md) replication both allow
[concurrent writes](happens-before-and-concurrency.md) to the same record on
different replicas. All replicas must nevertheless **converge** on the same
final value. Building any of the strategies below means first answering two
design questions, made explicit in Dynamo's design: **when** to resolve —
on write (reject or serialize conflicting writes immediately, keeping reads
simple, but at the cost of ever rejecting a write) or on read (accept every
write unconditionally — an "**always writeable**" store — and push
resolution to whoever reads the value later); and **who** resolves — the
data store itself, limited to a generic convergent rule, or the
application, which can apply schema-aware merge logic (e.g. unioning a
shopping cart's added/removed items rather than picking one write to
discard outright). A store can support both: offer application-side
resolution to clients that want it, and fall back to a generic rule like
last-write-wins for clients that don't. Options for the generic rule,
roughly in order of preference:

- **Avoidance.** Route all writes for a given record to the same "home" leader
  (e.g. a user's data lives in their nearest datacenter). From that record's
  perspective the system is single-leader and conflicts cannot occur. Breaks
  down when the home must move (datacenter failure, user relocation).
- **[Last write wins](last-write-wins.md).** Pick the write with the highest
  timestamp, discard the rest. Convergent but silently loses data.
- **Replica ID ordering.** Writes from the higher-numbered replica win — same
  convergence, same data loss.
- **Value merging.** Concatenate or union the conflicting values; only
  meaningful for some data shapes.
- **Custom application logic.** The database invokes an application callback
  **on write** (conflict detected in the replication stream, e.g. Bucardo) or
  **on read**: conflicting versions are stored as *siblings* and handed to the
  application to merge next time the value is read (CouchDB, Riak). Merging
  siblings correctly is subtle — deletions need
  [tombstones](version-vectors.md) so removed items don't resurrect in a
  union.

## Automatic merge algorithms

Research-derived structures resolve concurrency without bespoke application
logic:

- **CRDTs** (conflict-free replicated data types): sets, maps, counters, and
  ordered lists that merge concurrent edits deterministically and sensibly,
  with no coordination (shipped in Riak 2.0).
- **Mergeable persistent data structures:** explicit version history and
  Git-style three-way merges.
- **Operational transformation:** the algorithm behind collaborative text
  editors (Etherpad, Google Docs), designed for concurrent edits to an ordered
  sequence of items.
