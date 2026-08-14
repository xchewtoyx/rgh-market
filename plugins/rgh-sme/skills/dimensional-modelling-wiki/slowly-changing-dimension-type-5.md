---
type: concept
title: "Slowly Changing Dimension Type 5: Mini-Dimension and Type 1 Outrigger"
description: Extending type 4 by embedding a current, overwritten mini-dimension key on the base dimension so it can be queried as one combined table.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

Type 5 extends [type 4](slowly-changing-dimension-type-4.md) by adding a *current* mini-dimension key as a [type 1](slowly-changing-dimension-type-1.md) (overwritten) attribute on the primary, larger dimension — logically presented to users as one combined table via the [outrigger dimension](outrigger-dimension.md) relationship. This reference is deliberately kept type 1 rather than type 2, to avoid reintroducing the row explosion that type 4 was designed to prevent. Joining the base dimension straight to the mini-dimension through this current-key reference — skipping the fact table entirely — is called a **shortcut join**: it answers "current profile" questions like "how many customers currently have high income?" directly, at the cost that a shortcut join generally can't be combined with a fact-table join in the same query.

This is useful for a current profile count without needing to touch fact table data at all, or for rolling up historical facts by a customer's *current* profile rather than the profile in effect at the time of each fact. Current-attribute columns exposed this way should be distinctly labeled (e.g., "current age band") to reduce confusion, since exposing both the standalone mini-dimension and this outrigger path to users adds functionality but also adds complexity. The type 1 reference must be overwritten by ETL on the base dimension every time the customer's current mini-dimension assignment changes.

The type numbering across [types 5-7](slowly-changing-dimension.md) is largely playful rather than mathematically meaningful: 5 = 4 + 1.
