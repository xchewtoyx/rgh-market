---
type: concept
title: Hierarchy Chart
description: A diagramming technique for discovering and documenting a dimension's hierarchy levels, using paired cardinality questions to place each candidate level correctly.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

A hierarchy chart is a lightweight diagram for discovering and documenting a [dimension](dimension-table.md)'s hierarchy levels during requirements gathering: a vertical bar with the dimension name at the bottom and its highest-level attribute at the top, with each intervening level marked as a tick on the bar in ascending order. Tick spacing can be even, or scaled to approximate cardinality — placing levels that reveal much more detail further from their parent — to visually cue stakeholders on how deep a drill-down goes or how selective a filter is. A single chart can document one hierarchy, several hierarchies belonging to the same dimension, or, as an **event hierarchy chart**, every dimension and hierarchy associated with one business event at once.

Complex shapes get their own annotation conventions on the chart: a bracketed level name marks an optional level in a [ragged hierarchy](ragged-hierarchy.md); a double bar between a child and more than one parent marks a multi-parent hierarchy; a circular path connecting two levels marks a variable-depth (recursive) [instance hierarchy](ragged-hierarchy.md). These annotations can be combined for the most complex cases. A chart can also show one or more query definitions as lines connecting the levels a query touches, marking filter levels (the `WHERE` clause) with an X and aggregation levels (the `GROUP BY` clause) with an O — this doubles as a way to document an [OLAP cube](olap-cube.md)'s or [aggregate fact table](aggregate-fact-table.md)'s intended dimensionality directly on the chart.

## Discovering and positioning levels

Ask stakeholders directly: "How do you organize [dimension] hierarchically?" — they typically volunteer candidate levels already in rough hierarchical order. Before a candidate is placed on the chart it must first pass the [dimension attribute belonging test](dimension-attribute-belonging-test.md) (single-valued for the dimension's subject at a moment in time) and have example values collected.

Once a candidate passes that test, its exact position in the hierarchy is confirmed with paired cardinality questions against its proposed neighbors, marking the chart temporarily with "1" or "M":

- **Parent side**: "Can a [Candidate] belong to more than one [Parent]?" and "Can a [Parent] have more than one [Candidate]?" An answer of no/yes (1 next to the parent, M next to the candidate) confirms the many-to-one relationship needed to place the candidate directly below that parent.
- **Child side** (skip if the child is the dimension's own subject, already known to be many-to-one with everything above it): "Can a [Child] belong to more than one [Candidate]?" and "Can a [Candidate] have more than one [Child]?" An answer of yes/no (M next to the child, 1 next to the candidate) confirms the correct one-to-many relationship with the level below.

Other outcomes redirect the placement rather than confirm it:

- **Two "1" answers** (one-to-one) — the candidate is at the *same* level as an existing attribute, not a new level; it may still replace the existing attribute as the preferred report label (e.g., a category name replacing a category code) without being added as a separate hierarchy level.
- **Two "M" answers** (many-to-many) — the two attributes cannot coexist in the same balanced hierarchy; if both matter, model them as separate parallel hierarchies instead (e.g., week and month as two distinct time hierarchies rather than one combined hierarchy).
- **A reversed relationship** — one-to-many where many-to-one was expected (or vice versa) means the candidate is at the wrong level: move it up if it turns out one-to-many with its proposed parent, or down if it turns out many-to-one with its proposed child, then retest against its new neighbors.

## Hot levels

Once a hierarchy's levels are discovered, ask whether the business has plans, budgets, forecasts, or targets associated with the dimension, and at what level(s) those are set. Any level identified this way is marked **hot** (conventionally with an asterisk) — it's a level that matters enough for actual-vs-plan comparison to be worth its own [shrunken (rollup) dimension](shrunken-dimension.md) or aggregate, since planning data is rarely captured at the same atomic grain as the transactions being compared against it. Hot levels are especially likely wherever two different hierarchies (e.g., a product category hierarchy and an employee department hierarchy) intersect at a role that owns both — a product sales manager who owns both a category and a department, say — and hot levels being mandatory (not ragged) is particularly important for the cross-process analysis that plan-vs-actual comparisons depend on.

Before finishing a hierarchy, check that every level is mandatory across all members; a level found to have missing values during data profiling is evidence of a [ragged hierarchy](ragged-hierarchy.md) rather than a balanced one, and should be bracketed on the chart pending resolution with stakeholders.
