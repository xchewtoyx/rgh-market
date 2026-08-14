---
type: concept
title: Durable Key
description: A permanent, DW/BI-assigned identifier for a real-world entity that never changes, used to tie together its multiple historical dimension rows.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3, 5"
---

A durable key (also called a supernatural key) is an identifier the DW/BI system assigns and controls, immutable for the life of the system, used when the [natural key](natural-key.md) from the source system isn't guaranteed to stay stable over time (organizational mergers, duplicate-entry cleanup, multi-source integration). The best format is a simple sequential integer starting at 1, independent of the source business process — the same shape as a [surrogate key](surrogate-key.md), but serving a different purpose.

A durable key is handled as a dimension *attribute*, like the natural key — it does not replace the [dimension-table](dimension-table.md)'s [surrogate key](surrogate-key.md) primary key. Its role is to identify one real-world entity across all of the multiple physical rows a [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) change can generate for it over time: while each type 2 change assigns a fresh surrogate key, the durable key stays fixed, and is described as "the glue that holds the separate type 2 rows for a single [entity] together" — the correct join column for distinct-count questions like "how many products," and the join column used by [slowly changing dimension type 6](slowly-changing-dimension-type-6.md) and [type 7](slowly-changing-dimension-type-7.md) to deliver current-value ("as-is") reporting alongside historically accurate ("as-was") reporting from the same dimension. [Behavior study group](behavior-study-group.md)s are also built on durable keys, so that group membership stays valid even as the customer dimension continues to accumulate type 2 history.
