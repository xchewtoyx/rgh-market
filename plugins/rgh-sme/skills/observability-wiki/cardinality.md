---
type: concept
title: Cardinality
description: Cardinality is the number of unique values a field can take, and high-cardinality fields — user ID, trace ID, build ID — are the most useful ones for debugging precisely because they're unique, which is also what breaks traditional metrics systems' cost model.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 1"
---

Cardinality is the number of unique values present in a field (or column) — a boolean field has cardinality 2, a UUID field has the highest possible cardinality (every value is unique). High-cardinality fields (user ID, trace ID, build ID, span ID) are exactly the fields most useful for precise search and debugging, since they let you isolate a single request, user, or deploy from everything else — but that same uniqueness is what breaks traditional [metrics](metric-anatomy.md) systems: adding a high-cardinality label to a time-series metric multiplies the number of distinct series that must be stored, causing a cost blowup (see [cardinality explosion in time-series databases](cardinality-explosion-in-tsdbs.md)).

A further, one-directional problem: once high-cardinality data has been pre-aggregated away (e.g. collapsed into a per-minute average with no per-user breakdown), it cannot be recovered later — see [pre-aggregation is a one-way trip](pre-aggregation-is-irreversible.md). This is the central reason the [unified/wide-event telemetry model](three-pillars-vs-wide-events-model.md) treats high cardinality as a feature to preserve rather than a cost to minimize.

Cardinality is distinct from, but multiplies with, [dimensionality](dimensionality.md) (the number of distinct fields per event) — together they determine how precisely you can slice a dataset when investigating an anomaly, as in the [core analysis loop](core-analysis-loop.md).
