---
type: concept
title: Behavioral Dimension Load Mechanics
description: >
  Pushing past-behavior computation into the load so end users can filter on
  it directly, and the two load-design rules that keep the resulting
  dimension attribute from breaking under its own maintenance.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Adamson), ch. 6"
---

A **behavioral question** — filtering or grouping facts by a dimension
member's *past behavior* ("customers who spent over $1M last year," say) —
effectively uses one fact as if it were a dimension attribute of another. Computed
at query time, this needs a correlated subquery or procedural logic well
beyond a plain SELECT/GROUP BY: it performs poorly enough to force these
reports into scheduled batch windows, and it's typically beyond the SQL
skill of the end users and even junior analysts who'd want to ask this kind
of question themselves.

The fix is a **behavioral dimension**: extend the relevant dimension table
with columns that capture past behavior, computed once during the load
instead of recomputed by every query that needs it. Three variants:

- **Past association with another dimension** — store a historic date or
  reference directly on the dimension row (`first_order_date`,
  `last_order_date`), so a query can filter on "when did this customer last
  order" with a plain column comparison instead of a fact-table query.
- **Historic fact** — store an aggregated, qualified value directly on the
  dimension row (a customer's `annual_sales`), turning a correlated subquery
  into a plain `WHERE` clause. See [aggregated fact as a dimension
  attribute](aggregated-fact-as-dimension-attribute.md) for this variant's
  full load-consistency treatment.
- **Categorizing ("banding")** — bucket a historic fact into named ranges as
  its own attribute (`annual_sales_group`: "under $500K" / "$500K–$1M" /
  "over $1M"), purpose-built for `GROUP BY` where the raw numeric value
  isn't.

**Two load-design rules keep a behavioral attribute from becoming a
maintenance problem of its own:**

- **Never version a behavioral attribute as [Type 2](insert-only-history-pattern.md).**
  A behavioral attribute like `last_order_date` changes on every single
  transaction for an active entity — versioning it would insert a new
  dimension row on every order, defeating any control over dimension growth.
  Behavioral attributes are always [Type 1](scd-overwrite-load-mechanics.md)
  overwrites. On the rare occasion a *historic* value of a behavioral
  attribute is genuinely needed ("what was this customer's last order date
  as of last February?"), the answer is to query the fact table directly for
  that one-off need rather than trying to make the behavioral column
  versioned.
- **Match refresh cadence to actual need, not to the load's default
  schedule.** Recomputing a full trailing-year aggregate for every dimension
  member on every nightly load can be excessive load-processing cost for a
  figure nobody needs updated that often. Defining the attribute on a
  coarser, explicitly documented cadence (a quarterly refresh of "sales for
  the prior four quarters," say) keeps the computation cost bounded — as
  long as users are told the column's actual currency, so a quarterly figure
  isn't mistaken for a daily one. As with the Type 2 rule above, a genuinely
  up-to-the-moment number is still available by querying the fact table
  directly when that rare need arises; the behavioral column exists for the
  common case, not every case.
