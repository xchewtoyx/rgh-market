---
type: concept
title: Criteria for Selecting Safety Indicators
description: >
  Wreathall and Jones's five prioritised criteria for choosing a proactive
  safety indicator — objective, quantitative, available, worthy, compatible
  — grounded in a spectrum from formal models to expert-brainstormed factors.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 5"
---

Every candidate indicator in [a proactive monitoring
architecture](proactive-monitoring-control-model.md) is a proxy measure for
some parameter in an underlying model of safety, never the parameter itself
— it is inherently uncertain and only ever distantly linked to whatever
idealised, unmeasurable quantity it is standing in for (Wreathall, 2009).
That grounding can be formal (a fatigue-risk model relating shift-start
times, consecutive workdays, and flight-segment counts to accident risk, or
the [T2EAM model](t2eam-taskwork-and-teamwork-strategies.md) of air-traffic-
controller cognitive strategies, expert-scored during observation) or ad hoc (factors an outage-management team brainstormed from experience:
unplanned work, prolonged task duration, personnel turnover, weather, morale,
perfunctory status reporting). Investigating failure factors during this
grounding work routinely surfaces factors critical to *success* as a side
effect — the same information that predicts failure usually also predicts
what keeps things going right.

Wreathall and Jones (2000) give five selection criteria, in decreasing order
of priority:

1. **Objective** — drawn from observable data that cannot be manipulated by
   the people being measured.
2. **Quantitative** — measurable, and sensitive enough to register a change
   in performance over time.
3. **Available** — harvestable from data streams that already exist, rather
   than requiring a dedicated new collection programme.
4. **Simple to understand, and representing a worthy goal** — because an
   indicator inevitably *becomes* the operational goal people optimise
   toward (the mechanism [goal displacement in safety
   metrics](goal-displacement-in-safety-metrics.md) names generally), the
   indicator has to be a genuinely worthy target in its own right, not just
   a convenient one — an easy-to-game or trivial proxy will get optimised
   exactly as faithfully as a good one, with correspondingly worse results.
5. **Compatible / integrated** — fits cleanly into management programmes
   the organisation already runs, rather than sitting outside them as a
   parallel system nobody maintains.

The priority ordering matters on its own: it puts manipulation-resistance
and measurability ahead of ease of integration, so a criterion trades off
against the others in a fixed order rather than being weighed case by case.
Candidate indicators span a genuine spectrum from hard, objective metrics
(duty start times, work hours, turnover rate) to soft, subjective
assessments (staff morale, the perceived quality of a status report) — the
criteria above are meant to discipline selection across that whole range,
not just at the "hard data" end of it.
