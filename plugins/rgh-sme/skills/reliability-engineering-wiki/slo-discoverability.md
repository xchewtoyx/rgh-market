---
type: concept
title: SLO Discoverability
description: >
  An SLO that's technically correct but hard to find only delivers value to
  the team that wrote it — discoverability requires a central repository and
  dashboards, not just a well-written document.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 15"
---

Understanding an SLO must extend beyond the owning team: engineers on
dependent teams, product teams (need targets and recent performance),
leadership (needs visibility to allocate resources), and customer support
(needs to communicate status to paying customers, and is often first to
hear when an SLO drifts out of alignment with customer expectations) all
need to be able to find it.

Practical mechanisms:

- **Central repository** for all [SLO definition documents](slo-definition-document.md)
  — a folder tree plus a single searchable master index, a wiki, or
  documentation-as-code (which gains version history and can link to live
  SLI/SLO config to prevent drift, at the cost of a higher barrier to entry
  for non-technical stakeholders). Don't rely purely on org-structure-based
  search — ownership knowledge and team names both drift, while service
  names are comparatively durable.
- **Discoverability tooling** — scan documents via API to auto-populate a
  repository index, flag overdue revisits, or open a ticket automatically
  when a revisit date is missed.
- **Dashboards** — recommended components: current status as a simple
  binary good/bad indicator (not primarily a graph); an SLI-violations
  graph correlated against other events; a burndown graph plus
  error-budget-remaining panel (see
  [reliability burndown reporting](reliability-burndown-reporting.md)); and
  a link back to the full definition document. Keep the underlying data
  accessible non-visually too.

This matters beyond convenience: users (and dependent teams) silently form
[implicit SLOs from past performance](implicit-slo-from-past-performance.md)
regardless of what's formally stated — a discoverable, explicit SLO is what
lets that implicit expectation be replaced with an actual, negotiated one.
