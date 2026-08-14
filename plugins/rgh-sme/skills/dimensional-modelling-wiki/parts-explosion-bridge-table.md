---
type: concept
title: Parts Explosion Bridge Table
description: A ragged hierarchy bridge table joined through its parent key to roll a finished product's demand down into its components, rather than rolling components up.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 7"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 10"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

A [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md) also handles a bill-of-materials hierarchy — components made of other components, cascading down to raw parts — with one structural difference from an organization or ownership hierarchy: it is typically joined to facts through its **parent** key rather than its child key, since the analytic question is usually "roll this finished product's sales down into demand for its components" rather than "roll these components up into a parent." This direction of use is sometimes called a **parts explosion** or reverse hierarchy map. A **sub-assembly flag** marks whether a given component is itself built from further components (versus being a raw, unsplittable part), mirroring the lowest-child flag used for ordinary rollups.

The natural extra attribute here is **quantity** — how many of a given component go into its immediate parent — and quantity must be allowed to cascade multiplicatively along indirect paths exactly the way a weighting factor does for a shared-ownership bridge: a component several assembly levels removed from a finished product contributes the *product* of every intermediate quantity along the path (two of a defense system per car, four sensors per defense system, means eight sensors per car), not the quantity of its own immediate parent relationship alone. A cost or revenue-recovery weighting factor can be layered on top of the quantity column the same way an ownership percentage is layered onto a shared-ownership bridge, to allocate a bundled product's revenue across its components by their quantity and unit value.

Parts-explosion bridge tables grow according to the same level-by-level row-count math as any other bridge table, but a genuinely deep, highly reused bill of materials (a car, a submarine, an aircraft) can multiply out to an impractically large table — [estimating the tree's size](bridge-table-sizing-and-display.md) before committing to this pattern matters even more here than for typical organizational hierarchies.
