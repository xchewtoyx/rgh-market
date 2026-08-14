---
type: concept
title: Kimball DW/BI Architecture
description: The four-component architecture — operational sources, ETL, dimensional presentation area, BI applications — underlying the bus architecture.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1"
---

The Kimball DW/BI architecture has four components:

1. **Operational source systems** — systems of record capturing business transactions, outside the data warehouse team's control over content or format. They prioritize processing performance and availability, run narrow single-record queries as part of normal transaction flow, and maintain little history — a good warehouse relieves them of representing the past. They're often special-purpose applications with no built-in commitment to sharing common reference data (product, customer, geography, calendar).
2. **ETL system** — everything between the operational sources and the presentation area: extraction, cleansing, combining sources, de-duplication, and finally structuring and loading into the dimensional presentation area. Dimension processing (surrogate key assignment, code lookups, splitting/combining columns, flattening normalized source structures into denormalized dimensions) is often the bulk of the effort; fact tables are large and slow to load but comparatively straightforward to prepare. It is acceptable to stage data in a normalized structure to support ETL processing, but that structure must be off-limits to user queries — normalized staging is a means to an end, never the end goal, since it would defeat the twin goals of understandability and performance.
3. **Presentation area** — where data is organized for direct querying by users, report writers, and BI applications; "it is all the business sees and touches." It must be structured dimensionally ([star-schema](star-schema.md)s or [olap-cube](olap-cube.md)s), must contain detailed atomic data (aggregates may supplement but never replace it — see [grain](grain.md)), must be organized around [business process](business-process.md) measurement events rather than the "report of the day," and must use [conformed dimensions](conformed-dimensions.md) via the [enterprise data warehouse bus architecture](enterprise-data-warehouse-bus-architecture.md) — without which a dimensional model becomes an isolated "stovepipe."
4. **BI applications** — the range of tools that leverage the presentation area for decision making, from ad hoc query tools (usable effectively by only a small fraction of users) to prebuilt parameter-driven applications and templates (used by most business users) to sophisticated modeling and forecasting tools that may write results back into source systems, ETL, or the presentation area.

## Restaurant metaphor

The architecture maps onto a restaurant: **ETL is the back-room kitchen** — designed in advance for efficiency, consistency (sauces made once rather than varying at the table), and integrity (salad prep kept off surfaces used for raw chicken), and off-limits to patrons. **The presentation/BI layer is the front dining room** — scored on food, decor, service, and cost, mapped respectively to data quality, presentation-area organization (for patron comfort, not developer convenience), delivery service, and cost. A well-designed DW/BI environment trades off work in the front room in favor of work in the back room: front-room work is repeated over and over by business users, while back-room work is done once by the ETL staff. As in a restaurant, managers should proactively monitor patron (user) satisfaction rather than waiting for complaints, since unhappy patrons typically just leave silently.

This architecture is contrasted directly with the alternative normalized-hub architecture — see [Kimball versus Inmon architecture](kimball-vs-inmon-architecture.md).
