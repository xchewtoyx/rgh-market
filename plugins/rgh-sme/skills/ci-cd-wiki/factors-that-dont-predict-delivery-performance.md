---
type: concept
title: Factors That Don't Predict Delivery Performance
description: >
  Empirical research finds system age/tech stack, whether deployment is done
  by dev or ops, and the presence of an external change approval board have
  no predictive relationship to delivery performance — and CABs correlate
  negatively.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 1"
---

# Factors That Don't Predict Delivery Performance

Contrary to common assumptions, empirical analysis (Forsgren, Humble, Kim)
found these factors have no predictive power over the
[DORA four key metrics](dora-four-key-metrics.md):

- **System age and technology stack**: legacy mainframe "systems of record"
  perform comparably to modern greenfield "systems of engagement," as long as
  architectural loose coupling is maintained. Old technology is not itself a
  performance ceiling.
- **Deployer identity**: whether operations or development performs the
  deployment makes no measurable difference.
- **External change approval boards (CABs)**: the presence of a formal
  external approval board does not predict higher stability or lower risk —
  it correlates *negatively* with performance.

The CAB finding is the most consequential for pipeline design: it suggests
that risk reduction comes from what the
[deployment pipeline](deployment-pipeline.md) itself verifies automatically
(tests, gates, [smoke tests](smoke-test.md)) rather than from inserting a
human approval step external to the pipeline. An external approval process
doesn't add information the pipeline doesn't already have, but it does add
queue time — which, per
[capacity utilization and lead time](capacity-utilization-antipattern.md),
directly increases lead time without a compensating stability benefit. The
policy question of whether and how to gate changes on human approval belongs
to change-engineering; this note captures only the empirical pipeline-design
implication.
