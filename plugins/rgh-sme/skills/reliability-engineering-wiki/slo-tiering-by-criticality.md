---
type: concept
title: SLO Tiering by Criticality
description: >
  Applying different SLO targets by service criticality, customer tier, or
  responsiveness class rather than one blanket target keeps targets
  meaningful across services that aren't equally important.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2, ch. 3"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 13"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

A single blanket SLO applied to everything either over-constrains
low-criticality work or under-protects high-criticality work. Common
approaches to tiering:

- **By customer tier or responsiveness class** — premium vs. free customers,
  or interactive vs. batch/download workloads, can legitimately warrant
  different targets on the same underlying SLI. For API products, QoS
  guarantees are often decided **per API and client group** (e.g. all
  freemium clients of one API share one tier) and are usually tied to
  pricing or subscription models — what a client pays for should align with
  what reliability level they receive. A pricing plan that charges for
  consumption typically implies corresponding
  [service-level guarantees](service-level-objective.md) on performance
  and availability.
- **By service criticality, simplified into a small number of bands** — e.g.
  99.5% for non-selling/MVP systems, 99.9% for typical services, 99.95% for
  revenue-generating systems, 99.99% for shared infrastructure. Consumer-
  facing services generally tolerate more transient failure than
  infrastructure services that many other services depend on, since
  infrastructure failures cascade downstream — see
  [dependency reliability composition](dependency-reliability-composition.md).
- **By trust/testing level of the underlying component** — e.g. a
  production-hardened storage tier gets a tight support SLA (minutes), an
  untested tier gets best-effort support only, matching the support
  commitment to how proven the component actually is.
- **By component-count scale** — a single blanket percentage target can
  misapply across very different scales (e.g. a platform hosting 5 pods vs.
  200 pods); defining tiered constraints on one underlying SLI (percentage
  bands that change by scale) lets a platform hold one overall target while
  giving dependent teams calibrated strictness regardless of size.

Tiering by criticality is one of the standard levers alongside
[SLO count and scope](slo-count-and-scope.md) for keeping a set of SLOs
tractable while still reflecting real differences in what's actually at
stake.

When a tier carries a formal [SLA](sla-vs-slo.md), **usage limits** (rate
limits, quotas) on that tier protect the guaranteed performance level from
client abuse that would otherwise degrade service for others — the limit is
part of making the tier's SLO defensible, not merely a billing mechanic.
