---
type: concept
title: Audit Dimension
description: A dimension attached to a fact row at ETL time to capture data-quality and processing metadata for compliance and troubleshooting.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

When a [fact-table](fact-table.md) row is created during ETL, an audit dimension can capture processing metadata known at that time — basic data-quality indicators (potentially sourced from an [error event schema](error-event-schema.md)), the ETL code version that produced the row, or process execution timestamps. This is useful for compliance and auditing, letting a BI tool drill down from any fact row to determine which ETL software version created it and what quality checks it passed.

A practical way to key it: one audit row per *execution* of an ETL process, not per fact row — a nightly load with five ETL modules adds at least five new audit rows every night, and every fact or dimension row created or updated by a given execution carries that run's audit key. This directly gives basic lineage (which run touched this row, from which source, by which extraction/load method, at what time) without needing per-row audit metadata, while still letting per-execution indicator attributes flag quality or completeness concerns — out-of-bounds relative to profiled history, missing, adjusted, or allocated — that a query can filter or group by exactly like any other dimension.

This metadata is of interest not only to the ETL/IT team, but sometimes directly to business users asking questions like "what's my confidence in these numbers?" or "what version of the cost-allocation or currency-conversion logic produced this row?" — so example attributes include a general quality indicator, an out-of-bounds indicator, an amount-adjusted flag, and environmental variables such as which cost-allocation or currency-conversion rule version was in effect. Because it is an ordinary dimension, one of these indicators (e.g. out-of-bounds) can simply be dropped into a standard report to produce an "instrumented" report that shows normal and abnormal rows side by side, without any special tooling.

Start modest: limit the audit dimension's attribute set and the resulting number of distinct audit rows, to keep ETL complexity bounded — an audit dimension that tries to capture everything becomes as unwieldy as the process it's meant to make legible.
