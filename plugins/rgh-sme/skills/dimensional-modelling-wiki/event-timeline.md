---
type: concept
title: Event Timeline
description: A discovery diagram plotting an evolving event's milestone dates in chronological order, used to elicit and name the business-meaningful durations between them.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

An [evolving event](event-story-types.md) accumulates multiple milestone dates as it's modeled (order date, ship date, delivery date, and so on), and the business almost always cares about more than the dates themselves — the *intervals* between them are often the real process-performance measures stakeholders want (delivery time, time-to-review, days overdue). An event timeline is a discovery diagram that surfaces which intervals matter: plot the evolving event's milestone dates on a single horizontal line in chronological order, then walk each pairing of milestones with stakeholders to elicit a business name for the interval between them. A duration that already has a familiar business name in daily use is a strong signal it's worth modeling as a fact; the exercise also surfaces new or less obvious intervals stakeholders hadn't already named but recognize as meaningful once asked directly.

## Not every interval needs a name

The number of *possible* durations between n milestone dates is n(n−1)/2, which grows fast enough (15 possible durations from just 6 milestones) that naming all of them is rarely useful or even wanted. The intervals stakeholders actually care about are usually measured from one of a small number of fixed reference points — the process's own initiating date (order date) or a target date (a due date) — rather than from every possible pair of milestones; start the elicitation from those fixed points, then use the timeline's remaining white space to prompt for any other chronologically-placed milestones and durations worth naming.

## Documenting durations as derived facts

Once named, a duration is added to the underlying event table (still a business-requirements model at this stage, not a physical design) as a **derived fact**: a formula over two milestone dates, given a business name, a unit of measure, and an expected value range, without yet deciding how — or whether — it's physically stored (it may end up as a stored column, a database view, or a BI-tool metadata calculation; that's a later physical decision). Numbering the milestones in their chronological order (first, second, third, …) as part of this documentation makes duration formulas unambiguous to write (duration = later-numbered milestone minus earlier-numbered milestone) and doubles as a record of the process's expected sequence. Keep every duration within one event expressed in the same unit — mixing days and hours across an event's durations invites comparison and calculation errors later.

## As lasting documentation, not just a discovery tool

An event timeline is worth keeping as permanent design documentation alongside the event and dimension tables it was drawn from — it plays the same role for evolving events that a [hierarchy chart](hierarchy-chart.md) plays for dimensions: a compact, visual record of *why* a duration means what it means, readable by an audience wider than the ETL and BI developers who eventually implement it. Spacing milestones on the timeline proportionally to their actual typical duration (rather than evenly) can visually highlight which stage of a process is the slowest or most closely monitored, the same relative-spacing trick used on a hierarchy chart to cue cardinality. A timeline built this way also translates well into a live operational dashboard once the underlying [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) is built — a stacked horizontal bar showing current status counts and average inter-milestone durations at each stage.

A related, ETL-computed derived fact appears in the [movement event pattern](movement-event-pattern.md): a layover or gap duration between one movement and the next, discovered by looking ahead across a chain of related events rather than within a single evolving event's own milestones.
