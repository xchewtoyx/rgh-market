---
type: concept
title: Qualitative Coverage Depth
description: Evaluating verification thoroughness using qualitative depth tiers rather than misleading quantitative coverage percentages.
sources:
  - title: "Taking Testing Seriously"
    resource: "Taking Testing Seriously (James Bach, Michael Bolton), ch. 9"
---

# Qualitative Coverage Depth

**Qualitative coverage depth** is a framework for evaluating and communicating the thoroughness of verification activities. Relying on quantitative metrics (such as test execution counts or coverage percentages) creates a false illusion of certainty and incentivizes superficial checking (Goodhart's Law).

## Ordinal Scale of Verification Depth
Instead of quantitative percentages, verification depth should be classified into six qualitative tiers:
1. **Nothing**: The area or claim has not been examined.
2. **Sanity**: 1–2 basic happy paths verified to confirm basic functionality.
3. **More Than Sanity**: Primary functionality and basic error paths checked.
4. **Common Cases**: Broad scenarios, typical user workflows, and frequent failure conditions sampled.
5. **Some Corner Cases**: Stress conditions, boundary values, data variations, and large payloads tested.
6. **Deep Corner Cases**: Extreme data combinations, extended duration runs, multi-variable race conditions, and rare failure modes thoroughly investigated.

## Product and Release Coverage Outlines
To report verification coverage without deceptive metrics:
- **Product Coverage Outline (PCO)**: A hierarchical inventory of all verifiable components, interfaces, data elements, and operational paths. Unchecked areas are explicitly listed to expose blind spots.
- **Release Coverage Outline (RCO)**: A high-level visual summary or heatmap mapping the qualitative depth tiers across the product space for a specific release, highlighting newly changed or high-risk modules.
