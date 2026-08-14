---
type: concept
title: Surrogate-Key-Range Recovery for Fact Loads
description: >
  Using a fact table's single sequential surrogate key to cleanly back out or
  resume a load that failed partway through, by constraining on a key range.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

A large fact load can fail partway through for reasons outside the
pipeline's control — network, database, disk, or memory failures, a data
quality violation, an unannounced upstream system change. Two load-design
choices make recovering from that cleanly tractable:

- **Commit in small, adjustable-sized record batches, and track exactly what
  was committed.** A failure mid-load then only requires re-establishing
  where the last successful commit left off, rather than treating the whole
  load as one indivisible unit of work — the same
  [granularity](pipeline-granularity-and-blast-radius.md) principle applied
  at the commit-batch level rather than the job-step level. Batch size is a
  real tuning knob: it trades commit overhead against how much work a
  mid-batch failure loses.
- **Give the fact table a single-column, sequentially assigned surrogate
  key** — a plain incrementing integer, not a composite or hashed key. This
  single design choice gives recovery a cheap, unambiguous handle: backing
  out or resuming a halted load is a single `WHERE surrogate_key BETWEEN ...`
  range constraint, rather than having to reconstruct which rows belong to
  the failed load from business keys or timestamps. The same sequential key
  also makes [two-phase update](table-load-patterns.md) (insert corrected
  rows, delete originals in a second step) straightforward, gives every row
  an unambiguous single-column identity independent of its dimension foreign
  keys, and serves as a natural parent key when a child fact table needs to
  reference a specific parent fact row — or, within a single periodic-
  snapshot table, as a [self-referencing parent
  key](self-referencing-snapshot-drill-down.md) for rows that roll up into
  other rows of that same table.

Whether a restart is even possible without falling back to reprocessing the
whole load from scratch depends on the pipeline tool actually providing
reliable checkpoint tracking — without it, the only safe recovery is backing
out everything the failed run touched and restarting from the beginning,
which is exactly the expensive, all-or-nothing failure mode that
[fine-grained pipeline design](pipeline-granularity-and-blast-radius.md)
exists to avoid.
