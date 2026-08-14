---
type: concept
title: Span Links for Non-Linear Workflows
description: In streaming, fan-out, or long-running async pipelines, forcing every stage into one giant parent/child trace tree produces unreadable, unaggregable traces — link producer/consumer spans instead of parenting them, and correlate the whole logical transaction via a shared ID.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 7"
---

The default [trace](trace-anatomy-and-spans.md) model — one tree, rooted at the request that started it, with strict parent/child nesting — assumes work happens in a roughly synchronous, bounded call chain. Several common architectures break that assumption:

- **Streaming/event pipelines**: a message may be produced, sit in a queue for an arbitrary time, and be consumed by an unrelated process later. Forcing producer and consumer into one parent/child tree misrepresents the timing (the "span" would span the queue wait) and doesn't generalize across a whole pipeline. Instead: propagate context through the message envelope, mark producer and consumer spans as **linked** (not parented) via span links, and rely on a shared correlation ID per logical transaction. Metric counters (e.g. `processed_total`/`failed_total` per stage) plus metric exemplars are used for fleet-level alerting, since per-stage traces alone don't aggregate well across a whole pipeline.
- **Async fan-out/fan-in and long-running jobs**: the root span should be the entry point (e.g. the initiating HTTP `POST`); avoid turning an hours-long downstream stage into a direct child span (the "million children trace" hazard). Model each long-running stage as its own trace, related back to the root via correlation ID or span links, or fall back to a single wide summary event/span written once the stage completes.

The underlying principle: [context propagation](context-propagation.md) and correlation don't require a strict tree — a correlation ID plus explicit links is a better fit whenever the causal relationship between two spans is "related to" rather than "happened synchronously inside."
