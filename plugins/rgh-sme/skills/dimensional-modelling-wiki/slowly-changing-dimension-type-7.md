---
type: concept
title: "Slowly Changing Dimension Type 7: Dual Type 1 and Type 2 Dimensions"
description: Carrying both a durable key and a type 2 surrogate key on the fact table so it can support current-value and as-was reporting from the same dimension.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
---

Type 7 delivers the same functionality as [type 6](slowly-changing-dimension-type-6.md) — supporting both as-was and as-is reporting from one dimension — but via two [fact-table](fact-table.md) foreign keys instead of extra dimension columns: the entity's [durable key](durable-key.md) (or a separate durable key, if the natural key is unwieldy or reassignable), alongside the ordinary [type 2](slowly-changing-dimension-type-2.md) surrogate key.

The type 2 dimension holds historically accurate attributes for point-in-event filtering and grouping, exactly as in plain type 2. A second table or view exposes only current (type 1) values, keyed by the durable key, filterable and joinable independently of history:

- **Type 1 perspective**: constrain to the current-row flag, and join to the fact table via the durable key.
- **Type 2 perspective**: don't constrain the current-row flag, and join via the surrogate key.

These two perspectives are typically deployed as separate BI views. Type 7 usually costs less ETL effort than type 6, since the type 1 "current" table can be a view over the type 2 dimension filtered to current rows — queries against current values then hit a smaller table than the full type 2 dimension. The cost is an extra fact table column (the durable key); an alternative is to join the type 1 view to the durable key inside the type 2 dimension itself and skip storing it on the fact table, but then current-only queries must traverse the larger type 2 dimension first, hurting performance. A variation associates the current attribute values with *every* type 2 row sharing a durable key, rather than filtering to only current rows — both dimension tables end up with the same row count but different contents.

## "As of" reporting

Because the fact table carries the durable key, type 7 also supports rolling up historical facts by *any* specific point-in-time profile — not just current or event-time — by filtering the type 2 dimension's effective/expiration dates to a target date to get exactly one row per durable key, then joining to the fact table on the durable key (the effective/expiration filter is required, or multiple type 2 rows per durable key will multiply the results). This capability is recommended only for a limited, highly analytic audience given the complexity — "not for the timid."
