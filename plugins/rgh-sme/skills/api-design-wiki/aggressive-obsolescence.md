---
type: concept
title: Aggressive Obsolescence
description: >
  Deprecate and remove API parts or versions on a relative timeline after
  announcement, minimizing provider maintenance for low-value functionality.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

**Aggressive obsolescence** retires endpoints, operations, or representation
elements the provider no longer wants to support — three steps:

1. **Release** — production use.
2. **Deprecate** — announce removal point (often next major release); sunset
   headers or metadata optional.
3. **Remove** — deploy without deprecated parts; dependent clients fail or
   redirect.

Uses **relative** time from deprecation (not fixed at initial publication like
[limited lifetime guarantee](limited-lifetime-guarantee.md)). Fine-grained removal
limits blast radius to clients using that feature.

Forces: cut maintenance skills debt; respect client power dynamics; adjust
[pricing plans](pricing-plan-as-contract.md) when value drops. Legal drivers
(IBAN migration) may mandate it.

Maintain an accurate deprecated-parts list in the [API description](api-description.md).
Trace usage via logs and dependency tooling before removal. Master data fields
are harder to drop than operational fields.

Contrasts with open-ended stability; stronger than [experimental preview](experimental-preview.md).
