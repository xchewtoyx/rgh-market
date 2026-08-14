---
type: concept
title: Aggregated Fact as a Dimension Attribute
description: >
  Embedding a precomputed aggregate (lifetime spend, last year's total) as a
  dimension attribute so users can constrain on it directly, and the
  ongoing load burden that convenience creates.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 8"
---

This is one variant of the broader [behavioral dimension
pattern](behavioral-dimension-load-mechanics.md) — pushing past-behavior
computation into the load instead of computing it at query time. Users often
want to filter a dimension directly on an aggregated performance
metric — "customers who spent more than $X last year," or by lifetime
spend — rather than joining to the fact table and aggregating first. Storing
that aggregate as an ordinary dimension attribute (for constraining and
labeling only, never as an input to further numeric calculation) supports
that workflow directly, but it moves real, ongoing work onto the load: the
attribute has to be kept accurate and consistent with the fact rows it
summarizes, which is a second, separate consistency obligation on top of
whatever [aggregate table](aggregate-table-load-consistency.md) load
strategy the pipeline already runs for query-performance rollups.

Two load-design choices keep this manageable:

- **Only embed aggregates that are actually used often enough to justify the
  ongoing sync cost** — every additional embedded aggregate is another
  column the load has to keep current, not a one-time addition.
- **Prefer aggregates that refresh infrequently over ones that don't**: last
  year's total spend only needs updating once a year, while a year-to-date
  total needs updating on every load — pick the lower-maintenance framing
  wherever the business need allows it.

A further mitigation worth considering: replace or supplement the raw
numeric aggregate with a descriptive label derived from it (e.g., "High
Spender" instead of a literal dollar figure). A label is more resilient to
the aggregate drifting slightly out of sync with the underlying facts than a
precise number would be, and it gives every consumer the same shared
definition of "high spender" instead of each user applying their own
threshold to a raw value.
