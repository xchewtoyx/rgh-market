---
type: concept
title: Fact-to-Fact Join Cardinality Trap
description: >
  Why joining two fact tables directly through a shared dimension produces
  silently wrong totals whenever their cardinalities relative to that
  dimension differ, and the two load-time fixes.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 8"
---

Joining two fact tables directly through a dimension they both share (a
solicitations fact table and a responses fact table, both joined through
customer, say) looks like an ordinary query but produces **wrong answers**
whenever the two fact tables have different cardinality relative to that
dimension — not every solicitation gets a response, and some responses
don't correspond to a solicitation at all. This is a many-to-one-to-many
join, and no choice of inner, outer, left, or right join fixes it: the
database is working exactly as designed, the query itself is the mistake.

Two load-time-relevant fixes, not just a query-writing rule:

- **Never build a report or downstream table on a raw fact-to-fact join.**
  Query each fact table separately against the shared dimension, then
  combine the two independent result sets afterward (a full outer join on
  the dimension's key, keeping rows present in only one side) — the
  [drill-across](conformed-dimension-publish-subscribe.md) technique. This
  is a query-construction discipline every pipeline consumer needs to know
  about, but it's the pipeline engineer's job to make sure no ETL step ever
  takes the fact-to-fact shortcut internally either, since a materialized
  view or downstream table built on a bad join bakes the wrong cardinality
  into something consumers will trust without re-checking.
- **When users need the combination often enough to justify it, build a
  dedicated consolidated fact table** that merges the two processes' data at
  load time instead of relying on drill-across at query time. This doesn't
  make the cardinality problem disappear — it moves it earlier: the load
  now has to encode an explicit business rule for what happens to
  solicitations with no response and responses with no solicitation (include
  both sides regardless of match, or only matched pairs), because there's no
  cardinality-neutral default the ETL can silently pick on the business's
  behalf.
