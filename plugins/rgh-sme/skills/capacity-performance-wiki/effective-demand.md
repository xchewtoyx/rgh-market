---
type: concept
title: Effective Demand
description: An unbounded, regression-estimated measure of true resource demand — work actually serviced plus work that would have been serviced with more capacity — used to see past a saturated resource's artificial 100% utilization ceiling.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 8"
---

Measured [utilization](utilization-law.md) is capped at 100% by definition — a saturated CPU cannot report more than fully busy, no matter how much additional work is queued waiting behind it. This hides the true shape of demand: once a resource saturates, raw utilization measurements flatten out at exactly the moment demand is actually growing fastest, which is precisely the wrong time for a forecast input to go flat.

**Effective demand** is a derived, *unbounded* measure meant to see past this ceiling: it estimates the work actually serviced plus the work that *would have been* serviced had more capacity been available — analogous to the older mainframe concept of "latent demand." A value of 167% effective demand means the workload needed the equivalent of 1.67 servers' worth of capacity, even though only one, fully saturated, physical server existed to measure.

## How It's Estimated

Effective demand can't be measured directly (there's no meter for "unserved work"); it's estimated via multivariate regression against other collected metrics that keep moving even after utilization itself flatlines — such as run-queue length and its dispersion, which keep growing under saturation even while utilization sits pinned at 100%. Critically, utilization itself cannot be used as an input to this regression, since it's the very quantity whose ceiling the technique exists to see past.

## What It Assumes, and Where It Breaks

This is a statistical, not a structural, technique: it extrapolates from patterns in currently-collected metrics and implicitly assumes the *same* resource stays the bottleneck throughout the forecast horizon. It has no way to anticipate a *different* resource becoming the constraint once the modeled one is relieved — see [the law of bottlenecks](law-of-bottlenecks.md) for why that assumption eventually fails, and why effective-demand forecasts need periodic re-validation against reality rather than being trusted indefinitely once fit.

## Practical Use

A time series of effective demand (rather than raw, ceiling-capped utilization) is the more honest input to a growth-trend fit such as [the capacity doubling period](capacity-doubling-period.md) — fitting a growth curve to utilization data that's already been flattened by saturation understates both current demand and the true growth rate.
