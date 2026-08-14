---
type: concept
title: Single-Hue Saturation Over Rainbow Encoding
description: >
  Encoding ranked or quantitative values as a rainbow of categorical hues
  makes every cell look different and nothing stand out; varying saturation
  of one hue preserves order, draws the eye to extremes, and stays
  colorblind-friendlier.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

When a table or grid must show magnitude or rank across many cells, a
full-spectrum rainbow (1=red, 2=orange, …, 10=purple) fails as an encoding:
every value is a different hue, so nothing pops, and the palette actively
distracts. Hue has no inherent "greater than," so the sequence also fails as
a [quantitative preattentive encoding](preattentive-attributes-for-dashboards.md).

  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4, ch. 9"
---

Prefer varying the **saturation (or intensity) of a single hue** — a heat-
map treatment of the same cells. More saturated reads as greater (or lesser,
if you invert deliberately), so leaders draw the eye first, and the encoding
remains legible under [colorblind-safe](colorblind-safe-color-encoding.md)
constraints that intensity-of-one-hue already satisfies. On a
[dark background](color-logic-on-dark-backgrounds.md), re-validate which end
of the saturation scale pops — the same numbers can read with a different
tone. This is the table-scale counterpart of
[vivid color restraint](vivid-color-restraint.md): one accent family used
purposefully beats many colors used for decoration.

Validate with the eye-path check used for
[visual hierarchy](visual-hierarchy-with-preattentive-attributes.md): look
away, look back, and confirm the first landing matches the intended focus —
or have a colleague narrate their scan order.
