---
type: concept
title: Agile Data Profiling
description: Test-first validation of a business-requirements dimensional model against candidate source data, done early and by the team that will build the ETL.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 5"
---

Converting a business-requirements dimensional model (a completed set of event tables and the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md), per [gathering business requirements](gathering-business-requirements.md)) into a viable physical design starts with **agile data profiling**: examining candidate source data for structure, content, and quality to verify the model against what's actually available, before any physical schema or ETL is written. This is test-driven design applied to the model itself — profiling metrics test the model's fit against reality the same way a unit test checks code, and the checks are written *before* the thing they're testing (the physical schema) exists.

Agile data profiling is:

- **Targeted** — scoped only to the events and dimensions prioritized for the next release, not every source in the enterprise.
- **Done early**, as a modeling activity that precedes any technical schema, not a QA step that follows one.
- **Done frequently**, especially against sources still being built in parallel with the warehouse.
- **Done by the people who will build the ETL** — the profiling work directly informs their own load-effort estimates.
- **Recorded back into the business model**, so results are reviewable with stakeholders before any technical schema is even proposed.

The alternative — building an idealized target schema first, attempting to load it, and discovering the source's real profile only from the resulting ETL failures — is the single most expensive and painful way to find these problems, and is explicitly the mistake to avoid. Profiling early also has a political benefit: issues found before the warehouse schema exists are attributable to the system of record itself, not blamed on the new database or its ETL.

## Identifying the system of record

Warehouse extracts should come from the **system of record (SoR)** — the authoritative source for a given fact or dimension — rather than from a downstream copy-of-a-copy, to minimize latency, extra dependencies, and compounded quality loss (the exception being a downstream system that genuinely improves quality or exposes an otherwise-proprietary format). Facts usually have one obvious SoR (the claims-processing system is the SoR for claim submissions, say). [Conformed dimensions](conformed-dimensions.md) are typically harder: common reference data (customers, products, employees) is often independently maintained across several operational systems with no single obvious best source, and even a formally designated SoR may not carry every attribute or use the same business keys as the systems that need to conform to it. A **Master Data Management (MDM)** system, where one exists, captures, cleanses, and synchronizes reference data across operational systems and can supply the cross-referenced business keys ETL needs to reconcile multiple sources into one conformed dimension.

## Three basic profiling checks

Sophisticated profiling tools help at scale, but three simple SQL checks, run against a snapshot or off-line copy (never a live operational system, to avoid degrading its performance), cover most of what matters:

- **Missing values** — count nulls and (for character columns) blanks per candidate column, and calculate the missing percentage. Essential for every column, and especially for anything stakeholders marked mandatory during [event story discovery](event-story-themes.md).
- **Uniqueness and frequency** — count distinct values and the ratio of distinct values to total rows. A column at or near 100% uniqueness is a candidate business key; a set of columns with progressively lower uniqueness suggests a viable hierarchy. Ranking values by frequency and graphing the result can expose a column that carries no real information despite not being null — a dominant default value, empty-but-non-null strings, or a suspiciously common "favorite date" pointing at lazy data entry.
- **Ranges and lengths** — min/max/average for numeric columns, earliest/latest for date columns, shortest/longest for character columns. Useful for choosing physical data types and date ranges, and for spotting outlier errors. Grouping these by insert/update month (where reliably timestamped) shows how source quality has changed over time — the worst quality issues sometimes predate the warehouse's own intended historical scope.

## Proactive profiling: nothing to profile yet

When a new operational system is being built in parallel — see [proactive requirements analysis](dw-requirements-analysis-approaches.md) — there may be nothing to profile at all yet. The business-requirements model itself becomes an "advanced test specification," posed to the operational team as "can the system supply this data, to this specification?" while they're still in design mode and changes are cheap. If the operational team lags, define extract file layouts directly from the business model and get a committed delivery schedule, so ETL can be built and tested against (initially empty) files ahead of real data arriving; once real data does start flowing, profile it immediately against the agreed specification to keep the operational side honest.

## Model review

Profiling results are fed back to stakeholders in a **model review**, held as soon as possible after profiling — delaying it lets unrealistic expectations about what the next release will actually deliver keep growing unchecked. Its purpose is to make clear what's genuinely achievable given the real data and the resulting effort estimates, and to jointly decide, issue by issue, whether to include, exclude, add, or adjust the affected part of the model. See [model review severity checklist](model-review-severity-checklist.md) for how issues are triaged during this review.
