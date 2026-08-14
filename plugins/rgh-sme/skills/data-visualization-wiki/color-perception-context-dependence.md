---
type: concept
title: Color Perception Is Context-Dependent
description: >
  A color or intensity is never perceived in isolation — the surrounding
  colors change how it looks, so color choices must be validated in the
  actual context they'll appear in, not swatch by swatch.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.2.1"
---

Color has three attributes in the HSL model: hue (what's normally called
"color" — red, blue, etc.), saturation (how pure/full a hue is), and
lightness/brightness (how dark-to-light it appears). Few collapses saturation
and lightness into one practical concept, "intensity," since the technical
distinction rarely matters for dashboard design.

The key caveat: color perception is not absolute. Two demonstrations: (1)
identical mid-gray squares appear to differ in intensity depending on the
lightness of the gradient background placed behind each one; (2)
identical-hue text is less legible against a red background than against a
blue one, purely because of the surrounding color. This means a color chosen
in isolation (in a palette tool, or against a blank white mockup) can read
completely differently once placed next to a dashboard's other panels and
background — colors must be chosen and validated with full awareness of the
actual surrounding context, so data reads the same when it should and
different when it should.

This is one reason to keep a dashboard's palette small and
[regularized](visual-consistency-principle.md) — see also
[perceptual distinctness limits](perceptual-distinctness-limits.md) and
[vivid color restraint](vivid-color-restraint.md) for how much color variety
a dashboard should actually use.
