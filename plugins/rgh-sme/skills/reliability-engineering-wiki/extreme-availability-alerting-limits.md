---
type: concept
title: Extreme Availability Alerting Limits
description: >
  At very high availability targets, alerting alone cannot defend the SLO
  because a full outage can exhaust the entire budget faster than metrics
  can even be collected — the real defense has to be safe rollout mechanics.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
---

For extreme high-availability goals (e.g. 99.999%), the allowed downtime
becomes so tiny that a full outage can exhaust the entire
[error budget](error-budget.md) in a matter of seconds — potentially faster
than the metric collection interval itself. No alerting scheme, however
well-tuned, can react in time to defend a target that tight, because there's
no window in which to detect the problem and page a human before the budget
is already gone; see
[alerting response-time floor](alerting-response-time-floor.md) for why the
practical human-response floor makes this structurally impossible well
before six-nines territory.

The only real defense at this tier is designing safe rollout mechanisms so
failures are caught and contained before they scale to 100% of traffic —
small-percentage traffic rollouts and canarying (owned by `change-engineering`)
rather than detect-and-page. Alerting on SLOs and safe rollout mechanics are
complementary at every tier, but at the extreme end, rollout mechanics
become load-bearing in a way alerting cannot substitute for.
