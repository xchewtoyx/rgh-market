---
type: concept
title: Late Arriving Dimensions
description: Placeholder dimension rows created when a fact arrives before its full descriptive context is known, later corrected by overwrite once the context arrives.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

Facts sometimes arrive before their full dimensional context is available — anywhere from minutes to weeks — for example, a real-time inventory depletion event whose customer or product natural key can't yet be fully resolved against the [dimension-table](dimension-table.md). In these cases, a special dimension row is created with the unresolved natural key stored as an attribute and generic "unknown" values elsewhere (see [null handling in dimensional models](null-handling-in-dimensional-models.md)); when the real context arrives, the placeholder row is corrected via a [slowly changing dimension type 1](slowly-changing-dimension-type-1.md) overwrite.

Late arriving dimension data also occurs with retroactive changes to a [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) attribute discovered after the fact: a new dimension row is inserted for the corrected history, and the associated fact rows that should reference it must be restated. This is the dimension-side counterpart to [late arriving facts](late-arriving-facts.md), where instead a fact shows up after the dimensional context it should reference has already changed.
