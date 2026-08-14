---
type: concept
title: Real-Time Fact Table
description: A fact table updated far more frequently than a nightly batch, typically via a dedicated hot partition or deferred-update mechanism.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 20"
---

A real-time fact table needs updating far more frequently than a traditional nightly batch load, using techniques that depend on the underlying DBMS or OLAP platform. Two common patterns: a "hot partition" pinned in physical memory, deliberately built without the aggregations or indexes that the rest of the [fact-table](fact-table.md) carries, so it can accept rapid inserts; or DBMS/OLAP support for deferred updating, which lets already-running queries finish against a consistent snapshot before new updates are applied.

## Real-time partition design

The hot partition is best built as a physically and administratively separate partition of the fact table — ideally a true database partition rather than a distinct table — so it seamlessly extends the historical time series up to the current instant. It should hold only activity since the last conventional (e.g., midnight) static load, be indexed as lightly as possible (ideally not at all, since some RDBMSs force indexes not aligned with the partitioning scheme) so continuous "dribbling in" of new rows doesn't stall on index maintenance, and still answer queries responsively by being pinned in memory rather than relying on indexes for speed.

The design differs by grain: against a **transaction fact table**, the real-time partition shares the same dimensional structure as the static table and holds unindexed transactions accumulated since the last load — there's no time series to index within a single day's slice, only today's activity. Against a **periodic snapshot fact table**, the real-time partition is the current "hot rolling period" (e.g., the developing month): a continuously updated image of the period-to-date, with semi-additive balances and additive facts adjusted as often as new data is reported; at period end it is merged onto the static fact table as the newest period, and a fresh, empty real-time partition restarts the cycle. This pattern is not typically needed for an [accumulating snapshot fact table](accumulating-snapshot-fact-table.md), since that table's own destructive-update design already keeps it continuously current.

The distinguishing modeling implication is that a real-time fact table's grain and dimensionality are chosen the same way as any other fact table — see [grain](grain.md) — but its physical load pattern trades the batch-window simplicity of the other fact table types for continuous availability of the freshest data.

## The latency-versus-quality trade-off

Reducing latency is not free — it trades directly against data quality, and this trade-off needs to be actively communicated to business users who often assume "faster is strictly better." A conventional once-a-day batch load typically delivers complete transaction sets (an order, for instance, only appears once it has passed credit check and been finally committed) and gives the ETL system enough time to run a full spectrum of data quality checks. As extraction frequency increases through the day, that guarantee of completeness erodes — a transaction may appear before it has cleared every business rule, later requiring an adjustment — full quality checks may no longer fit in the available processing window, and records may need to post before all of their dimensional keys can be resolved, requiring [late arriving dimensions](late-arriving-dimensions.md) placeholder rows pending a later feed. At the extreme of near-instantaneous delivery, only raw transaction fragments may be available, with no time for any quality processing at all.

A practical hybrid balances the two: provide low-latency intraday delivery for freshness, then still run a nightly batch extract afterward to correct whatever data problems couldn't be handled during the day.
