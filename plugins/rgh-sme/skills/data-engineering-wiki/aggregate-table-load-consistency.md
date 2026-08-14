---
type: concept
title: Aggregate Table Load Consistency
description: >
  Keeping a pre-computed aggregate table's load in lockstep with the atomic
  base table it summarizes, including when a rebuild is unavoidable versus
  when an incremental update suffices.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

A pre-built aggregate table (or a shrunken/rolled-up dimension paired with
it) exists purely for query performance, but from a load perspective it's an
extra table that must never be allowed to drift out of sync with the atomic
base data it summarizes. Two load strategies:

- **Incremental update** — extend the aggregate with only the newly loaded
  base rows. Fastest, and the default choice whenever nothing about the
  underlying dimension structure has changed.
- **Drop and rebuild** — required whenever a major dimension attribute
  change invalidates the existing rollup (see [SCD Type 1/3 overwrite load
  mechanics](scd-overwrite-load-mechanics.md) for why an overwrite forces
  this), or after any other change that makes incrementally patching the
  aggregate unsafe. A [Type 1 change on a rollup-dimension
  attribute](type1-change-aggregate-corruption-trap.md) is the specific,
  easy-to-miss case: it doesn't just invalidate new loads, it silently
  misattributes aggregate rows already built before the change.

**Source an aggregate from its own base star, never from the aggregate's
original upstream sources.** Loading a rollup dimension or aggregate fact
table straight from the same source the base table came from risks applying
transformation rules slightly differently in two places, breaking the
aggregate's required conformance with the base star it's supposed to
summarize. Loading it from the already-loaded base table instead guarantees
structural and content conformance for free, and simplifies the ETL itself —
a rollup dimension that's an identical replica of part of the base dimension
needs no transformation logic at all beyond straight replication, and a
conformed rollup (month rolled up from day, say) only needs to detect which
base-dimension rows changed since the last run, which housekeeping columns
like `date_created`/`date_modified` on the base dimension make cheap to
detect.

For very large aggregations, building outside the database engine — dumping
the base data out and computing sums via an external sort utility, using
sort-break rows to aggregate additive numeric facts as they stream past — can
outperform computing the same aggregate inside the DBMS.

The consistency rule that matters most operationally: **an aggregate table
must be taken offline the moment it's known to be inconsistent with its base
data**, rather than left queryable with silently stale numbers while a
rebuild runs in the background. A wrong total that's visibly missing is a
much smaller problem than a wrong total that looks normal.

What to build aggregates *for* is itself a load-adjacent input, not a
one-time design decision: capturing a log of frequently run slow queries —
and, where possible, inferring queries that never even got attempted because
users learned they'd time out — is the concrete signal that should drive
which aggregates get built next.

A related but distinct case is embedding a single aggregated value directly
on a dimension row rather than in its own aggregate table — see
[aggregated fact as a dimension attribute](aggregated-fact-as-dimension-attribute.md)
for the different consistency obligation that creates.
