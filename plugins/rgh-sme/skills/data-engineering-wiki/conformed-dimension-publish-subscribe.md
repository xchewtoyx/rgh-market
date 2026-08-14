---
type: concept
title: Conformed Dimension Publish/Subscribe Delivery
description: >
  Delivering a conformed dimension from one central publisher to every fact
  table that consumes it, in lockstep, so drill-across queries never compare
  two fact tables against different dimension versions.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

A conformed dimension needs a single, consistent source of truth — if two
fact tables that share a dimension each maintained their own copy, drill-
across queries between them would silently compare rows against
inconsistent dimension state. The load-mechanics answer is a
publish/subscribe split of responsibility:

- A **dimension manager** owns preparing and publishing one conformed
  dimension: applying agreed descriptive labels, adding rows for new
  entities and for [Type 2](insert-only-history-pattern.md) changes (new
  surrogate keys), applying [Type 1/3](scd-overwrite-load-mechanics.md)
  changes in place, and — critically — replicating the revised dimension to
  every subscribing fact table **simultaneously**, not on each consumer's own
  schedule. There can be several dimension managers, each owning a different
  dimension, but only one manager per dimension.
- A **fact provider** owns one or more fact tables and receives dimensions
  from whichever managers it depends on. On receiving an update it replaces
  or locally applies the new dimension state via its own
  [surrogate key pipeline](surrogate-key-pipeline.md), loads new fact rows
  against it, and — because a dimension change can invalidate them — drops
  and recalculates any affected [aggregates](aggregate-table-load-consistency.md),
  incrementally extending them if the dimension's version didn't change or
  fully rebuilding if it did.

The mechanism that makes "simultaneous" enforceable across fact tables that
may live on different machines or tablespaces: every conformed dimension row
carries a **version number**, incremented on any change. A drill-across query
tool can then check that every fact table it's about to join against is
running the same dimension version before trusting the comparison, rather
than silently joining across two tables that received the same logical
update at slightly different times.

Drilling across through a shared conformed dimension — querying each fact
table separately and combining the results afterward — is also the fix for
the [fact-to-fact join cardinality
trap](fact-to-fact-join-cardinality-trap.md): joining two fact tables
directly through their shared dimension in one query, rather than combining
two independent result sets, silently produces wrong totals whenever the
two fact tables' cardinality relative to that dimension differs.
