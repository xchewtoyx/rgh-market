---
type: concept
title: Read Path vs. Write Path Precomputation
description: >
  Deciding whether a result gets computed once when data arrives or freshly
  on every query, and why every index, cache, and materialized view is that
  same decision applied to a specific piece of work.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

Any piece of derived output — an aggregate, a joined view, a search result —
can be produced one of two ways, and naming which one a given design choice
is clarifies what it's actually trading off:

- **Write path (eager evaluation)**: do the work when new data arrives, once,
  and store the result — precomputing an index, updating a
  [materialized view](stream-enrichment-and-joins.md), incrementally
  advancing an aggregate. Every future read is then cheap, because the work
  already happened.
- **Read path (lazy evaluation)**: defer the work until a query actually asks
  for it, computing the result fresh each time. Every write stays simple and
  cheap, because nothing downstream has to be kept in sync with it.

Indexes, caches, and [aggregate tables](aggregate-table-load-consistency.md)
are all instances of deliberately shifting work from the read path to the
write path: the cost of computing a result is paid once, up front, by
whichever process handles the write, instead of being paid repeatedly by
every future query. This is exactly the same trade-off
[transformation vs. query](transformation-vs-query.md) already names at the
pipeline-persistence level — a transformation is a write-path choice; an
ad hoc query left unmaterialized is a read-path choice — and it's also the
same axis a [semantic/metrics layer](semantic-metrics-layer.md) decision
runs along: whether a governed metric gets materialized into a table ahead of
time or computed on demand from a shared definition at query time.

The general rule this framing makes explicit: push work to the write path
when the same result will be read many times relative to how often the
underlying data changes (the precomputation cost amortizes); leave work on
the read path when data changes about as often as it's queried, or more
often — precomputing a result nobody ends up reading, or that goes stale
before its next read, wastes the write-path cost with no payoff. Every
pipeline design decision about where to materialize a result — in a
warehouse table, in a cache, or not at all — is a version of this same
choice, made at a different point along the write-to-read continuum.
