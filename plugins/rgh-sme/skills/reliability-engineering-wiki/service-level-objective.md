---
type: concept
title: Service Level Objective (SLO)
description: >
  A target value or range for a service level indicator that a team commits
  to as an internal, revisable engineering objective rather than a contract.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1, ch. 4"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3, ch. 9"
---

An SLO pairs a [service level indicator](service-level-indicator.md) with a
target: `SLI ≤ target` or `lower bound ≤ SLI ≤ upper bound`. Example: "99% of
HTTP requests return in under 200ms, measured over a 30-day window."

Two hallmark traits of a *good* SLO: exceeding it correlates with happy
users, and missing it correlates with unhappy users. If neither correlation
holds, the SLO is measuring the wrong thing — see
[identifying a miscalibrated SLO](identifying-a-miscalibrated-slo.md).

An SLO is a target, not an agreement — it can and should change as
circumstances change (see [SLO evolution triggers](slo-evolution-triggers.md)).
This is what distinguishes it from an [SLA](sla-vs-slo.md), which is a
contractual promise with consequences attached.

SLOs should never target 100% — see
[100% reliability is the wrong target](hundred-percent-reliability-is-the-wrong-target.md).
The gap between 100% and the SLO target becomes the
[error budget](error-budget.md).

## SLOs inside an external SLA

When an SLO appears in a customer-facing [SLA](sla-vs-slo.md), it is usually
written with more contractual precision than an internal engineering target.
Each SLO should identify the specific operations or endpoints it covers so
client developers can evaluate guarantees before integration. Common
quality-attribute groupings include performance, availability, security,
data management, and personal-data protection — some driven by regulation
(see [compliance requirements as SLOs](compliance-requirements-as-slos.md))
rather than product choice.

A fully specified external SLO typically states:

- the **threshold** and unit of measurement (e.g. response time under
  500ms, measured from request arrival at the service boundary to response
  dispatch — excluding client network travel);
- the **guarantee** — what fraction of valid events must meet the threshold
  (e.g. 99% of requests);
- the **[measurement window](slo-window-selection.md)** (e.g. 30 days);
- the **[violation consequence](sla-violation-consequences.md)** when the
  guarantee is missed.

Derive thresholds from measurable quality attributes defined during service
design, not from aspiration alone — see
[choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md).
