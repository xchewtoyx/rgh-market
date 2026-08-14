---
type: concept
title: SLI Types by Service Category
description: >
  The recommended starting set of SLI types differs by what kind of service
  is being measured — request-driven, storage, or pipeline.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
---

A useful starting point when defining SLIs for a new service: categorize its
components and reach for the SLI types that category typically needs.

- **Request-driven** (user-facing HTTP/RPC): availability, latency,
  throughput. HTTP semantics are a common standardization point — 5xx as
  service-caused failure (SLO-driving), 4xx as client-caused (tracked, not
  SLO-driving).
- **Storage / database**: latency (read/write), availability,
  [durability](durability-as-sli.md). For training/ML data specifically,
  whether cross-replica consistency also needs its own guarantee is a
  further, data-dependent question — see
  [training data consistency requirement](training-data-consistency-requirement.md).
- **Pipeline / asynchronous processing**: see
  [pipeline SLI types](pipeline-sli-types.md) for freshness, correctness,
  completeness, and isolation.

A fifth category, [cost/efficiency](cost-efficiency-as-sli.md), is often
neglected but worth tracking for any of the above.

Recommended practice: pick at most a handful of SLI types per service (rules
of thumb range from ≤3 to ≤5 across different sources — see
[SLO count and scope](slo-count-and-scope.md)), and prefer multiple latency
thresholds over a single one to capture both typical and long-tail
experience — see
[layered percentile SLO thresholds](layered-percentile-slo-thresholds.md).

This categorization is a starting point, not a ceiling: real services often
need SLIs tailored to their actual [critical user journeys](critical-user-journey.md)
rather than a generic per-component checklist.
