---
type: concept
title: Write Skew and Phantoms
description: >
  Concurrent transactions each read a shared precondition, then write to
  different objects, jointly violating an invariant no single write breaks —
  the anomaly snapshot isolation cannot catch.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
---

# Write Skew and Phantoms

**Write skew:** two transactions read the same objects to check a
precondition, decide independently, and update *different* objects — so
neither [lost-update detection](lost-updates.md) nor per-row locks fire, yet
together they break an invariant.

Canonical example: hospital on-call scheduling requires at least one doctor
on call. Alice and Bob both request leave simultaneously; each transaction
checks `COUNT(on_call) >= 2` against its
[snapshot](snapshot-isolation.md) (both see 2), each sets *its own* row off
call, both commit — zero doctors on call. Same shape: double-booking a
meeting room, two users claiming one username, double-spending a balance
across concurrent debits.

**Phantoms** generalize the trigger: a write in one transaction changes the
*set of rows matching another transaction's search condition*. When the
precondition is the absence of rows ("no booking for this room at this
time"), there is no row to lock — the conflicting row doesn't exist yet.

Mitigations:

- `SELECT ... FOR UPDATE` on the precondition rows — works only when the
  precondition is over rows that exist.
- **Materializing conflicts:** pre-create lockable rows for the phantom
  space (e.g. a row per room-timeslot, locked on booking). Effective but
  ugly — concurrency control leaks into the data model. Last resort.
- **[Serializable isolation](serializability.md)** — the only general
  solution; SSI detects these premise invalidations automatically.

Write skew is the reason "we use snapshot isolation, we're fine" is not a
complete answer: any invariant spanning multiple objects — or asserting
absence — is exposed. The same shape reappears across replicas as
[multi-writer conflicts](write-conflict-resolution.md), where even
serializability on each node can't see the other replica's writes.
