---
type: concept
title: Heavy-Tailed Load Skew
description: A capacity planning hazard where a load parameter's distribution is heavy-tailed rather than uniform, so average-case sizing misses the rare, extreme-cost events that actually break the system.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
---

Capacity models often size a system around the *average* value of a [load parameter](load-parameters.md). This works only if the parameter's distribution is reasonably uniform. When it is instead **heavy-tailed** — a small number of entities are orders of magnitude larger than the typical case — average-based sizing systematically under-provisions for the entities in the tail, and those entities are often exactly the ones whose failure is most visible or most costly.

## Worked Example: Social Media Fan-Out

A social network's average user has 75 followers, so a naive capacity model sizes write fan-out (delivering a post to every follower's feed) around a fan-out factor of ~75. But follower counts are heavy-tailed: a small number of celebrity accounts have tens of millions of followers. A single post from such an account can generate over 30 million fan-out writes — a workload spike many orders of magnitude above the "average" case the system was sized for, arriving with the same latency budget as an ordinary post.

## Why This Breaks Uniform Strategies

A single fan-out strategy tuned for the average case cannot absorb the tail:

*   Sizing for the average leaves the tail case unprovisioned and it fails or blows the latency budget.
*   Sizing for the tail (provisioning enough capacity to fan out 30 million writes within the same window as a 75-follower post) means paying for that capacity almost all the time it goes unused — a severe overprovisioning cost.

## Mitigation: Segment the Distribution, Don't Average It

Rather than picking one strategy for the whole distribution, treat the tail as a distinct case with its own handling. See [fan-out-on-write vs. fan-out-on-read](fan-out-on-write-vs-fan-out-on-read.md) for the concrete hybrid pattern this produces: bulk of the distribution handled one way, tail entities handled another. The general principle generalizes beyond fan-out to any capacity model driven by a skewed load parameter (e.g., per-tenant resource consumption in a multi-tenant system, per-key request rate in a sharded store) — check the shape of the distribution, not just its mean, before sizing.
