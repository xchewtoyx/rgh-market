---
type: concept
title: System Stability
description: >
  Stability is a system's ability to keep functioning under stress, degrade
  gracefully rather than collapsing, and recover automatically from localized
  component failures — not the absence of errors.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 3"
---

A stable system is not one that never fails; it is one that keeps delivering
its function under adverse conditions, degrades in a controlled way when it
can't keep up, and recovers on its own once a localized failure clears.
Stability is a property to design for deliberately, not a byproduct of
writing bug-free code — even fault-free systems face conditions (traffic
spikes, resource exhaustion, hardware failure) that a stable architecture
must absorb.

## Two kinds of load threat

- **Impulse** — a sudden, transient spike in load or traffic (a flash mob, a
  marketing blast, a retry storm). Impulses are handled by
  [load shedding](load-shedding.md) and [circuit breakers](circuit-breaker-pattern.md):
  fail fast and shed excess demand rather than letting it queue up and
  exhaust resources.
- **Strain** — sustained load applied over an extended period that exposes
  latent resource leaks (memory leaks, database connection leaks, open file
  handle accumulation, unbounded thread growth). Strain is handled by
  [steady-state design](steady-state-design.md): bounding resource and state
  growth so the system can run indefinitely without manual intervention.

Distinguishing which threat a given failure mode represents matters for
choosing the right mitigation — an impulse problem needs admission control at
the boundary, while a strain problem needs resource bounding inside the
running system; applying the wrong one to the other leaves the system
exposed.

Left unchecked, either threat can trigger the
[fault-error-failure chain](fault-error-failure-chain.md) that leads to a
[cascading failure](cascading-failure.md).
