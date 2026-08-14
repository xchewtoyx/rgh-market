---
type: concept
title: Clock Dimension
description: A dimension table modeling time-of-day at minute grain, kept separate from the date dimension to avoid a row-count explosion.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 7"
---

When users need to roll up or filter by day-part groupings (15-minute intervals, hours, shifts, lunch hour, prime time), model time-of-day as its own full dimension table, separate from the [date dimension](date-dimension.md) — typically one row per minute (1,440 rows, plus a reserved special row for "time unknown"), avoiding second-level granularity unless there's a genuinely useful rollup finer than a minute. Sub-minute precision is generally better stored as a fact for computing exact durations, keeping the clock dimension itself small and description-focused. When a fact table [role-plays](role-playing-dimension.md) both a date and a clock dimension for two related milestones (order date/time and delivery date/time, say), the elapsed duration between them is difficult to compute and aggregate through the dimensions themselves — store it directly as a fact instead.

A clock dimension's own attributes split by mutability the same way any dimension's do: minute and hour are fixed values that never change, but embellishments like "peak/off-peak" or a named work shift are [historic value](slowly-changing-dimension-type-2.md) attributes, since their definitions can be redefined over time while historical facts still need the definition that was in effect when they occurred.

## The Day Clock pattern: avoiding a full date-by-time cross product

A clock attribute like "peak/off-peak" or work-shift name often depends not just on the time of day but on what *kind* of day it is — 11:59 a.m. might be "Peak" on a weekday and "Off-Peak" on a weekend or holiday. The naive fix — combining date and clock into one row-per-minute-per-day dimension — is exactly the row-count explosion the date/clock split was designed to avoid (365 × 1,440 rows per year, worse at finer date ranges), so it should not be done. The workable middle ground is a **day clock**: one row per minute per *day type* (weekday, weekend, holiday — or, at coarser grain, just weekday/weekend), rather than per specific date. At 3 day types this is only 3× the size of an ordinary clock dimension (4,320 rows for minute grain), and it still lets the peak/off-peak or shift-name attribute vary correctly by day type without exploding to one row per literal calendar date. ETL loading a fact under this pattern must resolve, per event, the day type (looked up from the date dimension), any relevant location type if peak/off-peak also varies by location, and the currently-in-effect version of that day-type-minute combination.
