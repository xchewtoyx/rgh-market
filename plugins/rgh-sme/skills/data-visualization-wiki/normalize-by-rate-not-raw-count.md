---
type: concept
title: Normalize by Rate, Not Raw Count, Across Unequal Groups
description: >
  Comparing raw counts across groups with different underlying exposure or
  population size can reverse the real pattern; divide by the right
  denominator before charting a comparison.
sources:
  - title: Calling Bullshit
    resource: "Calling Bullshit: The Art of Skepticism in a Data-Driven World (Carl T. Bergstrom, Jevin D. West), ch. 7"
---

A bar chart of raw counts across categories silently assumes the categories
are equally comparable — but if they differ in size, exposure, or
opportunity to generate the count, the raw comparison can show the opposite
of the real effect. A real example: charting total car-accident-fatality
counts by driver age group made 16-19-year-olds look safer than 20-24-year-
olds, and made senior drivers look no more dangerous than middle-aged ones —
because it ignored that different age groups log very different total miles
driven. Replotting the same data as fatalities *per mile driven* recovered
the expected pattern: the youngest and oldest drivers are the most dangerous
per mile traveled.

Before charting any count comparison across categories, ask what the right
denominator is — miles driven, population size, number of opportunities,
person-years of observation — and check whether it varies enough across the
categories to change the picture. This is a special case of
[choosing the right measure](choosing-the-right-measure.md): the "right"
measure for a fair categorical comparison is very often a rate, not a raw
count.
