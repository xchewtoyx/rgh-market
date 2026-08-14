---
type: concept
title: Time-Varying Relations
description: >
  Extending SQL relations to evolve over time while preserving relational
  closure, with stream and table renderings as two physical views of the same
  underlying data.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 9"
---

Historical streaming-SQL attempts broke **relational closure** — treating
streams and tables as separate types with distinct operators and conversion
rules — raising adoption cost and still failing on out-of-order processing
and temporal joins. The fix: make streaming a first-class citizen of
relational algebra by replacing point-in-time relations with **time-varying
relations (TVRs)**.

A TVR (Julian Hyde) is a classic relation's evolution over time. If a classic
relation is a 2D table (columns × rows), a TVR adds a z-axis of successive
snapshot versions — e.g., `SELECT TVR * FROM UserScores` returns the relation
as it looked during each contiguous, disjoint processing-time interval
(`[-inf,12:01)`, `[12:01,12:03)`, …).

Because each interval holds an independent classic relation, applying any
relational operator to a TVR equals applying it independently to each snapshot
in the sequence — yielding another TVR with the same intervals. **Closure
is preserved**: `WHERE`, `GROUP BY`, joins, and the full operator set compose
freely on TVRs exactly as on static relations.

TVRs are largely theoretical — fully materializing them for large, fast-
changing datasets is unwieldy — which motivates the practical
[streams-and-tables duality](streams-and-tables-duality.md) as two renderings
of the same TVR:

- **Table rendering** — observe the TVR at time T; get the point-in-time
  snapshot. Precedent exists in SQL:2011 temporal tables plus `AS OF SYSTEM
  TIME`.
- **Stream rendering** — emit the *sequence of changes* producing those
  snapshots, not full snapshots each time. A `Sys.Undo` column marks
  retractions (`undo` rows) vs. normal inserts; omitting `Sys.Undo` from the
  projection yields accumulating-only output. Aggregated changes require undo
  of old values plus new values (e.g., Julie's score 7 → 8 emits undo-7 and
  new-8).

Full-fidelity STREAM and TABLE renderings encode the same information —
Hyde's analogy: streams and tables are to TVRs as waves and particles are to
light. Real implementations are commonly **lossy**: tables keep only the
latest version; streams/logs retain limited history. Claiming "streams are
just never-ending tables" conflates the shared TVR primitive with the distinct
views.

## Beam vs. SQL bias

**Beam is stream-biased:** `PCollection`s are always streams; even grouping
(producing a conceptual table) yields another stream. Sources reading tables
hardcode their triggering policy; sinks writing tables hardcode grouping.
Triggers must be **predeclared** (forward-propagating, Beam 2.x) because
Beam lacks first-class table objects to attach triggers to — a real
shortcoming addressable by making both streams and tables first-class.

**SQL is table-biased:** queries take tables and yield tables. Decomposing
`SELECT team, SUM(score) … GROUP BY team` exposes SCAN (snapshot table →
bounded stream) → project (stream→stream) → GROUP BY (stream→table). Split
into two queries and the intermediate stream must implicitly become a table
(grouped by row identity), then re-SCAN'd for the next GROUP BY.

Implicit SQL conversion rules:

- **Input tables** — triggered in entirety at query time into a bounded
  stream (classic batch/MapReduce behavior).
- **Output tables** — direct grouping products, or implicit row-identity
  grouping of terminal nongrouping streams.
- **Ungrouping** — one implicit behavior only: trigger the intermediate table
  entirely once all upstream data arrives. Rich grouping (`GROUP BY`, `JOIN`,
  `CUBE`); zero flexibility shaping intermediate streams.

**Materialized views** are SQL's existing stream-processing form: a standing
query kept current as sources evolve — effectively a TVR. Physical plan change
vs. batch: substitute **SCAN-AND-STREAM** for SCAN — emit full snapshot,
then all subsequent modifications (INSERTs; UPDATEs/DELETEs as undo/redo
pairs). Table bias persists: real stream processing without abandoning SQL's
fundamentally table-oriented data-flow model.

See [streaming SQL extensions](streaming-sql-extensions.md) for the concrete
language additions (stream/table selection, windowing operators, triggers,
system columns) that make robust streaming SQL practical on top of TVRs.
