---
type: concept
title: "Gestalt Principle: Continuity"
description: >
  Objects that are aligned with each other, or that appear to continue one
  another, are perceived as a single whole — alignment alone can group table
  columns without needing grid lines.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 3"
---

One of six Gestalt grouping principles. Continuity: objects aligned with one
another, or that visually appear to continue one another, are perceived as
one connected whole (a dashed line is seen as one wavy line, not a series of
disconnected segments). The eye seeks the smoothest path and will invent
continuity where it is not drawn.

The practical dashboard application: text alignment and indentation in a
table can distinguish grouped categories — e.g., division vs. department vs.
headcount columns — without needing vertical grid lines to separate them.
Alignment alone does the grouping work that a grid line would otherwise be
needed for, which is another way to
[eliminate a non-data pixel](data-ink-ratio.md) without losing any
information. On a bar chart, the vertical y-axis line can often be removed
entirely: consistent white space between labels and bars still reads as
alignment along the smoothest path, and stripping the axis chrome lets the
data dominate.
