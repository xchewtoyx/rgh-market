---
type: concept
title: SLO Stakeholder Buy-In Sequence
description: >
  Building organizational agreement to live by SLOs works best in a specific
  order — engineering and operations first, then product, then leadership,
  then legal, with QA informed rather than asked to approve.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 6"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 9"
---

SLIs, SLOs, and error budgets only matter if the organization actually
agrees to live by them. The recommended order of operations:

1. **Engineering and operations first** — their agreement on *principles*
   (not implementation details) is the linchpin for everyone else. The
   mutual trade to establish: engineers get freedom to deploy until budget
   is exhausted, operations gets real teeth via the
   [error budget policy](error-budget-policy.md) once it is.
2. **Product** — wants to know engineering and operations are already
   aligned before weighing in. Pitch: reliability is a first-class feature —
   an SLI is essentially an automated way to monitor whether a product
   requirement's user journeys are being honored.
3. **Leadership** — wants "the big three" functions already in agreement.
   The biggest hurdle here is that leaders often implicitly want 100%
   reliability — see
   [100% reliability is the wrong target](hundred-percent-reliability-is-the-wrong-target.md)
   for the argument to make: no system has ever been 100% reliable, and
   demanding perfection creates incentives to misreport or to become
   overcautious, neither of which helps.
4. **Legal** — mostly reassurance. SLOs are almost always stricter than
   [SLAs](sla-vs-slo.md), so adopting them changes external legal risk
   little to none, and better SLI/SLO data gives legal advance warning of
   SLA-violation risk instead of finding out after the fact.
5. **QA** — informed, not asked for approval; QA is a consumer of the
   decision, not a decider, since SLO/error-budget adoption tends to
   redistribute QA skills into engineering over time rather than eliminate
   them.

Sales, marketing, and support are downstream consumers too, not part of the
core convincing sequence. See
[SLO adoption anti-patterns](slo-adoption-anti-patterns.md) for the pitfalls
to avoid once buy-in is secured and rollout actually begins.

## External SLA negotiation

Drafting a customer-facing [SLA](sla-vs-slo.md) is a heavier process than
adopting internal SLOs. Involve C-level executives, legal, and security
officers **early** — agreeing on content and wording is often an intense
negotiation with a large human factor, typically requiring several
iterations and formal review/approval before publication. The sequence above
still applies for internal adoption, but legal moves from "mostly
reassurance" to active co-author when the artifact carries external
[violation consequences](sla-violation-consequences.md).
