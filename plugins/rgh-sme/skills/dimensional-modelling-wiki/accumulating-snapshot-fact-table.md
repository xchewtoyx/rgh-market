---
type: concept
title: Accumulating Snapshot Fact Table
description: A fact table whose grain is a pipeline instance with a defined start and end, whose rows are revisited and updated as the instance progresses through milestones.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4, 16"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 11"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

An accumulating snapshot fact table row summarizes measurement events at predictable steps between the start and end of a pipeline or workflow process — order fulfillment, claim processing, a job applicant pipeline — with a defined start, standard intermediate steps, and a defined end. It is one of the three fundamental [fact-table](fact-table.md) grain types, alongside [transaction fact table](transaction-fact-table.md) and [periodic snapshot fact table](periodic-snapshot-fact-table.md). During requirements gathering, a business event classified as an [evolving event story](event-story-types.md) is the signal that an accumulating snapshot is the right grain type.

A row is inserted when the process begins (e.g., an order line is created) and is **revisited and updated** as the pipeline progresses — this ongoing in-place updating is unique among the three fact table types; the other two either never touch a row after posting or preserve prior rows as history. The row reflects only the current status of the pipeline instance, not a history of intermediate states.

## Why a status-change transaction table isn't enough on its own

A [transaction fact table](transaction-fact-table.md) can track a pipeline as a series of status-change events — one row per status transition, referencing the item and the status reached — and this supports volume and workload questions well (how many applications were submitted, reviewed, processed this month, by counting rows grouped on status). What it can't do efficiently is answer elapsed-time questions (days from submission to review): each status change lives on its own row, so computing the gap between two milestones for one instance, let alone aggregated across many, requires a correlated subquery matching each instance's rows to each other — poor performance and hard to write. Giving each status row a begin/end date pair doesn't fully fix this either: operational systems describe completed milestones ("Submitted," "Reviewed"), not time-bounded states, so the vocabulary has to be translated; a process that can revisit an earlier stage produces more than one row per stage, so finding "the" begin/end pair for a stage again needs correlation; and a multi-stage span (submission to settlement) still crosses several rows no matter how each individual stage is dated. The accumulating snapshot's one-row-per-instance, repeatedly-updated design exists specifically to make elapsed-time analysis a plain aggregation instead of a correlated subquery — the transaction table remains the better source for volume, workload, and process-pattern questions, and the two are typically paired (see "Complementary use" below).

## Structure

The table contains a date foreign key for every critical milestone, handled as [role-playing dimension](role-playing-dimension.md)s against a single physical [date dimension](date-dimension.md), plus often a "last updated" date column. Undefined future-milestone dates use a default surrogate date key (see [null handling in dimensional models](null-handling-in-dimensional-models.md)) rather than a null. The table often includes:

- **Lag/duration facts** — rather than forcing every query to calculate every possible lag from stored date/time stamps, one time lag per step is stored, measured against the process's start point; any lag between two steps then becomes a simple subtraction between two stored lags. These pairwise date differences are also averageable directly across every other dimension, and can instead be exposed through a view rather than physically stored. The ETL system may compute a more sophisticated elapsed time than a raw date subtraction — for example, a workday lag that accounts for weekends and holidays — and, for short-lived, closely monitored processes, lags at finer grain (hours or minutes) sourced from operational timestamps rather than dates.

  For workflows with many, unstable intermediate milestones rather than a handful of stable ones (a start and end date are still definite, but the steps in between vary case to case), storing every pairwise lag doesn't scale — N milestones produce N(N-1)/2 possible pairwise lags (20 milestones → 190). Instead store only the N-1 lags measured from the anchor start event to each other milestone, and derive any other pairwise lag by subtracting two of those stored lags (e.g., a B-to-C lag is the A-to-C lag minus the A-to-B lag). A null in either component lag propagates to a null result, correctly signaling "this event never occurred" and aggregating/averaging gracefully across rows where different subsets of milestones fired.

  Name each lag/duration fact after the **stage** it measures (e.g. `days_reviewing`, `days_processing`), not after the milestone pair that bounds it (e.g. not `lag_submitted_reviewed`) — this pays off directly for a reentrant stage (see "Nonlinear and reentrant processes" below), where the same named fact keeps accumulating across however many times that stage is revisited, with no need to rename or add columns.
