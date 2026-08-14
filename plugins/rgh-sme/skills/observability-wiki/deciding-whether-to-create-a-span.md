---
type: concept
title: Deciding Whether to Create a Span
description: Only create a span for a piece of work if it's both interesting (it meaningfully affects the request's overall latency or failure) and aggregable (grouping by its name/attributes across many requests would produce a useful trend) — most fine-grained internal calls fail this test.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 7"
---

Before wrapping a piece of work in its own [span](trace-anatomy-and-spans.md), ask two questions:

1. **Is it interesting?** Does it meaningfully affect the latency or failure outcome of the overall request?
2. **Is it aggregable?** Would grouping by its name/attributes across many requests produce a useful trend?

Only create a span if both are true. Examples that pass: HTTP handlers, DB queries, external API calls, cache lookups, queue publish/consume, business transactions. Examples that fail: private helper functions, loop iterations (unbounded [cardinality](cardinality.md) of span instances), getters/setters, pure-CPU validation logic, and orchestration code whose duration is just the sum of its children's durations (redundant with the children).

This test is what keeps a trace tree from becoming so deep and noisy that it's unreadable and unaggregable — over-applying spans to fine-grained internal timing is the specific failure mode covered in [recording sub-operation timings as attributes, not child spans](timings-as-attributes-not-child-spans.md).

This is a real design fork, not just a style preference: some tracing systems (X-Trace) deliberately instrument at every point control passes between software layers *within* a single process, not just at network/node boundaries — richer detail, at a real overhead cost. Dapper's own low-overhead requirement pushed it the other way on purpose: instrument the minimum set of mechanisms needed to tie together all the work done on behalf of one request (node/RPC boundaries), and let anything finer-grained be an opt-in application annotation rather than automatic instrumentation. Neither choice is universally correct — it's a trade-off between richer default detail and [keeping unsampled overhead negligible](unsampled-instrumentation-overhead-must-be-near-zero.md), and which side to lean on depends on how overhead-sensitive the traced services are.
