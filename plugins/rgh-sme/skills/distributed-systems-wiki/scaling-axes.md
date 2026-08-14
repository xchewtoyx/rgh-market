---
type: concept
title: Three Axes of Scaling (the AKF Cube)
description: >
  A named framework distinguishing three orthogonal ways to add capacity —
  replicate everything, split by function, or split by data — and when each
  one is the right move to reach for.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 5"
---

# Three Axes of Scaling (the AKF Cube)

Abbott, Keeven & Fisher's "scaling cube" names three genuinely independent
moves for adding capacity, useful as shared vocabulary for which move a
given bottleneck actually calls for:

- **x-axis — horizontal duplication.** [Replicate](single-leader-replication.md)
  the whole system; a load balancer spreads requests across the interchangeable
  copies. Scales close to linearly *only* when transactions complete
  independently per replica; scales worse the moment replicas must
  coordinate on a write, which is the same constraint
  [CAP](cap-theorem.md) states for any replicated system.
- **y-axis — functional (service) split.** Split distinct *functions* or
  *transaction types* onto dedicated resources instead of replicating a
  monolith wholesale — e.g. pulling a contended database off a shared
  machine, or routing latency-sensitive interactive traffic away from
  latency-tolerant batch traffic so engineering uniformly low latency for
  everything isn't required. Also applies by user type: routing a
  high-value customer segment to its own dedicated pool. Once split, each
  piece can independently apply x-axis scaling on top — cheaper than
  replicating the whole system just because one piece needs more capacity.
- **z-axis — data split.** [Partition](partitioning.md) the data itself
  rather than the processing — by hash, by key range, by geography, or by
  any other rule that gives each partition a bounded, roughly even share.
  This is the axis with the highest migration cost: moving from
  unpartitioned to partitioned data typically forces real application
  refactoring, so it's usually the last axis reached for, after x- and
  y-axis options are exhausted.

Real systems blend all three rather than picking one: hot data partitions
get replicated deeper than cold ones (x layered on z); replica count flexes
live with observed load (dynamic x); infrequently accessed partitions move
to cheaper, slower storage tiers while hot ones stay on fast media
(an operational refinement of z). The framework's value is diagnostic —
naming which axis a proposed fix actually moves along keeps "add more
replicas" from being reached for when the real bottleneck is one contended
function or one oversized partition that replication won't touch.
