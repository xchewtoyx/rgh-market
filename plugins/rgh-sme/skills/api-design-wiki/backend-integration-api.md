---
type: concept
title: Backend Integration API
description: >
  A message-based remote API consumed exclusively by other backends for B2B or
  in-application service decomposition without frontend coupling.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3–4"
---

**Backend integration** (horizontal) connects independently deployed backends —
business-to-business exchange or application-internal service components —
preserving conceptual integrity without frontend coupling.

Runtime qualities dominate: performance, scalability, large payloads.
Cross-organizational integrations need interoperability and security; budget
ownership may be unclear for community or internal APIs.

Entry point usually business logic (auth, transactions, rules); data-layer
integration suits data-centric scenarios with little logic. Asynchronous
queue-based messaging is common across system boundaries.

Choose [API visibility](api-visibility.md); compose messages with standard
structure patterns; document via [API description](api-description.md). Service
decomposition uses domain, scaling, and changeability criteria — a collection of
solution-internal backend APIs may form a **platform API** (cloud provider
surface, message broker management APIs).

**Modular monolith** note: local DTO message APIs ease later extraction to
remote services versus call-by-reference coupling.

Differs from [frontend integration API](frontend-integration-api.md) in
protocol preferences (messaging vs browser-friendly HTTP) and message breadth.
Serving both integration types from one API forces compromises or optional
complexity — design separately when possible.
