---
type: concept
title: Stream Processing Timers
description: >
  Per-key hooks that fire on wall-clock time or on watermark progress,
  journaled for durability and guaranteed to fire in increasing timestamp
  order with the same exactly-once guarantee as ordinary records.
sources:
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §4.6"
---

# Stream Processing Timers

A timer is a per-key hook, set by user code running inside a computation,
that fires later and runs arbitrary code at that point. Two kinds, chosen
per use case:

- **Wall-time timers** fire at a specific clock time regardless of how much
  of the input has actually been processed by then — the right choice for a
  heuristic that wants to act "on the hour" even if some data is running
  late (e.g. sending a monitoring email).
- **[Watermark](stream-processing-watermarks.md) timers** fire once the low
  watermark passes a given value — the right choice when correctness depends
  on having a *complete* picture up to that timestamp, such as closing out a
  windowed aggregate. Setting a watermark timer for the end of a time bucket
  and only emitting the bucket's result when it fires is a direct way to get
  "wait until this window is definitely complete" without polling.

Timers are guaranteed to fire in **increasing timestamp order**, are
journaled in persistent state so they survive process restarts and machine
failures, and carry the same [exactly-once](effectively-once-delivery.md)
guarantee as ordinary record processing when they fire.

Using timers at all is optional — some detection logic doesn't need to wait
for completeness. A traffic-spike detector, for instance, can act as soon as
observed traffic already exceeds a threshold: arriving late data could only
add to the total and make the spike more pronounced, never explain it away,
so there is nothing to gain by waiting for the watermark to catch up. A
*dip* detector is the asymmetric case — traffic looking low could mean a
real dip, or it could mean data just hasn't arrived yet — which is exactly
when waiting for the watermark to pass the bucket's end is worth the delay.

Under the hood, each computation folds its pending-work timestamps into the
low watermark it reports; user code virtually never touches the watermark
directly, only indirectly by assigning timestamps to records and letting the
framework roll timer semantics up from that.
