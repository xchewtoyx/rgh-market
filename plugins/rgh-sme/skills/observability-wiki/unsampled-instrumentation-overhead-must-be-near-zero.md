---
type: concept
title: Unsampled Instrumentation Overhead Must Be Near-Zero
description: Tracing overhead splits into distinct components — span create/destroy, annotating an unsampled span, annotating a sampled span, and disk/network I/O — and keeping the unsampled-path cost near-zero is what lets instrumentation stay compiled into hot paths permanently without engineers fearing it.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §4.1"
---

A tracing system's runtime overhead is not one number — it splits into distinct components with very different costs, and the split matters for how liberally instrumentation can be used. Dapper's measurements: root [span](trace-anatomy-and-spans.md) creation/destruction costs ~204ns on average, non-root ~176ns (the difference being the cost of allocating a globally unique trace id); adding an annotation to a span that turns out **not** to be sampled costs only ~9ns (a thread-local lookup); adding the same annotation when the span **is** sampled costs ~40ns; and writing the resulting data to local disk is by far the most expensive step, mitigated by coalescing multiple writes and executing them asynchronously to the traced application.

The design implication: because the unsampled-path cost (~9ns) is negligible, annotation calls can be left compiled into every code path — hot loops included — with no measurable production impact regardless of what fraction of traffic actually gets sampled. Only the sampled fraction pays the higher cost (~40ns plus eventual disk I/O). This is what makes it safe to apply the [instrumentation litmus test](instrumentation-litmus-test.md) routinely and use the full annotation API without performance fear, and it's a distinct concern from the friction problem [low-cost instrumentation](low-cost-instrumentation-with-statsd.md) solves — that's about how much effort it takes a developer to *add* an instrumentation call; this is about how much it costs at runtime once it's already there, whether or not [sampling](head-vs-tail-sampling.md) keeps that particular execution.
