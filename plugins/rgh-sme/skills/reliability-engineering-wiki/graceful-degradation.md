---
type: concept
title: Graceful Degradation
description: >
  Shedding non-essential functionality under stress or dependency failure so a service keeps serving its core user journeys instead of failing outright.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 1-2"
---

**Graceful degradation** is the practice of designing a service to shed
non-essential functionality under stress — rather than failing outright —
so it keeps serving the [critical user journey](critical-user-journey.md)
even when parts of the system are unhealthy. It's a reduction in
functionality, not a reduction in capacity: the service intentionally does
less, in a controlled way, instead of doing everything badly or not at all.

Concrete forms this takes:

- **Reduced fidelity**: serving cached, static, or non-personalized content
  in place of a compute-heavy personalized response — e.g. a generic
  recommendation list instead of one computed from a live model — when the
  personalization dependency is slow or unavailable.
- **Feature removal**: dropping a non-critical feature from a page or
  response entirely (rather than degrading the whole response) when that
  feature's dependency is unhealthy, so the rest of the page still renders.
- **Fallback values**: returning a last-known-good or default value when a
  live lookup fails, rather than propagating the failure to the user.
- **Deadline truncation**: in a fan-out request, giving up on a sub-query
  that hasn't replied within its share of a [latency
  budget](latency-budget-partial-response.md) and rendering with whatever
  did arrive in time.

Graceful degradation is what makes a [hard dependency into a soft
dependency](hard-vs-soft-dependency.md) in practice — the dependency stops
being able to take the whole request down with it. It's typically triggered
by the same failure signal that would otherwise trip a [circuit
breaker](circuit-breaker-pattern.md): once calls to a dependency are failing
or timing out past a threshold, the service switches to its degraded path
instead of continuing to wait on (or retry) the failing call. This is a
structural complement to [load shedding](load-shedding.md): load shedding
protects a service from being overwhelmed by *volume* by rejecting excess
requests, while graceful degradation protects a service from being taken
down by a *failing dependency* by serving a worse — but still valid —
response to requests it accepts. Both exist to keep a system inside its
[cascading failure](cascading-failure.md) defenses rather than letting a
local problem become a global outage.

Degradation is best designed as a sequence of fallback tiers rather than a
single on/off switch, so the response gets progressively simpler as more
dependencies fail instead of jumping straight to full unavailability: e.g.
full interactive UI → read-only mode against a replica (when the primary
database stops accepting writes, often a deliberate defense against
detected corruption) → a lightweight/static UI served from client-side
cache → a generic "service unavailable" status page as the last resort.
Even a minimal placeholder response is preferable to no response at all,
since it at least confirms to the user that the outage is known rather than
leaving them staring at a hung connection.
