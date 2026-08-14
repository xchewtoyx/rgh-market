---
type: concept
title: Dimensionality
description: Dimensionality is the number of unique fields/attributes captured per event, and a dataset's investigative value grows combinatorially, not linearly, with the number of dimensions it carries — which is why splitting signals into separate silos destroys most of their value, not just some of it.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 1"
---

Dimensionality is the number of unique fields (attributes) an event carries. The number of ways those fields can be combined for a query — filtering or grouping by any subset of them — grows combinatorially with the field count: 4 fields yield 15 possible combinations, but 30 fields yield over 1.1 billion. Each additional field is therefore combinatorially more powerful than the last one, not just additively so.

This is why splitting telemetry across separate silos (a metrics store, a log store, a trace store — see [three pillars vs. wide-event model](three-pillars-vs-wide-events-model.md)) destroys most of a dataset's investigative value, not merely some of it: a question that needs to cross two silos (e.g. "which build IDs show elevated p99 latency for enterprise-tier users in the EU") requires reconstructing relationships that existed at write time but were thrown away by storing each signal type separately.

Dimensionality compounds with [cardinality](cardinality.md) (how many unique values each field takes) to determine how finely a dataset can be sliced when hunting for the cause of an anomaly — see [high-cardinality querying for outlier isolation](high-cardinality-outlier-isolation.md) and the practical checklist of [what attributes to capture on a wide event](wide-event-attribute-checklist.md).
