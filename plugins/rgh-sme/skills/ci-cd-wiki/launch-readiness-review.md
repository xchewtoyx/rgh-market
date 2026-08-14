---
type: concept
title: Launch Readiness Review
description: >
  A structured pre-launch review of a major release's dependencies, capacity,
  and failure modes, distinct from routine release automation, aimed at
  catching launch-day outages that only large or novel traffic patterns would trigger.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 27"
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

# Launch Readiness Review

Routine releases go through the standard
[deployment pipeline](deployment-pipeline.md) and
[release strategy components](release-strategy-components.md). A launch that
introduces a major new capability or is expected to draw significant new
traffic warrants an additional, more deliberate review before it ships,
covering ground the standard pipeline doesn't automatically check:

- **Architecture and dependency review**: map every upstream and downstream
  service the launch touches, and identify where a failure in one of them
  would propagate.
- **Capacity validation**: load test the backends the launch depends on and
  confirm the resource capacity actually exists where it's needed (across
  whichever datacenters or regions will serve the traffic), rather than
  assuming existing headroom is sufficient.
- **Failure mode analysis**: check behavior under conditions the routine test
  suite may not exercise — network partition, a dependent database going
  down, a third-party API outage.
- **Client behavior audit**: confirm calling clients (mobile, web, other
  services) implement sane failure behavior — exponential backoff, retry
  caps, caching — so a backend hiccup doesn't turn into a retry storm that
  makes the hiccup worse. (The deep resilience-pattern design behind this
  belongs to reliability engineering; this review's job is to confirm the
  launch doesn't skip it.)

## Relationship to staged rollout

This review determines whether it's safe to *start* a
[staged rollout across failure domains](canary-release.md) at all — it's a
gate before the first canary, not a replacement for the gradual-exposure
mechanics that follow.

## Accumulate the checklist across launches, don't rebuild it each time

Any one team launches infrequently enough that institutional memory of what
to check fades between launches. Treat the review's checklist as a living
document that every launch adds to: when a launch fails for a reason the
checklist didn't cover (a missing overload contingency plan, an
un-sign-posted dependency rate limit), add that specific item to the
checklist before the postmortem closes, rather than trusting the lesson to
be remembered informally next time. At organizations running many launches
across many teams, this can scale into a dedicated Launch Readiness Engineer
role or launch committee that shepherds every team through the same
continuously-updated checklist, making a launch's technical review
self-service rather than something each team improvises from scratch.
