---
type: concept
title: Fact State Table
description: A small table recording each fact table's load recency and completeness, so queries can compute correct as-of-date logic without relying on the system clock.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 7"
---

Comparisons that depend on "as of when" — year-to-date figures, "last N complete weeks," report footers stating how current the data is — need to know exactly how current and how complete a fact table's data actually is. `SYSDATE` (or "yesterday," under the assumption of a uniform nightly load) is not a reliable stand-in for this in any warehouse with more than one refresh cadence: some fact tables load nightly, others weekly, monthly, or on demand from external feeds, and even a nightly-loaded table can be incomplete for a given date because of ETL errors or [late-arriving facts](late-arriving-facts.md) whose full set for that date isn't available for days or weeks (roaming call charges, medical insurance claims filed long after treatment, are typical examples). Comparing this year's year-to-date figure against last year's is silently wrong whenever last year's period is fully complete but this year's is still in progress relative to it.

The fix is to store recency and completeness as **data in the warehouse**, not as an assumption living "in the heads of ETL support staff or BI users." A fact state table holds one row per fact table, with (at minimum) two attributes: the **most recent load date** (updated automatically by the fact table's own loading ETL every time it runs) and the **last complete load date** (the latest date for which the fact table is known to hold its full, final data set — this often can't be inferred automatically and needs manual confirmation for sources with unpredictable late-arriving data).

## Using it directly is awkward

Joining the fact state table into a fact table query — filtered to the one row for the fact table being queried — lets its attributes replace `SYSDATE`-based date arithmetic. But because fact state isn't "properly" joined to any other table in the query (there's no natural foreign key relationship pulling it in), many BI tools flag this as a possible Cartesian product, and even where a tool doesn't complain, the pattern is fragile and confusing: dropping or mistyping the fact-table-name filter silently breaks every downstream calculation with no obvious error. See [fact-specific calendar](fact-specific-calendar.md) for the pattern that avoids this by merging fact state directly into a role-playing date dimension instead.

## Other uses

- **Report footers**: fact state supports descriptive, self-explanatory footers beyond a bare timestamp — "Report run on 23rd March. Data reflects loads up to 17th March. The last complete week's data is for week 10; data up to week 12 is included but incomplete" — derived from `SYSDATE` plus the table's most-recent and last-complete attributes.
- **Data quality signals**: fact state can be expanded with audit-style attributes (whether the latest load has been signed off, say) surfaced through the same footer mechanism.
- **Conformed date ranges across fact tables**: comparing two fact tables that load on different schedules (sales complete through end of May, commissions only through end of April) needs a shared, defensible cutoff — derive it as the *earliest* last-complete date among every fact table involved in the comparison, so neither side is compared against data it doesn't actually have yet.
