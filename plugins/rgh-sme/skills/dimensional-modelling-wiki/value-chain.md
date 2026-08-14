---
type: concept
title: Value Chain
description: The natural sequence of an organization's primary business processes, where each process's output typically feeds the next process's input.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 4"
---

A value chain identifies the natural flow of an organization's primary [business process](business-process.md)es — for example, a retailer's purchasing → warehousing → retail sales, or a general ledger's budgeting → commitments → payments. Because each process along the chain produces unique metrics at unique time intervals, granularity, and dimensionality, each process typically spawns at least one atomic [fact-table](fact-table.md), even though the processes share many of the same [dimension-table](dimension-table.md)s (date, product, store). Deciding exactly where one process ends and the next begins — and therefore whether a group of related transactions gets one fact table or several — is a recurring design quandary; see [single vs. multiple fact tables](single-vs-multiple-fact-tables.md).

The value chain gives high-level insight into overall DW/BI data architecture: it is the map from which the rows of the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md) are drawn, and it is the reason shared, conformed dimensions across processes matter — without them, the separate fact tables spawned along the chain cannot be integrated via [drilling across](drilling-across.md).

## Value sequence versus process sequence

Listing an organization's processes in **value sequence** — from the lowest-value output process through to the highest — usually approximates their rough chronological order (low-value activity generally precedes the high-value activity it feeds into), even though many processes really happen simultaneously or asynchronously rather than in one strict global order. This looser value sequence is a useful way to discover the chain in the first place, by repeatedly asking "who does what next that adds value?"

Within that looser value sequence, some processes form a stricter **process sequence**: a chain of events that must occur in a fixed serial order to complete one larger process — a purchase order, then its component deliveries, then the resulting supplier payments, where a delivery cannot occur before its order and a payment cannot occur before its delivery. A process sequence's member events necessarily share a conformed dimension that ties them together at the atomic level (often just a shared [degenerate dimension](degenerate-dimension.md) like a purchase-order number), and exactly one event in the sequence is the one that *creates* that shared identifier's values in the first place — every other event in the sequence can only ever reference values that event already created, which is what guarantees the strict ordering holds.

## Two techniques a discovered process sequence unlocks

Recognizing a process sequence during discovery motivates two further design moves:

- **Model it as an [evolving event](event-story-types.md)**, bringing every milestone in the sequence together into one [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) for direct, detail-level comparison across the whole process — a purchase-to-payment sequence combined this way gives stakeholders direct access to cross-milestone measures like late-delivery rates, average delivery time, and outstanding order value that no single milestone's own fact table could answer alone.
- **Enrich a later milestone's dimensionality with the initiating event's own dimensions.** Because everything knowable about the process's initiating event (an order's product, quantity, and requested date, say) is already fixed and known by the time a later milestone occurs (its delivery or payment), it's safe to carry those originating-event dimensions forward onto the later event's own fact table too — a safety that specifically depends on the sequence's strict chronology; it does not generalize to events that aren't provably ordered this way.
