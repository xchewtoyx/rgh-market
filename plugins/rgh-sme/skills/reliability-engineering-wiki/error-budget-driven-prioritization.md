---
type: concept
title: Error-Budget-Driven Prioritization
description: >
  Error budget consumption is a quantitative input for prioritizing
  reliability work — both for ranking which past incidents deserve
  remediation effort and for deciding what a team does next.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 5"
---

**Sizing investigation priority by budget impact.** Using how much budget an
incident consumed to prioritize investigation and remediation ("this outage
used 65% of budget") replaces a qualitative priority debate with a number
everyone can agree on.

**Aggregating burn events to find systemic causes.** Analyzing burn events
over time surfaces patterns a single incident review misses — e.g. "1 in 5
releases causes burn" motivates investing in the release/testing process
generally rather than fixing one release. Aggregating by cumulative cost,
not just per-incident size, changes the ranking: a "smaller but constant"
problem (5 minutes/day of latency issues = 1,825 minutes/year) can actually
cost more cumulative budget than a "bigger but rare" one (30 minutes/month
outage = 360 minutes/year), even though the rare outage looks more dramatic
in the moment. Use this to stack-rank remediation priorities by real
cumulative cost rather than by incident size or recency.

**A decision matrix for day-to-day prioritization.** Combining SLO status
(met/missed), toil level, and customer satisfaction into a small decision
matrix turns "what should we work on" into a lookup rather than a debate:
met + low toil + high satisfaction → relax release process or redeploy
engineering elsewhere; missed + high toil + low satisfaction → offload toil
or improve automated mitigation. The specific matrix cells matter less than
the discipline of deciding this ahead of time rather than re-litigating it
during every planning cycle. Doing so protects the team's long-term
[initial vs. sustained velocity](initial-vs-sustained-velocity.md).

This is the deficit-side counterpart to
[using error budget surplus for experimentation](error-budget-surplus-for-experimentation.md).
Both rely on the same underlying idea: the budget number is a shared,
objective input to a prioritization decision, not just a pass/fail gate on
shipping.

The same "what would this actually change" filter should also decide where
to spend *measurement* effort in the first place, not just remediation
effort after the fact — see [measurement inversion for reliability
investment](measurement-inversion-for-reliability-investment.md) for why the
highest-value monitoring gap is rarely the metric already getting the most
attention.
