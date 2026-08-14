---
type: concept
title: Size Signals Relative Importance
description: >
  Relative size is read as relative importance, so equally important elements
  should be sized similarly and the truly focal element should be made
  conspicuously larger — never leave sizing to layout happenstance.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

Among [preattentive attributes](preattentive-attributes-for-dashboards.md),
size is one of the strongest attention levers: audiences treat bigger as more
important. If several elements carry roughly equal weight, size them
similarly; if one element is genuinely the lead, make it conspicuously larger
so the hierarchy is unambiguous.

Size allocations that arise from data availability or placeholder layout —
rather than from an explicit importance decision — mislead. A worked
dashboard example reserved ~60% of the screen for the only metric available
early in development; once peer metrics arrived in the remaining
placeholders, that first metric's oversized footprint still pulled undue
attention until all three were resized equally. The lesson matches other
encoding channels: do not let defaults or temporary constraints make the
importance decision for you.

On a dashboard, size works alongside
[screen position](screen-position-emphasis.md) as a static emphasis tool; in
an explanatory graphic it is one channel within
[visual hierarchy with preattentive attributes](visual-hierarchy-with-preattentive-attributes.md).
In both settings, oversizing everything cancels the signal — the same failure
mode as [over-highlighting](static-vs-dynamic-highlighting.md).
