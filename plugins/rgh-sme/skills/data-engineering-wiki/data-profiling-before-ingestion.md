---
type: concept
title: Data Profiling Before Ingestion
description: >
  Analyzing a candidate source's content, consistency, and structure before
  building a pipeline against it, so problems surface as an early go/no-go
  rather than as a late, career-risking discovery.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Data profiling is technical analysis of a source's content, consistency, and
structure before a pipeline is built against it — even a `SELECT DISTINCT` to
check a column's actual cardinality is a form of profiling, though dedicated
profiling tools are more productive than hand-coding every check.

Profiling plays two distinct roles, at two different points in a project:

- **Strategic profiling**: a light assessment done immediately after a
  candidate source is first identified, aimed purely at an early go/no-go
  decision. Disqualifying a source at this stage — because it's missing a
  required field, or its data quality is unworkable — is cheap and earns
  credibility; the same discovery made after [source system
  evaluation](source-system-evaluation.md) and pipeline design are already
  committed is expensive and can be "potentially fatal" to the project.
- **Tactical profiling**: a lengthier effort during modeling and pipeline
  design, aimed at surfacing as many concrete problems as possible before
  build starts. Findings from tactical profiling go one of two places: back
  to the source system's owner as a data-quality improvement request, or
  forward into the pipeline's own cleaning and validation requirements (see
  [data quality validation tests](data-quality-validation-tests.md)).

The practical payoff is expectation-setting: profiling results, done upfront,
give business sponsors a realistic view of schedule risk and source-data
limitations before they've been promised a delivery date that the data itself
can't support.
