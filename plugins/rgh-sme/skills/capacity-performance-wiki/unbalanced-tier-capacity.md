---
type: concept
title: Unbalanced Tier Capacity
description: Scaling each tier of a multi-tier system independently, without coordinating their relative capacity, lets a well-scaled front end overwhelm a comparatively under-scaled back end even though neither tier individually looks broken.
sources:
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 4"
---

A layered system — a web/API front end backed by a database, a legacy system, or another internal service — is often scaled tier by tier: the front end gets more instances to handle rising request volume, without a matching look at whether the tier behind it can actually absorb the traffic that added capacity is now able to generate. A front end provisioned to accept 10,000 requests/second in front of a database or legacy system that can only sustain 500 requests/second isn't protected by the front end's own healthy capacity numbers — it's a bigger funnel pointed at the same narrow opening, and it will drive the back end into overload faster, not avoid it.

## Why This Slips Past Normal Capacity Review

Each tier's own utilization and headroom can look fine in isolation: the front end has room to grow, and the back end's *steady-state* utilization looks acceptable under current traffic. The imbalance only becomes visible once the front end's added capacity lets through a burst the back end was never sized for — at which point the back end saturates while the front end's own dashboards show it operating well within its limits, which can misdirect troubleshooting toward the wrong tier during an incident.

## Mitigation

*   **Capacity-plan tiers together, not independently.** Any decision to add capacity to one tier should be checked against whether the tiers it depends on can absorb the resulting demand — see [capacity headroom](capacity-headroom-safety-margin.md) for sizing a single tier's safety margin; this is the same question applied across a dependency chain rather than within one component.
*   **Protect the narrower tier explicitly** with [concurrency limiting as admission control](concurrency-limiting-as-admission-control.md) or rate limiting at the boundary between tiers, so a traffic burst the front end can handle doesn't reach the back end faster than the back end can process it.
*   **Track the ratio between tiers' capacities, not just each tier's own utilization**, as an explicit capacity-planning input — a front end that scales without a corresponding plan for what it fans out to is scaling the exposure to the bottleneck, not the system's real throughput ceiling.
