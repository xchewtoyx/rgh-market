---
type: concept
title: Layered Telemetry Signal Selection
description: Choosing which telemetry type to emit for a given piece of information comes down to a three-question test — full-request causality needs a trace, cheap long-term alerting needs a metric, rare or audit-critical events need a log — and a common pattern emits both a trace span and a metric for the same request rather than duplicating everything into every format.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 7"
---

Rather than duplicating every piece of information into every telemetry format, pick the right signal at the right granularity using a three-question test:

- Needs full-request causality/context (which downstream calls did this request trigger, in what order, with what timing) → a **trace**. See [trace anatomy and spans](trace-anatomy-and-spans.md).
- Needs cheap, long-term storage and fast, reliable alerting → a **metric**. See [metric anatomy](metric-anatomy.md).
- Is rare, or has an audit requirement → a **log/event**.

A common concrete pattern combining two of these: emit both a trace span *and* a histogram metric for the same request, so you can [head-sample](head-vs-tail-sampling.md) the traces (keeping cost down) while the metric still gives reliable alerting and aggregate coverage even for the sampled-out portion. **Metric exemplars** — a metric data point carrying a link back to a specific representative trace — bridge the two: an alert or dashboard spike on the metric can jump straight to one concrete trace exhibiting the behavior, rather than requiring a separate search.

For streaming/event pipelines specifically, a single request-scoped trace tree often doesn't fit the architecture — see [span links vs. parent-child nesting](span-links-vs-parent-child.md) for the pattern used there instead.
