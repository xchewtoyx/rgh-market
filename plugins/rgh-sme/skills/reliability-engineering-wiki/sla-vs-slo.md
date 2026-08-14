---
type: concept
title: SLA vs SLO
description: >
  A Service Level Agreement is an external, contractual promise with
  consequences attached, distinct from a Service Level Objective, which is
  an internal engineering target teams set stricter to create a safety margin.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
  - title: Guerrilla Capacity Planning
    resource: "Guerrilla Capacity Planning (Gunther), ch. 2"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3, ch. 9"
---

A **Service Level Agreement (SLA)** is an explicit or implicit business
contract with users, carrying financial or legal consequences for missing it.
A **[Service Level Objective](service-level-objective.md)** is the internal,
engineering-facing target that a team actually manages toward.

SREs manage systems to meet SLOs, not SLAs. SLOs are intentionally set
stricter than SLAs so that engineering has a safety margin to react before a
miss triggers real financial or legal consequences — e.g. internal SLO
99.9%, external SLA 99.5%.

Both are informed by the same underlying [SLI](service-level-indicator.md)
and [error budget](error-budget.md) math, but they sit alongside each other,
not one on top of the other: an SLA is a business/legal artifact, while the
SLO is what drives day-to-day engineering and operational decisions. SLOs are
often the practical first step toward being able to defend an SLA at all —
see [dependency reliability composition](dependency-reliability-composition.md)
for why naively composing SLAs across dependencies erodes the achievable
end-to-end guarantee fast.

When a platform is consumed by a third party (a vendor, or your own cloud
provider), see [sharing your SLO with a vendor](sharing-slo-with-vendor.md)
for why exposing your own SLO, not just relying on their published SLA, is
often the more useful practice.

See [compliance requirements as SLOs](compliance-requirements-as-slos.md)
for a related framing move: treating an externally-imposed compliance
requirement itself as an SLO, with the reporting that demonstrates it as the
SLI, rather than tracking compliance as a separate process outside the usual
SLI/SLO machinery.

**Terminology note — OLA.** ITIL's Service Level Management process names
a third artifact, the **Operational Level Agreement (OLA)**: an internal
agreement between IT teams (e.g. the app team and the network team) that
underpins a customer-facing SLA, analogous to how an SLO underpins an SLA
but framed as an inter-team contractual commitment rather than an
engineering target with a safety margin. A team encountering "OLA" in ITIL
process documentation should treat it as playing roughly the same
structural role an SLO plays here — the internal promise that has to hold
for the external SLA to hold — without assuming it carries the same
error-budget-driven, engineering-facing rigor an SLO implies.

## External SLA structure

A customer-facing SLA is more than a list of targets. At minimum it should
carry:

- at least one testable [SLO](service-level-objective.md), scoped to the
  operations or endpoints it governs;
- [violation consequences](sla-violation-consequences.md) — penalties,
  compensation credits, or other remedies;
- reporting and claims procedures so clients know how violations are
  measured, verified, and remediated.

Well-crafted external SLAs use assertive, unambiguous language and a
recognizable structure — ideally standardized across offerings so client
developers can compare guarantees before committing.

## When an external SLA is worth offering

Publishing measurable SLAs signals maturity and transparency, but they also
create legally binding business risk, substantial design/monitoring effort,
and organizational resistance (accountability for failures). An external
SLA only makes sense when clients require and pay for guarantees, when
communicated QoS is a competitive differentiator, or when regulation mandates
specific commitments — otherwise alternatives are often healthier:

- **No SLA** — rely on trust, historical performance, or implicit
  expectations; common for internal or low-criticality APIs where negotiation
  room is absent.
- **Informal quality goals** — loose objectives without measurable
  thresholds or enforcement; better than nothing when formalization cost
  exceeds benefit.
- **"Commercially reasonable efforts"** — a common fallback for qualities
  (especially security) that resist crisp measurement without becoming
  unrealistic or unvalidatable; an SLA can mix formal SLOs for some
  attributes with informal statements for others.

An **internal-only SLA** — the provider defines and measures performance
targets without publishing them externally — is the variant Site Reliability
Engineering practice usually calls an [SLO](service-level-objective.md)
with an [error budget policy](error-budget-policy.md), not a customer
contract at all.
