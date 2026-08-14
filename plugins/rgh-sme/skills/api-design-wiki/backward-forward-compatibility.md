---
type: concept
title: Backward and Forward Compatibility
description: >
  Definitions of when an old client works against a new provider and when a new
  client works against an older provider, and why both erode after launch.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

At first deployment, provider version *n* and clients written for *n* are
compatible by definition — the API description gives shared semantics.

After launch, only one side may change at a time:

- **Forward-compatible provider** — a client for version *n* still works when
  talking to provider *n−1* (provider lags client).
- **Backward-compatible provider** — a client for version *n* still works when
  talking to provider *n+1* (provider leads client).

Compatibility "vaporizes" without coordinated releases. Microservice rolling
deploys often run **multiple provider versions** while **multiple client
versions** coexist — evolution design must assume simultaneous mixes, not a
single global cutover.

**Extensibility vs compatibility:** adding optional metadata (for example a
`currency` field on a price previously assumed USD) can silently break clients
that cannot ignore unknown elements — extensibility and compatibility pull in
opposite directions.

Public and community APIs need evolution strategy before release; ad hoc
changes break unmaintained integrations. Power dynamics decide who bears
migration cost: monopolist providers vs clients with leverage. Whole-API version
bumps without sunset guarantees train clients to assume immortality — eventual
retirement then damages reputation.

Balance autonomy, loose coupling, extensibility, compatibility, and
sustainability over the API life cycle via [version identifiers](version-identifier.md),
[semantic versioning](semantic-versioning-api.md), and explicit
[lifecycle guarantees](limited-lifetime-guarantee.md).
