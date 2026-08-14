---
type: concept
title: Timeliness vs. Integrity
description: >
  Separating "users see fresh state" from "state is never corrupt" — lag is
  temporary and tolerable, integrity violations are permanent, and dataflow
  systems can guarantee integrity without coordination.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

# Timeliness vs. Integrity

"Consistency" conflates two demands worth separating:

- **Timeliness:** users observe up-to-date state. A violation is
  [replication lag](replication-lag.md) — annoying, temporary, self-healing.
- **Integrity:** no corruption, loss, or false data — derived
  [views](change-data-capture.md) actually reflect their source, money is
  neither created nor destroyed. A violation is *permanent* until explicitly
  repaired; the system is not eventually consistent but perpetually
  inconsistent.

**Integrity is vastly more important than timeliness.** A bank statement
lagging a day is fine; a wrong balance is a crisis. Yet architectures often
buy timeliness with the machinery ([linearizability](linearizability.md),
[distributed transactions](two-phase-commit.md)) whose real justification
would be integrity — paying coordination costs on every operation.

Log-based dataflow keeps integrity *without* coordination: an ordered,
durable [log](log-based-messaging.md) of immutable events, deterministic
derivation, [idempotent](idempotency.md) replay, and
[end-to-end](end-to-end-argument.md) request ids give exactly-once *effect*
— asynchronously. What you give up is only timeliness, and where even
apparent constraints can bend, [coordination can be avoided
entirely](coordination-avoidance.md).

Trust but verify: integrity can also be *lost* silently — disk bit-rot,
[corruption below the fault model](byzantine-faults.md), software bugs — so
mature systems audit themselves (background checksum scanners as in
HDFS/S3, Merkle-tree verification as in Certificate Transparency), which
immutable [event logs](event-sourcing.md) make tractable: provenance is
preserved and derived state can be recomputed and compared.

**Replication is not a backup.** [Replicating](single-leader-replication.md)
protects against losing a physical copy — a disk or a datacenter dying —
but a bad write (a bug, an operator error, a malicious delete) is itself
replicated to every copy just as faithfully as a good one, usually within
the normal [replication lag](replication-lag.md) window. A system that only
has live replicas has no integrity recovery path once corruption has
propagated; the actual defense against that class of failure is a
point-in-time-recoverable backup or a delayed/soft-deletion window, kept
deliberately outside the live replication path so a bad write can't reach
it before it's caught.
