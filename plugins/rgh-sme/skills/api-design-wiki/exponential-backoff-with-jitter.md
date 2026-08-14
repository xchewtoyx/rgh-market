---
type: concept
title: Exponential Backoff With Jitter
description: >
  Client-side retry timing that doubles wait after each failure, caps delay and
  attempt count, and adds random jitter to desynchronize herds.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 29"
---

When the server is a black box, clients use **exponential backoff**: wait 1s,
then 2s, 4s, 8s, … before retries — proven from TCP congestion control.

Refinements:

- **`maxRetries`** — fail cleanly after N attempts instead of infinite loop
- **`maxDelayMs`** — clamp doubled delay at a ceiling
- **Jitter** — add random delay (for example up to 1000ms) **on top of** the
  computed backoff, not compounded into doubling. Without jitter, many clients
  retry in synchronized waves ("stampeding herds") and keep failing together.

When the response includes [Retry-After](retry-after-header.md), honor it for
that attempt instead of the computed backoff.

Pair with [client retry eligibility](client-retry-eligibility.md) — backoff
only applies to retriable errors.
