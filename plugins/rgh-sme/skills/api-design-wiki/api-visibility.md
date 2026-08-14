---
type: concept
title: API Visibility
description: >
  Where an API is reachable — public internet, restricted community network, or
  solution-internal only — shaping security, funding, and lifecycle obligations.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3–4"
---

**Visibility** decides who may reach the API — a managerial choice with deep
technical impact on workload, security, and evolution.

**Public API** — unlimited/unknown clients on the public Internet; detailed
[API description](api-description.md) required. High peak loads; strong
authentication ([API key](api-key-as-message-element.md) or richer protocols);
[rate limits](rate-limit.md) and [pricing plans](pricing-plan-as-contract.md);
[service level agreements](service-level-agreement-as-contract.md). Truly open
APIs omit auth — rare for production services.

**Community API** — closed group across legal entities (extranet, partner
network). Share description only with members; diverse stakeholders and stricter
lifecycle expectations (paying customers may resist deprecation). Variants:
enterprise, product-shipped, access-limited cloud service APIs.

**Solution-internal API** — components within one application or product;
budget and lifecycle owned by one project. Predictable load unless fronted by a
public API. May **graduate** to community or public visibility — a conscious
decision revisiting security and SLA posture, not scope creep.

Message structure visibility is part of the published language — shared schemas
aid developer experience but couple clients and provider.

Pairs with [frontend integration API](frontend-integration-api.md) and
[backend integration API](backend-integration-api.md) — any visibility can
combine with either integration direction.
