---
type: concept
title: Transformation vs. Query
description: >
  Why persisting a result for reuse — not just retrieving it — is what turns
  a query into a transformation, and why that distinction is what makes
  orchestrated pipelines necessary at all.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
---

A query retrieves data via filter and join logic. A **transformation**
additionally **persists** the result — ephemerally or permanently — for
reuse by further transformations or queries. That persistence is the key
distinguishing property, and it exists for a concrete reason: avoiding
repeatedly rerunning an expensive, multi-dataset, long-running query dozens
or hundreds of times a day at real compute cost.

The second distinguishing property is **complexity**: a real pipeline
combines many sources and reuses intermediate results across multiple final
outputs (normalizing, modeling, aggregating, featurizing). This is
technically buildable as one giant query using CTEs, scripts, or nested
logic, but it quickly becomes unwieldy, inconsistent, and intractable to
reason about as a single unit — which is exactly the problem breaking work
into discrete, persisted transformations (stitched together by
[orchestration](orchestration-vs-scheduling.md)) solves. Increasingly, a
transformation pipeline spans not just multiple tables but multiple systems
entirely, which is what makes the orchestration layer — not just the
transformation logic itself — a first-class design concern rather than an
afterthought.
