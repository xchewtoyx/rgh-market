---
type: concept
title: Visualization for Exploration vs. Communication
description: >
  Data visualization serves two distinct purposes — finding patterns in data
  and presenting findings to others — and designs that work for one often fail
  for the other.
sources:
  - title: Data Science from Scratch, 2nd Edition
    resource: "Data Science from Scratch, 2nd Edition (Joel Grus), ch. 3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4, ch. 8"
---

Data visualization has two primary uses: **exploring** data and
**communicating** data. Creating a chart is easy; producing a *good* one is
much harder — the gap shows up differently depending on which purpose the
display serves.

**Exploration** is iterative and often private: the analyst tries many views,
filters, and encodings to find structure, outliers, or relationships. A rough
plot with minimal labeling may be enough when the only reader is the person
who made it and the goal is to ask the next question. During exploration,
mostly **avoid** strong [preattentive](preattentive-processing.md) emphasis —
highlighting one point makes other points harder to see, and you do not yet
know which point matters. See [analytical dashboards](dashboard-role-taxonomy.md)
for the production equivalent — richer context, drill-down, and interaction
because the viewer needs to understand *why* a number moved.

**Communication** (explanatory analysis) targets an audience that did not
build the chart and usually has one specific story to tell. The graphic must
carry its own context — title, axis labels, units, legend — and honest
scales, because the viewer cannot click around for missing detail. Use
[visual hierarchy with preattentive attributes](visual-hierarchy-with-preattentive-attributes.md)
to make that story clear: color and text focus attention, and
[progressive emphasis across slides](progressive-emphasis-across-slides.md)
can reuse one decluttered chart for successive claims in a live sequence. See
[a standalone graphic must be self-sufficient](self-sufficient-graphic-elements.md)
and [graphical integrity](bar-graph-zero-baseline-rule.md) rules. A display
optimized for exploration (dense, interactive, context-light) usually
communicates poorly when copied or presented without the surrounding analysis
environment.

The same chart type can serve either role, but the design constraints differ:
exploration favors speed, flexibility, and neutral encoding; communication
favors clarity, self-sufficiency, deliberate emphasis, and
[aesthetics that serve the message](aesthetics-serve-communication.md).
