---
type: concept
title: Event Sourcing and Immutable Logs
description: >
  Storing application state as an append-only log of immutable domain events
  and deriving current state by replay — the state/stream duality made
  explicit.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
---

# Event Sourcing and Immutable Logs

Event sourcing stores every change to application state as an immutable
**domain-level event** (`ItemAddedToCart`) in an append-only log; current
state is derived deterministically by replaying the log. Where
[CDC](change-data-capture.md) extracts low-level row changes from a database
that remains the source of truth, event sourcing makes the *event log itself*
the source of truth, with meaningful, intention-revealing events.

Key distinctions and properties:

- **Command vs. event.** A user request arrives as a *command*, which can be
  validated and rejected (is the seat still free?). Only once accepted does
  it become an *event* — an immutable fact that downstream consumers may
  rely on. Validation must happen synchronously at the boundary; you cannot
  retract a fact later. (Enforcing such constraints across nodes leads back
  to [total order broadcast](total-order-broadcast.md).)
- **State/stream duality.** Current state is the integral of the change
  stream; the stream is the derivative of state. Storing the stream loses
  nothing and lets you derive *several* read-optimized views from the same
  log (CQRS — separating the write path from query-shaped
  [materialized views](dual-writes-problem.md)), each rebuildable by
  replay.
- **Auditability and error recovery.** Like an accountant's ledger, mistakes
  are corrected by appending compensating events, not by mutating history —
  a complete audit trail, and buggy code can't destroy the input needed to
  recover.
- **Limitations.** Replay-from-scratch needs snapshots or compaction to stay
  practical; and regulations demanding *physical* deletion of data
  (privacy) conflict with immutability, requiring explicit excision
  mechanisms that rewrite history.
