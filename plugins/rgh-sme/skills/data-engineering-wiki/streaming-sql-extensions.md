---
type: concept
title: Streaming SQL Extensions
description: >
  The minimal language additions beyond time-varying relations — stream/table
  selection, first-class windowing, trigger vocabulary, and system columns —
  needed for robust streaming SQL with sensible defaults.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 9"
---

Once [time-varying relations](time-varying-relations.md) replace point-in-time
relations, robust streaming SQL needs only two extension categories beyond
standard algebra — with good defaults, rarely invoked explicitly:

1. **Stream/table selection** — choosing the physical rendering when
   materializing a TVR.
2. **Temporal operators** — timestamps, windowing, triggering.

## Stream and table selection

Hypothetical `TABLE` and `STREAM` keywords after `SELECT` pick the desired
rendering. Default when neither is specified (honoring SQL's table-biased
feel):

- All table inputs → **TABLE** output.
- Any stream input → **STREAM** output.

Physical rendering matters only when viewing or writing output; intermediate
`WITH … AS` / `SELECT … INTO` can stay as full-fidelity TVRs internally.

Event time is an ordinary column — `ORDER BY EventTime` vs. `ORDER BY
ProcTime` re-sorts the same snapshot. For bounded execution, TABLE and STREAM
renderings of a terminal aggregate converge (STREAM adds an explicit
`END-OF-STREAM` marker).

## Windowing

Two approaches:

1. **Ad hoc** — compute boundaries manually in `GROUP BY` (e.g.,
   `EventTime / INTERVAL '2' MINUTES`).
2. **First-class operators** — e.g., Calcite's
   `TUMBLE(EventTime, INTERVAL '2' MINUTES)` in projection and `GROUP BY`.

First-class windowing avoids hand-computation errors and expresses dynamic
groupings like [sessions](streaming-window-types.md) concisely — ad hoc SQL
via analytic functions and self-joins is described as unmaintainable for
sessions.

## Triggers

SQL warrants a different default than Beam's watermark trigger:
**per-record triggering** (emit on every new input row) — matching
[materialized view](time-varying-relations.md) semantics and change-data-
capture fidelity. Beam approximates via `Repeatedly(AfterCount(1))`.

Custom trigger vocabulary via hypothetical `EMIT <when>`:

| Trigger | Form | Notes |
| --- | --- | --- |
| Watermark | `EMIT WHEN WATERMARK PAST WINDOW_END(Window)` | One output per window; classic late-data problem under heuristic watermarks |
| Watermark + late | `EMIT WHEN WATERMARK PAST <col> AND THEN AFTER <duration>` | On-time plus incremental late amendments; duration 0 = per-record late |
| Processing delay | `EMIT AFTER <duration>` | Unaligned processing-time delay; no watermark needed; spreads load vs. aligned microbatch |

Data-driven triggers (`EMIT WHEN Score > 10`) are unnecessary — per-record
triggering plus `HAVING` covers the case.

## Accumulation and retractions

Default examples used **accumulating mode**, but accumulating alone is
"plain broken" for two or more serial grouping operations — downstream
aggregations overcount when multiple revisions of an intermediate row arrive.

**Default: accumulating-and-retracting under the covers** via `Sys.Undo`.
Omit `Sys.Undo` from SELECT → accumulating-only view; project it → full
retraction semantics. Systems can detect single-grouping queries writing to
per-key-update storage and disable retractions as an optimization.

Motivating example: incremental session windows to a key/value store.
Without retractions, merged sessions grow with no signal of superseded
sessions — downstream needs expensive read-modify-write overlap detection,
breaking [idempotency and exactly-once](idempotent-and-replayable-jobs.md).
With retractions, explicit `undo` rows accompany replacements; consumers write
new rows and delete `undo` rows trivially (eventual consistency; globally
coherent instant views need timestamped reads behind the output watermark, or
serving from pipeline state tables per
[streams-and-tables duality](streams-and-tables-duality.md)).

**Discarding mode** — not worth SQL-level support; narrow cases can use
non-SQL options.

## System columns

| Column | Meaning |
| --- | --- |
| `Sys.MTime` | Processing time row last modified/arrived |
| `Sys.EmitTiming` | Early / on-time / late relative to watermark |
| `Sys.EmitIndex` | Zero-based revision index (for merging windows: max of merged sessions + 1) |
| `Sys.Undo` | Retraction marker; omitting yields accumulating-only semantics |

Together: TVRs preserve closure; Beam is stream-biased while SQL (including
materialized views) is table-biased; these extensions — with per-record
default triggering and retractions-on-by-default — bridge the gap without
abandoning relational algebra. Much of this vision (2017 Calcite/Flink/Beam
collaboration building on Julian Hyde's Calcite streaming-SQL work and Flink's
2016 Calcite integration) remains aspirational as of publication — Calcite
has windowing constructs; many trigger/system-column pieces do not yet exist
concretely.
