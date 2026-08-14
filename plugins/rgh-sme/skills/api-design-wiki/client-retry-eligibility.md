---
type: concept
title: Client Retry Eligibility
description: >
  Which HTTP failures and methods are safe to retry, grouped by whether the
  server likely never started work versus ambiguous or permanent errors.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 29"
---

Retries target **transient** failures — overloaded servers, maintenance — not
request validation errors that will fail identically on replay. HTTP status is
a guideline, not a complete rule; method idempotency and
[request deduplication](request-deduplication-and-idempotency-keys.md) matter
for ambiguous cases.

**Generally retriable** (server likely never began work): 408, 421, 425, 429,
503.

**Definitely not retriable** (permanent unless external state changes): 403,
405, 412, 501.

**Maybe retriable** (unknown whether downstream started): 500, 502, 504 — retry
only when duplicate side effects are impossible (idempotent methods or
deduplication keys).

Goal: maximize successful responses **system-wide** while minimizing retry storms.
Document eligibility in the [API description](api-description.md).

See [exponential backoff with jitter](exponential-backoff-with-jitter.md) and
[Retry-After header](retry-after-header.md) for timing.
