---
type: concept
title: Streams and Tables Duality
description: >
  Tables as data at rest and streams as data in motion, and the three pipeline
  operation types — nongrouping, grouping, and ungrouping — that unify batch
  and streaming execution.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 7"
---

**Tables** are data at rest: not static — useful tables change continuously —
but at any instant a snapshot shows the dataset as a whole. A table is a
conceptual resting place where data accumulates and is observed over time.
Some tables accept time as a query parameter, yielding snapshots of past
states.

**Streams** are data in motion: a discretized view of how a table's data
evolves. Julian Hyde's framing: streams are the derivatives of tables, tables
the integrals of streams. Most databases are append-only logs under the hood;
transactions applied to a table are recorded in that log, then serially
applied to materialize updates — the log *is* the stream.

Two relative definitions tie them together:

- **Stream → table** — aggregating a stream of updates over time yields a
  table (materialized views fed by a source table's changelog are the classic
  example).
- **Table → stream** — observing changes to a table over time yields a
  stream.

Streams and tables are related but not identical; one can be fully derived
from the other without being the same thing. Stream constitution is
orthogonal to [bounded vs. unbounded](bounded-vs-unbounded-data.md)
cardinality — bounded batch pipelines are "streams and tables all the way
down."

## Three operation types

Every data-processing pipeline (batch or streaming) alternates among three
operation signatures; **table → table does not exist** — no operation moves
data from rest back to rest without passing through motion:

| Signature | Name | Effect | Examples |
| --- | --- | --- | --- |
| stream → stream | **Nongrouping** | Keep data in motion; may change cardinality | Filters, maps, parsers, partition-by-key (routes same-key records together but does not rest them) |
| stream → table | **Grouping** | Bring data to rest | Joins, aggregations, list/set accumulation, changelog application, histograms, model training |
| table → stream | **Ungrouping** | Put resting data back in motion | [Triggers](streaming-triggers-and-panes.md) — watermark completeness, per-record, early/late firings |

**Partition-by-key vs. group-by-key:** partitioning colocates same-key records
on one machine while keeping them in motion; grouping is partition-by-key
*plus* write-to-group, which is what converts the stream to a table.

## MapReduce as the pattern

A MapReduce job decomposes into six phases with clear stream/table roles:

`TABLE → STREAM → STREAM → TABLE → STREAM → STREAM → TABLE`

- **MapRead / ReduceRead** — read a table, emit a stream (one record at a
  time).
- **Map / Reduce** — nongrouping transforms; stream in, stream out.
- **MapWrite** — group-by-key into persistent storage; stream → table (the
  shuffle).
- **ReduceWrite** — stream → table at the sink.

The batch pattern derived from this: (a) read entire tables as streams; (b)
process streams until a grouping operation; (c) grouping rests the stream as
a table; (d) repeat until the pipeline completes.

## Mapping to the Dataflow model

The [four questions](dataflow-model-four-questions.md) map cleanly onto
stream/table operations:

- **What** — nongrouping transforms (stream → stream) and grouping transforms
  (stream → table).
- **Where** — windowing alters grouping semantics: window assignment combines
  with the user key into an implicit composite key; [merging windows](streaming-window-types.md)
  (sessions) treat window as a hierarchical child of the key, with key (not
  key+window) remaining the unit of atomicity — otherwise consistency for
  merged windows becomes far more expensive.
- **When** — triggers are ungrouping (table → stream). Batch effectively uses
  one trigger type: fire when input is complete. Incremental triggering is
  the main practical difference between batch and streaming — more a
  latency/throughput tradeoff than a semantic one.
- **How** — [accumulation mode](streaming-accumulation-modes.md) at ungrouping
  time determines whether emitted streams carry deltas, full values, or values
  plus retractions.

Trigger semantics are intentionally loose (`AfterWatermark` does not guarantee
firing exactly at the window boundary; `AfterCount(N)` may process more than
N) because triggering is inherently asynchronous even in low-latency systems.

## Database-as-stream-processor

Wherever a pipeline hits a grouping operation, that operation creates a table
holding current output values. If those values *are* the final result, read
directly from that state table rather than materializing to a separate sink —
saving compute, disk, and sink engineering — provided only the pipeline may
modify the table (otherwise consistency breaks). MillWheel customers serve
from Bigtable-based state this way. If downstream processing continues, the
table must be incrementally converted back to a stream via triggering.

## Physical execution

Optimizers fuse logical stages and annotate intermediate collections with
key/value/window/partition metadata. A typical team-score pipeline separates
physically into: nongrouping parse; nongrouping window assignment;
grouping (partition + group-by-key + window merge + incremental combine);
ungrouping trigger; sink write (itself a grouping if the sink is a table).

Net effect: batch and streaming are the same conceptual machinery —
[bounded data](bounded-vs-unbounded-data.md) is just a special case, and
[batch/stream unification](batch-streaming-unification-architectures.md)
at the execution-engine level (not just API level) is the natural end state.

Full-fidelity STREAM and TABLE renderings encode the same information. See
[time-varying relations](time-varying-relations.md) for the formal TVR
foundation and [streaming SQL extensions](streaming-sql-extensions.md) for
language-level defaults (per-record triggering, retractions-by-default).
