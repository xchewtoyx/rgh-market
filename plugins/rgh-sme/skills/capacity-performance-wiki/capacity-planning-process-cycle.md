---
type: concept
title: Capacity Planning Process Cycle
description: The measure-model-design-build-deploy cycle that connects capacity planning to actual architectural decisions, and how schedule pressure typically collapses it down to guesswork.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 2"
---

Capacity planning has more leverage the earlier it enters a product's lifecycle, formalized as a five-phase cycle that can be entered at any point:

*   **Measure** — gather measurements from the current or previous-generation product (or, for a wholly new product, back-of-envelope estimates with explicit fudge factors).
*   **Model** — build a performance model from the measured parameters (e.g., [fitting a scalability model](fitting-universal-scalability-law-to-data.md)), since capacity planning is fundamentally about prediction, not description.
*   **Design** — feed the model's projections into architectural decisions before they're locked in ("performance-by-design") — the cheapest point in the lifecycle to change course based on a capacity finding.
*   **Build** — capacity involvement drops off here, but attending build-phase engineering meetings and gathering unit/functional test data still feeds future modeling.
*   **Deploy** — the day of reckoning: the more investment went into the measure/model/design phases, the more likely the deployed system actually meets its capacity plan. Instrumentation designed in during the design phase makes deploy-time measurement far easier than trying to retrofit it later.

## Why the Cycle Gets Skipped

Under schedule pressure, the natural response is to drop the measure and model phases entirely, reducing the cycle to a bare guess-build-guess loop: decide the design by guesswork, build it, then guess again for the next round — faster, but with no forecasting content behind any decision. This isn't irrational from a schedule-driven manager's perspective: performance problems discovered post-launch can become an additional revenue source through paid support/upgrade contracts, creating a real (if perverse) incentive *against* investing in the measure/model phases up front — the customer effectively ends up financing the fix. Any capacity-planning methodology that doesn't survive this pressure (i.e., that visibly inflates the schedule) gets cut regardless of its technical merit — see the tactical, schedule-preserving posture in [capacity headroom safety margin](capacity-headroom-safety-margin.md) for one way to keep planning lightweight enough to survive this pressure.
