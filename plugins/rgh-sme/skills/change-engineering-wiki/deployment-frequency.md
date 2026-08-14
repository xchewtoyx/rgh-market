---
type: concept
title: Deployment Frequency
description: >
  One of the four DORA delivery-performance metrics, measuring how often an
  organization ships to production, used as an operational proxy for batch
  size.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 2"
---

# Deployment Frequency

Deployment frequency measures how often an organization successfully
releases to production. It is one of the two "tempo" metrics in the DORA
four-key-metrics model, alongside [lead time for changes](lead-time-for-changes.md).

It matters as a delivery-safety metric, not just a speed metric, because it
is an inverse operational proxy for [batch size](working-in-small-batches.md):

    deployment frequency ≈ 1 / batch size

Higher deployment frequency directly implies smaller batches per release,
which reduces cycle time and flow variability — and, per the
[speed-stability trade-off myth](speed-stability-tradeoff-myth.md), higher
frequency correlates with *lower* [change failure rate](change-failure-rate.md),
not higher.

Empirical performance tiers (2017 DORA benchmark):

- **High performers**: on-demand, multiple deploys per day.
- **Medium performers**: between once per week and once per month.
- **Low performers**: between once per month and once every six months.
