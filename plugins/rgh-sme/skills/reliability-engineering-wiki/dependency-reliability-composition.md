---
type: concept
title: Dependency Reliability Composition
description: >
  A service's reliability ceiling is bounded by its hard dependencies, and
  naively composing several "reasonable" per-component targets multiplies
  down to a much lower overall guarantee than intuition suggests.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4, ch. 12"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 3"
---


A service can never be more reliable than its [hard dependencies](hard-vs-soft-dependency.md).
Naively, N independent components each at target reliability R compose
multiplicatively: `R^N`. Example: 40 components each at 99.9% →
`0.999^40 ≈ 96.08%` maximum composite reliability — stacking many
individually-"reasonable" per-component targets erodes overall reliability
much faster than intuition suggests. A smaller worked example: vendor 99% +
internal 99% composes to only ~98.01% (~14.5 hours/month unavailability),
even though each number "looks fine" in isolation.

Don't naively "math your way" to higher availability via redundant
zones/replicas either — shared fate, common [failure
domains](failure-domain.md), and global control planes undermine the
independence assumption the multiplication relies on. Real-world composition math needs to account for retry logic
(which changes effective end-to-end reliability) and genuinely shared
failure domains, which can trigger a [cascading failure](cascading-failure.md),
rather than naive independent multiplication.

**Practical implications**:

- A critical dependency's reliability guarantee should be at or above the
  reliability guarantee it supports — a dependency can't quietly under-
  promise relative to what's built on top of it.
- When the cumulative failure rate of a deep infrastructure stack is too high
  for a critical service's SLO, engineers must utilize a [low-dependency
  design](low-dependency-design.md) to simplify the serving stack.
- For dependencies outside your control (vendor, open source, hardware),
  it's still worth setting an SLO target as a baseline for justifying
  config/architecture changes or vendor/hardware decisions, even though you
  can't "just fix the code." For hardware fleets specifically, statistically
  meaningful measurement generally needs real scale; lean on vendor/reseller
  aggregate failure-rate data as a proxy otherwise.
- Explicitly compose dependency reliability (multiplication, or more
  rigorous statistical methods) rather than assuming it out — this is part
  of what makes an SLA/SLO defensible; see [SLA vs SLO](sla-vs-slo.md).
- Introducing intermediate infrastructure components (such as administrative or security proxies) creates new hard dependencies and potential single points of failure. To mitigate this risk, run multiple redundant instances and ensure that all underlying dependencies have acceptable service level agreements (SLAs) or objectives, alongside documented emergency escalation paths.

Contrast with [independent failover reliability composition](independent-failover-reliability-composition.md),
where *adding* a genuinely independent failure domain multiplies failure
probabilities down rather than reliability up — the same multiplicative math
working in the team's favor instead of against it.
