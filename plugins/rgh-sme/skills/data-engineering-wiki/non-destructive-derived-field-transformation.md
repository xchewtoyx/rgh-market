---
type: concept
title: Non-Destructive Derived-Field Transformation
description: >
  Writing a lossy or derived transformation as a new field alongside the
  original value instead of overwriting it, so the transformation logic can
  still be changed later.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 2"
---

Any pipeline transformation that reduces information — bucketing a
continuous value into discrete ranges (age in years into a decade bucket, a
raw timestamp into a coarser reporting period), or any other many-to-one
mapping — should write its result as a **new field**, leaving the original
value intact in the same record, rather than overwriting it in place.

The reason is forward-looking rather than about the current load: once the
original value is gone, changing the transformation later (a different
bucket width, a different rounding rule) becomes impossible without
re-extracting from the source — which may no longer even be possible if the
source has since moved on or the original extract wasn't
[archived](extract-archival-for-reprocessing.md). Keeping the original
alongside the derived value costs one extra column and preserves the option
to redefine the transformation, or to run both the old and new definitions
side by side while validating a change, without a reprocessing project.

**A second, subtler failure this prevents**: two systems each bucketing the
same underlying data independently, on different boundaries (one grouping
ages by decade, another by five-year bands), silently disagree in a way
that's hard to detect from the bucketed output alone — the original values,
if both systems had kept them, are what makes the disagreement diagnosable
at all instead of just visible as "the numbers don't match."
