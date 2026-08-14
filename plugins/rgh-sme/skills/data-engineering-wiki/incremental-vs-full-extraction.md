---
type: concept
title: Incremental vs. Full (Snapshot) Extraction
description: >
  The two ways to get data out of a CRUD-based source — pull the current
  state, or pull the history of changes — and what each buys and costs.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
---

A CRUD-based source (the standard create/read/update/delete pattern behind
most application databases and REST APIs) can be extracted two ways:

- **Snapshot-based (full) extraction**: pull the source's current
  point-in-time state. Simple to reason about, but every run re-reads the
  whole table, and it throws away the history of how a row got to its current
  value — an update overwrites the prior value with no record it ever
  existed.
- **Incremental extraction via [change data capture](change-data-capture.md)**:
  pull the stream of insert/update/delete operations rather than the current
  state, preserving full history and enabling near-real-time downstream
  processing without re-reading the whole source each time.

The choice is a direct trade-off between extraction cost and history
fidelity: snapshotting is cheap to build and understand but loses history and
gets more expensive to run as the source grows, while CDC preserves history
and scales better but requires source-side support (a readable log or
trigger mechanism) and more pipeline machinery to consume correctly.

Which one a pipeline needs follows directly from what the target model has to
support — a target that only ever needs current state can snapshot; a target
that needs to reconstruct how a row changed over time (e.g., feeding
slowly-changing-dimension processing) needs the incremental history that only
CDC or an [insert-only history pattern](insert-only-history-pattern.md)
preserves.

This choice is about *which time range or change set* to pull, independent
of the separate question of whether to keep every record it returns — see
[ingestion-time sampling](ingestion-time-sampling-tradeoff.md) for the
volume-driven decision to keep only a fraction of what extraction produces.
