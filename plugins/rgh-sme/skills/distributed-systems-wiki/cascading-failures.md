---
type: concept
title: Cascading Failures
description: >
  How one node's failure spreads: load shifted onto survivors kills them in
  sequence, and blocked synchronous callers propagate a downstream failure
  upstream — with slow responses worse than outright death.
sources:
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 4"
---

# Cascading Failures

Two distinct spreading mechanisms, often combined:

- **Chain reaction (horizontal).** One instance in a load-balanced pool
  dies; its traffic redistributes over the survivors, raising per-node load;
  the next-weakest node tips over, shrinking the pool further — nodes fail
  in sequence until the tier is gone. Any pool running close to capacity is
  one node-death from this; the same dynamic is triggered by
  [failure-detector](timeouts-and-failure-detection.md) false positives and
  by [automatic rebalancing](rebalancing-partitions.md) migrating data onto
  already-stressed nodes.
- **Cascade (vertical).** A downstream dependency (database, payment
  gateway) fails or slows; synchronous callers block waiting on it, their
  thread/connection pools fill with waiting work, and *they* stop answering
  — so the failure climbs the call graph layer by layer. The transmission
  medium is blocked resources, which is why unbounded waits are the enabler.

Aggravating semantics:

- **Slow is worse than dead.** A dead service fails callers fast, freeing
  their resources; a *slow* one holds callers' sockets, threads, and memory
  for the full wait — maximal resource consumption per failure. This is the
  core argument for aggressive [timeouts](timeouts-and-failure-detection.md)
  and for failing fast when overloaded.
- **Unbalanced capacities.** A front tier scaled to 10,000 req/s feeding a
  back end sized for 500 req/s is a standing invitation: any traffic surge
  becomes the back end's outage, then (via the cascade) everyone's.
- **[Retry storms](retry-design.md)** multiply load exactly when capacity is
  lowest, preventing recovery.

Containment — circuit breakers, bulkheads, load shedding — is the province
of resilience engineering; what this domain contributes is the recognition
that *every synchronous integration point is a potential cascade conduit*,
and the blast-radius question belongs in the architecture ([cell-based
isolation](cell-based-isolation.md), capacity matching, queue decoupling via
[message brokers](message-brokers.md)) rather than only in per-service
defenses. A fleet-wide [control-plane](control-plane-vs-data-plane.md)
action is the sharpest version of this: it can apply the equivalent of a
cascading failure to every node simultaneously, on purpose, in one step.
