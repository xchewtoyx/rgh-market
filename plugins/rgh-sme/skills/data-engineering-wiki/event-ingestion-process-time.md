---
type: concept
title: Event Time, Ingestion Time, and Process Time
description: >
  The three distinct timestamps a streaming pipeline must track separately,
  and why conflating them breaks late-data and windowing logic.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
---

A pipeline processing events needs to distinguish three different points in
time, especially in streaming contexts:

- **Event time**: when the event actually happened at the source. There is
  always some lag before it's ingested or processed.
- **Ingestion time**: when the event lands in the pipeline — a message queue,
  cache, object storage, database, or similar.
- **Process time**: when, and for how long, transformation processing runs on
  the event after ingestion. Data may be processed immediately or may sit
  unprocessed for minutes, hours, days, or indefinitely first.

These three routinely diverge, and by how much is itself meaningful: a large
gap between event time and ingestion time is exactly what
[late-arriving data](late-arriving-data.md) looks like, and windowing logic
in a streaming transform (tumbling/sliding windows, watermarks) has to pick
which of the three timestamps it windows on — windowing by ingestion time
when the business question is really about event time silently produces
wrong aggregates for anything that arrived late.

The practical recommendation is to log and monitor all three timestamps at
every stage a record passes through, rather than assuming one timestamp field
stands in for all three — that's what makes it possible to diagnose whether a
downstream discrepancy is a late-arrival problem, an ingestion backlog, or a
slow transform.

**Client-reported event time is not always trustworthy enough to bucket
on.** A mobile client can buffer events offline for an extended period
(days, in some real systems) before it regains connectivity and finally
sends them, and individual device clocks drift out of sync with true time —
both mean the event-time field a client attaches to its own data can be
meaningfully wrong. Where a pipeline has to assign each record to a discrete
time bucket (an hourly partition, say) and getting that assignment right
matters more than preserving the client's own claimed timestamp, using
**server receipt time** — the ingestion timestamp the pipeline itself
generates the moment it receives the record — as the bucketing field sidesteps
both problems, at the cost of that bucket no longer exactly reflecting when
the event actually happened on the client. A pipeline that buckets this way
should track, as its own explicit quality signal, how much of its data lands
in the wrong bucket relative to where a perfectly accurate client timestamp
would have placed it — a **skew** rate — since bucket-closing heuristics are
never perfectly correct and some genuinely-late data will always land one
bucket later than it should.

**Processing-time lag vs. event-time skew** are two views of the same
processing/event-time divergence (they form a right triangle against the
ideal 45° completeness line):

- **Processing-time lag** — vertical distance: delay between when events
  occurred and when they were processed.
- **Event-time skew** — horizontal distance: how far behind the ideal (in
  event time) the pipeline currently is.

Because this mapping varies arbitrarily over time, windowing purely by
processing time is unsafe when event-time correctness matters — some
event-time data lands in the wrong processing-time window. Event-time
windowing introduces a **completeness problem** (when have you seen all data
for event time X?), addressed by
[watermarks](watermark-computation-and-propagation.md) and
[triggers](streaming-triggers-and-panes.md) rather than pretending batches
eventually become complete. See also
[processing-time windowing methods](processing-time-windowing-methods.md)
for when processing-time slicing is deliberately appropriate.
