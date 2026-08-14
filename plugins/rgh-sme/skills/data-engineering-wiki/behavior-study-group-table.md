---
type: concept
title: Behavior Study Group Table
description: >
  Persisting the durable keys of a customer (or product) cohort identified
  by a complex query, so later analysis can reuse the cohort as a plain join
  constraint instead of recomputing it.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 8"
---

Some analytic questions ("customers who bought more this month than their
average monthly purchase last year") don't reduce to a single SQL statement
a typical BI tool can generate, and re-running the query that identifies
such a cohort every time it's needed downstream is wasteful once the cohort
itself is what matters, not how it was derived.

The **behavior study group** pattern: run the identifying query once,
capture the resulting entities' [durable
keys](durable-key.md) into a small, physical single-column table, and use
that table as an ordinary join constraint against other fact tables from
then on. Persisting the durable key rather than the dimension's surrogate
key is what makes the study group immune to subsequent
[Type 2](insert-only-history-pattern.md) changes in the entity's dimension —
a customer who later gets a new surrogate-keyed version row is still
correctly recognized as a member of the study group, since the durable key
they were captured under never changes.

Load-mechanics properties that make this useful beyond a one-off query:

- **Set operations compose cleanly.** Because a study group table is just a
  column of keys, union/intersect/except between two study groups (e.g.,
  intersecting "problem customers this month" with "problem customers last
  month" to find customers who were problems in both) is a plain set
  operation, no different from combining any other key lists.
- **An occurrence-date column turns a study group into a panel study** —
  tracking an entity's follow-on behavior after some initiating event, with
  the date column preserving the sequence between the initiating and
  follow-on observations.
- **Hide it behind a view equijoined on the durable key** so the schema
  still presents as an ordinary star to BI tools that don't need to know a
  study group is involved — but label the view clearly (e.g., "top 100
  customers") so it isn't mistaken for a primary dimension.

The trade-off against this convenience: a study group table needs its own
UI or process for creation and administration, and — because it joins
directly against the dimension it constrains — it has to live in the same
database space as the fact table it's meant to filter, which is a DBA
consideration, not just a modeling one.
