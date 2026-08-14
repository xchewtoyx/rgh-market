---
type: concept
title: Processing Resource
description: >
  An activity-oriented endpoint that exposes operations bundling commands or
  business activities, often stateful, in contrast to data-holder endpoints.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3"
---

A **processing resource** lets clients **trigger actions** — bundled
application activities or commands — rather than CRUD a persistent entity
directly. Exposes [operation responsibility patterns](operation-responsibility-patterns.md):
computation, retrieval, creation, and transition operations as needed.

Choose processing vs [information holder resource](information-holder-resource.md)
from required client functionality. Truly stateless processing is rare (audit
logs alone introduce state); account for coupling when operations read or
write. Fine-grained action endpoints improve client control; coarse operations
improve consistency and can reduce chatty integrations.

Often hosts [computation functions](computation-function.md) and
[state transition operations](state-transition-operation.md) including the
business activity processor variant. May reference
[reference data holders](reference-data-holder.md) and
[link lookup resources](link-lookup-resource.md) in requests and responses.

Separate processing endpoints from information holders at runtime — retention,
protection, and scaling policies differ (transient workflow state vs master
data).
