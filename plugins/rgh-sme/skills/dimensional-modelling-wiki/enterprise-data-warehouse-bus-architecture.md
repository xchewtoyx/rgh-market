---
type: concept
title: Enterprise Data Warehouse Bus Architecture
description: An incremental approach to enterprise DW/BI design where independently built dimensional models for each business process share a standardized set of conformed dimensions.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1, 4"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 4"
---

The term "bus" is drawn from the electrical power / computer bus concept: a common structure that everything connects to and derives power from, letting components built by different vendors at different times coexist. Applied to DW/BI, a standard bus interface lets separate dimensional models — one per [business process](business-process.md), each corresponding to a row in the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md) — be implemented by different teams at different times and still "plug together," as long as each adheres to the standard: a shared, comprehensive set of [conformed dimensions](conformed-dimensions.md) and conformed facts.

The bus architecture decomposes enterprise DW/BI planning into manageable, independently and asynchronously implementable pieces focused on individual business processes, while still delivering enterprise-wide integration through the shared dimensions. It is technology- and platform-independent: any relational [star-schema](star-schema.md) or [olap-cube](olap-cube.md) can participate, provided it is built around the conformed dimensions and facts. Starting DW/BI implementation with a single business-process row minimizes risk, since most implementation risk comes from ETL scope; consolidated, cross-process models (e.g., profitability, combining revenue and cost from different processes) are valuable but harder to implement and should follow individual process rows rather than come first.

## Contrast with a normalized enterprise data warehouse

The bus architecture is one of two competing approaches to enterprise-wide integration in DW/BI, contrasted directly with the hub-and-spoke normalized-warehouse approach — see [Kimball versus Inmon architecture](kimball-vs-inmon-architecture.md). Normalization does not by itself deliver integration: separate, incompatible data sources can be normalized without addressing integration at all. The bus architecture instead resolves data inconsistencies directly through conformed dimensions, without requiring a normalized layer.

## Relationship to agile delivery

Conformed dimensions are frequently framed as being in tension with agile delivery, but the bus architecture is argued to enable rather than obstruct it: because a dimension is built and maintained once and reused across every process that plugs into the bus, new ETL work increasingly focuses on facts alone, since dimension tables are "already sitting on the shelf ready to go." Full enterprise-wide attribute agreement isn't required up front — identifying a minimal subset of enterprise-significant attributes and expanding iteratively, sprint by sprint, is an acceptable starting point. Skipping the bus matrix under delivery pressure tends to produce inconsistent departmental silos where data sets look comparable but rest on different business rules, undermining the very decision-making agile development is meant to speed up.

### The silo data mart anti-pattern as technical debt

An agile team tempted to scope each release strictly to one process or department, without ever checking it against a bus matrix, risks building a **silo data mart**: it delivers real value quickly, but its descriptions and measures are incompatible with (or entirely missing from) the marts other teams build next, so cross-process comparison becomes impossible later without reworking what's already shipped. This is a form of **technical debt** — ordinarily an acceptable, even deliberate, agile trade-off (ship something "just barely good enough" now, refactor later when the cost is better understood) — but the interest on *this* debt is unusually severe: refactoring means reprocessing terabytes of historical data that was captured in an incompatible shape, not just rewriting some application code.

This is not, however, an argument for reverting to big design up front (BDUF): a fully specified enterprise model designed before any delivery starts doesn't match how BI requirements actually evolve, and a DW/BI project that doesn't start agile rarely becomes agile later. The bus architecture's answer is a middle path — **just enough design up front (JEDUF)** for future cross-process integration, layered on top of **just in time (JIT)** detailed design for whatever business process the current sprint is actually building: model each event for the current sprint in full JIT detail, but model *ahead*, at a shallower level, far enough to recognize which of that event's dimensions are enterprise-significant and therefore worth conforming now rather than discovering the mismatch only after several silo marts already exist.
