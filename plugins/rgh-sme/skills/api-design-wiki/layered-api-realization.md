---
type: concept
title: Layered API Realization
description: >
  Every remote API is implemented through client SDK, provider SDK, and a
  lower transport interface — three contract layers integrators must align.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

A **remote API** in product terms is one published contract. In implementation
terms it rests on at least **three interfaces**:

1. **Client-side local API** — OS, middleware, language library, or SDK exposing
   transport services (HTTP client, socket API, message producer) to application code.
2. **Provider-side local API** — server framework or runtime binding incoming
   transport calls to handler logic.
3. **Remote interface at the next-lower stack layer** — e.g. HTTP over TCP/IP
   between the two local APIs.

Application integrators usually work at the top published layer ([API description](api-description.md),
OpenAPI, SDK methods). Platform teams own the middle and bottom layers. Misalignment
— wrong base URL, TLS mismatch, header stripped by a gateway — surfaces as
integration failures even when the domain contract is correct.

See [local interface to remote API](local-interface-to-remote-api.md) for why the
published contract must specify both endpoints and [message representations](atomic-parameter.md).
