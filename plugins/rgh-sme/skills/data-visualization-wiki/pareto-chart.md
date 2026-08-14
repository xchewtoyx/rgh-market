---
type: concept
title: Pareto Chart
description: >
  Bars show individual values ranked largest to smallest; an overlaid line
  shows the running cumulative total, revealing how concentrated the
  contribution is across ranked categories.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
---

Named for Vilfredo Pareto (of the 80:20 rule — his original 19th-century
observation was that 20% of the population owned 80% of the wealth). A
Pareto chart is a deliberate, named exception to "never use a line on a
nominal/ordinal scale" (see
[categorical scale types and bar vs. line choice](categorical-scale-types-and-bar-vs-line-choice.md)):
bars show individual values (e.g., revenue per sales rep), ranked largest to
smallest (see [order categorical values by magnitude](order-categorical-values-by-magnitude.md)),
and a line shows the running **cumulative total** across the ranked
categories.

The line is legitimate here specifically because each cumulative point is
mathematically derived from the previous one — genuinely connected, unlike an
arbitrary line drawn across unrelated nominal categories. The line's slope
directly shows each item's relative contribution, and its overall shape
reveals how evenly or unevenly the total is distributed across the ranked
items — e.g., a shape showing the top 3 of 10 reps produced 75% of quarterly
revenue.
