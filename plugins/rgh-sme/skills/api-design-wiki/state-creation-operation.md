---
type: concept
title: State Creation Operation
description: >
  A write-only operation where the client reports an incident or new facts and
  the provider appends provider-side state, usually returning an acknowledgment.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

A **state creation operation** `sco: in -> (out, S')` adds provider state
without requiring a detailed provider reaction — order intake, batch-job
completion reports, contact events. Returns "got it" or an id for status lookup
and resend on transmission failure.

Forces: expressiveness vs parsimony of the incident report; client occurrence
time vs arrival time; limited state reads complicate invariant validation;
lost, duplicated, or out-of-order delivery.

Design: document syntax, semantics, pre/postconditions. Prefer idempotent
processing. Request is often a [parameter tree](parameter-tree.md); response
an atomic acknowledgment or [error report](error-report-shape.md). Unless
writing to an append-only log, commit the write in one transaction matching
the operation boundary. Give each item a unique id and client-side occurrence
timestamp when not fire-and-forget.

**Event notification variant** — past-tense external events stored as-is;
current state derived by replay (event sourcing). Events may be full snapshots
or deltas correlated by id or timestamp.

**Bulk report variant** — multiple incidents in one [request bundle](request-bundle.md).

Differs from [state transition operation](state-transition-operation.md),
which usually references existing state (order id). Differs from
[retrieval operation](retrieval-operation.md), which pulls without writing.
