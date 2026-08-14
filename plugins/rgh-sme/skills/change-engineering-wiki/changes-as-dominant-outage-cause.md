---
type: concept
title: Changes as the Dominant Outage Cause
description: >
  Across thousands of production postmortems, binary and configuration
  pushes together account for the large majority of outage triggers, which
  is the empirical justification for investing in gradual rollout over
  other reliability work.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), Appendix C"
---

# Changes as the Dominant Outage Cause

Analysis of thousands of Google postmortems (2010-2017) found the
following distribution of outage *triggers* (the proximate cause, not the
underlying root cause):

- Binary push — 37%
- Configuration push — 31%
- User behavior change — 9%
- Processing pipeline — 6%
- Service provider change — 5%
- Performance decay — 5%
- Capacity management — 5%
- Hardware — 2%

**Binary and configuration pushes together account for 68% of outage
triggers.** This single number is the empirical backbone for prioritizing
[canary release](canary-release.md), [gradual/staged rollout](staged-percentage-rollout.md),
and [change freeze triggers](change-freeze-triggers.md) ahead of most other
reliability investments: if two-thirds of outages are triggered by a
change someone made on purpose, the highest-leverage reliability work is
making changes safer to ship, not just faster to detect or diagnose after
the fact.

It also explains why [change failure rate](change-failure-rate.md) is
treated as a first-class delivery metric rather than a secondary one — it's
measuring the single largest source of production risk directly, rather
than a proxy for it.
