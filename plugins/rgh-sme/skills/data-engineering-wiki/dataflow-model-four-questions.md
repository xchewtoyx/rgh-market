---
type: concept
title: The Dataflow Model Four Questions
description: >
  What, Where, When, and How as the four independent dimensions that configure
  any unbounded-data pipeline's output shape, latency, and correctness.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
---

The Beam/Dataflow model organizes unbounded-data processing around four
questions, each answered by an independent configuration dimension:

1. **What** results are calculated? → pipeline **transformations** (sums,
   histograms, joins). Classic batch processing answers only this question.
2. **Where** in event time are results calculated? → **windowing** (fixed,
   sliding, sessions, or none). See [streaming window types](streaming-window-types.md).
3. **When** in processing time are results materialized? → **triggers** and
   optionally **watermarks**. See [streaming triggers and panes](streaming-triggers-and-panes.md).
4. **How** do refinements relate? → **accumulation mode**. See
   [streaming accumulation modes](streaming-accumulation-modes.md).

Supporting concepts:

- **[Event time vs. processing time](event-ingestion-process-time.md)** —
  when events happened vs. when the system observed them.
- **Watermarks** — input completeness signal with respect to event times.

Minimal code changes to one summation pipeline — adding windowing, then
triggers, then watermark/accumulation combinations — produce substantially
different output shapes, latency profiles, and correctness trade-offs over
the *same* underlying dataset. That composability is the model's central
design bet: balance correctness, latency, and cost by tuning four orthogonal
knobs rather than rewriting pipeline mechanics.

Apache Beam's **PCollections** (datasets) and **PTransforms** (transforms
producing new PCollections) are the API surface; by publication most major
streaming engines had converged on a similar decomposition.
