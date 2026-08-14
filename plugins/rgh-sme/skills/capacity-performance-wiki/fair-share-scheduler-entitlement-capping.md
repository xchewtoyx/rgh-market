---
type: concept
title: Fair-Share Scheduler Entitlement and Capping
description: Fair-share schedulers give each tenant a resource entitlement proportional to their allocated shares of currently-active shares, not the whole pool — meaning uncapped tenants can silently receive far more than their nominal entitlement whenever other tenants are idle.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 7"
---

**Fair-share scheduling** (used by hypervisors, enterprise UNIX resource managers, and container CPU-share mechanisms alike) allocates a physical resource among tenants proportional to administrator-assigned shares, rather than time-slicing it equally the way a plain time-share scheduler does. "Fair" here means *equity*, not *equality* — like corporate shareholding, a tenant with more shares gets a proportionally larger slice, not an identical one.

## Entitlement Is Computed Against Active Shares, Not Total Shares

A tenant's entitlement is:

$$E_i = \frac{S_i}{\sum_k S_k^{active}}$$

The denominator is the sum of shares belonging to *currently active* tenants, not the full nominal pool. This has a consequence that's easy to miss: a tenant with a nominal 10% entitlement who happens to be the *only* active tenant at some moment receives 100% of the resource, not 10% — because the other 90% of shares aren't contributing to the denominator while their owners are idle.

## Why This Creates a Governance Problem, Not Just a Technical One

This dynamic, demand-responsive behavior is usually desirable from a pure utilization standpoint (idle capacity doesn't go to waste), but it creates a real operational risk: tenants who experience occasional above-entitlement performance during other tenants' quiet periods come to expect that level of performance permanently, and will push back (at the next capacity review or SLA renewal) when contention returns it to their nominal share. A period of good luck silently redefines the tenant's expected baseline.

## Capping as the Fix

Where chargeback accounting or SLA guarantees matter, entitlement should be explicitly **capped** — a hard ceiling that prevents a tenant from exceeding their nominal share even when the resource is otherwise idle. This trades away some aggregate utilization (the ceiling leaves capacity unused rather than lending it to an under-entitled tenant) for predictability: a capped tenant always gets exactly what they were promised, with no future performance-expectation surprises to manage. Not every fair-share implementation offers a capping option, which makes checking for it explicitly worthwhile before relying on a fair-share mechanism for multi-tenant capacity guarantees. This is the same underlying tension addressed by [bulkhead pattern](bulkhead-pattern.md) resource isolation and by [container CPU throttling](container-cpu-throttling.md) limits — hard isolation trades some efficiency for predictability, versus soft/shared allocation that trades predictability for efficiency.
