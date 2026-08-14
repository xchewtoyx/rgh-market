---
type: concept
title: Audit Statistics Tie-Back
description: >
  Accumulating aggregate counts and sums during extraction and comparing
  them against the source and against load results, to give a pipeline's
  output a defensible claim of matching the source system.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 20"
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §3.3"
---

While extracting data — especially during a large historic load — accumulate
simple audit statistics as a side effect: row counts, subtotals, and sums
over the values being extracted. These numbers then tie back two ways: to
the source system's own operational reports (establishing that the pipeline
extracted what the source actually had), and forward to the load's own
results (establishing that what was extracted is what actually landed).

This is a coarser, aggregate-level complement to
[reconciliation with set operators](reconciliation-with-set-operators.md),
which checks agreement row by row — audit statistics catch a class of
problem row-level diffing can miss (a systematic under- or over-count
introduced by a query filter) while being far cheaper to compute at very
large volumes, where a full row-by-row EXCEPT/INTERSECT comparison may not
be practical at all.

**The same tie-back idea generalizes to continuous streaming pipelines**,
where there's no single extraction batch to accumulate stats over. One
concrete mechanism: each producer periodically emits a monitoring event
recording how many messages it published per topic within a fixed time
window, publishing these events to a *separate* topic from the data itself
so the audit trail is never mixed with — or lost alongside — the data it's
auditing. Consumers then count what they actually received and compare
against the producer-reported counts for the same window, turning
completeness verification into an ongoing background check rather than a
one-off batch reconciliation step.

A perfect tie-back to the source isn't always achievable, and that's not
automatically a bug: business rules the warehouse applies that the source
never did, known source-system errors, and timing differences between when
each side's numbers were captured can all produce a legitimate, explainable
mismatch. The requirement isn't that the numbers always match exactly — it's
that any mismatch has a documented explanation, so a stakeholder questioning
the warehouse's credibility gets a specific answer rather than "we're not
sure why the numbers differ."
