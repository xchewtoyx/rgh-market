---
type: concept
title: Pipeline SLI Types
description: >
  Data-processing pipelines need a distinct SLI vocabulary — freshness,
  correctness, completeness, and isolation — rather than the request-driven
  availability/latency pair.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4, ch. 25"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 13"
---

- **Freshness** (data latency) — expressed as "X% of data processed within Y
  time," "oldest data no older than Y," or "job completes within Y."
- **Correctness** — hard to define without ground truth; common techniques
  include generating synthetic "golden data" through test accounts to compare
  expected vs. actual output, or using automated background **data validation
  scrubbers** to verify output schema correctness. Correctness SLOs are often
  necessarily backward-looking (e.g. "no more than 0.1% of invoices incorrect
  per quarter"). A specific, high-stakes case of "no ground truth" is a
  supervised-learning label pipeline, where the recorded label itself can
  silently stop matching reality — see
  [training label correctness as SLI](training-label-correctness-as-sli.md).
- **Completeness** — the proportion of expected/published data actually
  delivered or processed, measured via an audit comparing input counts to
  output counts or run-time check sums.
- **Isolation / data prioritization** — whether high-priority data segments
  get preferential processing under resource constraints (priority queues,
  differently provisioned worker pools); not always promoted to a customer
  SLO but a real internal design constraint.

A concrete worked example (a large-scale event-delivery pipeline) split
freshness into **timeliness** (max delay before a data bucket is delivered,
tiered by priority), **skewness** (% of data misplaced into the wrong time
bucket due to imperfect bucket-closing heuristics), and **completeness** (%
of published events actually delivered), deliberately declining to add a
data-quality/accuracy SLO — content-quality ownership was left to the teams
producing the events, since the pipeline's own job was purely to deliver
data on time and intact.

**End-to-end over per-stage measurement**: measuring only per-component
freshness/correctness misses the user's actual experience and can hide
cross-stage corruption bugs where each stage individually "succeeds" but the
composition is wrong (e.g. a field one stage adds that a downstream stage
silently drops). See
[end-to-end vs per-component SLI measurement](end-to-end-vs-per-component-sli-measurement.md).

See also [durability as SLI](durability-as-sli.md) for the storage-side
analog of freshness/completeness.

For a long-running job measured against a hard deadline (a training run, a
large batch job), see
[catch-up-time deadline alerting](catch-up-time-deadline-alerting.md) for how
to alert on a freshness SLI like this without either drowning in noise from
every progress fluctuation or waiting until the deadline has already passed.
