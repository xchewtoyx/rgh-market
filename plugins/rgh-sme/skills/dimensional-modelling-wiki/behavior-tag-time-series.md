---
type: concept
title: Behavior Tag Time Series
description: Storing a sequence of periodic customer-cluster tags as positional attributes on the customer dimension, for simultaneous multi-period queries.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

Data-mining customer cluster analyses often produce a periodic textual behavior tag (e.g., a monthly cluster assignment such as "high value," "at risk," "dormant"). The resulting time series of tags should be stored as positional attributes directly on the [dimension-table](dimension-table.md) — one column per period, plus optionally a single concatenated full-sequence text string — rather than as a separate fact history, because these tags are the target of complex simultaneous queries across periods (e.g., "customers who were 'high value' in month 1 and 'at risk' by month 3") rather than of numeric computation.

The current-period tag value can additionally be placed in a [slowly changing dimension type 4](slowly-changing-dimension-type-4.md) mini-dimension, distinct from the full positional history kept on the customer dimension itself — this lets fact rows be analyzed by whichever behavior tag was in effect at the moment each fact row was loaded, rather than only by the customer's full historical tag sequence.
