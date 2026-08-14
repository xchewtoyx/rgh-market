---
type: concept
title: Weighted vs. Impact Reports
description: The two ways to query a bridge table whose members jointly share responsibility for the same facts — a weighted report that avoids double-counting and an impact report that doesn't.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 8"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 9"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

When a [bridge table](bridge-table.md) associates several dimension members that jointly share responsibility for the same measured facts — several account holders on one joint bank account, for instance — each bridge row can carry a numerical **weighting factor**, with the weights for all members of one group summing to exactly 1.00. Summing a fact after multiplying it by the weighting factor, then grouping by individual member, produces a **correctly weighted report**: the grand total across members matches the original fact total, with no double-counting. Querying the same bridge without applying the weights instead produces an **impact report** (e.g., "total balance of all individuals matching some demographic profile") — a number business users understand may overcount, because the underlying facts are legitimately associated with more than one bridged member at once. Both views are useful for different questions, and are typically exposed as two separate views over the same bridge join.

Physically multiplying the weighting factor into the fact and storing the result (changing the fact table's grain to one row per group member instead of one row per group) is rarely done: it multiplies fact table size by the average group size, compounds badly when a fact table has more than one multivalued dimension, and destroys the unallocated numbers some users still want — which are hard to reconstruct once the allocation has already been baked in. Applying the weighting factor at query time, through a view, keeps both the allocated and unallocated numbers available. A clean, business-vetted weighting factor is not always available in the first place (e.g. there is often no defensible rule for allocating a healthcare claim's cost across multiple diagnoses) — where a genuine allocation factor exists at the source, it may be cleaner to redefine the fact table's own grain around it (e.g. "order lines allocated to salesreps") than to build a bridge at all, and ownership of any allocation rule belongs with the business, not with the technical team building the schema. Some facts (a quantity of 1 for a single indivisible unit, for instance) can't be meaningfully allocated at all without producing confusing fractional results.

## The grain rule for impact reports

Simply avoiding a grand total is not sufficient to keep an impact report safe: query results must be grouped by a dimension column that takes a unique value per group member — typically its natural key — never by a coarser attribute. Grouping Ann and Henry's joint order by region instead of by salesperson, for example, still double-counts that order within "East," because the fact-to-bridge-to-dimension join repeats the fact row once per matching dimension row regardless of what the final `GROUP BY` targets. This is the same underlying hazard as the general fact-to-fact join Cartesian-product problem — see [drilling across](drilling-across.md).

A second layer of protection, alongside exposing weighted vs. impact views, is to supplement the bridge with a direct, ordinary one-to-many foreign key isolating just a **primary** role (e.g. `primary_salesrep_key`) on the fact table itself. Casual users and BI tools can then use that direct relationship without any risk of double-counting, while the full bridge — needed only for genuine multi-member analysis — stays reserved for trained analysts.
