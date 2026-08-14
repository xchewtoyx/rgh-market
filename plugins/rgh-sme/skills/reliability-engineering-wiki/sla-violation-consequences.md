---
type: concept
title: SLA Violation Consequences
description: >
  External SLAs attach explicit penalties, compensation credits, and
  reporting procedures to missed SLOs so violation handling is measurable
  and negotiated upfront rather than litigated after the fact.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 9"
---

Every external [SLA](sla-vs-slo.md) should define what happens when an
[SLO](service-level-objective.md) is not met — not just what was promised.
Typical elements:

- **Penalty or compensation** — e.g. a percentage discount on the next
  billing period when latency or availability targets are missed over the
  measurement window.
- **Claims procedure** — how the client submits evidence (incident dates,
  times, affected operations) and who verifies the claim.
- **Reporting procedure** — how the provider communicates SLO attainment
  and violations during and after the window.

Each SLO tied to a quality attribute should specify three numbers alongside
the consequence: a **threshold** and unit (e.g. responses under 500ms), a
**guarantee** (minimum percentage of time or requests the threshold will
hold), and the **penalty** if the guarantee is missed — all over an explicit
[measurement window](slo-window-selection.md). Example structure: "99% of
requests answered in under 500ms over a 30-day window; otherwise the
customer receives a 10% credit on the current billing period."

Providers often **cap liability** by limiting remedies to service credits
rather than broader damages — a deliberate risk-management choice when
mitigating violations (dedicated operations staff, refunds) is expensive.
Internal [error budget policies](error-budget-policy.md) serve a parallel
role for engineering teams: they define what engineering does when budget
burns, whereas SLA consequences define what the business owes customers.

State clearly **how measurement is performed and interpreted** — including
where the measurement boundary sits (see
[SLI measurement point selection](sli-measurement-point-selection.md)) —
so clients do not form unrealistic expectations about what the provider
controls.
