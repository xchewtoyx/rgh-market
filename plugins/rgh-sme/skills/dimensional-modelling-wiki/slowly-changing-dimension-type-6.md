---
type: concept
title: "Slowly Changing Dimension Type 6: Add Type 1 Attributes to a Type 2 Dimension"
description: Carrying both a historic (type 2) column and a current (type 1, overwritten across all versions) column for the same attribute on every dimension row.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 8"
---

Type 6 combines [type 1](slowly-changing-dimension-type-1.md), [type 2](slowly-changing-dimension-type-2.md), and [type 3](slowly-changing-dimension-type-3.md) in one dimension table — hence "6," since 1 + 2 + 3 = 1 × 2 × 3 = 6 (the numbering is deliberately playful, not a ranking). Each dimension row carries two versions of an attribute: a "current X" column, overwritten on *every* row for the entity — both past and newly issued — whenever the value changes, and a "historic X" column, fixed per row, reflecting what was true when that specific row was in effect.

On a type 2 change (a new row issued for the new value), the current-X column is updated across *all* rows sharing the entity's [durable key](durable-key.md), past and new, while historic-X is preserved per row exactly as type 2 would preserve it alone. The net effect: the historic column groups facts by the value in effect at the time of the measurement event; the current column rolls up all history, across every surrogate key version, under today's assignment — giving both perspectives from a single dimension table without a second join.

This is a hybrid technique, trading analytic flexibility for complexity; pursue it only when the business has confirmed the specific need for both views simultaneously — as with [type 3](slowly-changing-dimension-type-3.md), exposing many current/historic column pairs can overwhelm users, so consider limiting which columns are surfaced to which audiences. Compare [type 7](slowly-changing-dimension-type-7.md), which delivers the same functionality via two fact table foreign keys instead of extra dimension columns.
