---
type: concept
title: Conformed Facts
description: The requirement that the same named measurement have an identical technical definition wherever it appears across fact tables.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4"
---

If the same measurement (revenue, profit, a standard price or cost, a quality or satisfaction score) appears in separate [fact-table](fact-table.md)s, its technical definition — the same underlying equation, the same dimensional context, the same unit of measure — must be identical wherever it is identically named, so that it can be compared or combined across tables via [drilling across](drilling-across.md). If exact conformance isn't possible, the facts must be given distinct names so users don't inadvertently combine incompatible values.

Setting up [conformed dimensions](conformed-dimensions.md) is roughly 95% or more of the enterprise data architecture effort; conforming facts is the remaining, smaller portion — but skipping it is just as damaging: unconformed facts sharing a name are a common way drill-across reports quietly produce wrong answers.

## Units of measure

A frequent source of non-conformance is a mismatch in units of measure along a [value chain](value-chain.md) — for example, product flow measured in shipping cases at a warehouse but in scanned units at a store. Burying a conversion factor in a dimension table for users to find and apply themselves is an unacceptable, error-prone solution. The correct approach is to carry the fact in both units of measure directly on the fact table, so a drill-across report can pick off comparable facts at each step of the value chain. See [multiple units of measure facts](multiple-units-of-measure-facts.md) for the equivalent technique applied within a single fact table.
