---
type: concept
title: Offset Calendar
description: A companion calendar dimension counting periods relative to each record's own origin date, used alongside the standard date dimension for business events better understood on their own timeline.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 7"
---

Some business events are more naturally understood relative to their own origin date than to the standard calendar — an insurance policy's claims are more meaningful counted in "months since the policy renewed" than in standard calendar months. An **offset calendar** (e.g. a POLICY MONTH dimension counting 1, 2, 3, … from each policy's own renewal date) supplies this alongside the standard [date dimension](date-dimension.md), rather than replacing it — a fact table can carry foreign keys to both the standard calendar and an offset calendar at once, letting the same data be analyzed either by ordinary calendar month or by each record's own relative timeline. This roughly doubles the row count of a periodic snapshot built at both granularities simultaneously (one row per period per standard-calendar-period per offset-period), which is the trade-off for supporting both views without forcing users to recompute one from the other at query time.
