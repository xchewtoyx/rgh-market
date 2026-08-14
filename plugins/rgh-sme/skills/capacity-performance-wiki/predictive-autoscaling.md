---
type: concept
title: Predictive Autoscaling
description: Scaling capacity ahead of demand using a forecast of expected load rather than reacting only to current utilization, needed when instance startup time is too slow to react to spikes as they happen.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 15"
---

Reactive autoscaling — scaling in response to a currently-observed [signal](autoscaling-signal-selection.md) — assumes new capacity comes online fast enough to matter before the triggering spike has already caused damage. That assumption breaks down when instance startup time is long relative to how fast demand can rise: if a new instance takes many minutes to become ready, a reactive autoscaler triggered by a fast-arriving spike adds capacity only after the spike has already overwhelmed the existing pool.

**Predictive autoscaling** addresses this by forecasting expected demand ahead of time and provisioning capacity to meet the forecast, rather than waiting for demand to actually materialize as an observed signal. This trades the simplicity of pure reactive scaling for lead time.

## When It's Needed

Predictive scaling matters most when a workload has three properties together:
- Slow instance startup (tens of minutes, not seconds) relative to how fast demand can change.
- Demand with predictable, recurring structure (daily/weekly usage patterns) rather than pure noise.
- A real cost to under-provisioning during the ramp (degraded user experience, dropped requests) that outweighs the cost of moderate over-provisioning ahead of a forecast.

Purely reactive [autoscaling safety bounds](autoscaling-safety-bounds.md) can't compensate for a startup-lag problem — no amount of tuning how fast the autoscaler reacts helps if the new capacity simply isn't ready in time. Predictive scaling is a different lever: it moves the reaction earlier, before the spike, rather than making the reaction faster.

## Forecasting Technique

One documented approach (Netflix's "Scryer" predictive autoscaling engine) combines three components on top of raw utilization telemetry:
1. **Outlier detection** to discard spurious data points before they distort the forecast.
2. **Fast Fourier Transform (FFT)** to identify and preserve legitimate recurring (e.g. daily, weekly) demand cycles in the historical signal.
3. **Linear regression** to project the identified pattern forward into a near-term demand forecast.

This combination is specifically suited to demand that is *not* Gaussian-distributed but *is* strongly periodic — ordinary mean/standard-deviation anomaly detection performs poorly on this kind of data (see the non-Gaussian telemetry problem this shares with alerting), but FFT-based cycle extraction handles it well because it doesn't assume any particular distribution shape, only recurring structure.

## Failure Modes of Reactive-Only Scaling That Predictive Scaling Fixes

- **Slow ramp-up:** a reactive scaler triggered only by an already-arrived spike can't add capacity fast enough if instance startup is slow — by the time new capacity is ready, the spike may have already caused user-visible failures.
- **Post-outage over-correction:** after an outage suppresses demand (e.g., users give up and stop retrying), a purely reactive scaler sees measured demand collapse and removes capacity aggressively — then gets caught flat-footed when demand rebounds as users return, compounding the original outage with a second capacity shortfall. This is a specific instance of [delayed feedback loop oscillation](delayed-feedback-oscillation.md): the scaler is reacting to a stale, artificially-depressed signal.
- **Ignoring known patterns:** a reactive scaler has no way to use the fact that, say, Monday evenings reliably see 3x weekday-average load — it only reacts once that load has already arrived, whereas a forecast-driven scaler can have the capacity ready in advance.

## Relationship to Reactive Scaling

Predictive and reactive autoscaling are complementary, not substitutes: the forecast sets a baseline capacity level tracking known demand structure, while reactive scaling (with its own [safety bounds](autoscaling-safety-bounds.md)) still handles the residual, unpredicted variance on top of that baseline. Neither the forecasting model nor the reactive fallback should be trusted alone — a forecast that has drifted from reality (a real product or traffic-pattern change) still needs a reactive layer as a backstop.
