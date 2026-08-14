---
type: concept
title: API Description
description: >
  The shared human- and machine-readable specification of message structures,
  behavior, quality policies, and organizational facts clients need to invoke
  an API correctly.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 9"
---

An **API description** documents what clients must know to invoke an API and
interpret responses — beyond bare URLs and sample payloads.

Include:

- Request/response structures ([atomic parameters](atomic-parameter.md),
  [trees](parameter-tree.md), [error reports](error-report-shape.md))
- Dynamic behavior: allowed sequences, pre/postconditions, invariants,
  idempotency, transactionality
- [Version identifier](version-identifier.md) and evolution strategy
- Quality and business policies — often split into
  [service level agreement](service-level-agreement-as-contract.md),
  [pricing plan](pricing-plan-as-contract.md), and [rate limit](rate-limit.md)
- Licensing, ownership, support contacts

**Minimal description** — addresses, operation names, data contract. Compact
but forces guesswork and reverse engineering.

**Elaborate description** — examples, parameter tables, error codes, compliance
tests. Better interoperability; higher maintenance and leakage risk if
implementation internals appear.

Machine-readable formats (OpenAPI, JSON:API, API Blueprint) enable portals,
validation, and codegen — debated but widely used. Underspecified contracts
are easy to edit but unsafe; overspecified contracts are costly ("antilean").

Documentation depth scales with relationship: same-team integrations need less;
public unknown clients need more. Update descriptions as the API evolves —
each change carries cost and drift risk.

Every pattern in the book relates to what the description must capture; mission-
critical APIs pair descriptions with SLAs and explicit lifecycle patterns
([two in production](two-in-production.md), [limited lifetime guarantee](limited-lifetime-guarantee.md)).
