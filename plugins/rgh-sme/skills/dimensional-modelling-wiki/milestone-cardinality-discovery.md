---
type: concept
title: Milestone Cardinality Discovery
description: How to check the cardinality relationship between each pair of milestones before merging them into one accumulating snapshot row, and how to handle each case.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4, 16"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 11"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

Before merging several discrete events' milestones into one [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) row, check the cardinality relationship between each pair of milestones — this is a discovery-time question, best asked directly of stakeholders ("how many shipments can there be for one ordered product?"), not an assumption. The right handling depends on what's found:

- **1:1** — each order has exactly one shipment has exactly one delivery, say. Combining is straightforward: nothing is lost, and the milestone's details attach directly to the evolving event with no reduction needed.
- **1:M** (the milestone repeats) — several shipments and deliveries fulfilling one order, for instance. Because an accumulating snapshot holds one row per process instance, every repeating milestone's details must be reduced to a single value before they can attach: sum additive quantities (total quantity delivered so far, across every partial delivery) and take the most recent value for anything else (the latest delivery date and carrier, say) — a natural fit, since an accumulating snapshot's job is to summarize current progress, not preserve full milestone-by-milestone history. If stakeholders genuinely need every individual milestone occurrence, not just the current summarized state, that detail belongs in its own atomic-grain [transaction fact table](transaction-fact-table.md) instead — see [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) for why the accumulating snapshot alone can't stand in for it — model both, rather than distorting the accumulating snapshot to carry history it isn't designed for.
- **M:1** (the milestone is on the "many" side, several process instances converging on one milestone occurrence) — a single shipment partially fulfilling two separate orders, for instance. This needs an explicit allocation rule to split any additive quantity across the instances it covers (190 shipped units splitting 100/90 across two orders) — the same allocation-ownership caution that applies to any other allocated measure: the rule belongs with the business, not picked unilaterally by the design.
- **M:M** — a milestone that can't be cleanly reduced to either side. This is usually a sign that milestone's detail doesn't belong folded into the accumulating snapshot at all; leave it as its own separately queried event instead of forcing a bad reduction.

What this discovery finds determines whether it's safe to build the accumulating snapshot directly, or better to build it incrementally — see [incremental accumulating snapshot build](incremental-accumulating-snapshot-build.md).
