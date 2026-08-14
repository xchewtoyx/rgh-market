---
type: concept
title: Temporal Validity Windows
description: >
  Windowing rows by the time intervals during which their values are valid,
  requiring incremental construction and window shrinking as later rows arrive.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 10"
---

**Temporal validity windows** apply when each row in a relation defines a value
valid over a time region — e.g., currency conversion rates where each row
states the rate effective as of some event time, implicitly valid until the
next rate for that currency arrives. A row's validity region is
`[thisEventTime, nextEventTime)` for the same key; the last-known rate is
valid until `+inf`.

Because a row's validity region depends on rows arriving *after* it, regions
must be built incrementally and can change retroactively — even for in-order
arrival (a "valid forever" rate becomes "valid until X" when the next rate
arrives), and more severely under out-of-order delivery. A single incoming
row can force **transactional updates to multiple existing output rows at
once** — the same multi-row-transaction phenomenon as
[session window merging](streaming-window-types.md).

**Critical requirement:** validity windows must be able to **shrink** —
splitting data from a wider window across two narrower windows as boundary
information arrives. No mainstream streaming system natively supported this
at time of writing; partial implementations correct in isolation fail when
combined with joins because they lack a mechanism for redistributing data
from a shrunken window.

SQL equivalent: a three-way self-join finding each row's immediate next
same-key successor (crediting Martin Kleppmann).

**Temporal validity joins** match orders to rate windows via
`WINDOW_START <= Order.EventTime < WINDOW_END`, assigning each order the
rate valid at its event time despite out-of-order arrival on both sides. A
late-arriving rate can retract a prior conversion and emit a corrected value
— eventual correctness via
[accumulating-and-retracting](streaming-accumulation-modes.md) semantics.

Reduce chattiness by switching FULL OUTER to INNER (drop unjoined noise) and
projecting away window-boundary-only updates. For lowest latency without
speculative/retracted intermediates, replace per-record triggers with a
[watermark trigger](streaming-triggers-and-panes.md) firing only after the
watermark passes the validity window end relevant to each order — one correct
result per order at the cost of waiting for completeness.
