---
type: concept
title: Preattentive Attributes for Dashboards
description: >
  Of the many visual attributes perceived preattentively, eleven are relevant
  to dashboards, and only some of them can express "greater than / less than"
  rather than merely "different from."
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.2.1-4.2.5"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4 (adapting Few, Show Me the Numbers, 2004)"
---

Colin Ware catalogs 17 preattentive attributes across four categories; Few
narrows this to 11 relevant to dashboard design (the same catalog Knaflic
adapts for explanatory charts — size, hue, intensity, position, line length,
line width, shape, enclosure, and related form attributes):

- **Color**: Hue; Intensity (Few deliberately collapses saturation and
  lightness/brightness into one practical "intensity" concept).
- **Position**: 2-D location.
- **Form**: Orientation, Line length, Line width, Size, Shape, Added marks,
  Enclosure.
- **Motion**: Flicker.

Not all of these support **quantitative** perception ("greater than / less
than") — some only support **categorical** perception ("different from," with
no inherent order):

| Attribute      | Quantitative? |
|----------------|---------------|
| Hue            | No |
| Intensity      | Yes, but limited |
| 2-D position   | Yes |
| Orientation    | No |
| Line length    | Yes |
| Line width     | Yes, but limited |
| Size           | Yes, but limited |
| Shape          | No |
| Added marks    | No |
| Enclosure      | No |
| Flicker        | Yes, based on speed, but limited |

**2-D position** is the most accurate and easiest of all preattentive
attributes to perceive, which is why it's the primary means of encoding
quantitative data in graphs (a point's position relative to a quantitative
scale). **Line length** (bar length) is the other reliably accurate
quantitative encoding. Size/area is only "yes, but limited" — see
[avoid area encoding for quantitative comparison](avoid-area-encoding-for-quantitative-comparison.md)
for the failure mode this causes. 3-D/stereoscopic position is deliberately
excluded: it's rarely necessary for business data, hard to design well, and
introduces its own perceptual problems (see
[avoid 3-D effects and occlusion](avoid-3d-effects-and-occlusion.md)).

Purely categorical attributes (hue, orientation, shape, added marks,
enclosure) are still valuable — for dividing data into distinct groups,
visually linking spatially separated data (see
[Gestalt similarity](gestalt-similarity.md)), and highlighting (see
[static vs. dynamic highlighting](static-vs-dynamic-highlighting.md)) — just
not for showing magnitude. Individual attribute notes:
[color perception context dependence](color-perception-context-dependence.md),
[perceptual distinctness limits](perceptual-distinctness-limits.md)
(how many levels of one attribute can actually be told apart),
flicker as used for real-time alerting (see
[static vs. dynamic highlighting](static-vs-dynamic-highlighting.md)), and
orientation, whose main dashboard use is italics — generally discouraged
since slanted text is harder to read than upright text.
