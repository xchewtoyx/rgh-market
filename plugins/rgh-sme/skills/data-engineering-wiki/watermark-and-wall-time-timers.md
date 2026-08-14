---
type: concept
title: Watermark and Wall-Time Timers
description: >
  Per-key hooks a stream computation can schedule against either wall-clock
  time or watermark progress, and why the choice between the two changes
  what the timer actually means.
sources:
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §4.6"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 8"
---

A stream computation can schedule a per-key timer to fire at either a
**wall-time** value or a
[watermark](watermark-computation-and-propagation.md) value, and which one
to pick depends on what the timer is actually supposed to mean:

- **Wall-time timers** fire when the clock reaches a given value, regardless
  of whether the data for that period has fully arrived — appropriate for a
  deadline that's genuinely about real time, like "send the hourly summary
  email on the hour" even if some of that hour's data is still delayed.
- **Watermark timers** fire only once the watermark has advanced past a
  given value — appropriate whenever the timer's job depends on having a
  *complete* picture of the data up to that point, such as closing a
  windowed aggregate. Firing this on wall-clock time instead would risk
  closing the window before genuinely-pending (not yet late) data has
  arrived.

Timers set this way are guaranteed to fire in increasing timestamp order,
are journaled in persistent state (surviving process restarts and machine
failures the same way any other MillWheel state does), and get the same
[exactly-once guarantee](delivery-guarantees-exactly-once-vs-at-least-once.md)
as ordinary input record processing — a timer firing is not a weaker or
best-effort event compared to a regular record delivery.

**Timers are an optional mechanism, not a required one** — some
computations don't need a completeness signal at all. Detecting a traffic
*spike*, for example, doesn't need to wait for a watermark timer the way
detecting a *dip* does: if observed traffic already exceeds the predicted
baseline, any [late-arriving data](late-arriving-data.md) can only add to the total and make
the spike more pronounced, so there's no risk in acting on an incomplete
picture. Detecting an anomalous *absence*, by contrast, is exactly the case
where acting before the watermark confirms completeness risks a false
positive from data that simply hasn't arrived yet.

In Beam's [generalized state API](generalized-streaming-state-api.md), timers
are a first-class `@TimerId` binding either `EVENT_TIME` or
`PROCESSING_TIME`, complementing watermark/processing-time
[triggers](streaming-triggers-and-panes.md) with per-record scheduling —
e.g., defer attribution logic until the earliest pending goal's event time
rather than waiting for a whole window's watermark to pass.
