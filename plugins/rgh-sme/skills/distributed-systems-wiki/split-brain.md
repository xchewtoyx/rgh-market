---
type: concept
title: Split-Brain
description: >
  The failure mode where two nodes simultaneously believe they are the leader
  and both accept writes, causing conflicting or lost data.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Split-Brain

Split-brain occurs when two nodes both believe they are the leader at the same
time — typically after a botched [failover](leader-failover.md) or a network
partition that isolates the old leader without killing it. Both nodes accept
writes; with no conflict resolution in place, writes diverge and data is lost
or corrupted.

The root cause is that a node cannot locally know it has been deposed: a leader
paused by GC, cut off by the network, or merely slow looks identical to a dead
one from outside (see [process pauses](process-pauses.md) and [unreliable
networks](unreliable-networks.md)), and from inside it still thinks it holds
the role.

Mitigations:

- **STONITH** ("Shoot The Other Node In The Head"): mechanisms to forcibly
  power off or isolate the old leader when a new one is elected. Crude, and if
  misconfigured can shut down both nodes.
- **[Fencing tokens](fencing-tokens.md):** rather than trusting the deposed
  leader to stop, downstream resources reject requests carrying a stale
  leadership token — the robust fix.
- **Quorum-based leadership:** requiring a [quorum](quorum-reads-and-writes.md)
  of nodes to acknowledge a leader means at most one leader can hold a majority
  at a time; this is how [consensus](consensus.md) algorithms prevent
  split-brain by construction.

Some designs accept this risk deliberately rather than mitigate it: an
[emergent leader](emergent-leader.md) has no quorum-backed election at all,
so a network partition reliably produces two independently-functioning
coordinators, one per side — a conscious trade of availability for the
consistency a quorum-based leader would otherwise guarantee.
