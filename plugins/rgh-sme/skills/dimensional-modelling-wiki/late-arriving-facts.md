---
type: concept
title: Late Arriving Facts
description: Fact rows whose dimensional context at load time doesn't match the context that was actually in effect when the measurement event occurred.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

A fact row is late arriving if the dimensional context available at load time doesn't match the incoming (delayed) measurement event — the current [dimension-table](dimension-table.md) rows reflect a later state of the world than the one in effect when the event actually happened. Loading it correctly requires searching the relevant [slowly changing dimension](slowly-changing-dimension.md) type 2 history to find the dimension surrogate keys that were actually effective at the event's true timestamp, rather than simply using whichever keys are current now.

## Book date: a second time dimension for when the fact was recorded, not when it happened

A [transaction fact table](transaction-fact-table.md) that regularly receives late-arriving corrections or adjustments — common in finance, where an entry must be booked into a specific accounting period regardless of when the underlying event actually occurred — benefits from a second, explicit **book date** (or "applicable period") [role-playing](role-playing-dimension.md) date dimension alongside the transaction's true event date. The event date answers "when did this really happen"; the book date answers "which period does this count against for reporting," and the two only diverge for late-arriving or adjustment rows. Keeping both as separate foreign keys, rather than trying to force a single date to serve both purposes, avoids having to silently reassign an event's true date just to make it land in the right reporting period.

This is the fact-table-arrival counterpart to [late arriving dimensions](late-arriving-dimensions.md), where instead a dimension row's context shows up after fact rows that should reference it have already been loaded.
