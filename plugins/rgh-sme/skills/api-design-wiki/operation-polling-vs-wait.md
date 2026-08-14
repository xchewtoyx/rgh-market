---
type: concept
title: Operation Polling vs Wait
description: >
  Two client patterns for LRO completion — repeated GetOperation calls versus
  a blocking WaitOperation custom method kept separate for observability.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10"
---

Clients resolve a [long-running operation](long-running-operation.md) by
**polling** or **waiting**.

**Polling** — call parameterized `GetOperation(id)` until `done` is true,
with delay or exponential backoff between calls. Simple and client-controlled,
but wastes requests with empty progress and updates are not instantaneous.

**Waiting** — custom idempotent `WaitOperation` (`GET .../:wait`) holds the
connection until `done`, making async work feel synchronous. Keep this a
**separate method**, not a boolean on `GetOperation`: one flag would mix
infra slowness with expected long waits and break SLO monitoring. Downside:
connection loss (mobile clients) forces fallback to polling or push
notification; many held-open connections increase server complexity.

Progress lives in `metadata` on each poll — counters, estimates, or other
domain-specific fields. Percent complete is optional; raw counts or ETA can
be clearer, and percentages can mislead if progress appears to move backward.
