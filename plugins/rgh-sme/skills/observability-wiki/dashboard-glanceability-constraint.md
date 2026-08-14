---
type: concept
title: Dashboard Glanceability Constraint
description: A dashboard is, by definition, a display of the most important information for one or more objectives, consolidated onto a single screen so it can be monitored at a glance — scrolling or navigating between screens to see related data defeats the purpose, because the visual comparisons that reveal problems require seeing everything simultaneously, within eye span.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 1, 3"
---

A dashboard's core job is to signal "this deserves attention" in no more than a glance, and that constrains its design more than any stylistic choice does: everything the viewer needs to compare must fit on one screen, within eye span, at the same time. Splitting related data across multiple screens or tabs, or requiring scroll to see the rest of a metric set, breaks the perceptual mechanism that makes a dashboard useful — simultaneity of vision is what lets a viewer notice that two things relate, or that one number is anomalous relative to another, without having to hold either value in short-term memory while navigating away to check it. A metrics page that requires scrolling or tab-switching to see the full picture is not one dashboard; it is several, and should be designed (and evaluated) as such.

This directly motivates the anti-pattern of the "wall of graphs" — piling on more panels doesn't make a dashboard more useful once it exceeds what a viewer can actually take in in one glance; it just fragments the picture the same way scrolling does, while additionally overwhelming the "most important information" requirement (a dashboard is a display of the *most important* information for an objective, not everything that could conceivably be measured). A dashboard curated to fit in a glance is, by construction, the wrong tool once the question moves from "is something wrong" to genuine open-ended exploration — that shift is exactly where [the core analysis loop](core-analysis-loop.md)'s dimension-by-dimension querying takes over from a fixed panel layout. See also [dashboard role determines its design](dashboard-role-determines-design.md) for how a dashboard's intended use (strategic, analytical, or operational) governs whether it should stay purely at-a-glance or support drill-down into that exploration.
