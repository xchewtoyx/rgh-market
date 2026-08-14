---
type: concept
title: Additive Fact
description: A numeric fact that can be correctly summed across every dimension attached to its fact table.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1-3"
---

A fully additive fact can be summed across any dimension associated with its [fact-table](fact-table.md) row — this is the most flexible and useful category of fact, since BI queries typically retrieve and sum many rows at once. Sales quantity and extended sales dollar amount are canonical examples: extending a fact by quantity (rather than leaving it as a per-unit metric) is generally what makes it additive.

**Derived (calculated) facts** — such as gross profit (extended sales − extended cost) — can be perfectly additive across all dimensions despite being computed rather than captured directly. The recommended practice is to physically store derived facts, computed consistently once in ETL, rather than leaving the calculation to users or BI tools; inconsistent user-side calculation is costly and undermines consistency across tools and users. A view that performs the calculation is an acceptable alternative only if every user is forced through the view with no ad hoc backdoor access to the raw table.

Additivity is contrasted with [semi-additive fact](semi-additive-fact.md)s (summable across some dimensions but not all) and [non-additive fact](non-additive-fact.md)s (never summable). All candidate facts must also be true to the fact table's [grain](grain.md) — a measurement at the wrong grain will be silently overcounted by an automatic SUM, regardless of whether it is otherwise additive.

When a source system corrects an already-loaded additive fact after the fact, simply landing every raw version and summing over them double-counts the change — see the [reverse balance fact table](reverse-balance-fact-table.md) pattern for how to capture corrections without breaking plain SUM aggregation.
