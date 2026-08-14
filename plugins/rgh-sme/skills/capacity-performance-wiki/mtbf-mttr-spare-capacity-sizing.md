---
type: concept
title: MTBF/MTTR-Based Spare Capacity Sizing
description: How much spare capacity an N+M pool needs is a function of how often units fail (MTBF) relative to how long it takes to replace a failed one (MTTR), not a fixed rule of thumb — and pool granularity determines how expensive that spare capacity is to carry.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

Choosing $M$ in [N+M redundancy](n-plus-m-redundancy.md) is a quantifiable trade-off, not an arbitrary safety margin: the extra capacity is insurance against a second failure occurring before the first is repaired, and its cost scales with how big and how granular the pool is.

## The Core Ratio: MTTR / MTBF

**MTBF** (mean time between failures) measures how often a unit fails; **MTTR** (mean time to repair) measures how long a failed unit stays out of service before it's restored. The probability of a *second* failure occurring while the first is still being repaired is approximately:

$$\frac{\text{MTTR}}{\text{MTBF}} \times 100\%$$

A repair window of one week against a 100,000-hour MTBF gives roughly a 1.7% (about 1-in-60) chance of a second failure landing during that repair — survivable with a single spare. The same one-week repair window against a 336-hour (two-week) MTBF gives a 50% chance — a coin flip that clearly justifies carrying a second spare on top of the first. MTTR itself varies enormously by failure type and is often the harder number to pin down: a crashed process might restart in seconds, an on-site disk swap might leave a system under-redundant for a long rebuild window, and a physically remote hardware failure might take weeks once parts have to be sourced and shipped — the sizing calculation is only as good as the MTTR estimate feeding it.

**Rule of thumb:** N+1 as a baseline minimum for any service that can't tolerate an outage; N+2 once the MTTR/MTBF ratio makes a second failure during the first repair a realistic possibility, not just a theoretical one.

## Pool Granularity Determines How Expensive the Insurance Is

The same *proportional* redundancy costs very different amounts of idle capacity depending on how large the pool is: 1+1 redundancy wastes 50% of provisioned capacity sitting idle in the normal case, while 20+1 wastes under 5% for the equivalent "survive one failure" guarantee. Bigger, more finely-divided pools are strictly more capital-efficient per unit of redundancy purchased — this is a direct argument for preferring many smaller units over few large ones when redundancy cost matters, independent of any other capacity consideration.

## A Reframing: Capacity Gauge, Not Binary Health

Sizing spares this way changes what's worth monitoring and alerting on. A pool with real spare-capacity accounting turns "is the service up or down" (binary) into "how much spare capacity headroom remains" (continuous) — operational attention shifts from paging the instant any single unit fails to alerting only as the capacity gauge approaches the threshold where a further failure would cause a real shortfall. This is the same shift in framing that [capacity headroom safety margin](capacity-headroom-safety-margin.md) makes for demand-driven headroom; here the headroom is being consumed by failures instead of by demand growth, but the gauge-not-switch mental model is identical.
