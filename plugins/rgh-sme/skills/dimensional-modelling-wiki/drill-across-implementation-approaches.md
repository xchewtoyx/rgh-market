---
type: concept
title: Drill-Across Implementation Approaches
description: The three ways a BI tool or query can physically realize drilling across's two-phase procedure, and the fallback when a tool cannot drill across at all.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 4"
---

[Drilling across](drilling-across.md)'s two-phase procedure (per-fact-table aggregation, then a full outer join merge) can be physically realized in three ways:

1. **Splitting the processing.** Phase 1 queries run in the RDBMS; the intermediate result sets are sent to the reporting environment (desktop tool or app server), which performs the Phase 2 merge itself. Often criticized as inefficient — data crosses the network to be joined outside the database that's built for joining — but if the RDBMS pre-sorts each result set consistently, the reporting-side merge is a comparatively cheap sort-merge step, sometimes faster than doing it in the RDBMS.
2. **Using temporary tables.** Both phases stay in the RDBMS: Phase 1 results are spooled to temp tables, and a further query performs the Phase 2 join (and any ratio computation) against those temp tables inside the database, forwarding only the final result to the reporting environment. Keeps data on the RDBMS but shifts burden there — DBAs must provision temp space, watch join cost and log growth, and ensure temp tables are cleaned up.
3. **Leveraging SQL.** A single SQL statement expresses both phases: two subqueries (Phase 1) full-outer-joined by an enclosing query (Phase 2), using `COALESCE`/`NVL` to consolidate the dimension value from whichever subquery has it. Avoids explicit temp-table management, but the RDBMS performs equivalent work under the hood — the difference is which layer manages the staging.

A business intelligence tool can auto-generate drill-across processing using any of the three approaches via a **semantic layer** — a business-facing view of "things available to report on," mapped by a developer onto the physical schema, so that a user dragging fields onto a report canvas triggers query generation based on that mapping. In practice most vendors don't use the term "drilling across" at all, and some tools support it only in limited situations requiring specific configuration.

## When the tool can't drill across

Cube-based/[OLAP](olap-cube.md) tools in particular often permit interaction with only one cube at a time, so they may not support any of the three approaches above — the same problem arises if a supported approach performs poorly. The fix is to perform the drill-across operation in advance, at load time, storing the result in a dedicated [consolidated fact table](consolidated-fact-table.md) (or cube) built specifically for cross-process reports, while the original per-process fact tables remain in place for single-process analysis. Even when the toolset *can* drill across at query time, precomputing a table this way can still improve performance.
