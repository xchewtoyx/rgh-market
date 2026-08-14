---
type: concept
title: Service Level Indicator (SLI)
description: >
  A carefully defined, quantitative measure of a service's behavior, expressed
  as the ratio of good events to total events, that stands in for user-perceived
  reliability.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
---

An SLI is a metric measuring some property of a service, converted into a
binary "good"/"bad" judgment for each event so it reduces to simple percentage
math:

```
SLI = good events / total events × 100%
```

Example: page loads under 2 seconds count as "good"; 59,982 good out of
60,000 total = 99.97%.

The standard-ratio form matters beyond convenience — it makes [error budget](error-budget.md) math and shared alerting/reporting tooling consistent
across services, rather than every team inventing its own metric shape.

An SLI is the foundation of the [reliability stack](reliability-stack.md): SLI
feeds a [service level objective](service-level-objective.md) (a target for
the ratio), which in turn drives an error budget. Choosing *what* counts as a
good event is governed by [user-centric SLI selection](user-centric-sli-selection.md);
choosing *how* to compute it in practice is a separate question — see
[SLI specification vs implementation](sli-specification-vs-implementation.md).

SLIs are considered the single most load-bearing layer of the stack: a team
can operate without formal SLOs or error budgets, but a genuinely
user-centric SLI alone is transformative, because it forces attention onto
what users actually experience rather than internal proxy metrics.
