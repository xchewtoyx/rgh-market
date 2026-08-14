---
type: concept
title: Proportional Ink Principle
description: The shaded area or length used to represent a value in a chart must be directly proportional to that value, and violations of this rule are a specific, checkable way charts distort accurate data.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 7"
  - title: "Information Dashboard Design"
    resource: "Information Dashboard Design (Stephen Few), ch. 3-4"
---
# Proportional Ink Principle

Edward Tufte's **principle of proportional ink**: when shaded area or length in a chart represents a numerical value, that area or length must be directly proportional to the value. This single rule explains why bar charts must start at zero (bars use area to represent magnitude, so a truncated baseline breaks proportionality) while line charts don't need to (a line uses vertical *position*, not filled area, to represent change, so it isn't subject to the same constraint) — and it gives a reviewer a concrete, checkable test for a wide range of chart types.

## Checkable Violations
- **Truncated bar-chart axis**: a y-axis that doesn't start at zero gives bars ink disproportionate to their actual values — a modest real difference (e.g., ~1.08x) can be rendered with several times the visual ink (e.g., ~2.7x), because the *visible* portion of the bar, not its true value, determines the reader's impression.
- **Bar length not matching its own label**: independently check whether a bar's rendered length is proportional to the number printed on or next to it — a bar can be stretched or shrunk relative to its own stated value, which no amount of correct axis labeling will catch, since the distortion is in the bar itself.
- **Two variables encoded into one shape's width and height**: encoding a single ratio using both a shape's width and height compounds the distortion, since area scales as the *square* of a linear shrink — a ratio of 1/6 rendered by shrinking both dimensions can occupy only 1/36 the area, understating the true value far more severely than either dimension alone would suggest.
- **Donut/ring charts**: rings farther from the center sweep more physical area per unit value than rings closer to the center for the same angular width, at a value proportional to radius — ordering categories smallest-to-largest from center outward exaggerates differences between them, while reversing the order understates them.
- **Filled ("area") line charts**: because these shade the area under the line, they inherit the bar chart's zero-baseline rule even though ordinary line charts don't — a filled chart truncated above zero exaggerates the visual change the same way a truncated bar chart does.
- **3D charts and 3D pie charts**: perspective rendering gives unequal ink to equal values depending on their apparent depth or facing angle — elements nearer the viewer or facing the viewer more directly can visually occupy noticeably more area than their true share, even when the underlying numbers are correct. 3D compounds an existing weakness of pie charts generally, since angle comparison is intrinsically harder for readers to judge accurately than bar-height comparison.
- **Denominator/exposure mismatches presented as if they were direct rate comparisons**: see [unfair comparison detection](unfair-comparison-detection.md) for the case where a raw-count chart is presented as if it already controlled for a varying denominator (e.g., exposure, population, or opportunity) when it hasn't.

## Why Area Encodings Specifically Mislead: Diameter, Not Area, Is What's Perceived
Charts encoding a value as the size of a circle or bubble are especially prone to this violation because viewers instinctively judge a circle's *diameter* rather than its *area* — and area scales with the square of diameter, so the perceptual understatement compounds badly at larger ratios. A circle with roughly 9 times the true area of another (i.e., about 3 times its diameter) is read by viewers as only about 3 times larger, silently discarding two-thirds of the actual magnitude difference. This is a specific, well-documented instance of the proportional-ink violation, not a separate concern: the rendered visual quantity (perceived size) is not proportional to the underlying value, even when the circle's mathematical area technically is.

## Verification Action
For any chart where area, length, or shading represents a value, check whether that visual quantity is actually proportional to the underlying number — not just whether the axis labels are technically correct. Measure or estimate the rendered proportions directly (e.g., does a bar twice as tall represent a value roughly twice as large) rather than trusting that correct labels guarantee proportional rendering.

## See Also
- [Chart Framing Verification](chart-framing-verification.md)
- [Chart Form Mismatch](chart-form-mismatch.md)
- [Unfair Comparison Detection](unfair-comparison-detection.md)
