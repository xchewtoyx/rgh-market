---
type: concept
title: Multi-Foci Time Display
description: >
  Show recent history at fine granularity and older history at progressively
  coarser granularity, as adjoining chart sections, so a long time series
  still fits within the single-screen constraint.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 5 §5.2.2.1, ch. 8 §8.4"
---

A summarization technique (Few's term, "multi-foci displays") for historical
time series where recency matters more than distance: show the current month
at daily granularity, the preceding 12 months at monthly granularity, and the
preceding several years at annual granularity, as three adjoining chart
sections with increasing summarization the further back in time you go. This
fits far more history within the
[single-screen constraint](single-screen-constraint.md) than a single
uniformly-grained time series could, without pretending old data deserves the
same resolution as recent data.

This is a specific case of a more general "more detail near, less detail
far" logic, which Few notes applies spatially too (three wall maps of
different scope — local, national, global — each sized to match how much the
viewer actually cares about that scope).

A worked example: a marketing-analysis dashboard split visitor time-series
data into three sections at three different granularities at the top of the
dashboard, giving daily detail for the current period and progressively less
detail further back — the same technique applied directly.
