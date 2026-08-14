---
type: concept
title: Retrieval Operation
description: >
  A read-only operation that returns machine-readable data from provider state
  without changing application state except access logs.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

A **retrieval operation** `ro: (in, S) -> out` satisfies an information need
from remote state — ad hoc or periodic, possibly reshaped from the domain
model (by time, concept, aggregation).

Forces: varying client interest (frequency, breadth, depth); whether clients
replicate whole datasets locally vs provider-side filtering; small many-round-
trip messages vs few large payloads.

Design: read-only access documented in the API description. Simple cases use
[atomic parameter lists](atomic-parameter-list.md) of query params returning
[parameter trees](parameter-tree.md) or forests. Complex cases may accept a
declarative query string (GraphQL, SPARQL). Apply [pagination](pagination.md),
[wish list](wish-list.md) or [wish template](wish-template.md), and [metadata elements](metadata-element.md)
to control volume and interpretation.

**Variants:**

- **Status check** — id in, status code or enum out (polling).
- **Time-bound report** — interval parameters; one result tree per interval.
- **Business rule validator** — reads provider state to validate before a
  [state transition operation](state-transition-operation.md).

Scales via replication; heavy queries can bottleneck. Public open-data APIs
often expose retrieval with [API key](api-key-as-message-element.md) and
[rate limits](rate-limit.md).

Differs from [computation function](computation-function.md) (no provider state)
and [state creation operation](state-creation-operation.md) (push vs pull).
