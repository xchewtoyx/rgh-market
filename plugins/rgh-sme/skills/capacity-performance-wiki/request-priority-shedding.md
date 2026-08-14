---
type: concept
title: Request Priority Shedding
description: A server-side overload response that categorizes incoming requests into priority tiers and rejects the lowest tiers first, preserving capacity for the traffic that matters most under saturation.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 21"
---

**Request priority shedding** is a server-side overload response: rather than treating all incoming requests as equally important once capacity runs out, the server classifies requests into priority tiers ahead of time and, under overload, rejects the lowest tiers first so the finite remaining capacity goes to the traffic that matters most.

## A Typical Tier Scheme

*   **Critical-plus:** essential production requests whose failure has severe consequences — shed only as an absolute last resort.
*   **Critical:** normal user-facing requests — the traffic the service exists to serve.
*   **Sheddable-plus:** non-urgent background operations that can tolerate delay or failure without direct user impact.
*   **Sheddable:** batch and low-priority traffic — the first and cheapest capacity to give up under load.

Under overload, the server rejects requests starting from the lowest tier upward (typically returning an explicit "unavailable" response) until remaining demand fits within available capacity, rather than degrading service quality uniformly across all traffic or, worse, collapsing entirely.

## Why Tiering Beats Uniform Degradation

Without tiers, a server under overload either serves everything slowly (risking the [queueing latency blow-up](mm1-queue-model.md) that pushes response times toward timeout for all requests) or fails requests indiscriminately regardless of importance. Tiering converts an undifferentiated capacity shortfall into a controlled trade: capacity is deliberately reallocated away from the traffic that can most afford to lose it, protecting the traffic that can't. This requires the classification to be assigned deliberately in advance (by the caller declaring its own priority, or by a policy applied at the server) — a server cannot infer priority from the request itself after the fact.

## Relationship to Other Overload Mechanisms

Priority shedding decides *what to reject*; it works alongside mechanisms that decide *when* to reject and *how to queue* what's accepted — see [adaptive client-side throttling](adaptive-throttling.md) for reducing load before it reaches the server, and [LIFO vs. FIFO queueing under overload](lifo-vs-fifo-queueing-under-overload.md) for how accepted-but-not-yet-processed requests should be ordered once a queue starts forming. More generally, tiered rejection is fixed-priority scheduling taken to its logical extreme — see [request scheduling policy selection](request-scheduling-policy-selection.md) for the fuller space of policies that decide serving order rather than outright rejection.
