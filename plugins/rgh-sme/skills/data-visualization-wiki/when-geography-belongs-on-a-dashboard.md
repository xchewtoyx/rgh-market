---
type: concept
title: When Geography Belongs on a Dashboard
description: >
  Plot data on a map only when its meaning genuinely depends on spatial or
  geographic relationships that a table or ranked bar graph could not reveal.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.5, ch. 6 §6.2.6"
---

A common mistake: encoding purely categorical data (e.g., four sales regions,
each colored by performance) on a literal map, when the regions have no
meaningful geographic relationship to each other. This adds no insight over a
simple table or [ranked bar graph](order-categorical-values-by-magnitude.md)
and wastes space that could show the data more directly.

Maps earn their place only when spatial adjacency itself carries information
that would otherwise be invisible — Few's example: interstate wine-shipment
tax boundaries, where the geography *is* the regulation. A building floor
plan used to monitor, say, temperature by room is a similar legitimate case:
adjacent rooms' readings relative to each other may reveal a pattern (a
localized HVAC fault) that a flat list of room names would not surface.

Default to a table or bar graph; reach for a spatial map only when you can
name the specific spatial relationship the audience needs to see.
