---
type: concept
title: Service Level Agreement as Contract
description: >
  Published, measurable service-level objectives with penalties and measurement
  rules, complementing the technical API description for QoS commitments.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 9"
---

The **service level agreement (SLA)** states testable **service-level objectives
(SLOs)** — availability, latency, data handling, support — plus penalties,
credits, and reporting when missed. QoS belongs here rather than overloading the
[API description](api-description.md), though the description references the SLA.

Each SLO needs: threshold and unit, guarantee (% of time met over a window),
penalty (often billing credit), and **how measurement works** (for example
latency from endpoint arrival to response send, excluding client network).

**Forces:** clients depend on uptime for downstream promises; competitive APIs
signal confidence with guarantees; providers balance cost, liability, and
monitoring effort. Regulations (GDPR erasure, data residency) may mandate SLO-like
commitments. Alternatives — "commercially reasonable efforts" or informal text —
risk ambiguity under business-critical use.

Scope per operation or whole API — personal-data protection usually global;
backup frequency may differ by endpoint. Mix formal SLOs with informal security
commitments when formalization is unrealistic. Internal-only SLAs (SRE practice)
possible without external publication.

Document alongside [version identifiers](version-identifier.md),
[two in production](two-in-production.md), and [limited lifetime guarantee](limited-lifetime-guarantee.md).
[Rate limits](rate-limit.md) and [pricing plans](pricing-plan-as-contract.md)
often appear in the same commercial package — pricing implies certain guarantees;
[experimental preview](experimental-preview.md) pairs poorly with paid SLA tiers.

[Public API](api-visibility.md) offerings need realistic promises;
[solution-internal](api-visibility.md) APIs may stay lighter. Legal review for
binding terms.

Information-holder endpoints may SLO on data volume; processing endpoints on
concurrency and compute — align SLA with [operation responsibility patterns](operation-responsibility-patterns.md).
