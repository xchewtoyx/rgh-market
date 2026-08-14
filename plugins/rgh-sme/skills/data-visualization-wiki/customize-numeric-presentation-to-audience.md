---
type: concept
title: Customize Numeric Presentation to the Audience
description: >
  Match a number's precision, units, and vocabulary to what the audience
  actually needs and understands — more precision or unfamiliar statistical
  terms only slow viewers down without adding value.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.3, ch. 5 §5.1.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 5"
---

Excess numeric precision is a common, easy-to-fix mistake: $3,848,305.93 vs.
$3,848,305 vs. $3.8M convey the same decision-relevant information, but each
extra digit costs the viewer time spent filtering out what's unimportant.
"Every unnecessary piece of information results in time wasted trying to
filter out what's important." Precision should match the task: most
executives don't need figures to the cent or even below the nearest thousand,
while an accounting manager might need every penny. Context also rules out
nonsensical precision (e.g., fractional "adults per 1,000" when the story
only needs whole people) — part of
[eliminating distractions](visual-affordances-for-charts.md).

This is one instance of a broader customization requirement: use the
audience's own vocabulary and units, not the data's native ones. Don't show a
linear correlation coefficient to an audience without a statistics
background — use a familiar graph instead (see
[scatter plot for correlation](scatter-plot-for-correlation.md)). Break data
into the time granularity the audience actually thinks in (weeks, not months,
if that's how they plan). Straightforward language and spelled-out acronyms
belong here too: specialist five-syllable vocabulary can alienate and make
viewers feel dumb even when the chart is otherwise clear.

This customization requirement is also why a [dashboard](dashboard-definition.md)
must be built for a specific person, group, or function rather than as a
generic template — the same underlying data may need entirely different
precision and vocabulary for two different audiences.
