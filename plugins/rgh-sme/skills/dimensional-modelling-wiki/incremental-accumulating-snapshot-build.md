---
type: concept
title: Incremental Accumulating Snapshot Build
description: Whether to build an accumulating snapshot directly or from a sequence of individually-delivered transaction fact tables, depending on milestone cardinality and source-system risk.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4, 16"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 11"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

Whether an [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) is safe to build directly depends on what data profiling finds about its milestones: if every milestone genuinely has a 1:1 relationship to the others and all of them come from the same source system, building the accumulating snapshot directly is reasonable — there's no cardinality reduction to get wrong and no cross-system integration risk. The moment milestones have 1:M or M:M relationships (see [milestone cardinality discovery](milestone-cardinality-discovery.md)) and are sourced from more than one operational system, building the merged accumulating snapshot directly becomes high-risk, "big design up front" work unlikely to be delivered correctly within a normal sprint or two, with nothing demonstrable produced while it's underway.

In that riskier case, an incremental build sequence is the better path: model the evolving event's milestones first, then implement each milestone as its own simple [transaction fact table](transaction-fact-table.md) — far easier to build, test, and deliver individually, and each one delivers real BI value on its own well before the full accumulating snapshot exists. The accumulating snapshot is then assembled from those already-built, already-conformed transaction stars, which is comparatively straightforward merging rather than a single large integration effort — and the underlying transaction stars remain available afterward for the granular, explanatory drill-down the accumulating snapshot alone can't provide.

**Real-time caveat**: staging every milestone through its own fully-built transaction fact table first can introduce more latency than a same-day reporting requirement can tolerate. Where the staged milestone tables aren't themselves needed for direct querying, they can be built as unindexed tables truncated every load cycle, or bypassed altogether by piping ETL inserts and updates directly into the accumulating snapshot's own load process. Where both a low-latency current snapshot and queryable milestone-level detail are needed, staging as unindexed real-time partitions — merged into the full tables by the regular overnight load — supports both without duplicating the milestone data twice over.

Naming and documenting the durations that combining these milestones makes possible is best done with an [event timeline](event-timeline.md) before implementation begins.
