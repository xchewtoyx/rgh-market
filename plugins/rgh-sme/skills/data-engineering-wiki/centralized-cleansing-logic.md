---
type: concept
title: Centralized Cleansing Logic
description: >
  Why data-cleaning code belongs in one reviewable place in a pipeline
  rather than scattered across every stage that happens to touch the data.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 2"
---

As a pipeline's data volume and consumer count grow, cleaning and
consistency-fixing logic — handling missing fields, deduplication,
misclassifications, encoding errors — tends to become its own pipeline
stage rather than something handled inline wherever it happens to be
noticed. That consolidation is worth doing deliberately rather than letting
cleaning logic accumulate wherever a given consumer happens to need it,
for three concrete reasons:

- **Fragility from unchecked assumptions**: as more pipeline stages come to
  assume the data is already clean, the pipeline's actual ability to
  guarantee that assumption holds doesn't grow along with it — a scattered
  design has more places where the assumption can silently stop being true.
- **Logic drift**: a fix or improvement to a cleaning rule made in one place
  isn't automatically propagated everywhere the same raw data gets cleaned
  independently, so different consumers can end up working from
  inconsistently cleaned versions of what should be the same underlying
  data.
- **Destructive double-correction**: two independent cleaning steps can each
  "correct" the same field in ways that compound rather than agree — a
  record normalized twice by two different pieces of logic can end up worse
  than either single pass would have produced, and the original value needed
  to detect or undo that is often already gone.

This is the same instinct behind
[warehouse source/staging/presentation layering](warehouse-layering-source-staging-presentation.md)
and [data lake zone layering](data-lake-zone-layering.md): a raw layer stays
untouched specifically so that transformation and cleansing logic has
exactly one place to live, downstream of it, rather than being re-applied
independently by whichever consumer reaches the raw data first.
