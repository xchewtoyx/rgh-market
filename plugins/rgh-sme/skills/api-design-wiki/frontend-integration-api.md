---
type: concept
title: Frontend Integration API
description: >
  A message-based remote API from backend to client-side UIs for displaying,
  updating, and invoking activities on behalf of end users.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3–4"
---

**Frontend integration** (vertical) exposes backend services to Web, mobile, or
rich clients physically separate from server logic. Design follows UI information
needs — expressive shapes ([pagination](pagination.md), [wish list](wish-list.md))
aid incremental fetch but cost more to build and can tighten coupling.

Security and data privacy weigh heavily — frontends often handle sensitive
customer data. Typically HTTP resource APIs (REST-style verbs on URIs); also
gRPC, WebSockets, or GraphQL ([wish template](wish-template.md) at scale).

Choose [API visibility](api-visibility.md); compose
[atomic parameters](atomic-parameter.md) and [parameter trees](parameter-tree.md);
apply endpoint roles, quality patterns, [version identifier](version-identifier.md),
and [API description](api-description.md). May serve all clients or specialize
per client type (Backends For Frontends).

Often combined with public or community visibility for customer channels; less
common as pure solution-internal unless the UI is in the same product boundary.

**Write locality:** in multi-service frontends, some architectures restrict
**mutating** calls to the service that owns the data — cross-service integration
uses read-only APIs while HTML **transclusion** lets one service embed another's
fragment so writes still originate from the owning service's pages. SACAC applied
this rule to keep authorization boundaries aligned with UI ownership.

Differs from [backend integration API](backend-integration-api.md) — never
consumed directly by end-user frontends in the backend-integration case.
