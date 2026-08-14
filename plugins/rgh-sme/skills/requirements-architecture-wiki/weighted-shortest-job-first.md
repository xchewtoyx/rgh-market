---
type: concept
title: Weighted Shortest Job First (WSJF)
description: >
  Sequencing features by Cost of Delay divided by effort, rather than by
  raw value or raw size alone, accounts for how sequence itself changes
  the economics of a delivery plan.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 13"
---

Prioritizing features by return on investment alone is a documented
failure mode: a higher-ROI feature is not automatically the one to build
first, because the economics of a delivery plan are sensitive to
*sequence*, not just to each feature's standalone value. A high-ROI
feature whose value barely decays if delayed can safely go later; a
lower-ROI feature whose value decays fast if delayed may need to go
first, and delaying it can cost more than the ROI gap between the two
features.

**Weighted Shortest Job First (WSJF)** makes this explicit by sequencing
features by `Weight = Cost of Delay / Effort`, taking the highest-weight
feature first. A feature with small effort and high cost of delay
dominates the ranking even against a much larger feature with a higher
absolute cost of delay, because the small feature retires its cost faster
per unit of capacity spent.

**Cost of Delay** itself is composed of three factors, each usually scored
as a relative rating rather than an absolute number (sufficient for
ranking without needing to be precise in absolute terms):

1. **User/business value** — value relative to other candidate features.
2. **Time value** — how fast the feature's value decays if delivery is
   delayed; this ranges from negligible (a rebrand) to severe (a
   seasonal deadline the business can't move).
3. **Risk reduction / opportunity enablement value** — value from
   retiring uncertainty or unlocking a future opportunity, independent of
   the feature's direct user-facing value; a [spike](spike-story.md) at
   the story level is the same idea one layer down.

The counterintuitive result WSJF is built to produce: a feature with the
*lowest* raw user value and the *lowest* raw ROI can still rank first,
if its time-value component is high enough — sequencing purely by value
or by ROI would get this wrong. WSJF also has an explicit expiry built
into how it should be used: because cost of delay and available capacity
both shift over time, a WSJF ranking is only valid for the context it was
computed under and must be recalculated at each planning boundary rather
than treated as a fixed, durable ranking — see [requirements
prioritization](requirements-prioritization.md) for the broader family of
techniques WSJF belongs to.
