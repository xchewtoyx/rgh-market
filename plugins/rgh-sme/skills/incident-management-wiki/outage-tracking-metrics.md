---
type: concept
title: Outage Tracking Metrics
description: A standard set of timing and impact measures — detection, mitigation, resolution, and user-impact minutes — used to compare incidents and find systemic trends across many of them.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 16"
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives: A Practical Guide to SLIs, SLOs, and Error Budgets (Alex Hidalgo), ch. 17"
---

Individual [blameless postmortems](blameless-postmortems.md) capture what
happened in one incident; a centralized outage database aggregating a
consistent set of metrics across *all* incidents is what turns that history
into a trend an organization can act on. Four measures recur:

- **Time to Detect (TTD)**: from outage onset to the first alert firing.
- **Time to Mitigate (TTM)**: from the alert firing to user-facing impact
  being resolved (not necessarily the underlying cause).
- **Time to Resolve (TTR)**: from mitigation to the permanent code or
  infrastructure fix landing.
- **User-Impact Minutes**: outage duration multiplied by the fraction of
  users affected — a single number that makes a short, severe outage and a
  long, narrow one comparable.

Recording these consistently, alongside postmortem metadata (roles,
timeline, severity, detection mechanism), turns individual incidents into
data: which failure modes recur across otherwise-unrelated services (e.g.,
configuration push failures, dependency timeouts), and which of them cost
the most in aggregate user-impact minutes. That comparison is what
justifies engineering investment in a systemic fix — see
[action item quality](action-item-quality.md) — over chasing whichever
outage is most recent or most memorable.

### The pitfall of averaging

A mean across these measures can actively mislead: twenty short incidents
totaling 400 cumulative minutes of impact produce a better-looking mean
time-to-resolve (20 minutes) than a single 3-hour outage (180 minutes),
even though the frequent-incident period caused users more than twice the
total harm. Incidents also resist clean bucketing for averaging in the
first place — nominally "the same" incident type (e.g., different flavors
of a denial-of-service attack) varies enough in cause and responder
experience that lumping them into one MTTR figure hides more than it
reveals. Prefer cumulative, user-impact-weighted totals (like user-impact
minutes above) over means when comparing periods or justifying
prioritization.
