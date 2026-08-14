---
type: concept
title: Smoothing and Anomaly-Detection Techniques for Periodic Telemetry
description: Moving averages, Fourier transforms, and the Kolmogorov-Smirnov test are statistical techniques for finding real anomalies in telemetry that has daily/weekly periodicity, without assuming a normal distribution the way mean/standard-deviation alerting does.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 15"
---

Much operational and user-behavior telemetry (web traffic, retail transactions, usage counts) has strong daily/weekly/yearly periodicity — comparing "is this Monday like other Mondays" is a more meaningful question than comparing against a global mean. Several techniques exploit this instead of assuming a [Gaussian distribution](statistical-threshold-alerting-limits.md):

- **Smoothing (moving/rolling averages)** — average each point against a sliding window to damp short-term noise and reveal the underlying trend. Variants: weighted moving average, exponential smoothing (recent points weighted more heavily).
- **Fast Fourier Transform (FFT)** — decomposes a time series into its periodic components, useful for isolating and preserving legitimate recurring spikes (e.g. daily traffic peaks) while smoothing out noise.
- **Kolmogorov-Smirnov (K-S) test** — a non-parametric test for whether two data sets differ significantly, making no assumption of normality. Well suited to comparing periodic/seasonal data directly (this week's Monday vs. other Mondays) and can catch anomalies — such as a Monday that fails to rebound to its expected volume — that a 3-standard-deviation rule misses entirely because the anomalous value still falls within the (skewed) global distribution.

These techniques are generally available in analysis tools built for time-series work (e.g. built into Graphite and Grafana) rather than requiring a bespoke statistics implementation, and the same periodicity that makes user-behavior data hard for naive thresholding is exactly what makes it tractable for these methods.
