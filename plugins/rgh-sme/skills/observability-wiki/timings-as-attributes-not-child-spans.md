---
type: concept
title: Record Sub-Operation Timings as Attributes, Not Child Spans
description: Wrapping every sub-operation in its own child span is a common first-time tracing mistake, because child-span durations are hard to aggregate across all requests; recording the same duration as an attribute on the main span keeps it directly groupable at the cost of minor duplication.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 6"
---

A frequently-seen mistake when engineers first get access to tracing tools: wrapping every sub-operation (a DB call, a cache lookup) in its own child [span](trace-anatomy-and-spans.md). The problem isn't that the data is wrong — it's that child-span durations are hard to query and aggregate *across all requests*, since doing so requires an expensive join between the parent span and its children, rather than a flat `GROUP BY`.

The alternative: record the timing as an **attribute on the main span** instead of (or in addition to) a child span — e.g. `db.duration_ms` directly on the request's primary span. This makes the timing directly groupable across every request with a simple aggregation, at the cost of some minor duplication if a child span for the same operation also exists.

This is one specific instance of a more general judgment call — see [deciding whether to create a span](deciding-whether-to-create-a-span.md) for the "interesting and aggregable" test that helps decide, for any given piece of work, whether it deserves its own span at all.
