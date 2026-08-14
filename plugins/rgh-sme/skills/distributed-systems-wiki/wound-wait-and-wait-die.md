---
type: concept
title: Wound-Wait and Wait-Die Deadlock Avoidance
description: >
  Ordering transactions by age instead of building a waiting-for graph, so
  lock conflicts resolve by aborting one side deterministically rather than
  deadlocking.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 21, Two Phase Commit"
---

# Wound-Wait and Wait-Die Deadlock Avoidance

A transaction spanning multiple nodes under [two-phase
commit](two-phase-commit.md) needs two-phase locking to get serializable
isolation: read locks taken immediately, write locks taken at prepare time,
all held until commit or rollback. Two transactions can legitimately want to
upgrade conflicting locks at the same time — a real deadlock, not a
transient race — and a distributed system has no cheap way to build and
check a cross-node waiting-for graph the way a single-node database can.
Three policies avoid the graph entirely by making age the tiebreaker,
requiring only a comparable, monotonically ordered transaction id (not a
wall-clock timestamp — see [unreliable clocks](unreliable-clocks.md) for why
that would be unsafe) plus each transaction's elapsed age since it started:

- **Error.** Fail the requester immediately on any conflict; the caller
  retries after a random backoff. Simplest, but causes many restarts under
  contention since neither side gets priority.
- **Wound-Wait.** On conflict, compare ages. If the requester is *older*
  than every current lock holder, it "wounds" them — aborts the younger
  holder(s) and takes the lock. If the requester is younger, it queues and
  waits normally. One exception: a holder that has already reached the
  prepared state of [two-phase commit](two-phase-commit.md) is never
  wounded, because it's too late to safely unwind.
- **Wait-Die.** The symmetric opposite: an older requester waits; a younger
  requester is aborted immediately ("dies") rather than being allowed to
  queue.

Wound-Wait produces fewer restarts than Wait-Die in practice — a younger
transaction wounded by an older one restarts once and, being younger still
relative to whatever it retries against, is likely to succeed quickly,
whereas Wait-Die's immediate self-abort of the younger party can repeat.
This is why Spanner specifically uses Wound-Wait. Whichever policy is
chosen, the effect is the same: the two-node deadlock resolves to exactly
one restart instead of a stall or a naive double-restart, with the retry
itself going through an exponential-backoff-with-jitter loop like any other
contended operation (see [retry design](retry-design.md)).
