---
type: concept
title: Quality Screens
description: >
  Diagnostic filter tests embedded directly in a pipeline's data flow, and
  the three ways a pipeline can respond when one fails.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

A quality screen is a diagnostic filter test embedded directly in a
pipeline's data flow, run against every record as it passes through. A
passing test has no side effect on the record; a failing test raises an error
event and triggers one of the response strategies below. Screens fall into
three ascending-scope types:

- **Column screens** — test a single column in isolation: unexpected nulls in
  a required field, a value outside its expected range, a format violation.
  The cheapest and most common type; the [binary validation
  checks](data-quality-validation-tests.md) most pipelines start with are
  column screens.
- **Structure screens** — test a relationship across columns or rows:
  hierarchy validity (a many-to-one relationship that's supposed to hold),
  foreign-key/primary-key relationships (see [declared vs. enforced
  constraints](declared-vs-enforced-constraints.md) for why a warehouse often
  won't catch this for you), or a compound field like a postal address
  matching its expected internal structure.
- **Business rule screens** — everything else: complex, often time-dependent
  rules (a loyalty-tier flag requires both a minimum tenure and a minimum
  activity threshold to be simultaneously true) or aggregate threshold checks
  that only fire once a statistically improbable count accumulates over a
  period, rather than on any single row.

When a screen fails, a pipeline has three response strategies, in roughly
ascending order of preference:

1. **Halt the process** — stop the pipeline and require manual intervention.
   Reliable but painful; reserve it for errors severe enough that continuing
   would produce actively wrong output.
2. **Suspense file** — set the bad record aside for later correction and
   reintroduction. Often a poor choice in practice: it's frequently unclear
   whether or when a suspended record actually gets fixed and reloaded,
   leaving the target data questionably incomplete in the meantime. Not
   recommended for minor issues.
3. **Tag and pass through** — attach a marker to the record (via an
   [audit dimension](audit-dimension.md) for facts, or a dedicated error
   value in the attribute itself for dimensions) and let it continue flowing.
   Usually the best choice when it's available, because it keeps the pipeline
   moving and keeps the record visible and queryable rather than parked out
   of sight in a suspense file. This is the same instinct behind a
   [dead-letter queue](dead-letter-queue.md) in a streaming context — isolate
   and mark the bad record instead of blocking everything else — except that
   tagging keeps the record in the main flow rather than rerouting it to a
   separate queue.
