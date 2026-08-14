---
type: concept
title: Mean vs. Median Selection
description: Checking whether a reported average was chosen because it best represents the data, or because it tells a more favorable story.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Mean vs. Median Selection

The **mean** and **median** can diverge sharply on skewed data, and the choice between them can be used to make an identical dataset tell very different stories, both of them technically accurate.

## Worked Example
A policy change (e.g., a regressive tax cut) that saves a small top slice of the population a very large amount, and the rest of the population nothing, can be truthfully advertised using the *mean* ("$4,000 average family savings"), even though the *median* family — the one at the actual middle of the distribution — sees $0. Both numbers are correct; only one represents what a typical member of the population actually experiences.

## Verification Action
When a draft cites an average, check whether the underlying distribution is likely to be skewed (income, latency, error magnitude, and similar quantities frequently are). If so, ask whether the mean or the median better represents what a typical case actually looks like, and whether the document chose the statistic that best matches its claimed conclusion rather than the one that best represents the data. Where the distribution's shape matters, both figures — or a fuller distributional summary — should be reported rather than one in isolation.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
