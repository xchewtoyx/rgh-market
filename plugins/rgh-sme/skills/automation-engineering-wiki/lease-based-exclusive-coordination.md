---
type: concept
title: Lease-Based Exclusive Coordination
description: >
  Automation that must have exactly one active owner at a time — a
  singleton scheduler, a leader-elected control loop — should grant that
  ownership as a time-bound lease renewed by heartbeat, not a permanent
  lock, so a crashed or hung owner can't block the system forever.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 26 (Lease)"
---

# Lease-Based Exclusive Coordination

A permanent lock granting exclusive ownership of some automated
responsibility (who runs this job, who is the active controller) has an
obvious failure mode: if the owner crashes or is partitioned away while
holding it, nothing else can ever take over. A **lease** fixes this by
making the grant time-bound from the start — the owner must actively
renew it via periodic [HeartBeat](fencing-tokens-against-zombie-actors.md)
before it expires, and if renewal stops for any reason (crash, GC pause,
network partition), the lease lapses on its own and another actor can
legitimately take over without needing anyone to detect the failure and
manually intervene first.

This only works safely if lease expiration is decided by a single,
consistent source of truth rather than by each interested party running
its own clock — otherwise two nodes can disagree about whether a lease
has expired and both act as owner simultaneously. Whatever coordinates
the lease (a consensus-backed core, or a shared datastore acting as one)
should be the sole authority on expiry, with the current holder informed
of the loss rather than each side inferring it independently. Because
expiry is exactly the moment ownership can change hands, every lease
should be paired with a [fencing token](fencing-tokens-against-zombie-actors.md)
— the old holder resuming after its lease already lapsed must have its
actions rejected structurally, not merely be expected to notice and stop
on its own.

A detail easy to get wrong: lease timing must be measured with a
**monotonic clock**, not wall-clock time. Wall-clock time is
NTP-corrected and can jump backward between two reads on the same
machine — if a lease's remaining time-to-live is computed as a
difference between wall-clock reads, an NTP correction can make an
expired lease appear to still have time left, or make a fresh lease
appear already expired. A monotonic clock only ever moves forward and is
exactly what "how much time has actually elapsed" questions need;
wall-clock time is for stamping *when* something happened in human terms,
not for measuring *how long* something has been running. Practical
heartbeat cadence: renew at roughly half the lease's TTL, so a single
missed renewal still leaves a safety margin before the lease actually
lapses — the same interval logic that governs any
[HeartBeat](fencing-tokens-against-zombie-actors.md)-based failure
detector, applied to a grant of authority instead of a plain liveness
check.

This is a narrower, more concrete instance of what [convergent vs. direct
orchestration](convergent-vs-direct-orchestration.md) assumes when it
talks about electing a single active controller for a reconciliation
loop — lease-based coordination is the mechanism that makes "exactly one
active owner, self-healing on failure" actually safe to rely on, rather
than just a design intention.
