---
type: concept
title: Launch Readiness Review
description: >
  For a rare, high-blast-radius event like a major product launch, run a
  dedicated cross-team review of dependencies, capacity, and failure modes
  before launch day, rather than relying on routine per-change review.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 27, appendix E"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

# Launch Readiness Review

Routine changes are safe to gate with [peer review as change
control](peer-review-as-change-control.md) and automated
[canary analysis](canary-metric-selection.md) alone. A major product
launch is a different category of risk: it concentrates a sudden, large,
mostly-unknown traffic surge onto a service and everything it depends on,
on a fixed calendar date the business cannot easily move — the kind of
event routine per-change gates aren't built to catch, because no single
change is at fault and there is no prior canary population that ever saw
launch-day load.

A launch readiness review addresses this with an upfront, cross-team audit
covering:

- **Dependency mapping** — every upstream and downstream service the
  launching feature touches, and whether each has been told the launch is
  coming.
- **Capacity validation** — load-testing backends against the actual
  expected traffic shape and securing resource headroom ahead of time,
  rather than discovering the shortfall live.
- **Failure mode analysis** — how the system behaves under a dependency
  outage, network partition, or database failure specifically during the
  launch window, since a failure on launch day gets amplified by the
  traffic spike itself.
- **Client behavior audit** — checking that calling clients (mobile apps,
  third-party integrators) implement backoff and retry caps, since a
  client-side retry storm can turn a minor backend hiccup into a
  fleet-wide overload at launch scale (retry storms and cascading failure
  are `reliability-engineering`'s territory; this is about auditing for
  the risk ahead of a known launch date).
- **Monitoring, alerting, and runbook availability** — confirming
  dashboards, alerts, and on-call runbooks for the launching feature exist
  and are wired up *before* launch day, not authored reactively once
  something is already on fire.

This front-loaded review pairs with, rather than replaces, the mechanics
that reduce launch-day risk directly: [gradual staged
rollout](staged-percentage-rollout.md) of the traffic ramp itself,
[dark launch](dark-launch.md) of the new code path ahead of the visible
launch date, and [feature flags](feature-flag-blast-radius-isolation.md)
as the kill switch if something is still wrong once real users arrive.

A lighter-weight technique worth running as part of the failure-mode-analysis
step, or on any risky change too small to warrant a full review: a
[premortem](premortem-risk-analysis.md), which asks reviewers to imagine
the launch has already failed and explain why, surfacing risks that a
straight "does this look right?" review of the plan tends to miss.

Because any one team launches rarely, institutional memory of what to
check fades between launches — the review should be run against a
**checklist that accumulates lessons across every past launch**, not
reconstructed from scratch each time; a launch failure's root cause
becomes a new permanent checklist item, so the checklist itself is the
organization's compounding memory of every way a launch has previously
gone wrong. At large scale, this can be made fully self-service — a team
works the checklist itself with a shepherding reviewer, rather than a
scarce central committee reviewing every launch by hand.
