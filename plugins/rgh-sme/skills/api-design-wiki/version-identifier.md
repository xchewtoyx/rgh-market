---
type: concept
title: Version Identifier
description: >
  An explicit version indicator in the API description and on the wire so
  receivers can reject incompatible interpretations before silent semantic drift.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

A **version identifier** tells clients which contract generation they are
speaking. Include it in the API description and in exchanged messages — as
metadata in the endpoint address, a protocol header, or the payload. Receivers
that see an unknown or incompatible version abort interpretation and return an
[incompatibility error](error-report-shape.md) rather than guessing.

Place the identifier in **one canonical location** per message unless
middleware genuinely needs duplicates. Common HTTP placements:

- `Accept` content type — `Accept: text/json+customer; version=1.0`
- Resource path prefix — `GET v2/customers/1234`
- Hostname — `v2.api.service.com`

SOAP/XML APIs often version via the top-level element's XML namespace. Payload
example: `"version": "1.0"` where price is implicitly EUR; `"version": "2.0"`
adds `"currency": "USD"` — without the version field, old clients misread
semantics even when syntax still parses. Adding a differently named field
(`priceInDollars`) avoids ambiguity but accumulates debt.

API version and implementation version evolve separately; facades or roll-forward
strategies can decouple them. Schemas may also carry their own version
identifiers, loosely aligned with operation versioning.

Hypermedia APIs need extra care: a backend emitting [link identifiers](link-element.md)
may not know which downstream API version the ultimate client supports. Tightly
coupled APIs in one product should version together; independent microservices
are harder to coordinate.

Versioning granularity ranges from whole contract to per-operation to
per-representation element — finer grain reduces forced client churn but raises
governance and test cost. Code generators can amplify bump cost (for example
namespace change renames every generated class).

**Hyrum's law:** fields documented as diagnostic-only (full fix version in a
header, support-only metadata) still become client dependencies over time —
partners built business logic on Terravis's version header despite explicit
"do not depend" guidance. Treat every wire field as part of the
[backward compatibility policy](backward-compatibility-policy.md) surface unless
you can enforce absence via validation.

Often structured with [semantic versioning](semantic-versioning-api.md);
required by [two in production](two-in-production.md) and related lifecycle
patterns.
