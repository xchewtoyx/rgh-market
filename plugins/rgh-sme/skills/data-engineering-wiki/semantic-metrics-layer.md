---
type: concept
title: Semantic / Metrics Layer
description: >
  Centralizing a business metric's definition in one governed place instead
  of re-embedding its logic in every ETL script and analyst query that needs
  it.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
---

Business-logic transformations are often far more complex than they look.
Computing something as apparently simple as "profit before marketing costs"
can require encoding a fraud-cancellation assumption; "profit after
marketing costs" additionally needs an attribution model connecting orders
to ad spend, and there are several legitimate ways to build that
attribution (naive price-weighted, department-level, per-item-click). This
is **derived data** — data computed from other stored data — and it creates
a consistency problem either way it's implemented: baking the logic directly
into ETL scripts violates DRY and makes updating the definition (a changed
attribution model, say) a manual, error-prone hunt across every script that
embeds it; leaving each analyst to reimplement the logic independently in
their own reporting queries is at least as bad, since getting every analyst
to consistently apply an updated definition is close to impossible.

The middle path is a **semantic** or **metrics layer**: business-logic
definitions are encoded once, centrally, and the layer generates the
underlying queries against the warehouse from that single definition.
Analysts and dashboard builders then compose from a governed metric library
rather than re-deriving "profit" or "active customer" from scratch every
time. This keeps [data quality](data-quality-dimensions.md)'s accuracy
dimension enforceable at the definition level instead of relying on every
downstream consumer getting the same complex logic right independently, and
it gives a schema or business-rule change exactly one place to land instead
of many.

For the simpler case of a single additive derived fact rather than a
multi-step business metric, [materializing it once during the load and
decomposing non-additive ratios into stored components](ratio-decomposition-and-derived-fact-materialization.md)
solves the same consistency problem at the load-mechanics level, without
standing up a full governed layer.
