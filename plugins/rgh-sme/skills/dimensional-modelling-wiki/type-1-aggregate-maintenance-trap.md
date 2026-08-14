---
type: concept
title: Type 1 Aggregate-Maintenance Trap
description: Why an aggregate fact table whose rollup dimension carries a type 1 attribute can't simply be refreshed by appending new activity, and the two common resolutions.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 15"
---

An [aggregate fact table](aggregate-fact-table.md) whose rollup dimension carries a [slowly changing dimension type 1](slowly-changing-dimension-type-1.md) attribute can't simply be refreshed by appending new activity, because a type 1 change on the base dimension can invalidate rows the aggregate already summarized in the past. If a product's manager attribute (type 1) is reassigned from one manager to another, loading the base dimension first overwrites the old manager value in place — by the time the aggregate fact table is loaded, prior orders for that product are still summarized under the old manager's aggregate row, but the base dimension no longer records that the old manager was ever associated with that product, so there's nothing left to correct *from*. Fixing this after the fact requires having captured both the before and after values of the change and still having access to the granular fact data to find and re-attribute the affected historical rows — extra complexity many teams decide isn't worth carrying. The common resolutions are to drop and rebuild the whole aggregate fact table whenever a type 1 attribute in its rollup dimension changes (often the default behavior of automated aggregate/cube tooling), or to exclude type 1 attributes from aggregate dimension designs altogether. A [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) attribute doesn't cause this problem in the first place, since it never restates the context already recorded against existing facts.
