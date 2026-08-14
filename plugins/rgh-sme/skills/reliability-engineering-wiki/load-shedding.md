---
type: concept
title: Load Shedding
description: Rejecting lower-priority requests during periods of overload to preserve system capacity for critical traffic.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 5"
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

Load shedding is a stability pattern used to prevent [cascading failure](cascading-failure.md) when a service operates near or beyond its capacity limits. Rather than accepting all incoming requests and risking resource exhaustion (e.g., CPU, memory, thread starvation), the system actively rejects a portion of traffic.

By returning an immediate error (like HTTP 429 or 503) for low-priority requests, the service preserves its remaining capacity to successfully serve high-priority, critical requests (such as a [critical user journey](critical-user-journey.md)). This fast failure prevents the service from degrading into a state of slow responses, which would otherwise tie up resources across the architecture.

A softer variant sheds work instead of users: rather than rejecting a
low-priority request outright, the service **defers** it — queueing a
low-priority database update for later processing, or recording that an
action was accepted without fully processing it yet. Deferred work still
needs to happen eventually, so indefinite deferral just relocates the
failure rather than avoiding it: a deferred-work queue needs its own
explicit staleness budget (an acceptable-delay target, functioning like a
miniature [SLO](service-level-objective.md) for the backlog itself) and an
escalation path — for example, automatically promoting a deferred item to
high priority once it crosses an age threshold — plus visibility into
queue age and size so operators can make an informed call about when to
re-enable shed work rather than unpausing everything at once and
re-triggering the same overload.
