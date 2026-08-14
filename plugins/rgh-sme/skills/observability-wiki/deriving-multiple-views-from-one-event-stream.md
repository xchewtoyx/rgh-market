---
type: concept
title: Deriving Multiple Views from One Event Stream
description: A single stream of wide structured events can be reshaped at query time into a metric time series, a re-sliced breakdown by any dimension, a log-style narrative, or an assembled trace — all without re-instrumenting, because the shape is decided when you query, not when you write.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 5"
---

Because a [wide structured event](structured-events-as-observability-substrate.md) preserves both raw values and their relationships, a single event stream can be reshaped into whichever traditional view a question calls for, entirely at query time:

- **A metric time series** — e.g. p99 latency `GROUP BY minute`.
- **A re-sliced breakdown** — add any dimension (e.g. `region`) to the `GROUP BY` with zero schema change, because the field was already captured on every event even if nobody had queried by it before.
- **A log-style narrative** — filter and order events to read as a sequence.
- **A trace** — stitch spans together via a shared `trace_id`.

This is "post-deciding shape" — choosing the view after you know the question — as opposed to committing to a shape (a specific dashboard panel, a specific pre-aggregated metric) at write time. It's the practical payoff of the [wide-event model](three-pillars-vs-wide-events-model.md): the same underlying data serves whichever of these views the [core analysis loop](core-analysis-loop.md) currently needs, rather than requiring you to have anticipated the right view in advance.
