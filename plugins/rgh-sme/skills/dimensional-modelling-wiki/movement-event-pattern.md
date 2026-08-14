---
type: concept
title: Movement Event Pattern and Journey Overloading
description: Recognizing events built from paired when/where details as movements, and deriving journey-level origin/destination context by looking ahead across a chain of related movement events.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 7"
---

An event whose details pair a *when* with a *where* — a departure time and place, an arrival time and place — is typically a **movement**: a flight leg, a shipment in transit, a website visitor's step from one page to another, a message passed between two people in a social network. Movement events give rise to distance, duration, and speed as derived measures, alongside whatever facts the event already carries directly (cost, emissions, and the like). Movement isn't limited to physical geography — "how long does it take to navigate from page A to page B, and how far apart are they" is the same pattern applied to a virtual location. The modeling clue that flags an event as a movement is stakeholders using **"from" and "to"** to connect a pair of *where* details to the event's main clause during [7Ws](seven-ws-framework.md) discovery.

A movement event is naturally modeled with role-playing [date dimension](date-dimension.md) (and, where time-of-day matters, clock dimension) and location dimension references for departure and arrival — see [role-playing dimension](role-playing-dimension.md).

## The default from/to isn't always the real question

A fact table's departure and arrival locations describe where each individual leg went — not necessarily where the traveler actually needed to end up. A multi-leg routing (three connecting flights on one day, all tagged with the same "conference" reason, en route to a single conference) looks at the per-leg grain like three separate trips, when stakeholders actually think of it as one journey. Recovering the journey-level view from per-leg rows requires comparing ordered pairs of movement events per traveler to spot which legs chain together (a short gap between an arrival and the next departure) versus which start a genuinely new journey (a longer gap, or a different stated reason) — a correlated, order-sensitive comparison that performs poorly as ordinary BI-tool SQL against a large fact table.

## Overloading facts with journey-level context

The practical fix is **journey overloading**: during ETL, apply a business rule for what counts as "the same journey" (e.g., "legs by the same traveler no more than four hours apart belong to the same journey"), then add extra foreign keys to the movement event's fact table recording the **journey origin** and **journey destination** — the first departure and last arrival of the whole chain — distinct from the leg's own departure/arrival keys. This makes journey-level questions ("where is this traveler actually based?", "where did they actually need to go?") a direct query against the fact table instead of a correlated multi-row comparison.

The same technique generalizes beyond geography, because a chain's first and last touchpoints often carry *why* and *how* information, not just location: a website visitor's first page-view record carries the referring URL — the *why* of the visit — and the last page viewed (a purchase confirmation, say) describes the *outcome* — effectively a *how*. Because first/last context is significant enough to want on every event in the sequence, it's attached the same way — as extra dimension foreign keys, or as entirely separate why/how dimension keys tailored to what the first/last touchpoint actually represents.

This costs real ETL complexity (a read-ahead pass to determine the full chain before the facts can be finally loaded, sometimes requiring the fact rows to be reloaded once the chain is known) and extra storage, but is judged well worth it wherever it turns an otherwise slow, hard-to-write correlated query into an ordinary constrained lookup.

## Related: the layover/gap as a derived fact

A related overloading technique computes gap durations directly during the same ETL read-ahead pass — for instance, a **layover duration** (time spent at a connecting location before the next leg) computed by looking at the next related movement event and storing the result as an ordinary additive fact, rather than leaving BI users to compute it themselves. See [event timeline](event-timeline.md) for the general technique of naming and documenting inter-milestone durations for an [evolving event](event-story-types.md), which this is a specific application of.
