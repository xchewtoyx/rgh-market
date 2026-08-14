---
type: concept
title: Model Review Severity Checklist
description: A severity-ordered checklist for triaging data-profiling findings against a dimensional model, from issues that stop a release to ones that only need reporting.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 5"
---

Once [agile data profiling](agile-data-profiling.md) has checked a business-requirements model against real source data, the findings need to be triaged with stakeholders by severity, not treated as a flat list — some findings force a genuine rethink of scope, while others are minor gaps worth noting but not worth delaying a release over. Working top-down by severity keeps a model review session focused on what actually matters first:

| Severity | Issue | Outcome |
|---|---|---|
| Highest | Missing conformed dimension | Stop |
| Highest | Missing event | Stop |
| High | Missing or incorrect business key | Stop |
| High | Conflicting data for a conformed dimension | Stop |
| Medium-high | Event [grain](grain.md) is different from what was declared | Stop / Pause |
| Medium | Missing non-conformed dimension | Pause |
| Medium | Missing or poorly populated event detail | Pause |
| Medium-low | Missing mandatory values | Pause |
| Medium-low | Incorrect hierarchical relationship | Pause |
| Low | Missing or poorly populated dimensional attribute | Go |
| Low | Mismatched detail and attribute values | Go |
| Lowest | Additional event details or dimensional attributes found | Go |

**Stop** issues force a major rethink or reprioritization of the release before design work continues. **Pause** issues need stakeholder feedback and a documented decision before physical development proceeds, but don't necessarily block the release outright. **Go** issues are proceed-with-caution items — real gaps or opportunities, but ones that should simply be reported and tracked rather than stopping progress.

Two categories deserve particular attention because of how their cost compounds: a completely missing event or dimension source may force serious reprioritization of the whole release, since there's nothing to build against; and conflicting sources for a [conformed dimension](conformed-dimensions.md) are especially damaging because the inconsistency compounds across every future iteration that relies on that dimension, building the largest technical debt of any issue on this list.

## Running the review

For each finding, ask stakeholders directly: "should we include, exclude, add, or adjust this item?" — and for conflicting sources specifically, "which of these should we choose?" Update the model and the [bus matrix](enterprise-data-warehouse-bus-matrix.md) together with stakeholders as each decision is made, rather than deferring the update to later. Close the review by asking whether the findings change stakeholders' event priorities for the release — if so, revisit whatever event-and-dimension prioritization exercise the team uses before moving on to sprint planning and physical design.
