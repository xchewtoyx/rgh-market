---
type: concept
title: Rate Limit
description: >
  A published cap on requests per time window (and optionally concurrency)
  enforced at the API contract layer to protect service quality and economics.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 9"
---

A **rate limit** defines how many requests a client may execute per interval.
When exceeded, the provider may reject, defer, throttle, or serve best-effort
with reduced resources. Limits reset on a fixed or rolling period (daily,
monthly, per second).

Scope flexibly: whole API, endpoint, operation group, or single operation —
costly operations (video upload) may consume more quota than cheap reads
(YouTube-style token weights). Limits may also cap **concurrent** in-flight
requests (for example one at a time on a free tier).

Enforcement requires **client identification** — [API key](api-key-as-message-element.md),
authentication, or IP when anonymous. Repeated abuse can suspend keys (deny
list). Document limits in the API description and [service level agreement](service-level-agreement-as-contract.md);
tie tiers to [pricing plans](pricing-plan-as-contract.md).

**Wire contract:** return `429 Too Many Requests` with
[Retry-After](retry-after-header.md) when the client should wait for quota reset,
and expose limit state in headers, for example:

```text
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-RateLimit-Reset: 1498811560
```

Alternatively embed remaining quota in a [context representation](context-representation.md)
in the payload. Introducing limits is often a **breaking change** — new error
responses require a [version identifier](version-identifier.md) bump.

Rate limiting makes the gateway **stateful** — account for that when scaling.
Pair burst caps with monthly quotas so clients cannot exhaust a month in
seconds. Clients should trace usage, queue, cache, and prioritize calls.

Throttling terminology overlaps with rate limiting across vendors; both slow
or reject excessive traffic.
