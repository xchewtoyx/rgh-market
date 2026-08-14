---
type: concept
title: Action Item Quality
description: The distinction between superficial, low-quality quick fixes and robust, high-quality systemic improvements in post-incident reviews.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 8"
---

Post-incident action items often suffer from low quality because organizations rely on superficial quick fixes:
* **Low-Quality Fixes**: Reprimanding operators, retraining individuals, writing more rules/procedures, or adding more technology. These actions shift blame and increase complexity without fixing systemic vulnerabilities.
* **High-Quality Fixes**: Altering organizational structures, rebalancing production vs. safety tradeoffs, adjusting code architecture, and fixing systemic goal conflicts.

Action items must follow **SMART** criteria:
* **Specific**: Defines the exact organizational unit, action, and timing.
* **Measurable**: Includes criteria for verification and monitoring.
* **Agreed**: Aligns with operational and production realities.
* **Realistic**: Feasible within organizational resource constraints.
* **Time-bound**: Enforces strict implementation deadlines.

High-quality action items focus on change factors (systemic levers for improvement) rather than simple explanatory factors, ensuring long-term resilience following [learning reviews](learning-reviews.md) and [blameless postmortems](blameless-postmortems.md).

**A specific way "measurable" and "realistic" can silently fail for ML monitoring action items**: a follow-up like "add an alert for this class of data anomaly" sounds SMART on paper, but real data and model behavior are naturally noisy — an overly sensitive monitor fires constantly on normal variation and gets ignored or disabled, while an overly broad one misses the next real partial outage. Tuning that threshold reliably can be genuinely hard, so these action items are prone to languishing open for years even when everyone agrees they're valuable, unlike a straightforward code fix. Treating "add monitoring" as done only once it's been tuned to a usable signal-to-noise ratio — not once the alert merely exists — keeps this failure mode from hiding inside an apparently-closed action item.
