---
type: concept
title: Choosing the Right Measure
description: >
  A measure can be perfectly accurate and still be the wrong choice — pick
  the derived value that directly answers the viewer's question instead of
  forcing them to compute it themselves.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.4"
---

If the question a viewer needs answered is "how far did we miss budget?",
showing actual revenue ($76,934) and budget ($85,000) side by side and
leaving the viewer to subtract is a worse design than directly showing the
variance ("-9%", optionally with "-$8,066"). Both designs are equally
accurate; only one directly serves the analytical question.

This generalizes: before choosing a display medium, first choose *which*
number(s) to show. A graph can bake the same idea in — e.g., encoding a
budget as a zero reference line and plotting variance as a line meandering
above/below it in percentage units, rather than plotting two separate raw
series and expecting the viewer to visually subtract them.

This is the first decision in [matching visual form to an analytical
question](contextualizing-metrics-with-comparisons.md): get the measure
itself right before worrying about chart type. It also interacts with
[matching precision to the audience](customize-numeric-presentation-to-audience.md) —
a well-chosen measure can still be undermined by showing it with more
precision than the decision requires.
