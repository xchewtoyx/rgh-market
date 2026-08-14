---
type: concept
title: Bound Annotation Volume Per Span to Protect Structural Data
description: Capping the total volume of application-added annotations a single span may carry keeps runaway or accidental logging from displacing the structural span/RPC fields a trace needs to reconstruct causality and timing.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §2.3"
---

A [span](trace-anatomy-and-spans.md) carries both structural data — start/end time, trace/parent ids, RPC timing — essential for reconstructing the trace's causal hierarchy, and free-form application annotations (text log lines, key-value attributes) added at the instrumenter's discretion. Annotation volume is under application control and can spike accidentally — a loop that logs on every iteration, a verbose debug flag left on — so an unbounded per-span annotation budget risks the annotations themselves crowding out or truncating the structural data the whole trace depends on.

The mitigation: give each span a configurable upper bound on total annotation volume, enforced so that structural span/RPC information is never displaced by application annotation activity, no matter how much a given application logs. This is a defensive property independent of [sampling](head-vs-tail-sampling.md) — sampling controls whether a span is captured at all, while this bound protects what's captured once a span is already sampled in.
