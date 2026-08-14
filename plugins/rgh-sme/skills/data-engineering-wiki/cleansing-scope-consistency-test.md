---
type: concept
title: Cleansing Scope Consistency Test
description: >
  A concrete test for deciding whether a proposed ETL cleansing step belongs
  in the pipeline at all — does it still leave the result consistent with
  what the operational source system itself would report.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Adamson), ch. 17"
---

A pipeline is often asked to clean up messy source data, but not every
cleansing request belongs in the load process — some genuinely belong back
at the operational source instead. The governing principle: a warehouse's
job is to **publish** operational data restructured for analysis, not to
**create** or reinterpret facts. Doing the latter produces a warehouse whose
numbers no longer match what the source systems themselves would report,
which is exactly what erodes a warehouse's credibility with business users
who cross-check it.

The concrete test for any proposed cleansing step: **will this action result
in a fact that is still consistent with the operational data?** Reformatting
a phone number, supplementing a code with its reference text, concatenating
fields, or turning a boolean flag into descriptive text all pass — they
enrich presentation without changing what the fact actually says. Silently
correcting a misassigned salesperson on an order fails the test: it makes
the warehouse disagree with the source system's own figures, which is only
acceptable if the correction happens in the source system too, in which case
the pipeline is simply publishing the corrected value rather than inventing
one on its own.

A useful side effect of holding this line: a warehouse that surfaces rather
than silently repairs source-data problems becomes a diagnostic tool for
driving cleanup of the *operational* systems themselves — see [data
profiling](data-profiling-before-ingestion.md) for the earlier point in the
pipeline lifecycle where this same surfacing role starts.

Where a cleansing rule does pass the test and is worth automating, prefer
expressing it as a **data-driven mapping table** the pipeline references at
load time (e.g., a table mapping each source system's inconsistent brand
codes to one standardized code) over hard-coding the rule directly into
pipeline logic. A mapping table documents the rule as data, and a source
system changing its coding scheme only needs a row updated rather than a
code change — though at high volume, a mapping-table lookup can be expensive
enough that hard-coding is still the right performance trade-off; even then,
keep the table around as documentation for developers and QA even if it's
no longer consulted at runtime.
