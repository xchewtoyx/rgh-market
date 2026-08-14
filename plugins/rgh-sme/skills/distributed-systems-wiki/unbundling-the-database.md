---
type: concept
title: Unbundling the Database
description: >
  Composing specialized storage systems into one coherent whole by connecting
  them with asynchronous event logs — database internals turned inside-out,
  with application code as derivation functions.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

# Unbundling the Database

No single storage engine fits every access pattern, so real applications
combine an OLTP database, search index, cache, and warehouse. A monolithic
database integrates the analogous internals — log, indexes, materialized
views, caches — and keeps them consistent automatically. "Unbundling" builds
the same structure out of separate best-of-breed systems:

- **Federation (unifying reads):** one declarative query interface over
  heterogeneous stores (PostgreSQL foreign data wrappers). Read-side only.
- **Unbundling proper (unifying writes):** the hard problem is keeping
  writes in sync — solved the way a database syncs its own index: an ordered
  [event log](log-based-messaging.md) of changes
  ([CDC](change-data-capture.md) or [event
  sourcing](event-sourcing.md)) consumed asynchronously by each derived
  system. This wins over [distributed transactions](two-phase-commit.md)
  across heterogeneous systems (XA) on fault tolerance and loose coupling:
  processors are **deterministic and idempotent**, faults are contained by
  buffering in the durable log, and a slow or failed consumer delays only
  itself instead of blocking the whole ensemble — at the price of
  [asynchrony](timeliness-vs-integrity.md) instead of atomic visibility.
- **Application code as derivation function:** custom logic (index builders,
  ML feature caches, notification fan-out) becomes a stream operator
  computing derived state from the log — like a spreadsheet formula that
  recomputes when its inputs change, but durable and fault-tolerant.

The mindset shift: instead of one system guaranteeing consistency
internally, dataflow direction plus [where reads meet
writes](read-path-and-write-path.md) becomes the design space, and integrity
is preserved by log ordering and idempotent replay rather than locks.
