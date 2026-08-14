---
type: concept
title: Quorum Replica-Count Reliability Tradeoff
description: >
  In quorum-based replicated systems, tolerating one more simultaneous
  failure requires jumping cluster size by two, not one, and each jump
  costs write throughput — which is why practical systems converge on
  three or five replicas rather than scaling redundancy smoothly.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 10, Quorum"
---

A quorum-replicated system only recognizes an update once a majority of
replicas confirm it: for `n` replicas the quorum size is `n/2 + 1`, and the
system tolerates `f = n - quorum` simultaneous failures. This produces a
step function, not a smooth curve: going from 3 replicas to 4 buys zero
extra fault tolerance (quorum for 3 is 2, tolerating 1 failure; quorum for
4 is 3, still tolerating only 1) — the tolerance only steps up once cluster
size reaches 5. The general rule is `n = 2f + 1` to tolerate `f` failures,
so each additional unit of fault tolerance costs **two** more replicas, not
one.

That cost is not free: every additional replica in the quorum adds latency
to each write (more round trips to collect acknowledgments) and reduces
sustainable write throughput, an effect that degrades faster than linearly
with cluster size. This is the same [cost of nines](cost-of-nines.md)
non-linearity applied to a specific architecture choice — buying the next
increment of fault tolerance from a replicated, coordinated system costs
disproportionately more throughput than the increment before it. It is why
real quorum-based systems (consensus stores, coordination services)
overwhelmingly settle on **three or five** replicas rather than treating
replica count as a dial to turn up arbitrarily: five is typically the
practical ceiling that still sustains meaningful write throughput while
tolerating two simultaneous failures.

This is a different lever from [N+M redundancy](n-plus-m-redundancy.md):
N+M sizes a pool of independent, uncoordinated capacity units against
demand, where adding a spare is cheap and roughly linear. Quorum sizing
instead governs a set of replicas that must *coordinate* on every write, so
the fault-tolerance-per-replica curve is discontinuous and the throughput
cost compounds — a reason a coordination-heavy dependency (a lock service,
a metadata store) often has a much lower practical availability/throughput
ceiling than an equally-replicated but uncoordinated data store, and should
be sized as a [hard dependency](hard-vs-soft-dependency.md) accordingly in
[dependency reliability composition](dependency-reliability-composition.md).
