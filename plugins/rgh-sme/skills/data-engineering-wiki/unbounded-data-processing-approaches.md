---
type: concept
title: Unbounded Data Processing Approaches
description: >
  Four categories of pipeline logic for infinite datasets — time-agnostic,
  approximate, windowed, and batch-sliced — and when each fits data-engineering
  workloads.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
---

[Unbounded data](bounded-vs-unbounded-data.md) from real distributed sources
is typically highly **unordered** in event time and has **varying event-time
skew** with no constant bound on when data for time X arrives. Four
processing approaches cover most pipeline shapes:

**1. Time-agnostic** — logic is purely data-driven; time irrelevant.
Filtering (drop records not matching a domain) and **inner joins** (buffer
until a matching key arrives from the other side) fit here. Switching inner
to outer join reintroduces completeness — how long to wait for the other
side? — which is windowing by another name.

**2. Approximation algorithms** — Top-N, streaming k-means. Low overhead on
unbounded data but limited algorithm set, often complex, and approximate.
Many assume in-order arrival for error bounds — weak when fed disordered,
variably-skewed data.

**3. Windowing** — chop data along temporal boundaries. The primary path for
event-time correctness. See [streaming window types](streaming-window-types.md),
[streaming triggers and panes](streaming-triggers-and-panes.md), and the
[Dataflow model four questions](dataflow-model-four-questions.md).

**4. Batch engines on unbounded data** — slice the stream into bounded chunks.
Fixed tumbling windows via time-named log files appear straightforward but
still have completeness problems (delayed events, mobile offline buffering).
Sessions split across batch boundaries unless batch size increases (latency
cost) or cross-run stitching logic is added (complexity cost) —
[streaming session windows](streaming-window-types.md) avoid both.

**Processing-time windowing** (buffer until N seconds of processing time
elapsed) is simple and correct for analyzing the arrival process itself but
wrong when event times matter — contents change with observation order. See
[processing-time windowing methods](processing-time-windowing-methods.md).

**Event-time windowing** costs more buffering and requires completeness
heuristics ([watermarks](watermark-computation-and-propagation.md)), but
produces results stable under reordering — the gold standard when when events
actually happened matters.
