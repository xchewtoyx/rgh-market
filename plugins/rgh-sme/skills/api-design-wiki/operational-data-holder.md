---
type: concept
title: Operational Data Holder
description: >
  An information holder tagged for short-lived transactional entities that
  change often and carry many outgoing relationships.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3, ch. 5"
---

An **operational data holder** is an [information holder resource](information-holder-resource.md)
for **operational data** — business-transaction events such as orders,
shipments, or hiring records. Characteristics: short lifetime, frequent
updates, many outgoing relations.

Expose fast create/read/update/delete while preserving accuracy and conceptual
integrity. Favor incremental [resource identification](resource-identifier.md)
from aggregates or business capabilities, not one CRUD endpoint per table column.

API and data definitions for operational holders typically evolve faster than
[master data holders](master-data-holder.md); plan [versioning](version-identifier.md)
and [lifecycle guarantees](limited-lifetime-guarantee.md) accordingly.
