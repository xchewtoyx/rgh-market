---
type: concept
title: Bounded Context
description: >
  A bounded context is the boundary within which a single domain model and
  its vocabulary apply consistently — a linguistic, ownership, and often
  physical seam that names where one design ends and another begins.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies (Susanne Kaiser), ch. 3"
---

A bounded context is the boundary inside which one domain model — the set
of abstractions and business rules for a specific subdomain — applies
consistently, expressed in a single ubiquitous language. Outside that
boundary, the same term can mean something else entirely; the ambiguity
that surfaces when it doesn't ("Session" meaning something different
during submission, evaluation, and scheduling) is itself the signal that a
boundary belongs there, not a naming problem to paper over.

A bounded context is defined by three overlapping boundary types, and
documenting one means being explicit about all three, since they don't
always coincide in practice:

- **Linguistic/semantic boundary** — terms and their meanings stay
  consistent and unambiguous inside the context.
- **Ownership boundary** — the context is implemented and evolved by one
  team (a team may own more than one context, but a context should not be
  jointly owned).
- **Physical boundary** — the context can correspond to a separate
  deployable artifact, repository, or path to production, though it does
  not have to.

A bounded context is a modeling and ownership boundary, not an
architecture-style mandate: it doesn't dictate microservices, a modular
monolith, or any particular [component-and-connector](component-and-connector-view.md)
structure — it says where conceptual integrity has to hold, and different
bounded contexts are free to use different internal architecture styles
entirely. What one bounded context looks like from the outside, and how it
relates to its neighbors, is the concern of a [context
map](context-map.md); this note is the boundary itself, that note is the
network of relationships between boundaries.

Bounded contexts are usually discovered from the [subdomains](subdomain-classification.md)
a business domain decomposes into — subdomain analysis gives strong hints
for where a boundary should fall, though the two don't always coincide
one-to-one, especially in legacy systems where existing structure has
already drifted from the domain it was meant to model.
