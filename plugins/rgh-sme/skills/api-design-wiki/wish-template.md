---
type: concept
title: Wish Template
description: >
  A request-side mirror of the response parameter tree whose populated branches
  tell the provider which nested fields to include.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 7"
---

When response data **nests deeply**, a flat [wish list](wish-list.md) is
insufficient. A **wish template** adds request parameters mirroring the
response [parameter tree](parameter-tree.md) — optional fields, Booleans, or
dummy/sample values marking inclusion interest. A template processor traverses
the structure to drive retrieval or translates declarative queries into
data-source filters.

**Benefits:** data parsimony (*Datensparsamkeit*) for nested
[retrieval operations](retrieval-operation.md); eases adding fields without
forcing every client to receive them.

**Costs:** more elaborate encoding than flat lists; invalid parameter wishes
(silent ignore vs error) must be specified; sophisticated notations resemble
embedded middleware. GraphQL is an advanced realization — query schema as template,
server as processor — with depth-related payload explosion risks.

Use only when wish lists cannot express the needed nested shape. Validate with
schema (JSON Schema, XSD) to catch typos and renames. Reduces transfer toward
[rate limit](rate-limit.md) quotas. Document templates in the
[API description](api-description.md).

Pairs with [embedded entity vs linked information holder](embedded-entity-vs-linked-information-holder.md)
when selecting nested embed depth.
