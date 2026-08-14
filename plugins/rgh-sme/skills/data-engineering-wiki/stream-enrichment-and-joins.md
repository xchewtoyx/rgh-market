---
type: concept
title: Stream Enrichment and Stream-to-Stream Joins
description: >
  Adding reference-data context to events in flight versus joining two
  independent streams together, and why differing per-stream latency makes
  the second much harder than the first.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 10"
---

**Enrichment** joins a stream to reference data — a lookup, not another
stream — to enhance events in flight. A typical shape: an incoming
product/user-ID event passes through a function that looks up product or
demographic detail in a cache or table, then emits an enriched event to a
new stream. The enrichment source can be a warehouse table, an RDBMS, or an
object storage file; the mechanism is simply "read from a source, keep what's
needed somewhere retrievable, and attach it to the event as it passes
through."

**Stream-to-stream joining** is a harder problem: joining two independently
arriving streams to each other, complicated by each stream having its own
latency (one source might lag by five minutes) and by individually delayed
events (a mobile session-close event that only reaches the stream once the
device regains connectivity — the same [late-arriving data](late-arriving-data.md)
issue, now on both sides of a join at once). The typical architecture holds
each stream in a configurable **streaming buffer**; events join against
whatever the other stream's buffer currently holds within a configured
retention interval, then get evicted. Longer retention catches more
legitimately-matching pairs at the cost of more storage and resource use —
this retention window is a direct trade-off between join completeness and
cost, tuned the same way a
[watermark](streaming-window-types.md) trades off lateness tolerance against
how long a window stays open.

**Table-table joining** is a related but distinct case worth naming
separately: rather than joining transient events, it joins two
[change data capture](change-data-capture.md) streams — each one the
changelog of an entire source table — to continuously maintain a downstream
materialized view. Each incoming change from either side triggers a
recomputation of the affected rows in the joined view, rather than a one-time
batch join; the join result is a live, always-current table rather than a
stream of enriched events. This is the mechanism behind keeping a derived
denormalized view (e.g., a fact table that joins two source tables' change
streams to stay pre-joined) continuously up to date without re-running a
batch join on a schedule.

## All joins are streaming joins

A join is a grouping operation: collecting previously unrelated elements that
share a key. Grouping consumes a stream and yields a table — so at heart all
joins, windowed or not, are streaming joins. Windowing, watermarks, and
[triggers](streaming-triggers-and-panes.md) apply unchanged; no separate
"streaming join theory" is needed.

**Windowing is optional.** Unwindowed joins over unbounded data work fine —
equivalently a join within a single global window covering all time. Consuming
the resulting table as a stream requires an ungrouping trigger other than
"wait until all input is seen" (per-record or periodic processing-time
triggering).

## FULL OUTER as the core primitive

Despite SQL's variety (FULL/LEFT/RIGHT/INNER/CROSS/ANTI/SEMI), there is one
core join: **FULL OUTER**. CROSS is FULL OUTER with a vacuously true
predicate. Every other variant is a filter on FULL OUTER's output stream:

- **LEFT OUTER** — drop rows with unjoined right side.
- **RIGHT OUTER** — drop rows with unjoined left side.
- **INNER** — drop all unjoined rows (intersection of LEFT and RIGHT OUTER).
  Retractions still occur when an already-joined input value is corrected.
- **ANTI** — unjoined rows only; heavy on retractions/false-starts as matches
  later arrive.
- **SEMI** — like INNER with one side's columns dropped; for N:M cardinality
  with M > 1, SEMI yields at most one output row per left key (existence
  check) vs. multiplicative duplication under INNER (k:k matching expands to
  k² rows).

Implementations are often far more efficient than literally computing FULL
OUTER and filtering.

## Why window a join

Two distinct motivations:

1. **Partition time meaningfully** — fixed windows for daily billing;
   [temporal validity windows](temporal-validity-windows.md) for rate tables
   whose rows define validity intervals.
2. **Anchor watermark-based timeout** — outer joins need a completeness
   reference. Unbounded data never "finishes." Windowing supplies the
   reference point: once the
   [watermark](watermark-computation-and-propagation.md) passes the window
   end, the engine can time out unjoined rows safely, as in bounded batch
   processing.

**Fixed-window join mechanics:** add `Left.Window = Right.Window` to the join
predicate (e.g., matching tumbling windows on each side). Rows that would
join unwindowed but fall in different window intervals do not join — each
surfaces as unjoined in its own window. Unwindowed joins reach eventual
completeness across all time; windowed joins complete only within the same
window slice. LEFT/RIGHT/INNER/ANTI/SEMI derivations apply identically once
windowed — windowing is orthogonal to variant filtering.

**Inner joins without windows** buffer one side until a match arrives from
the other — no temporal element. Outer joins reintroduce the completeness
problem (how long to wait?), which windowing plus watermarks address.
