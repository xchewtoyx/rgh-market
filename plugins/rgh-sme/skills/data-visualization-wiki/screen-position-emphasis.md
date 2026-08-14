---
type: concept
title: Screen Position as a Static Highlighting Tool
description: >
  Top-left and center are the highest-emphasis regions of a screen, so the
  most important, always-important data belongs there — and a logo or nav
  controls never should.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.10, ch. 5 §5.2.2.2, ch. 8 §8.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

Not all displayed data is equally important, and the two ways to make
important data stand out split along a time axis:

- **Always important** data should be highlighted through **static** means,
  since it doesn't change moment to moment.
- Data that's **important only at the moment** (something that has fallen
  behind target, an urgent operational condition) should be highlighted
  through **dynamic** means — see
  [static vs. dynamic highlighting](static-vs-dynamic-highlighting.md).

**Screen location is the primary static-highlighting tool.** A location
shouldn't move dynamically — partly for practicality, but mainly because
viewers learn to expect specific data in specific places, which speeds up
scanning over repeated use. The emphasis map of a screen: **top-left and
center are the highest-emphasis regions.** Top-left emphasis comes from
Western reading conventions (left-to-right, top-to-bottom); without other
cues, audiences often scan in zigzag "Z" motions from the top of the page,
so top real estate is precious — put the main takeaway or most important
data there rather than forcing viewers to wade through lesser content first.
Center emphasis is a more fundamental, non-reading-related perceptual
tendency — though centered content only reads as emphasized if it's visually
set apart from its surroundings (e.g., via white space, per
[Gestalt proximity](gestalt-proximity.md) or
[Gestalt enclosure](gestalt-enclosure.md)).

Work *with* natural reading associations, not against them. A process flow
meant to be read bottom-right to top-left feels uncomfortable even with
directional cues; a negative-to-positive scale with positives on the left
and negatives on the right fights the usual left/negative–right/positive
association and slows decoding. Position and scale orientation should reduce
that friction, not add it.

The direct consequence: never spend top-left or center real estate on a logo
or navigation/selection controls — a mistake illustrated repeatedly across
worked dashboard critiques, where a logo or nav bar occupied the single most
valuable position while the actual most-important metric sat somewhere less
prominent. This is also why a well-designed sample dashboard reserves its
upper-left section specifically for "key metrics," the most important data on
the page, and (for operational dashboards) for near-real-time alerts.
[Size](size-signals-relative-importance.md) is the companion static lever
when footprint, not just placement, must signal importance.

If everything on a dashboard is given equally strong location and styling,
nothing stands out and the viewer has no cue where to look first — over-using
emphasis is functionally the same failure as using none at all. See
[static vs. dynamic highlighting](static-vs-dynamic-highlighting.md) for the
caution against over-highlighting.
