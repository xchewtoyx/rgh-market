---
type: concept
title: Multiple Units of Measure Facts
description: Storing a fact once at a standard unit plus conversion factors in the same row, so views can present it in whatever unit each audience needs.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

When a fact must be stated in several units of measure (for example, pallets, ship cases, retail cases, and scan units for the same product movement), store the fact once at one standard unit, plus conversion factors between the standard unit and every other unit, all within the same [fact-table](fact-table.md) row. Deploy per-audience views that apply the appropriate conversion factor for that constituency.

Keeping the conversion factors in the fact row itself — rather than looking them up from a dimension at query time — keeps view calculations simple and guarantees correctness, since the exact factor in effect for that specific event travels with the event. This is the intra-table counterpart to the units-of-measure handling described under [conformed facts](conformed-facts.md), which addresses the same mismatch when it occurs across fact tables at different steps of a [value chain](value-chain.md).
