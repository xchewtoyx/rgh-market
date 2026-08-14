---
type: concept
title: Mini-Dimension Load Mechanics
description: >
  Loading a frequently-changing attribute cluster into its own small
  dimension keyed by attribute combination, joined into the fact table
  alongside the parent dimension's own key, instead of Type-2-versioning
  the parent dimension itself.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 5"
---

When a large, frequently-changing dimension (millions of customer rows,
demographic attributes that shift often) would otherwise need
[Type 2 versioning](insert-only-history-pattern.md), the resulting row
explosion becomes a load and browse-performance problem in its own right.
The mini-dimension pattern sidesteps it by splitting the volatile attributes
into their own small dimension table, keyed **by attribute combination**
rather than by parent-entity — one row per distinct combination of
age-band/income-band/purchase-frequency-band actually observed, not one row
per customer.

Load-mechanics consequences that don't apply to the parent dimension's own
Type 2 processing:

- **Build only the combinations that actually occur**, rather than
  materializing the full cross product of every band value up front — the
  full cross product (e.g., 5 attributes × 10 values each ≈ 100,000 rows) is
  a workable upper bound but wasteful when the load can instead mint a new
  mini-dimension row only the first time a combination is actually seen in
  the data.
- **Every fact row carries two related-entity foreign keys**, not one: the
  parent dimension's own (Type 1 or durably keyed) key, plus the
  mini-dimension key that was in effect at event time. A periodic-snapshot
  load naturally captures this by re-resolving the current mini-dimension
  key on every snapshot row, without ever touching or reprocessing earlier
  snapshot rows.
- **Continuous values must be banded before lookup**, not banded on the fly
  at query time — the mini-dimension row a fact resolves to is determined by
  which band the raw value falls into at load time, so changing band
  boundaries later means reprocessing which mini-dimension rows historical
  facts point to, not just relabeling existing rows.
- **A profile change with no accompanying fact event still needs to be
  captured** if point-in-time accuracy matters — a customer's demographic
  band can change between transactions. Where that matters, load a
  supplemental fact table with no measures of its own, keyed by
  parent-entity, mini-dimension key, and an effective/expiration date pair
  in the same style as the [insert-only history
  pattern](insert-only-history-pattern.md), purely to record every
  profile-key transition as it happens, independent of whether a business
  event triggered it.
