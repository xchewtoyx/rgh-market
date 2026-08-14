---
type: concept
title: Single-Screen Constraint
description: >
  A dashboard must fit entirely within one eye span, with nothing requiring
  scrolling or navigation to a different screen to be seen alongside the rest.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 1, ch. 3 §3.1"
---

A defining property of a [dashboard](dashboard-definition.md), not an
implementation detail: all information needed for its objective must be
visible together, within the viewer's eye span, so it can be seen "at a
glance." If a viewer must scroll to see it all, the display has transgressed
the boundaries of a dashboard. If a viewer must navigate between screens to
see it all, that is multiple dashboards, not one.

This is not an arbitrary aesthetic rule — it follows from how short-term
memory works. See [short-term memory chunk limit](short-term-memory-chunk-limit.md):
once data scrolls out of view it is gone unless it happened to be one of the
few chunks retained, and paging back to re-see it costs whatever was just on
screen. Seeing values simultaneously is what enables the instant comparisons
that produce insight; that capability is lost the moment content is split
across screens or scroll positions.

Two concrete ways this constraint gets violated in practice:

- **Fragmenting data that should be seen together** into separate navigable
  screens or separate interactive views (e.g., tabs, or per-item detail panels
  reached one at a time). Splitting is fine when the separated content
  genuinely doesn't need to be compared to the rest — but splitting data that
  *does* need side-by-side comparison (e.g., per-product dashboards that
  prevent comparing products, or interactive radio-button/slider controls that
  show only one region or one time period at a time) defeats the dashboard's
  purpose by making cross-comparison impossible.
- **Requiring scrolling** to reach lower-priority content. Viewers assume
  anything below the fold or behind a scrollbar is less important and often
  will not bother scrolling to find it — a paginated printed report is, in
  this respect, actually better than a scrolling screen, since a reader can at
  least lay out multiple printed pages side by side.

This constraint is why refresh cadence should match the objective rather than
default to real time (see [dashboard definition](dashboard-definition.md)),
and it is the reason dashboard content must be aggressively summarized — see
[summarization and exception reporting](summarization-and-exception-reporting.md)
and [multi-foci time display](multi-foci-time-display.md) for the main
techniques for fitting more history/detail inside this constraint without
violating it.
