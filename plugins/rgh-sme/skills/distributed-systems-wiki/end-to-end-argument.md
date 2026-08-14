---
type: concept
title: The End-to-End Argument
description: >
  Low-level reliability mechanisms (TCP, transactions, exactly-once
  processing) cannot guarantee application correctness; deduplication and
  integrity need an identifier carried end to end.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

# The End-to-End Argument

Each reliability layer only covers its own scope: TCP deduplicates packets
*within one connection*; a database [transaction](acid-transactions.md)
makes one commit atomic; a stream processor gives
[effectively-once](effectively-once-delivery.md) *within its pipeline*. None
of them survive the gaps *between* layers.

The canonical gap: a payment transaction commits, but the network drops the
response before the client sees it. The client — a new TCP connection, a new
database session — retries the POST, and every lower layer correctly
processes what it sees as a brand-new request. Money moves twice, despite
TCP, transactions, and retries each "working".

The fix must span the whole path: the *origin* generates a unique operation
id (UUID or request hash) that travels end to end — browser to service to
database — where a uniqueness constraint on the id makes the operation
[idempotent](idempotency.md) across every retry at every layer. Suppressing
duplicates anywhere short of the endpoints only narrows the window.

The design rule: for each correctness property, ask *which endpoints* it
must hold between, and enforce it there. Low-level guarantees are
performance optimizations and complexity reducers — valuable, but never a
substitute for the end-to-end check. The same reasoning motivates
[application-level integrity verification](timeliness-vs-integrity.md)
rather than blind trust in any single layer.
