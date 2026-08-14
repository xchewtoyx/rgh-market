---
type: concept
title: Generalized Streaming State API
description: >
  The low-level escape hatch beyond raw grouping and incremental combining —
  typed state fields, fine-grained read/write, and event- or processing-time
  timers for scheduling when complex logic runs.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 8"
---

[Raw grouping and incremental combining](incremental-combining-vs-raw-grouping.md)
are the two implicit [persistent-state](streaming-persistent-state.md) forms
at opposite ends of a spectrum. Both fall short when a pipeline needs finer
control:

- **Raw grouping** buffers all inputs before processing the group as a whole.
- **Incremental combining** applies one record at a time but only for
  commutative, associative aggregations.

A generalized state API trades implementation complexity for three flexibility
axes:

1. **Data structures** — maps, sets, values, and multiple typed fields per
   key/window, not just appendable lists or a single accumulator. Beam lets
   one `DoFn` declare several `@StateId` fields so logically independent
   state (visits vs. impressions) stores and accesses separately.
2. **Read/write granularity** — blind writes of precisely what's needed;
   batched parallel reads via asynchronous I/O (`readLater()` futures) when
   a coarse load is cheaper than field-by-field access (e.g., a Bloom filter
   membership check before a full read).
3. **Processing scheduling** — [triggers](streaming-triggers-and-panes.md)
   bind firing to watermark or processing-time progress at window granularity;
   **timers** bind a point in either
   [event or processing time](watermark-and-wall-time-timers.md) to a method
   invoked when that point is reached, delaying work to a more appropriate
   moment. Timers also implement most trigger types and
   [allowed-lateness](allowed-lateness-horizon.md) garbage collection under
   the hood.

Raw grouping and combining remain the high-level, optimizable defaults;
generalized state is the imperative escape hatch ("think C/Java") complementing
the functional style of windowing and triggers ("think Haskell").

## Beam State and Timers mechanics

State and timers scope to the current key and window (window lifetime governed
by allowed lateness). State fields bind via `@StateId` / `@TimerId` annotations
to typed specs — `MapState`, `SetState`, `ValueState`, `Timer` — and appear
as method parameters in `@ProcessElement` and `@OnTimer` handlers.

Beam (at publication) requires timers declared at pipeline-definition time;
each can be set or reset at runtime to different timestamps. When dynamic timer
sets are needed, a common pattern is one timer set to the *minimum* pending
event-time among a collection, tracked in a `ValueState`, reset to the next
earliest after each firing.

## Conversion attribution example

Advertising **conversion attribution** — given visits, ad impressions, and
goals (purchases, signups), attribute each goal to the impression that started
the user's path — illustrates why generalized state is necessary:

- Out-of-order traffic from separate collection systems.
- High volume: potentially 90 days of visit/impression history per user.
- Spam protection: deduplicate logically-same events (multiple clicks on one
  ad within a day → one impression).

A single global window with per-user keys might declare:

- `MapState` for visits (keyed by URL) and impressions (keyed by
  `sourceUrl:targetUrl`).
- `SetState` for pending goals.
- `ValueState<Instant>` for the minimum pending-goal timestamp.
- One event-time attribution timer set to that minimum.

**`@ProcessElement`:** non-goal visits → blind write to visits map. Goals →
add to goals set; if timestamp precedes current minimum, reset timer and
update minimum. Impressions → write-if-absent (first-arrival-wins
deduplication — a performance/correctness tradeoff vs. first in event time,
which needs a pre-commit read).

**`@OnTimer`:** batch-read visits, impressions, and goals via parallel
futures; walk backward from the goal through referer chains to find a matching
impression; emit `Attribution` on success, remove consumed impression and
goal either way; recompute minimum remaining goal and reset or clear timer.

Production would also garbage-collect state older than the attribution
horizon. The pattern generalizes: defer expensive graph walks until the
earliest relevant event time, minimize I/O via typed fields and blind writes,
and collapse duplicates at write time when event-time ordering is too costly.
