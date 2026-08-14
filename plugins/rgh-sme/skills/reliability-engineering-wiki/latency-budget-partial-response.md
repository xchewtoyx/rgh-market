---
type: concept
title: Latency Budget with Partial Response
description: >
  Giving each fan-out call a deadline derived from the overall latency target and rendering with whatever has replied by then, so one slow dependency degrades the response instead of delaying it past the target.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 1"
---

A **latency budget** allocates the overall response-time target for a
request across the calls needed to build it, so each call has an explicit
deadline instead of an open-ended wait. In a fan-out request — one frontend
call spawning several backend sub-queries in parallel — the frontend
reserves a fixed slice of the total budget for composing and sending its
own reply (e.g. 10ms out of a 200ms target) and gives up on any sub-query
still outstanding when the remaining time runs out, rendering the response
from whichever sub-queries *did* reply in time.

This turns a slow dependency into a partial, degraded response rather than
a slow or failed one: a search results page whose ad backend misses its
deadline renders without ads instead of making the whole page wait on it.
It is the fan-out-specific mechanism behind [graceful
degradation](graceful-degradation.md) — the deadline is what triggers the
degraded path, playing the same role that an error-rate threshold plays for
a [circuit breaker](circuit-breaker-pattern.md) — and it is what makes a
fanned-out dependency a [soft dependency](hard-vs-soft-dependency.md) by
construction: the caller's response time is bounded regardless of how slow
that dependency gets.

Because the deadline is deliberately tighter than "wait until it fails,"
the design point is choosing which sub-queries are worth truncating early:
a dependency whose absence meaningfully breaks the [critical user
journey](critical-user-journey.md) should not be treated as an
optional latency-budget casualty, whereas a dependency that only enriches
the response (ads, secondary recommendations) is the natural candidate to
sacrifice first when time runs short.
