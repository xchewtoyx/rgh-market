---
type: concept
title: Canary Evaluation Metrics
description: >
  What to measure when classifying a canary as good or bad — reuse existing
  SLI instrumentation, keep the metric set small, and prefer metrics tightly
  scoped to the change under test.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 8, 27"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 13"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 16"
---

Reuse existing SLI instrumentation as [canary release](canary-release.md) evaluation metrics rather than
building a separate metric set — acceptance criteria that are too strict
produce false positives (discarding good releases), too loose miss real
regressions. Cap the metric set at roughly a dozen: more than that costs
more to maintain than the marginal metrics return, and an unmaintained
metric quietly erodes trust in the whole canary process. Because canary and
control share backends, networks, and datastores, isolation is never
perfect — a metric tightly scoped to the change under test (e.g. CPU time
actually spent serving the request under test, not whole-machine CPU
conflating unrelated processes) is far more informative than a broad one,
and a canary "stop and investigate" signal is a strong hint, not a
guarantee, that the canary itself is at fault. Always also check absolute
SLO thresholds directly, not only the canary-vs-control comparison.
