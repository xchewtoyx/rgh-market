---
type: concept
title: Dashboard as Launch Pad
description: >
  A single-screen dashboard usually cannot hold everything needed to act on a
  finding, so design it for interaction — drill-down and slicing initiated by
  clicking the data itself.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 7 §7.4"
---

Because a [dashboard](dashboard-definition.md) is deliberately condensed
(see [summarization and exception reporting](summarization-and-exception-reporting.md)),
it usually cannot carry everything needed to fully act on what it shows. It
should almost always be designed for interaction, most commonly:

- **Drilling down** into underlying detail.
- **Slicing** the data to narrow focus.

Two governing principles:

- **Let the viewer initiate by clicking the data itself**, not a separate
  control — this is both more intuitive and space-saving, since no extra
  buttons are needed. Examples: clicking a region's revenue bar to see that
  region's states broken out; hovering over a line-graph point to pop up its
  exact value as text.
- **Use consistent launch actions everywhere they appear** — see
  [visual consistency principle](visual-consistency-principle.md) — so a
  viewer doesn't have to relearn how to drill down in each panel.

This is the concrete mechanism behind an
[analytical dashboard](dashboard-role-taxonomy.md)'s need for interactivity:
the dashboard itself doesn't need to support the full downstream analysis,
only to link seamlessly to where that analysis happens. Interactive,
drillable displays like [treemaps](treemap.md) rely on this pattern directly.
