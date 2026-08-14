---
type: concept
title: Epistemic Level Separation
description: Explicitly distinguishing raw empirical data, direct logical inferences, and broader speculative interpretations within technical claims.
sources:
  - title: "Writing Science"
    resource: "Writing Science (Joshua Schimel), ch. 8"
---

# Epistemic Level Separation

**Epistemic level separation** is the practice of explicitly partitioning raw empirical evidence from analytical deductions and high-level interpretations. Unclear boundaries between observation and speculative interpretation weaken technical verification and hide unstated assumptions.

## The Three Epistemic Tiers
To ensure independent reviewers can verify assertions, technical documents must distinguish three distinct levels of claims:
1. **Raw Data & Observations**: Direct, unvarnished empirical measurements, system telemetry, or primary records. Data signals what actually occurred.
2. **Robust Inferences**: Direct logical deductions and statistical conclusions derived straight from the data. These conclusions must logically follow from the observed evidence.
3. **Broader Interpretations**: Contextual hypotheses, generalizations, or policy recommendations. These represent speculative or predictive extensions rather than verified facts.

## Evidence-First Presentation
Structure technical arguments data-first to demonstrate that conclusions stem strictly from empirical evidence:
- **State recognizable schemas**: Clearly document the measurement methods, schemas, and any operational deviations so independent evaluators can assess [methodological boundaries](claim-scope-calibration.md).
- **Prevent inference leakage**: Avoid stating speculative interpretations as established facts in results or data presentations.
- **Maintain audit trails**: Ensure each interpretation explicitly traces back to the specific inference and raw data points supporting it.
