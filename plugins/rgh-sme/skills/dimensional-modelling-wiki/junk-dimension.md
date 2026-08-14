---
type: concept
title: Junk Dimension
description: A single dimension combining miscellaneous, low-cardinality transactional flags and indicators that would otherwise each need a separate dimension.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

A junk dimension (sometimes called a transaction profile dimension) combines miscellaneous, low-cardinality transactional flags and indicators — for example several unrelated Y/N indicators on a transaction — into a single [dimension-table](dimension-table.md), rather than giving each flag its own dimension and its own foreign key on the [fact-table](fact-table.md). This avoids the [centipede fact table](centipede-fact-table.md) anti-pattern that results from attaching many separate low-cardinality dimensions directly to the fact table.

A junk dimension need not contain the full Cartesian product of every possible combination of its constituent flags — only the combinations that actually occur in the source data, which is typically a small fraction of the theoretical maximum. Whether to pre-populate the full theoretical product or build rows incrementally as new combinations are encountered during extraction depends on how large the theoretical product is versus how many combinations are actually expected to occur.

Rough sizing guide for whether flags belong in one junk dimension: ten two-value indicators theoretically combine to 2^10 = 1,024 rows (workable, if not very browsable, as one dimension); five indicators of three values each combine to 3^5 = 243 rows (comfortably one dimension); five indicators of 100 values each would combine to 100^5 = 100 million rows — at that scale the indicators should instead become separate dimensions rather than one junk dimension.

## Naming

"Junk dimension" is useful shorthand among developers, but it's worth avoiding with business stakeholders during requirements discovery — a name that sounds dismissive of the dimension's contents undermines confidence in the design. "Miscellaneous dimension" is a safer generic term in front of stakeholders, and naming the table after the fact table it belongs to (a `call_detail` dimension for a `call_details_fact` table, or `sale_type` for `sales_fact`) is clearer still, since the dimension is genuinely specific to that one fact table rather than conformed and reused elsewhere — unlike most dimensions, it's expected to be non-conformed by design. If a single fact table ends up with several small, non-conformed junk-style dimensions, merging them into one is often a reasonable way to reduce the fact table's overall key count.
