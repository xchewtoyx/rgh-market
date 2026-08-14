---
type: concept
title: Limited Lifetime Guarantee
description: >
  A published promise not to break an API version until a fixed expiration date
  stated at release, letting clients plan migration years ahead.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

A **limited lifetime guarantee** commits: this [version identifier](version-identifier.md)
stays backward compatible until **`expireDate`** announced at publication —
often 6, 12, 18, or 24 months. No further coordination needed once the date is
public in the [API description](api-description.md) and
[SLA](service-level-agreement-as-contract.md).

Forces: plannable client roadmaps vs provider accumulation of compatibility
debt and blocked technology adoption. Problematic for unmaintained third-party
integrations that cannot migrate by the deadline.

During the window, only backward-compatible changes per
[semantic versioning](semantic-versioning-api.md) and
[backward compatibility policy](backward-compatibility-policy.md). Expiry acts
as implicit decommission notice.

More lenient for providers than [two in production](two-in-production.md) alone;
stricter for clients than [aggressive obsolescence](aggressive-obsolescence.md).
Often combined with two-in-production for bounded parallel versions plus a
firm end date.

[Master data holders](master-data-holder.md) commonly receive long guarantees;
[reference data holders](reference-data-holder.md) change rarely but benefit
from two-in-production when they do.
