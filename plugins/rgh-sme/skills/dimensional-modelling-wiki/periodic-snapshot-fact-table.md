---
type: concept
title: Periodic Snapshot Fact Table
description: A fact table whose grain is a regular time period, with one row summarizing many measurement events (or a point-in-time level) per period.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 11"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

A periodic snapshot fact table row summarizes many measurement events, or a level/balance, over a standard period (day, week, month) — the grain is the period, not an individual transaction. It is one of the three fundamental [fact-table](fact-table.md) grain types, alongside [transaction fact table](transaction-fact-table.md) and [accumulating snapshot fact table](accumulating-snapshot-fact-table.md). During requirements gathering, a business event classified as a [recurring event story](event-story-types.md) is the signal that a periodic snapshot is the right grain type.

Periodic snapshots are typically uniformly **dense**: unlike a sparse transaction fact table, a row is inserted for every combination of dimensions at every period even when there was no activity, with zero or null facts — a retailer, for example, may load a row for every product in every store every day, including explicit zero out-of-stock rows. This denseness gives predictable table growth, which can still be substantial and may force compromises such as reducing snapshot frequency for older history (e.g., keeping 60 days at daily grain, then reverting to weekly for anything older, stored in a separate fact table with its own periodicity).

Periodic snapshots often carry facts that are levels or balances rather than flow amounts — these are typically [semi-additive fact](semi-additive-fact.md)s, summable across every dimension except the date dimension. A snapshot table is often the only easy source of predictable longitudinal trend views.

## Velocity metrics from an enhanced snapshot

A balance or level alone (e.g., quantity on hand) is insufficient for velocity analysis. Adding a corresponding flow fact — quantity sold, or quantity shipped for a warehouse — enables derived metrics such as **number of turns** (quantity sold ÷ quantity on hand for a single period; for a longer span, total quantity sold ÷ average daily quantity on hand) and **number of days' supply** (final quantity on hand ÷ average quantity sold over a span). In such an enhanced snapshot, the balance fact remains semi-additive while the flow facts and any extended valuation columns (inventory value at cost, or at latest selling price) are fully [additive fact](additive-fact.md)s. Some schemas instead store a beginning balance, a delta, and an ending balance per row: the two balances stay semi-additive, while the delta is fully additive across every dimension, including time.

## Sourcing a periodic snapshot

When transactions equate to small pieces of activity (e.g., revenue), the snapshot can be built mainly for performance reasons by summing the transaction data over the period, and it usually shares most dimension tables with a companion [transaction fact table](transaction-fact-table.md), though typically with fewer dimensions and more facts. When transaction detail cannot easily be rolled up into the desired metric (as with an inventory position), the periodic snapshot must instead be sourced from an operational system that already performs the complex calculation, or the ETL system must implement that logic itself.

## Organizational hierarchies within a snapshot

When a periodic snapshot already holds rows at multiple levels of an ascending organizational hierarchy (department, division, enterprise), see [parent-child snapshot rollup](parent-child-snapshot-rollup.md) for a self-referencing surrogate key technique that lets users drill down through those levels directly.

## One row per natural key, despite type 2 history

A snapshot's grain-defining dimensions are identified by their natural keys, one row expected per key per period. When one of those dimensions carries [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) attributes, a single natural key can correspond to more than one dimension surrogate key (an old version and a new one, say, after an address change mid-period) — but the snapshot must still record only **one** fact row per natural key per period, referencing whichever version was current as of that period, or the natural key's activity gets double-counted. This holds for every grain-defining dimension, including a multi-dimension grain (e.g. product by store): one row per natural-key combination per period, regardless of how many type 2 versions exist for either dimension. This rule needs to be understood across the whole team, not just by ETL developers, and belongs in the star's documented grain statement — a report developer who assumes every current type 2 version is separately represented in the snapshot will get it wrong.

## Choosing the period dimension itself

A monthly (or other periodic) snapshot's period can be represented either by a conformed **period dimension** (e.g. month) matching what's actually being summarized, or by a **date dimension** row for the period's end date (e.g. the month's last day). A period-end date is valid and sometimes eases integration with reporting tools that handle month/day conformance poorly, but it has two drawbacks: the large majority of day-dimension rows (roughly 29 of every 30, for a monthly snapshot) have no corresponding snapshot data at all, and a date row still carries day-level attributes (day of week, holiday flag) that are semantically meaningless on a period-level summary row. A dedicated period dimension avoids both problems and is the more consistent design. An auxiliary day dimension for the period's last day can still be useful purely on the ETL side, to help maintain the "leading edge" of a snapshot still in progress (recomputing the current month's row throughout the month) — it can stay hidden from end users if the period dimension is the primary design they see.

## Nightly loading of monthly snapshots

A monthly (or quarterly) periodic snapshot is often assumed to load only once, at period end, but loading it nightly instead — recomputing each affected row from that day's activity rather than waiting for the period to close — has two advantages worth the extra ETL frequency. First, it staggers the workload: an end-of-month-only load must aggregate an entire month's activity in one run, concentrating both the processing cost and the failure risk (a failed load puts the whole month at risk) onto the single heaviest night, whereas nightly loading touches only one day's activity at a time and leaves the table at most a day stale. Second, it makes **period-to-date** rows possible — an extra row per grain-defining entity holding the period's running total as of last night's load — which matters because a snapshot that only updates at period end is, on average, about half the period out of date for any question asked before it closes, and operational stakeholders often can't wait that long.

## Complementary use with accumulating snapshots

Periodic and [accumulating snapshot fact table](accumulating-snapshot-fact-table.md)s can work together: a monthly snapshot can be incrementally built by rolling each day's transactions into an accumulating snapshot, while a periodic snapshot separately retains a longer rolling history (e.g., 36 months); at month-end the accumulating snapshot becomes the new period in the time series and a fresh accumulating snapshot starts. Some redundancy between transaction and snapshot tables is an acceptable trade-off — the goal is to publish data effectively for analysis, not to eliminate all redundancy.