- **Milestone completion counters** — 0/1 flags indicating whether each milestone has been reached. Deciding what "reached" means can itself be a non-trivial business rule rather than a simple presence check: whether an order counts as reached the "delivered" milestone might look like a question of whether any delivery date is present, but a process that allows partial shipments actually needs delivered quantity to equal ordered quantity before the milestone is genuinely complete. Evaluate this kind of status rule once during ETL and store its result as the 0/1 counter, rather than leaving each report to reconstruct the rule (and risk getting it wrong) from the raw milestone columns.
- A foreign key to a status dimension reflecting the pipeline's latest status.

## Limitations

Outlier or unusually complex scenarios are better analyzed via a companion [transaction fact table](transaction-fact-table.md) recording every granular step than accommodated within the accumulating snapshot's standard-scenario design. Accumulating snapshots are typically problematic for [olap-cube](olap-cube.md)s, because updates change both facts and dimension foreign keys on already-loaded rows, forcing cube reprocessing — unless the fact row is loaded only once the pipeline instance completes.

## Interaction with type 2 dimensions

Because an accumulating snapshot presents only the latest workflow state, if an associated dimension carries [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) attributes, the fact row's foreign key to that dimension should be updated to the current surrogate key each time the row is revisited while the pipeline is still active. Once a pipeline instance is complete, its row is typically no longer revisited, so it stops tracking any further type 2 changes in its dimensions from that point on.

## Loses history at past cut-off dates

Because rows are revisited and updated in place, an accumulating snapshot cannot answer "how many pipeline instances were at each stage as of a specific past date" — that historical state is overwritten as each instance progresses, so only the current status survives. When analysts need reliable counts as of specific, closely watched cut-off dates (an admissions early-decision notification date, for example), supplement the accumulating snapshot with either a genuine [periodic snapshot fact table](periodic-snapshot-fact-table.md) capturing status at those cut-offs before it's overwritten, or a companion [transaction fact table](transaction-fact-table.md) recording every state-change event so historical counts can be reconstructed after the fact. Alternatively, the accumulating snapshot itself can be adapted to preserve full history in place — see [insert-only accumulating snapshot](insert-only-accumulating-snapshot.md).

## Complementary use

Accumulating and [periodic snapshot fact table](periodic-snapshot-fact-table.md)s can work together, incrementally building a period's snapshot from an accumulating snapshot before it becomes a fixed row in the longer time series. Transaction and snapshot fact tables are described as "the yin and yang" of dimensional design — some redundancy between complementary fact tables is an acceptable trade-off.

## Focus on key milestones, not every operational status code

An operational source system typically exposes many more granular status codes than the business actually thinks in terms of — dozens of codes may all collapse onto the same handful of milestones an accumulating snapshot needs (several "awaiting X" and "under review by Y" codes might all just mean "Submitted" for reporting purposes). Work with business managers to define that mapping explicitly; the resulting schema looks identical to one built against a source with only a handful of clean status codes to begin with, but the ETL logic that maintains the mapping carries the extra complexity instead of the schema.

Once that mapping is settled, check each pair of milestones' cardinality before merging them into one row — see [milestone cardinality discovery](milestone-cardinality-discovery.md). Whether it's safe to build the accumulating snapshot directly, or better to build it incrementally, follows from what that discovery finds — see [incremental accumulating snapshot build](incremental-accumulating-snapshot-build.md).

## Nonlinear and reentrant processes

Real processes are frequently not a strict linear sequence — a stage can be skipped, repeated, or reached out of order (an application returned from processing back to review for a missing signature: Submitted → Reviewed → Submitted → Reviewed → ...). An accumulating snapshot still works for this: naming each stage's duration fact after the stage itself (see "Structure" above) means ETL simply resumes incrementing that same fact when a status reverts, without needing new columns or renamed ones. The genuinely hard question this raises is *which* date to record for a milestone reached more than once — the earliest occurrence, the latest, or something else — and this is a **business rule that must be decided by business users**, not a default a designer or developer should pick unilaterally, since the choice measurably changes the answer every derived duration fact produces.

## Tagging abnormal scenarios

An accumulating snapshot models a "standard scenario" pipeline (order created → shipped → delivered → paid → returned, for example) that works well when the large majority of instances follow it. Rare deviations from the standard path shouldn't be baked into the standard-scenario design. Instead, add a status dimension to the accumulating snapshot and tag the deviating row with a status like "Weird" or "Exception"; an analyst who wants the full story can then join, via the shared [degenerate dimension](degenerate-dimension.md) or natural key, to a companion [transaction fact table](transaction-fact-table.md) recording every granular step, itself joined to a transaction-type dimension containing entries for the specific deviation causes encountered. This transaction dimension grows over time but stays well bounded and stable, since genuine deviations are rare by definition.
