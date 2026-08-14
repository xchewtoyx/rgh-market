---
type: concept
title: Process Pauses
description: >
  A thread can be preempted for seconds or minutes at any point without
  knowing it, invalidating any local belief about time, leases, or leadership.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
---

# Process Pauses

A running thread can be suspended at *any* point in its code, for an arbitrary
duration, and resume without any awareness that time passed. Causes:

- Stop-the-world garbage collection (seconds, occasionally minutes).
- Virtual machine live migration or hypervisor CPU steal.
- Swapping/paging thrash; synchronous disk or network-attached storage I/O.
- OS context switches, `SIGSTOP` (accidental or operator-issued).
- Laptop lid closed (for client-side code).

## The lease expiry bug

The canonical failure: a leader checks `lease.isValid()`, the check passes,
then a 15-second GC pause hits *between the check and the action*. The lease
expires during the pause, another node is elected leader, and when the paused
node resumes it continues executing writes it no longer has the right to make
— a zombie leader corrupting data. Within one machine such check-then-act
races are fixed with locks; against wall-clock time there is nothing to lock.

The general lesson: **a node cannot trust its own judgment about its role or
about elapsed time.** Any "am I still leader?" answer is stale the moment it
is produced. Correct designs move the enforcement to the receiving side with
[fencing tokens](fencing-tokens.md), and make authority decisions by
[majority](truth-defined-by-majority.md), not self-assessment.

Mitigations at the margin: hard real-time systems bound pauses but sacrifice
throughput and are impractical for servers; some systems treat an imminent GC
as planned node maintenance (drain traffic first) or restart processes before
full-heap GCs are needed. These reduce pause frequency; they do not eliminate
the need for pause-tolerant protocols. Pauses look identical to network
delays from outside — one more reason [failure
detection](timeouts-and-failure-detection.md) is guesswork.
