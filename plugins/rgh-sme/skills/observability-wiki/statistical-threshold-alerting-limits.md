---
type: concept
title: Statistical Threshold Alerting and Its Limits on Non-Gaussian Data
description: Alerting when a metric deviates by N standard deviations from its mean is a cheap way to avoid hand-tuning thousands of static thresholds, but it badly over- or under-alerts on the skewed, non-Gaussian distributions common in operational telemetry.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 15"
---

A basic statistical alerting technique: compute a metric's mean and standard deviation over a trailing window, and alert when a new value deviates by more than N standard deviations (commonly 3). Under a Gaussian/normal distribution, 3 standard deviations should contain 99.7% of the data, so this should page only rarely — and it avoids the impossible task of hand-setting a static threshold for every one of thousands (or hundreds of thousands) of metrics.

**The technique breaks down when the underlying data isn't Gaussian**, which is the common case for operational telemetry (e.g. downloads per minute: mostly near-zero with recurring spikes, not symmetric around a mean). Symptoms of this failure:

- **Over-alerting**: a skewed histogram makes the 3-SD rule fire almost continuously, training responders to ignore it — see [alert fatigue](alert-fatigue-and-normalized-deviance.md).
- **Nonsensical results**: computing "3 SD below the mean" for a count metric can yield a negative number, which is meaningless.
- **Under-alerting**: a real, severe problem (e.g. a 50% mid-day drop in completed transactions from a component failure) can still fall within 3 SD of a noisy mean, so no alert fires and customers discover the outage before operators do.

The fix is not to abandon statistical alerting but to use techniques that don't assume normality — see [smoothing and anomaly-detection techniques](smoothing-and-anomaly-detection-techniques.md), several of which (notably the Kolmogorov-Smirnov test) are specifically designed for this kind of skewed, periodic data.

The same fixed-cutoff brittleness shows up in liveness/health checking, not just metric alerting — see [adaptive liveness detection vs. fixed timeouts](adaptive-liveness-detection-vs-fixed-timeouts.md) for the accrual-detector approach of scoring suspicion continuously instead of hard-coding one timeout.
