---
type: concept
title: API Integration Type Decision
description: >
  Choosing whether an API serves front-end clients or backend-to-backend
  integration is an architectural decision that shapes security, coupling,
  expressiveness, and runtime quality requirements.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

Integration type answers: does this API primarily populate and update
user-facing clients (mobile apps, Web apps, rich clients), or does it
let independently built backend components exchange data and trigger each
other's activity? The two recurring options — **frontend integration**
(vertical, UI-to-server) and **backend integration** (horizontal,
server-to-server) — combine independently with any [API visibility
decision](api-visibility-decision.md) and should be recorded as separate
[architectural decisions](architectural-decision-capture.md) with their
own rationale and rejected alternatives.

Frontend integration APIs are shaped strongly by what the UI needs to
display and collect; richer, more expressive operations (e.g., supporting
pagination for incremental fetch) improve developer experience and UI
fit but cost more to build and can tighten coupling. Security and data
privacy are usually paramount because these clients often handle sensitive
customer data.

Backend integration APIs prioritize runtime qualities — performance,
scalability, interoperability across organizations — over presentation
concerns. Backends may serve multiple frontends or move large data
volumes; cross-organizational use raises interoperability and security
requirements; development budget and cost allocation may be unclear when
the API is community- or solution-internal rather than owned by a single
product. Integrating systems can also surface clashing development
cultures that the decision record should acknowledge as constraints, not
surprises.

When documenting the decision, capture which integration type was chosen,
which was explicitly neglected, and how that choice interacts with
visibility (public APIs often support both types; community APIs often
emphasize backend integration for replication or event sourcing). See
[documenting trade-offs](documenting-trade-offs.md) for laying out the
forces before committing, and [interface documentation](interface-documentation.md)
for the contract both integration styles require.
