---
type: concept
title: Pipeline Granularity and Blast Radius
description: >
  Why decomposing a pipeline into smaller recoverable steps beats one large
  monolithic job that must fully restart on any failure.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 4"
---

A cautionary real-world pattern: a monolithic ETL pipeline that took 48 hours
to run end to end and had to fully restart from the beginning on any
failure. It was eventually discarded because it broke chronically and left
business users receiving reports "two days late by default" — the recovery
cost of a single failure was as large as the entire pipeline's runtime.

The lesson generalizes past that one anecdote: a pipeline's granularity is a
retry-and-recovery design decision, not just a style preference. A pipeline
broken into smaller, independently retryable steps has a failure blast
radius limited to the step that failed — recovery means rerunning that step,
not the whole multi-hour job. This is the same reasoning that makes
[idempotent and replayable jobs](idempotent-and-replayable-jobs.md) valuable:
granularity is what makes replaying a single failed segment safe and cheap
instead of an all-or-nothing gamble.

This is also why [orchestration](orchestration-vs-scheduling.md) engines
model pipelines as a DAG of discrete tasks rather than one opaque script —
the DAG's task boundaries are exactly the granularity boundaries that bound
blast radius and enable partial retry and backfill.
