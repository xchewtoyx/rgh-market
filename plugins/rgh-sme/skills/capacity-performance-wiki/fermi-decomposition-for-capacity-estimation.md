---
type: concept
title: Fermi Decomposition for Capacity Estimation
description: Breaking an unmeasured demand or capacity quantity into a chain of smaller sub-quantities that can each be estimated from what's already known produces a usable range far faster than waiting for direct measurement, and reveals which sub-estimate is driving the uncertainty.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything: Finding the Value of Intangibles in Business (Douglas W. Hubbard), ch. 2, ch. 4"
---

Capacity planning often needs a number for something that hasn't been directly measured yet — expected load for a feature that hasn't shipped, peak demand for a market that hasn't been entered, cost impact of an outage class that hasn't happened at the current scale. **Fermi decomposition** (after Enrico Fermi's estimation technique) produces a usable estimate for exactly this situation by splitting the unknown quantity into a chain of smaller sub-quantities, each of which is easier to bound from data or judgment already on hand, then combining them.

## The Technique

Decompose the target quantity into a multiplicative or additive chain of sub-factors — each one something a domain expert can put a defensible range on, even if the top-level quantity feels unknowable. A capacity-planning example: estimating additional support-ticket load from a new feature might decompose into (expected daily active users) × (fraction who try the new feature) × (fraction of trials that hit a rough edge) × (fraction of rough edges that generate a ticket) — none of these four factors is easy to know exactly, but each is far easier to bound than the combined quantity, and historical data or comparable-feature experience usually exists for at least some of them.

This is explicitly **not itself a measurement** — no new observation is made — it's an organized assessment of what's already known, structured well enough to (a) produce a usable range immediately, and (b) reveal which sub-factor's uncertainty is doing the most damage to the overall range, which is exactly where a real measurement (an instrumented rollout, a small pilot, a targeted query against existing logs) would pay off most.

## Why Decomposing Improves Accuracy, Not Just Speed

Decomposition isn't just a stalling tactic while waiting for real data — controlled comparisons of direct estimation against decomposed estimation on high-uncertainty quantities found decomposing into as few as five sub-variables reduced estimate error by a factor of 10 to 100, compared to guessing the combined quantity directly. The effect is strongest precisely where uncertainty is highest and direct intuition is weakest — which is exactly the situation capacity planning faces for genuinely novel demand (a new feature, a new market, a first-of-its-kind failure mode), not for quantities already well characterized by existing telemetry.

## Where This Fits in a Capacity Workflow

When one of the sub-factors in a decomposition is itself an operation's latency or resource cost rather than a demand quantity, [cost of common operations](cost-of-common-operations.md) supplies the ballpark figures (network round-trips, storage I/O, allocation, cache misses) to bound that sub-factor without a fresh measurement.

Fermi decomposition is a stand-in for [effective demand](effective-demand.md) or a proper [capacity doubling period](capacity-doubling-period.md) fit when neither has enough real data behind it yet — a bridge to get a defensible planning number now, with an explicit map of which sub-estimate to go measure first once the decision is consequential enough to justify the cost of measuring. Once real telemetry exists for the launched feature or entered market, replace the decomposed estimate with the measured one rather than continuing to reason from the original guess.
