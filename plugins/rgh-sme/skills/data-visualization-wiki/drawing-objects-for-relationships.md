---
type: concept
title: Drawing Objects for Process Flow and Entity Relationships
description: >
  Use shapes for entities and lines (with arrows for direction) for their
  relationships to show process flow or org-chart-style structure — a
  distinct display need from quantitative charts.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.5, ch. 2 §2.2.2"
---

Some dashboard content isn't quantitative at all — sequential process steps
with branching paths, or an organization chart — and calls for a different
display medium than any chart type built for numbers. The convention:
entities as rectangles or circles, relationships between them as lines or
arrows (arrows add directionality). Switching shape type (rectangle vs.
circle) can distinguish different entity types within the same diagram.

This medium leans directly on
[Gestalt connection](gestalt-connection.md) — a visible line between two
entities is a stronger grouping/relationship cue than proximity or similarity
alone — which is why a drawn connector, not just placement, is the right tool
whenever the relationship itself (not just co-membership in a group) is the
point. Quantitative information can still be layered on top: e.g., time
elapsed between process steps shown via a number or line length, or entity
size scaled to revenue or headcount.
