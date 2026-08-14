---
type: concept
title: Designing From Reports Antipattern
description: The mistake of designing a fact table around one intended report instead of around the underlying measurement process, leading to schema proliferation.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 16"
---

A [fact-table](fact-table.md) should represent a measurement process — facts derive from numeric measurements, and dimensions describe the circumstances of those measurements — independent of how any single user happens to want to frame a report. Designing directly from a report's layout, rather than from the underlying [business process](business-process.md) and its [grain](grain.md), is a serious design mistake: it produces a schema tightly coupled to one requester's current question, unable to serve the next question without a redesign.

The failure mode compounds: one project team built several hundred report-specific fact tables, each extracting the same underlying order management data repeatedly with a slightly different shape, and as a result could not fit the ETL workload into the nightly batch window. The fix would have been a single well-designed atomic-grain schema plus a handful of performance [aggregate fact table](aggregate-fact-table.md)s, not report-driven schema proliferation — an atomic schema, correctly grained, can answer arbitrary future analytic requests through ordinary [drilling down](drilling-down.md) and regrouping, without needing a new table per request.

This is the specific failure mode that over-reliance on [reporting-driven requirements analysis](dw-requirements-analysis-approaches.md) is prone to, when a modeler treats stakeholders' requested reports as the design target itself rather than as clues pointing toward the underlying business process that actually needs modeling.
