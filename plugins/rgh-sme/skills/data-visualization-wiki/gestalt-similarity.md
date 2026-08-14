---
type: concept
title: "Gestalt Principle: Similarity"
description: >
  Objects that share color, size, shape, or orientation are perceived as
  grouped together, even when they sit in different locations on the screen.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 3"
---

One of six Gestalt grouping principles. Similarity: objects that look alike —
in color, size, shape, or orientation — are perceptually grouped, even across
separate, non-adjacent screen locations. This is what makes it possible to
link things that [proximity](gestalt-proximity.md) alone cannot, because they
aren't physically next to each other. In tables, coloring related cells
similarly can cue reading across a row and eliminate borders that would
otherwise direct attention.

The practical application used throughout dashboard design: use the same
color for the same measure (e.g., "revenue") everywhere it appears across
multiple graphs, so a viewer's eye links those instances and is invited to
compare them. This is the mechanism behind
[support meaningful comparisons](support-meaningful-comparisons.md)'s
shared-color technique, and it's also why an *unintentionally* reused color
is dangerous — it invites a comparison the designer never intended (see that
same note's "discourage meaningless comparisons" half). Similarity is also
the perceptual basis for the [visual consistency principle](visual-consistency-principle.md):
reusing the same chart type, color meaning, and styling for the same kind of
data is what lets similarity do useful grouping work instead of misleading
work.
