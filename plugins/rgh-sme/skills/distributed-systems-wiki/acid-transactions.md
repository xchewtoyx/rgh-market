---
type: concept
title: ACID Transactions
description: >
  What atomicity, consistency, isolation, and durability actually guarantee —
  a transaction is an abstraction that collapses partial failure into
  commit-or-abort.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
---

# ACID Transactions

A transaction groups several reads and writes into one logical unit that
either **commits** entirely or **aborts** with all its writes discarded.
Its purpose is error-handling simplification: instead of reasoning about
[partial failure](partial-failure.md) — crash mid-way, network drop,
concurrent interference — the application reasons about exactly two outcomes,
and [retries on abort](transaction-aborts-and-retries.md).

What each letter actually guarantees (the terms are often misused):

- **Atomicity** = *abortability*, not concurrency. If anything fails partway,
  all writes so far are undone. Nothing to do with what concurrent readers
  see.
- **Consistency** = *application invariants* (credits equal debits) hold
  before and after. This is a property of the application's logic; the
  database supplies atomicity and isolation as tools but cannot guarantee
  your invariants for you. The C is not really the database's letter.
- **Isolation** = concurrent transactions don't interfere. Formally
  [serializability](serializability.md); in practice most databases default
  to weaker levels — [read committed](read-committed.md) or
  [snapshot isolation](snapshot-isolation.md) — each admitting specific
  anomalies.
- **Durability** = committed data survives crashes: a [write-ahead
  log](write-ahead-log.md) on nonvolatile storage, and in replicated systems,
  replication to other nodes
  ([which asynchronous replication can violate](leader-failover.md)). No
  durability is absolute — it's always a risk-reduction story.

## Single-object vs. multi-object

Storage engines give single-object atomicity (crash-recovery log) and
isolation (per-row lock) almost universally, plus atomic increments and
compare-and-set — these are not "transactions" in the multi-object sense.
Multi-object transactions earn their cost when several records must change
together: foreign-key references, denormalized counters updated with the
data they mirror, secondary indexes updated with the base row. Distributed
data raises the stakes: many partitioned stores abandoned multi-object
transactions because they are [hard across
partitions](two-phase-commit.md), pushing invariant maintenance onto the
application.
