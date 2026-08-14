---
type: concept
title: Radar Chart Pitfalls
description: >
  Radar (spider) charts arrange a quantitative scale radially from center to
  perimeter, which obscures data a linear bar graph would show clearly, and
  are rarely appropriate for business data.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.5, ch. 6 §6.2.1.10"
---

In a radar (spider) chart, quantitative values run along spokes radiating
from a center point, with smaller values sitting closer to the center. This
circular arrangement is harder to read than a linear bar graph — axis labels
are often missing or hard to place, and comparing values across spokes is
harder than comparing bar lengths along a shared baseline.

Radar charts are rarely appropriate for typical business data. The one
legitimate exception is when the categorical scale being plotted is itself
naturally circular — e.g., hours of a clock-face day — where the radial
layout matches the data's actual structure instead of fighting it. Otherwise,
prefer a [bar graph](categorical-scale-types-and-bar-vs-line-choice.md).
