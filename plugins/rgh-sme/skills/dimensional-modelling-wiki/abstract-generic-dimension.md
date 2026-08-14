---
type: concept
title: Abstract Generic Dimension
description: An anti-pattern that merges dissimilar entity types (e.g., employees, customers, vendors) into one generic dimension, harming performance and legibility.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

Some modelers are attracted to an abstract generic dimension — for example, one generic location dimension instead of embedded geographic attributes in separate store, warehouse, and customer dimensions, or one generic person dimension merging employees, customers, and vendor contacts. This should be avoided in the presentation-layer [dimension-table](dimension-table.md): the attribute sets genuinely differ per entity type, shared attributes (e.g., a "state" field) should be uniquely labeled per dimension rather than forced into one shared column, and merging the varieties invariably produces a single larger, sparser dimension table than keeping them separate.

This kind of abstraction may be appropriate in the operational source system or the ETL layer (for master data management purposes, for instance), but it hurts both query performance and legibility once it reaches the dimensional model itself.

## The Party/Party Role pattern, and when it's actually justified

The classic form of this generalization merges every *who*-type detail (customers, employees, suppliers, and so on) into one generic **Party** entity, with a separate associative **Party Role** entity recording each party's type or position. This is a genuine, deliberate design pattern — not merely a mistake — but its cost/benefit only clears the bar in a narrow case: where stakeholders truly care about entities that *switch roles over time* and need to analyze that switching (a person who is a supplier's contact today and an employee tomorrow; a regulator who later becomes a lobbyist for the industry they regulated). Absent that specific analytical need, collapsing dissimilar entities into one dimension is wasted at best and actively harmful at worst — a combined Customer/Employee dimension is confusing to query compared to two purpose-specific dimensions, exactly as described above.

The general caution extends beyond Party/Party Role: agile dimensional modelers should favor modeling each of the [7Ws](seven-ws-framework.md) as specifically as stakeholders actually describe it, reserving generalization for cases with an obvious, articulable business benefit (understanding a genuine cross-process commonality) rather than reaching for it by default. A model that values abstraction and flexibility over simplicity is harder for BI users to query than a transactional system, where structure is hidden behind an application interface — a warehouse has no such interface to hide behind. Generalizing purely for technical, DBA, or ETL convenience is a legitimate motive, but belongs in physical star-schema and ETL design, not the business-facing dimensional model, and should be postponed until that stage. Compare this to [role-playing dimensions](role-playing-dimension.md), which achieve a related kind of reuse (one physical table serving several roles) without merging dissimilar entity types — a role-playing date or employee dimension is a much safer generalization than a Party/Party Role merge, precisely because every role it plays is still the *same* kind of thing.
