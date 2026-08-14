---
type: concept
title: Year-to-Date Facts
description: A caution against storing year-to-date totals as fact table columns, since YTD variants proliferate and are better computed at query time.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

Requests for year-to-date (YTD) metrics easily morph into variants — "YTD at close of fiscal period," "fiscal period to date," and similar — that a single stored YTD column cannot anticipate. It is more reliable and extensible to calculate YTD metrics in the BI application or [olap-cube](olap-cube.md) at query time, from the underlying [additive fact](additive-fact.md)s, rather than storing YTD facts directly in the [fact-table](fact-table.md).

A stored YTD (or quarter-to-date) total is also, fundamentally, not true to the fact table's [grain](grain.md): it represents a cumulative measurement over a growing span of periods layered onto a row that otherwise represents a single period, so an ordinary `SUM` across several such rows overstates the result — the same silent-overcounting failure mode as any other fact that doesn't match its row's grain.

If a period-to-date fact is stored despite this caution, it belongs in a [periodic snapshot fact table](periodic-snapshot-fact-table.md) rather than a [transaction fact table](transaction-fact-table.md) — like a balance, it measures a cumulative effect rather than an individual activity, so it is unrecoverable on no-activity periods and double-counted across multi-transaction periods if kept at transaction grain. It must also be stated at the same dimensional level as the snapshot's own non-period grain (an account-level snapshot needs an account-level period-to-date fact, not a branch-level one), since a coarser-grain fact repeated across every finer-grain row would break additivity across every other dimension.

## What "to date" is relative to

Even when YTD is computed correctly at query time from additive facts, a valid comparison needs the warehouse to answer three separate questions about the date range, not just "the current date": which day the year actually starts from (calendar year, fiscal year, or tax year — supplied by conformed [date dimension](date-dimension.md) attributes); what "to date" itself means (running to now, or to a specific past cutoff — and if "now," whether the fact table's data is actually complete up to today or only up to some earlier date); and which days to count on the prior-year side (the same calendar cutoff date, or the same day-count, and if day-count, calendar days or workdays only). The middle question — how current and complete a specific fact table's data actually is — cannot be answered from `SYSDATE` alone once fact tables load on different schedules or receive [late-arriving facts](late-arriving-facts.md); see [fact state table](fact-state-table.md) and [fact-specific calendar](fact-specific-calendar.md) for the pattern that tracks and exposes this directly in the warehouse.
