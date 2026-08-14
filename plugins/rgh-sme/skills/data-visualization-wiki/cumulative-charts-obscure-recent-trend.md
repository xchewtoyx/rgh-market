---
type: concept
title: Cumulative Charts Obscure Recent Trend Reversals
description: >
  A running-total chart can only ever go up (or stay flat), so it structurally
  cannot show that the underlying period-over-period rate is slowing or
  reversing — plot the per-period values when trend direction matters.
sources:
  - title: Calling Bullshit
    resource: "Calling Bullshit: The Art of Skepticism in a Data-Driven World (Carl T. Bergstrom, Jevin D. West), ch. 11"
---

A cumulative chart (running total over time) is monotonically non-decreasing
by construction whenever the underlying quantity is a count of things that
only accumulate — it looks like steady growth even in a period when new
additions have started shrinking. A real example: a company's cumulative
unit-sales chart, which by definition only ever goes up, was replotted as
quarterly sales and revealed two consecutive quarters of *declining* sales
immediately before the cumulative chart was presented — a decline the
cumulative framing could not show at all, not because anyone hid data, but
because the chart type itself cannot express a slowdown.

This is a [choosing the right measure](choosing-the-right-measure.md)
question: if the audience needs to know whether momentum is building or
fading, a cumulative total is the wrong measure regardless of how honestly
it's drawn — show the per-period ([bar](categorical-scale-types-and-bar-vs-line-choice.md))
values, or a [line chart](line-chart-for-trend-shape.md) of the period-over-
period rate, alongside or instead of the running total. Cumulative charts
still have a legitimate place when the audience genuinely only cares about
total-to-date (e.g., progress toward a fixed target) rather than current
momentum — the failure mode is using one when the question actually being
asked is about trend direction.
