---
type: concept
title: Structured Events as the Observability Substrate
description: All three traditional telemetry types can be decomposed into and reconstructed from one common substrate — an arbitrarily wide structured event (or trace span) per unit of work — and the shape you choose to capture pre-decides which questions you'll later be able to ask.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 5"
---

Central thesis: **the shape of the data you collect constrains the questions you can ask later.** Deciding a data shape up front (a fixed dashboard, a pre-aggregated metric) pre-decides your future investigation's boundaries.

Metrics, logs, and traces — the traditional "three pillars" — can all be decomposed into, and reconstructed from, one common substrate: the **arbitrarily wide structured event**, a flat key-value record (or a trace span, which is the same shape with a few required fields) capturing one unit of work. A [structured event](structured-logging.md) is any application-emitted record parseable into key-value pairs, as opposed to unstructured free text.

From a single stream of wide events, you can dynamically regenerate any of the traditional views without re-instrumenting: derive a p99 latency [metric](metric-anatomy.md) time series by grouping by minute; re-slice that same metric by any dimension with zero schema change (e.g. add `region` to the grouping); reconstruct a log-style narrative; or stitch spans into a full [trace](trace-anatomy-and-spans.md) via a shared trace ID. This is "post-deciding shape" — deriving whatever view you need at query time — as opposed to "pre-deciding shape," which is what happens when data is aggregated or split into separate stores at write time (see [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md)). This substrate is what the [three-pillars vs. wide-event model](three-pillars-vs-wide-events-model.md) choice is actually about.
