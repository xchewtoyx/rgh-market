---
type: concept
title: Heatmaps vs. Percentiles for Visualizing Variance
description: When the spread/variance of a measurement across a population is itself the thing you need to see, a heatmap preserves that distribution shape directly, while collapsing the same data into percentile lines hides exactly the variance that matters.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 20"
---

[Percentiles](latency-percentiles-not-averages.md) are a good default for latency, but they're a lossy summary: a p50/p95/p99 line chart only shows a handful of points on the underlying distribution, and can look calm even while the shape of that distribution is changing underneath it. When the variance itself — not just a couple of summary points — is the thing worth seeing (e.g. node CPU or memory saturation across a fleet, where uneven bin-packing or noisy-neighbor effects show up as spread, not as a shift in the median), a **heatmap** (value on one axis, density/frequency as color intensity, typically over time) preserves the full distribution shape directly, rather than collapsing it to a few chosen percentiles.

This is a specific instance of a more general dashboard-design principle: pick the visualization that preserves the property of the data you actually need to reason about, rather than defaulting to whichever aggregate is most familiar. It parallels [percentile aggregates being misleading with a heterogeneous population](percentile-aggregates-misleading-with-heterogeneous-population.md) — both are cases where a standard, generally-good default aggregate (percentile lines) hides the specific thing an investigator needs to see, and a richer visualization (a heatmap, or a completion-rate proxy) recovers it.
