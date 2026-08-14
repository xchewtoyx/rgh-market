---
type: concept
title: Lead Time for Changes
description: >
  One of the four DORA delivery-performance metrics, measuring the elapsed
  time from code commit to that code running in production.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 2"
---

# Lead Time for Changes

Lead time for changes is the elapsed time from **code commit** to **code
running in production**. It is one of the two "tempo" metrics in the DORA
four-key-metrics model, alongside [deployment frequency](deployment-frequency.md).

It deliberately excludes the "fuzzy front end" of product design and
development (high-variability, non-standardized work) and measures only
**product delivery** — commit to deploy — which is low-variability and
repeatable, and therefore comparable across teams and organizations.

Empirical performance tiers (2017 DORA benchmark):

- **High performers**: less than one hour.
- **Medium performers**: between one week and one month.
- **Low performers**: between one month and six months.

Short lead time is a delivery-safety enabler, not just a speed metric: a
pipeline that can get a fix from commit to production in minutes is what
makes [roll-forward a viable alternative to rollback](rollback-vs-roll-forward.md)
in the first place.
