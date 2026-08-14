---
type: concept
title: Heuristic Source Watermarks for Pub/Sub
description: >
  How a pipeline builds an event-time watermark from a messaging source that
  exposes only processing-time backlog signals, using a dual-subscription
  tracking pattern.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 4"
---

Google Cloud Pub/Sub delivers messages with no hard ordering guarantee even
within a single publisher's sequence. A perfect event-time watermark is
impossible; Dataflow builds a heuristic instead.

**Assumption:** source-side event timestamps are well behaved — bounded
out-of-order before publish. Data outside that bound counts as late. The
implementation uses an **estimation band** (at least 10 seconds when caught
up): the watermark sits that far behind real time to absorb source-side
reordering. When backlogged, the entire backlog feeds the estimate, not just
the band.

**Problem:** Pub/Sub exposes only processing-time signals — oldest
unacknowledged publish timestamp — which can differ arbitrarily from event
time (historical replay, delayed publishing).

**Dual-subscription solution:**

- **Base subscription** — what the pipeline reads and processes.
- **Tracking subscription** — metadata-only, kept nearly caught up. Inspects
  backlog ahead of the base subscription's oldest unacknowledged message and
  takes the minimum event timestamp there. Messages are acked on the tracking
  subscription once publish/event timestamp metadata is durably saved (sparse
  histogram format).

The watermark advances when either the tracking subscription is ahead of the
base by at least the estimation band, or the tracking subscription has no
backlog. The value is the minimum event time in the band of tracking-subscription
timestamps newer than the base's oldest unacknowledged publish time. Correct
within the reorder bound, but can advance too slowly because it may include
timestamps for messages already acknowledged on the base subscription.

**Sparse-data heuristic:** if no data arrives for more than two minutes and
there is no backlog, advance the watermark heuristically toward real time so
the pipeline keeps making progress without further messages.

This pattern illustrates why some source watermarks benefit from
[centralized watermark aggregation](watermark-aggregation-centralized-vs-in-band.md)
— global backlog and idleness signals are easier to compute outside the
in-band data path.
