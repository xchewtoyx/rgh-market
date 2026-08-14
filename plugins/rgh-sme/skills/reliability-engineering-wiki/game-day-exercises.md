---
type: concept
title: Game Day Exercises
description: >
  Scheduled, large-scale rehearsals of catastrophic failure (e.g. simulated data-center loss) that surface latent single points of failure in both systems and human response process.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
---

A **game day** is a scheduled exercise that rehearses a large-scale failure —
simulated destruction of an entire data center, a major dependency going
dark — against production or a production-equivalent environment, with
enough advance notice for teams to prepare but without full knowledge of
exactly when or how the fault will be injected. It is [chaos
engineering](chaos-engineering.md) taken to organizational scale: rather
than a continuous background program of small, automated fault injection,
a game day is a deliberate, larger, rehearsed event that also tests the
humans and processes around the system, not only the system itself.

Mechanics: pick a future date for the exercise; give teams lead time to
eliminate known single points of failure and build out monitoring/failover
procedures in preparation; run smaller drills beforehand (database
failovers, killing a network link) to close obvious gaps; then execute the
real, larger failure at the scheduled time and let systems and people
respond as they actually would.

The distinct value of a game day over smaller continuous chaos experiments
is that it surfaces **latent defects** invisible until a fault of sufficient
scale is actually injected — for example, discovering that the monitoring
or incident-management tooling needed to *respond* to an outage is itself
hosted on the infrastructure the exercise just took down, or that an
escalation contact list is stale. These are failures of the response
process and its dependencies, not just the system architecture, and they
only show up when the rehearsal is realistic enough to force people to
actually use those tools under simulated pressure. A secondary benefit is
organizational: people build the cross-team relationships and muscle memory
needed during a real incident, so that actions which would otherwise require
conscious coordination become closer to routine.

Game days are best run with increasing intensity and complexity over time,
until large-scale failure response feels like an unremarkable part of
normal operations rather than an exceptional crisis.
