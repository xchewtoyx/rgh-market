---
type: concept
title: Transactional Outbox Pattern
description: >
  Writing a state change and its change-event in the same database
  transaction so log-based CDC has something reliable to tail, avoiding the
  dual-write problem.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 10"
---

A source system that needs to both persist a state change and publish an
event about that change faces the **dual-write problem**: writing to its own
table and publishing to a queue/broker are two separate operations, and a
crash between them leaves the two out of sync — the state changed but no
event went out, or an event went out for a write that then failed.

The transactional outbox pattern avoids this by writing the event as a row in
an "outbox" table, in the *same* database transaction as the state change
itself. Since both writes commit or roll back together, the two can never
drift apart. A separate process then reads the outbox table and republishes
its rows as real events — typically via [change data capture](change-data-capture.md)
reading the database's own transaction log (log-based CDC is a natural fit
here, since the outbox table's writes flow through the same durability
mechanism CDC already taps).

This makes the outbox pattern the source-system-side half of a CDC-based
ingestion or event-driven integration: the source guarantees an event exists
for every committed change by construction, and the downstream log-based CDC
consumer only has to handle its own delivery semantics (typically
at-least-once, per-partition ordering) rather than also worry about whether
the source ever emitted the event at all. Because the transport is usually
at-least-once, consumers reading from the outbox still need to be
idempotent — the pattern solves *whether* an event is emitted, not how many
times it might be delivered downstream.
