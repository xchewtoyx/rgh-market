---
type: concept
title: Context Map
description: >
  A context map documents the relationship between two bounded contexts as
  a named integration pattern, making the change coupling and inter-team
  coordination cost between them explicit instead of implied by a diagram
  arrow.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies (Susanne Kaiser), ch. 3"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 2"
---

A context map documents how two [bounded contexts](bounded-context.md)
relate — both the contract-level data/functionality integration between
them and the inter-team dynamics that integration implies. Like
[connector semantics](connector-semantics.md) for a component-and-connector
view, a context map exists because an unlabeled line between two boxes
conceals the one piece of information a reader actually needs: how much a
change on one side forces a change on the other. Context maps are
deliberately **technology-agnostic** — the relationship pattern says
nothing about whether the underlying communication is synchronous or
asynchronous, and even asynchronous, event-driven integration can still be
tightly change-coupled (an event schema change can force every publisher
and consumer to change together). Change coupling and runtime
communication style are separate concerns, documented separately.

The named relationship patterns, in increasing order of required
inter-team coordination bandwidth:

- **Separate Ways** — no integration; each side duplicates functionality
  independently. Zero coordination cost, at the price of duplicated
  effort; appropriate when integration cost or team communication friction
  would outweigh the duplication.
- **Published Language** — a well-documented, standardized shared
  interchange format between the two contexts, often paired with an
  Open-Host Service.
- **Anticorruption Layer (ACL)** — the downstream side translates the
  upstream's model into its own internal model, protecting itself from
  foreign concepts, frequent upstream changes, or a poorly-designed
  upstream (a "Big Ball of Mud").
- **Conformist** — the downstream side adopts the upstream model as-is,
  with no translation. Simpler but more tightly coupled; appropriate when
  the upstream is stable and well-designed enough that building a
  competing translation isn't worth it.
- **Open-Host Service (OHS)** — the upstream exposes a well-defined public
  protocol usable by many downstream consumers, decoupling its public API
  from its internal model so the two can evolve at different rates.
- **Customer-Supplier** — an upstream-downstream relationship where the
  downstream ("customer") has some real influence over the upstream
  ("supplier")'s priorities and roadmap.
- **Shared Kernel** — both teams literally share a subset of the domain
  model as one artifact. Reduces duplication but requires tight
  synchronization whenever it changes — in practice, the teams become a
  Partnership for that shared piece.
- **Partnership** — two teams collaborate toward a shared goal; the
  highest-bandwidth pattern, and often impractical to sustain long-term.
- **Big Ball of Mud** — the degenerate case: no clear boundary, no
  consistent model, no architectural principle being followed. When forced
  to integrate with one, the standard defense is an Anticorruption Layer
  to keep its mess from propagating.

These patterns compose across a map: one upstream Open-Host Service can
have one downstream consumer that Conforms to it and another that wraps it
in an ACL, depending on how much isolation each downstream side needs.
Patterns also chain in ways that create *implicit* dependencies worth
surfacing explicitly — if a Customer-Supplier relationship gives context B
influence over context A, and context C Conforms to A, then B implicitly
gains leverage over C too, with no direct B–C relationship documented
anywhere. A context map's value is making exactly this kind of transitive,
otherwise-invisible coupling visible before it causes a surprise.

The context, complexity, and change frequency of a
[core-domain](subdomain-classification.md) bounded context makes loose
change coupling there especially important: prefer patterns that let a
volatile core evolve independently (OHS outward, ACL inward) over patterns
that couple tightly to it (Conformist against it, Partnership with it, or
a Customer-Supplier relationship that lets another team veto its
evolution).

When bounded contexts are realized as separate services with HTTP or
message APIs, the context map is also the checklist for **which new
interfaces need design**: each Customer/Supplier, Open Host Service, or
Conformist relationship implies a published contract whose [interface
documentation](interface-documentation.md) and [architectural decision
record](architectural-decision-capture.md) should trace to the
requirements artifacts that motivated the integration — see [API design
from requirements artifacts](api-design-from-requirements-artifacts.md).
