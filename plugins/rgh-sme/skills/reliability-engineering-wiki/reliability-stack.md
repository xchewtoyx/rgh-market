---
type: concept
title: The Reliability Stack
description: >
  The layered relationship SLI → SLO → error budget, in which each layer is
  built directly on the one below it and none of them are meaningful in
  isolation.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1"
---

Three layers, bottom to top:

1. **[Service Level Indicator](service-level-indicator.md)** — a metric that
   reduces to a good/bad judgment per event, measuring the service from the
   user's perspective.
2. **[Service Level Objective](service-level-objective.md)** — a target
   percentage for that SLI ratio.
3. **[Error budget](error-budget.md)** — how much the SLI is allowed to miss
   the SLO before a team must act, over a defined window.

The stack rests on three underlying truths about services: a proper level of
reliability is a service's most important operational requirement;
reliability is defined by how the service *appears* to users, not by internal
metrics (see [user-centric SLI selection](user-centric-sli-selection.md));
and nothing is perfect all the time, nor does it need to be, because cost
scales much faster than linearly as you approach 100% (see
[cost of nines](cost-of-nines.md)).

None of the three layers is a one-time deliverable — the stack is meant to be
iterated on continuously as user needs, dependencies, and architecture shift;
see [SLO evolution triggers](slo-evolution-triggers.md). SLOs are a *process*,
not a project.
