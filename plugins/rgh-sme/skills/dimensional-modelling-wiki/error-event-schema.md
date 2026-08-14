---
type: concept
title: Error Event Schema
description: A dedicated back-room dimensional schema recording data-quality screen failures as data flows from source systems into the presentation area.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

Managing data quality requires a comprehensive system of quality screens and filters that test data as it flows from source systems into the DW/BI presentation area. When a screen detects a problem, the event is recorded in a special dimensional schema available only in the ETL back room, never exposed to business users directly: an **error event fact table**, at the grain of an individual error event, plus an associated **error event detail fact table**, at the grain of each column in each table participating in that error event.

This is a dimensional schema applied to the ETL process itself rather than to a business process — it records what happened during data quality screening, and can feed an [audit dimension](audit-dimension.md) attached to the business-process fact rows it affected.
