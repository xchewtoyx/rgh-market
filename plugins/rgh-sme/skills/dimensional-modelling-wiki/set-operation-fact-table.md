---
type: concept
title: Set Operation Fact Table
description: A derived fact table precomputing the union, intersection, or difference between two stars sharing common dimensions, avoiding an expensive set operation at query time.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 14"
---

A set operation fact table is a [derived schema](derived-schema.md) that takes two stars sharing common dimensions and precomputes the result of a set operation (union, intersect, minus) or an equivalent subquery, storing that result in its own new fact table — moving the cost and complexity of the set operation out of every query and into ETL, done once.

The classic motivating case pairs a factless [factless fact table](factless-fact-table.md) condition star (customer-to-salesperson assignments, say) against a transaction star built from the same dimensions (customer orders). Finding the mismatch between them — assignments with no resulting orders, or orders from customers nobody was assigned to — is exactly the kind of comparison covered under [factless fact table](factless-fact-table.md)'s condition-versus-activity techniques (set difference, correlated subquery), and is expensive and awkward to write at query time either way.

## Which set operations are worth precomputing

Given two stars (call them set 1 and set 2, e.g. assignments and orders), a Venn-diagram view of the possible comparisons shows which are typically worth building:

- **1 minus 2** (assignments with no orders): identifies underperforming relationships, useful for sales management.
- **2 minus 1** (orders with no assignment): identifies activity that fell outside the expected relationship structure, often a source of organizational friction when named-account assignments exist.
- **1 intersect 2** (assignments with orders): identifies the "legitimate" overlap, useful when downstream calculations (commission, for instance) should only apply to activity within an assigned relationship, and can carry the same facts as the underlying activity star.
- **1 union 2**: not every combination has a clear business meaning — a straightforward union of assignments and orders, for example, answers no obvious question, so it isn't automatically worth precomputing just because it's technically possible.

Precomputing is worthwhile mainly for intersect and minus operations, and typically pairs a coverage/condition factless star against a transaction star: products that did or didn't sell while under promotion, weather's effect on sales, or eligible-party participation in a benefits program are all the same shape of comparison. Whether to precompute at all versus compute the comparison per-report is a volume judgment: if only a small share of reports need the comparison, computing it inline case by case is fine; once a substantial share of reports depend on it, the added ETL burden of a dedicated derived star (or cube) pays for itself in simpler, faster reports.
