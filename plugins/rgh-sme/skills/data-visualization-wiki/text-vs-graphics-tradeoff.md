---
type: concept
title: Text vs. Graphics Tradeoff
description: >
  Text excels at precise lookup of individual values; graphics excel at
  revealing shape and relationships — pick text alone when only one
  unqualified value matters, and graphics once shape or comparison matters.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Verbal language is processed serially, one word/number at a time, but is
unmatched for precision. For a single, unqualified value ("YTD Expenses
$487,321"), plain text beats a graph — a graph would only slow communication
down. The same applies when there are only **one or two numbers** to share:
putting them in a bar chart can strip their "oomph" and even mislead (e.g.,
labels outside bars making 20 fail to read visually as less than half of 41).
A sentence or a simple-text callout often communicates faster and more
honestly. Caution when collapsing several figures into one summary phrase
("decreased more than 50%"): check what context the actual magnitudes still
carry before dropping them.

Text, especially tabular text, is also excellent for **looking up** a
precise value (a bus schedule, a tax table, a book index): finding the exact
September 1996 CPI value in a table is fast and unambiguous. Tables suit
mixed audiences where each reader seeks their own row, and are often easier
than graphs when multiple different units of measure must appear together.
In a **live presentation**, a dense table usually costs the speaker the
audience's ears while they read — prefer a graphic of the single point you
are making, and park the full table in an appendix. Table chrome should fade
(light or no borders) so the numbers dominate; a
[single-hue saturation heat map](single-hue-saturation-over-rainbow.md) over
the cells can further speed ranking without leaving the verbal lookup form.

But text is poor at revealing **shape** — how values change over time or
relate to each other. Graphs interact with the visual system, which typically
processes faster than the verbal system used for tables: a well-designed graph
communicates trend, comparison, or relationship faster than a well-designed
table; conversely, the graph is bad for reading off an exact September value.
Neither medium is universally better — the choice follows from what the
viewer needs to do: look something up precisely (text/table), or perceive a
trend, comparison, or relationship (graph).

As a dashboard's content becomes more layered — a bare value, then a value
with evaluative styling, then a value plus target, then value + target +
variance — pure text remains adequate only as long as the goal is examining
one measure at a time. Once the goal shifts to comparing several measures or
seeing how something changed, graphics take over. See
[choosing the right measure](choosing-the-right-measure.md) for getting the
underlying number right first, and the individual chart-type notes (starting
with [categorical scale types and bar vs. line choice](categorical-scale-types-and-bar-vs-line-choice.md))
for which graphic fits which analytical need.
