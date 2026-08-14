---
type: concept
title: Change Failure Rate
description: >
  One of the four DORA delivery-performance metrics, measuring the
  percentage of production changes that cause degradation, outage, or
  require immediate remediation.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 2"
---

# Change Failure Rate

Change failure rate is the percentage of changes to production — software
releases or infrastructure modifications — that cause service degradation,
an outage, or require immediate remediation (hotfix, rollback, patch). It is
one of the two "stability" metrics in the DORA four-key-metrics model,
alongside [mean time to restore](mean-time-to-restore.md). It is the direct
delivery-performance analogue of Lean manufacturing's %C&A (percent complete
and accurate).

Empirical performance tiers (2017 DORA benchmark):

- **High performers**: 0-15%.
- **Medium performers**: 31-45%.
- **Low performers**: 46-60%.

**Medium-performer anomaly**: medium performers often show a *higher*
change failure rate than low performers. This happens during active
transformation, when teams push new feature work faster before they have
finished automating testing and deployment — [working in small batches](working-in-small-batches.md)
and [build quality in](build-quality-in.md) need to land *before* tempo
increases, or the transformation accumulates technical debt that shows up
as failed changes.

Change failure rate is also empirically dominated by a narrow set of
[change types](changes-as-dominant-outage-cause.md): binary and
configuration pushes account for the large majority of production outages,
which is the empirical justification for investing in
[canary release](canary-release.md) and gradual rollout ahead of any other
reliability work.
