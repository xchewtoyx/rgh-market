---
type: concept
title: Perceptual Distinctness Limits
description: >
  Most preattentive attributes have a practical ceiling of about 5 reliably
  distinguishable levels, and hue tops out around 9 before memory for what
  each one means starts to fail.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.2.6"
---

There's a practical limit on how many distinct expressions of a single
[preattentive attribute](preattentive-attributes-for-dashboards.md) viewers
can quickly tell apart. Example: gray-scale line shading on a line graph —
once lines are spaced far enough apart in intensity to look clearly distinct,
only about **5 distinct gray intensities** are practically usable. This
~5-item ceiling applies to essentially every preattentive attribute *except*
line length and 2-D position, which don't have this limit. For shape
specifically, the ceiling combines with a second constraint: only simple
shapes are usable at all (circles, squares, triangles, dashes, X marks),
since complex shapes and icons aren't perceived preattentively.

Hue is a partial exception: more than 5 hues can be visually *distinguished*,
but [short-term memory](short-term-memory-chunk-limit.md) can't
simultaneously retain the *meaning* of more than roughly **9 hues** — beyond
that, added hue variety just reads as clutter rather than added information.

The practical consequence: predefine a small, fixed set of hues, intensities,
and shapes up front, and reuse that set consistently across the whole
dashboard, rather than choosing colors or shapes ad hoc per chart. This is
also the direct reason [evaluative state banding](evaluative-state-banding.md)
caps good/bad categories at roughly 4-5 states, and why
[colorblind-safe color encoding](colorblind-safe-color-encoding.md) favors a
small number of intensity steps within one hue over a wide hue palette.
