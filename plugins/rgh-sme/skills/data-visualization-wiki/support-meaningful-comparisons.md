---
type: concept
title: Support Meaningful Comparisons, Discourage Meaningless Ones
description: >
  Deliberately design for the comparisons a viewer actually needs to make —
  through proximity, shared color, and combined graphs — and avoid visual
  choices that accidentally imply a comparison that isn't meant.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.7, ch. 7 §7.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

A raw measure is only as useful as the [comparison](contextualizing-metrics-with-comparisons.md)
a viewer can make against it, and comparisons that aren't visually supported
often don't happen at all — viewers rarely do the mental work of comparing
two numbers that are far apart on screen. Techniques to actively support an
intended comparison:

- Combine the compared items into a single table or graph rather than
  separate ones.
- Place the items physically close together (see
  [Gestalt proximity](gestalt-proximity.md)) — this specifically includes
  placing paired series (e.g., actual vs. budget per region) as adjacent bars
  rather than in separate groups, which otherwise makes the intended
  comparison needlessly hard to make.
- Link items that live in different groups or graphs by giving them a shared
  color (see [Gestalt similarity](gestalt-similarity.md)) — e.g., using the
  same color for "revenue" wherever it appears.
- Include ready-made comparative values (ratios, percentages, variances)
  directly, rather than making the viewer compute them — see
  [choosing the right measure](choosing-the-right-measure.md).
- When two series share the same unit, combine them in one graph; when they
  don't (e.g., very different magnitudes), resist jumping straight to a
  dual-axis chart — see
  [secondary y-axis alternatives](secondary-y-axis-alternatives.md) for
  direct-label and paired-chart options that avoid forcing the reader to
  decode two scales in one frame. A dual-axis view is a last resort for
  extreme space constraints, not the default combining trick.

The flip side is just as important: careless visual choices can *accidentally*
invite a comparison between unrelated data. If green/red consistently means
good/bad everywhere, but a third color (say, yellow) is reused with different
meanings in different panels — "satisfactory" in one, "forecast" in another,
just "the month of June" in a third — viewers will read a relationship into
that shared color that doesn't exist, because same-color-implies-linkage is a
natural (Gestalt similarity) inference. Countermeasures: spatially separate
unrelated items, and reserve distinct colors for genuinely unrelated things —
see [visual consistency principle](visual-consistency-principle.md) for the
general rule this is an instance of.
