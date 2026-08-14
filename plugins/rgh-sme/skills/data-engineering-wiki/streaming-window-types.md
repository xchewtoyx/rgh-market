---
type: concept
title: Streaming Window Types
description: >
  Session, tumbling, and sliding windows as the mechanisms that trigger
  computation directly off streaming data, and watermarks as the boundary
  that decides what counts as late.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2, ch. 5"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §2"
---

A traditional batch query treats the query engine as an external observer —
an hourly cron job, a dashboard refresh. Streaming systems instead support
computation triggered directly by the data itself, via **windows**: small
batches processed on dynamic triggers rather than a fixed external clock.

- **Session window**: groups events per key (e.g., per user) with no
  inactivity gap beyond a threshold — a 5-minute gap, say, closes and emits
  the window, and the next event for that key opens a fresh one. Session
  windows can absorb [late-arriving data](late-arriving-data.md) by allowing
  a grace period before finally closing. Making sessionization real-time
  instead of a next-day batch job changes what it can be used for — an
  in-app alert based on the last 15 minutes of behavior, rather than only a
  follow-up email the day after.
- **Fixed-time (tumbling) window**: fixed-length, non-overlapping windows on
  a set cadence (every 20 seconds, say), processing everything since the
  prior window closed and emitting as soon as it's computed — essentially
  traditional batch ETL cadence compressed to a much shorter, lower-latency
  interval. This is the concrete mechanism behind
  [batch as a special case of streaming](batch-streaming-unification-architectures.md).
- **Sliding window**: fixed-length windows that can overlap (a new 60-second
  window generated every 30 seconds, say). Can also slide continuously but
  only emit statistics when a specific trigger condition fires, producing
  bursty output correlated with real-world trigger frequency instead of a
  fixed cadence.

A **watermark** is the threshold a window uses to decide whether incoming
data genuinely belongs to its interval or should be classified as
[late-arriving](late-arriving-data.md) — it's the same late-data problem
from ingestion, now made a first-class, explicit part of the windowing
mechanism rather than something handled ad hoc after the fact.

**What a watermark actually claims, and why that matters beyond just closing
windows on time**: a low watermark for a processing stage is a timestamp
below which the pipeline has high confidence all data has already been
received — not merely a cutoff that data hasn't arrived by. Computed across
a distributed system as the minimum timestamp of all still-pending work
feeding that stage, its advance past some time *t* is the pipeline's own
positive signal that expected data for *t* is genuinely absent rather than
simply delayed on the wire. This distinction matters most for a use case
that has to detect an *absence* — e.g., flagging traffic dips, where the
pipeline needs to distinguish "quieter than usual so far, more data is still
in flight" from "confidently over, and it really was this quiet" before it
can safely emit an alert. A side effect of framing lateness this way, rather
than requiring inputs to arrive in order: out-of-order streams stop being a
special case the pipeline has to work around and become the default the
watermark mechanism is already built to handle. See
[watermark computation and propagation](watermark-computation-and-propagation.md)
for how the value itself is actually computed and kept trustworthy across a
distributed computation graph, and
[watermark and wall-time timers](watermark-and-wall-time-timers.md) for
scheduling per-key work off watermark progress instead of the clock.
See also [watermark aggregation patterns](watermark-aggregation-centralized-vs-in-band.md)
and [heuristic Pub/Sub watermarks](heuristic-source-watermarks-pubsub.md)
for implementation case studies.

## Session windows: merging proto-sessions

Sessions are **data-driven** (size and location follow input, not a predefined
pattern) and **unaligned** (apply per key/subset, not uniformly across all
data). When session membership isn't pre-tagged, construct sessions by
**merging overlapping proto-sessions**: each record starts in its own
proto-session (gap-duration wide, beginning at the record's event time);
overlapping proto-sessions merge as records arrive, even under out-of-order
delivery.

With early/on-time/late [triggers](streaming-triggers-and-panes.md) and
[accumulating-and-retracting](streaming-accumulation-modes.md) accumulation,
merging produces retractions for superseded sub-sessions — e.g., separate
panes of value 7 merge into 22, retracting the prior 7s; late data joining
existing sessions triggers immediate corrected panes plus retractions. This
multi-row transactional update pattern recurs in
[temporal validity windows](temporal-validity-windows.md).

Batch engines computing sessions by fixed time slices routinely split
sessions across batch boundaries; mitigations (larger batches, cross-run
stitching) trade latency or complexity. Streaming session support with proper
event-time semantics, speculative firings, and retractions is substantially
harder to replicate manually.

See [custom streaming windowing](custom-streaming-windowing.md) for unaligned
fixed windows, per-element window sizes, and bounded sessions.
