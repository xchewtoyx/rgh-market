---
type: concept
title: Resilience vs Stability
description: >
  Resilience — the capacity to recover from a large perturbation — is a distinct system property from stability, is invisible during normal operation, and is easily traded away for short-term efficiency without anyone noticing until it's gone.
sources:
  - title: Thinking in Systems
    resource: "Thinking in Systems: A Primer (Meadows, ed. Wright), ch. 3"
---

**Resilience** — a system's ability to survive a large perturbation and
recover its function afterward — is not the same property as **stability**,
which is simply the absence of visible fluctuation over some observation
window. A system can be dynamic (oscillating, cycling through periodic
stress) and highly resilient; a system that looks perfectly flat and stable
week to week can have quietly lost the reserves that would let it recover
from a real shock.

This asymmetry matters because stability is directly observable — you can
watch a dashboard and see it hold steady — while resilience is only
observable by actually testing the system's limits, which is exactly the
justification for [chaos engineering](chaos-engineering.md) and [game day
exercises](game-day-exercises.md): a system "pays more attention to its
play than to its playing space," so it can do the same thing successfully a
hundred times and then fail the hundred-and-first time it's pushed slightly
harder, with nothing in its recent history warning that the limit was close.

The mechanism behind resilience is a *rich structure of many feedback
loops* that can restore the system after a disturbance, operating through
different mechanisms and at different time scales, with redundancy so one
loop can compensate if another fails or is overwhelmed — the general-systems
version of why [circuit breakers](circuit-breaker-pattern.md), [load
shedding](load-shedding.md), the [bulkhead pattern](bulkhead-pattern.md),
and [graceful degradation](graceful-degradation.md) are deployed as
multiple independent layers rather than a single mechanism: each absorbs a
different failure mode, and having several means one layer's blind spot is
usually another layer's coverage.

**Resilience is a real cost, and it's the thing organizations trade away
first under efficiency pressure**, usually without deciding to: squeezing
out redundant capacity, standardizing away architectural diversity, or
removing slack all raise measured efficiency and look like pure wins right
up until the perturbation the removed slack would have absorbed actually
occurs. This is the same trade this bundle names on the SLO side — see
[being too reliable is a real cost](too-reliable-is-a-cost.md) for the
mirror-image problem of over-provisioning — but the systems-theory framing
adds the specific warning that resilience loss is usually *invisible*
until the moment it's tested, unlike an SLO miss, which at least shows up
in the numbers.
