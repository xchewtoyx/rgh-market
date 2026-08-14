---
type: concept
title: Recovery Time Objective and Recovery Point Objective
description: >
  RTO caps how long an outage may last and RPO caps how much data loss is acceptable, giving disaster-recovery design two independent, business-set targets instead of one vague "be resilient" mandate.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

Disaster-recovery planning is driven by two independent targets, each set by
business impact rather than by what's technically convenient:

- **Recovery Time Objective (RTO)** — the maximum acceptable duration of an
  outage before service must be restored. What counts as acceptable varies
  hugely by system: a day of downtime might be tolerable for an internal
  reporting pipeline, while an online storefront may need single-digit
  minutes.
- **Recovery Point Objective (RPO)** — the maximum acceptable amount of data
  loss, expressed as how far back in time the recovered state is allowed to
  fall short of the moment of failure (e.g. "no more than 5 minutes of
  writes may be lost").

The two are independent because they cap different failure dimensions:
a system can restore service almost instantly (low RTO) while still losing
several minutes of writes (nonzero RPO), or vice versa — recovering a fully
consistent, zero-loss state slowly. Setting both explicitly, rather than
just one, forces a design conversation to happen up front: a low RPO
generally requires synchronous replication or frequent durable checkpoints
(engineering cost paid continuously), while a low RTO generally requires
automated failover and a warm or hot standby (engineering cost paid to keep
recovery fast) — see the [hot/warm/cold spare
grades](n-plus-m-redundancy.md) for the standby-side half of this tradeoff.

RTO and RPO are the disaster-recovery-scoped siblings of the SLO/error-budget
machinery rather than replacements for it: an [SLO](service-level-objective.md)
governs ordinary, expected operation, while RTO/RPO specifically bound the
*disaster* case — a correlated, larger-scale failure the ordinary SLO isn't
meant to absorb. [Durability as an SLI](durability-as-sli.md) is the
day-to-day analog of RPO (an ongoing measurement, not a one-time recovery
target), and the two should be set consistently: an RPO looser than the
system's stated durability SLI quietly admits that recovery from a real
disaster is allowed to lose more data than routine operation ever would.
