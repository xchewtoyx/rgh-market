---
type: concept
title: Four-Step Dimensional Design Process
description: The four ordered decisions — business process, grain, dimensions, facts — that every dimensional design must make.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 18"
---

Every dimensional design follows the same four decisions, made in this order:

1. **Select the [business process](business-process.md)** — a low-level operational activity the organization performs (taking an order, processing a claim, registering a student), not an organizational department.
2. **Declare the [grain](grain.md)** — specify exactly what a single fact table row represents, in business terms.
3. **Identify the dimensions** — answer "how do business people describe the data resulting from the measurement events?" Dimensions typically supply the who, what, where, when, why, and how of the event (date, product, customer, employee, facility). A dimension is only valid at the declared grain if it takes a single value for a given grain-row; if it would generate extra fact rows, either disqualify it or revisit the grain. Worked example of the test itself: if every transaction uses exactly one payment method, payment method is a straightforward dimension. But if a single transaction can legitimately involve multiple payment methods, payment method no longer takes a single value at a transaction-grain fact row — the fix is not to distort the grain (e.g., inventing one row per payment-method-per-product), but to model payment method in a **separate fact table**, either at transaction grain with each payment option as its own fact, or at one-row-per-payment-method-per-transaction grain with its own dimension.
4. **Identify the facts** — answer "what is the process measuring?" All candidate facts must be true to the grain from step 2; facts belonging to a different grain go in a separate fact table. Typical facts are additive numeric figures (see [additive fact](additive-fact.md)).

If step 3 or 4 reveals that the grain statement was wrong, the design must return to step 2 and redo steps 3 and 4 — grain is never adjusted implicitly by adding dimensions or facts around it.

Both business requirements and source data realities should jointly drive these four decisions — resist designing from source data alone; data profiling establishes feasibility, but it is not a substitute for [gathering business requirements](gathering-business-requirements.md). See [agile data profiling](agile-data-profiling.md) for how a completed business-requirements model gets validated against real source data before physical design, and the [model review severity checklist](model-review-severity-checklist.md) for triaging what profiling finds. After the four decisions are made, the team determines table/column names, sample domain values, and business rules, with data governance participation to ensure buy-in.

## Finding fact table boundaries when stuck on step 1

Because a real business process routinely decomposes into several plausible subprocesses, it isn't always obvious from interview notes alone where one candidate fact table ends and another begins. A fact/dimension cross-reference matrix resolves this directly rather than by argument: list every candidate fact discovered in interviews as a row, every candidate dimension as a column, and mark which dimensional detail is actually available, at what timing, for each fact. Re-sorting the matrix so facts sharing an identical pattern of available dimensionality group together turns each resulting group into a candidate fact table — matching dimensional detail and availability timing across facts is exactly the test (see step 3 above) for whether facts belong together at one grain, so the matrix makes the same test visible at a glance instead of requiring it to be reasoned through fact by fact. Each group that falls out of the matrix can then be run through the four steps above independently.

After the design is complete, most business processes correspond to one row in the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md).

When no business-side documentation exists at all — an undocumented legacy schema, for instance — these same four steps can be run in reverse against the physical tables to produce a draft candidate model; see [reverse-engineering dimensions and facts from an existing schema](reverse-engineering-dimensions-and-facts-from-a-schema.md).
