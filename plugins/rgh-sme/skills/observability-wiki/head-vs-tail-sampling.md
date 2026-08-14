---
type: concept
title: Head Sampling vs. Tail Sampling
description: A sampling decision can be made before emission using only information known at the start (head sampling, cheap but blind to what happens downstream), or after the fact once the full record is known (tail sampling, more accurate but requires buffering the whole event).
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 4"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 15"
---

Two points at which a sampling decision can be made:

- **Head (up-front) sampling** — the decision is made at the start of a trace/span (or when a metric is recorded), using only static fields known at that moment (endpoint, customer ID). Cheap, since nothing needs to be buffered, but blind to what happens downstream — a rare error that only reveals itself later in the request can be sampled away before it's ever seen. A 0.1%-frequency bug can vanish entirely under a 1% head sample rate. Any [metric](metric-anatomy.md) is itself effectively a form of pre-emission sampling, in the sense that it's an irreversible decision made before the full event is known.
- **Tail-based sampling** — the decision is deferred until dynamic fields are known (final status, total latency), which requires buffering the whole trace and deciding keep/discard against the complete record (e.g. discard "boring" 200 OKs, keep anomalies). This optimizes for fidelity over raw cost savings, but is computationally more expensive and typically needs external, collector-side logic rather than something purely in-process.

For distributed traces specifically, a head-sampling decision needs to be **consistent**: propagate a centrally-generated Sampling-ID to every child span (rather than each service independently rolling its own random decision) so a full end-to-end trace is captured or dropped as a single unit — otherwise a downstream error span can end up kept while its upstream context is missing. See [sampling rate selection strategies](sampling-rate-selection-strategies.md) for how the keep-rate itself is chosen once you know whether you're sampling at the head or the tail.
