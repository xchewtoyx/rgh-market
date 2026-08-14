---
type: concept
title: Watermark Computation and Propagation
description: >
  How a low watermark is computed as a minimum over pending work and
  propagated through a computation graph, and the policy choices a pipeline
  still has to make when data arrives behind it.
sources:
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §4.5, 5.2"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 4"
---

A [watermark](streaming-window-types.md)'s value isn't set by a fixed delay
off wall-clock time — it's computed as a **minimum over pending work**,
recursively propagated through the computation graph:

```
low_watermark(A) = min(oldest_work(A), low_watermark(C) for each upstream C feeding A)
```

where `oldest_work(A)` is the timestamp of the oldest record A currently has
in flight, stored, or waiting to be delivered. A stage with no upstream
inputs has its watermark equal to its own oldest pending work; every
downstream stage's watermark is capped by whatever its slowest upstream
still hasn't finished with. This is why a bottleneck anywhere upstream holds
back every downstream watermark, not just the stage that's actually slow —
the minimum propagates the delay forward through the whole graph.

**Seeding the graph**: external data enters via **injectors**, which have no
upstream computation to inherit a watermark from, so they compute and
publish their own — typically the minimum timestamp among whatever external
work is still outstanding (e.g., a file-based injector reports the oldest
creation time among files not yet fully read). Because that measurement of
external pending work is often only an estimate, some rate of records
arriving *behind* the watermark should be expected in practice, not treated
as a bug to eliminate. An injector distributed across multiple processes
publishes an aggregate watermark across the whole set, with the expected
process set specified up front — this is what keeps the watermark
meaningful and robust to an individual injector process failing or a
network partition, rather than stalling on a process that's simply gone.

**The watermark is guaranteed monotonic** even though
[late-arriving data](late-arriving-data.md) keeps showing up behind it — the
system does not let a late arrival retroactively
push the watermark backward. This pushes the actual policy decision onto the
application: when a record does land behind the current watermark, the
pipeline can either discard it (tracking how much was dropped as an explicit
[data quality](data-quality-dimensions.md) metric — Zeitgeist observes on
the order of 0.001% of records this way) or incorporate it and retroactively
correct whatever aggregate it affects. Neither choice is forced by the
watermark mechanism itself; it only guarantees the *signal* is trustworthy,
not what to do when the signal says "too late."

## Why naive progress metrics fail

Basing window closure on **processing time** misassigns events whenever
transport or processing delay varies — no robust event-time correctness.
**Message processing rate** is a useful health metric but cannot answer
whether all messages for an interval have been seen; one stuck message can
corrupt output while overall throughput looks fine. Watermarks require each
message to carry a logical event timestamp.

## Perfect vs. heuristic source watermarks

All watermark creation is either **perfect** or **heuristic**; propagation
preserves that classification — a heuristic source never becomes perfect
downstream.

**Perfect** watermarks guarantee no data with event times below the watermark
will ever reappear from that source. Achievable when the source structure is
fully known: ingress timestamping (watermark tracks processing time — easy
but loses correlation to real event times), or a statically known set of
time-ordered partitions each internally monotonic in event time (Kafka with
fixed partition set, file sets with known membership).

**Heuristic** watermarks estimate completeness — late data is possible and
must be handled for correctness-sensitive workloads. Examples: dynamic file
sets with unknown cross-file ordering, Pub/Sub with no delivery-order
guarantee, mobile devices going offline for extended periods. The more known
about a source, the better the heuristic and the less late data results.

## Input and output watermarks per stage

Each pipeline stage maintains two watermarks:

- **Input watermark** — progress of everything upstream. For sources, the
  source-specific creation function; for downstream stages, the minimum of
  all upstream output watermarks.
- **Output watermark** — progress of the stage itself: the minimum of its
  input watermark and the event times of all non-late active messages (data
  buffered for aggregation, pending downstream output).

Subtracting output from input watermark gives **event-time lag** introduced
by that stage — a 10-second windowed aggregation adds at least 10 seconds.
Later stages inherit upstream lag, so their watermarks sit further in the
past. Within a stage, per-buffer watermarks (input buffer, state, output
buffer) aid diagnosing where messages are stuck.

## Output timestamps and watermark progression

Because watermarks are monotonic, a window result's output timestamp must be
at or after the earliest non-late record in the window. Common choices:

- **End of window** — safest when the timestamp should represent window
  bounds; smoothest watermark progression.
- **Timestamp of first non-late element** — maximally conservative; delays
  downstream watermarks.
- **Timestamp of a specific element** — e.g., query time vs. click time in a
  join.

Using earliest-element timestamps on **overlapping sliding windows** can
needlessly delay materialization: downstream window N can be held up by
not-yet-complete upstream windows N+1, N+2 that share elements. Frameworks
like Beam add logic ensuring window N+1's output timestamp exceeds window N's
end to avoid this trap.

## Processing-time watermarks

An event-time watermark stuck far behind real time is ambiguous: the system
might be processing old data quickly or genuinely delayed. A **processing-time
watermark** — the processing-time timestamp of the oldest incomplete
operation (shuffle, state I/O, delayed aggregation trigger) — disambiguates:

- Processing-time watermark also stuck → genuine stall (network, retry loop).
- Processing-time watermark healthy while event-time watermark lags → normal
  buffering awaiting a window boundary.

Processing-time watermarks also drive garbage collection of temporary
exactly-once dedup state (see
[delivery guarantees](delivery-guarantees-exactly-once-vs-at-least-once.md)).

## Percentile watermarks

Instead of the minimum (100th percentile) of active message timestamps, track
any percentile and guarantee that fraction of earlier-timestamped events has
been processed. Business logic that only needs to be "mostly correct" gets a
watermark that advances faster by discarding long-tail outliers — a
latency/precision trade-off (implemented in MillWheel; not in Beam at time of
writing).
