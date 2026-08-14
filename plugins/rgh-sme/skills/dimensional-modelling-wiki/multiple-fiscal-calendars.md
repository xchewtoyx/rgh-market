---
type: concept
title: Multiple Fiscal Calendars
description: Techniques for handling more than one fiscal calendar, or a genuinely different calendar system, on top of a single date dimension.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 7"
---

With a single fiscal calendar, calendar month and accounting period are simply parallel hierarchical attributes on one daily [date dimension](date-dimension.md) — see [fixed-depth hierarchy](fixed-depth-hierarchy.md). When multiple fiscal calendars vary by subsidiary or line of business (fiscal periods often don't align with Gregorian months at all, e.g. thirteen 4-week periods or 5-4-4 patterns), the right technique depends on scale:

- **Small, fixed number of calendars**: add a uniquely labeled fiscal-attribute set per calendar directly to the single date dimension (one row shows "period 1 for subsidiary A, period 7 for subsidiary B" side by side).
- **Large or complex number of calendars**, three options: (1) keep the official corporate fiscal calendar on the primary date dimension, and add a date-dimension [outrigger dimension](outrigger-dimension.md) keyed by (date, subsidiary) — one row per day per subsidiary holding that subsidiary's fiscal groupings — presented through a subsidiary-filtered view so it reads as part of the date dimension; (2) build **separate physical date dimensions per subsidiary calendar**, sharing common surrogate date keys, favored when fact data is itself decentralized by subsidiary; or (3) add a foreign key to a compact **subsidiary fiscal period dimension** (e.g., roughly 36 rows for three years across a handful of unique calendars), which simplifies user access at the cost of pushing the complexity of picking the correct fiscal period key into ETL at transform time.

The same (date, grouping-key) outrigger technique applies to genuinely different *calendar systems* for a multinational deployment (Gregorian, Hebrew, Islamic, Chinese, and so on): the primary date dimension holds generic, calendar-system-independent attributes, and a **country-specific date outrigger**, keyed by primary date key plus country code, supplies country-specific attributes such as local holiday or season names — with the same caution as any multivalued relationship joined to a fact table: a query that doesn't constrain to a single country overcounts. When the variation is specifically in holiday and season attributes on an otherwise-shared Gregorian calendar, the [multinational calendar pattern](multinational-calendar-pattern.md) is usually the better fit — it avoids the per-query country-constraint requirement entirely by giving each geopolitically distinct version of a date its own surrogate key, rather than joining out to a country-keyed outrigger.
