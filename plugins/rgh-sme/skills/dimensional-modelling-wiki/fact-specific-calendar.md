---
type: concept
title: Fact-Specific Calendar
description: A per-fact-table view merging a fact state table's single recency row with every row of the standard date dimension, letting YTD-style logic use ordinary join columns instead of an unjoined filter table.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 7"
---

Joining a [fact state table](fact-state-table.md) directly into a query is awkward — it isn't naturally related to anything else in the query, so BI tools often flag it as an unjoined table risking a Cartesian product, and dropping its filter silently breaks the query with no obvious symptom. A fact-specific calendar avoids this by folding fact state into an ordinary [date dimension](date-dimension.md) join instead of leaving it as a separate, loosely-attached filter table.

Build it as a view (ideally materialized, so it auto-refreshes whenever the fact state table changes) that cross-joins the single fact-state row for one specific fact table against every row of the standard [date dimension](date-dimension.md). Because the fact state side contributes only one row, the result is exactly one row per calendar date — the same shape as the base date dimension — except every row now also carries that fact table's most-recent-load and last-complete-load attributes. Since a fact-specific calendar is always present in any meaningful query against its fact table (it's the table's own primary date dimension), its recency attributes can be compared with `WHERE` clauses exactly like `SYSDATE`, with no separate unjoined filter and no risk of a query silently running unconstrained if a filter is forgotten:

```sql
SELECT Year, SUM(Revenue) AS Revenue_YTD
WHERE (Year = 2010 OR Year = 2011)
  AND Day_In_Year <= Most_Recent_Load_Day_In_Year
GROUP BY Year
```

## Naming and role-playing

- A fact table with a single date dimension can give its fact-specific calendar a unique, role-specific name (e.g. `SALE_DATE`).
- A fact table with multiple date foreign keys must give every [role-playing](role-playing-dimension.md) instance of the calendar the *same* fact-specific name, distinguished only by which foreign key it's joined through — consistent with how any other role-playing dimension is exposed.
- If a BI toolset qualifies tables per-schema rather than globally, every fact table can instead share one generically-named fact-specific calendar name, as long as each is physically defined within its own fact table's schema.

To keep the view-building SQL mechanical, mirror the same attribute names between the date dimension and the fact state table — a `Quarter_In_Fiscal_Year` column on the calendar implies matching `Most_Recent_Load_Quarter_In_Fiscal_Year` and `Last_Complete_Load_Quarter_In_Fiscal_Year` columns on fact state, so any calendar attribute has an obvious, discoverable fact-state counterpart. The calendar can be further expanded with derived Y/N flags (`Most_Recent_Day`, `Prior_Month`, and similar) and a signed lag column numbering every date relative to the fact table's most recent load (0 = most recent, −1 = the day before, +1 = the day after) for BI tools that work better against a simple offset than a raw date comparison.
