---
type: concept
title: Release Latency at Scale
description: >
  Even with daily release creation, rolling a change safely through production
  can take a week or more at large scale, so debugging lags behind deployment
  unless frequent small batches keep divergence small.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Release Latency at Scale

**Release latency** is the wall-clock time from when a build is cut to when
every user (or every targeted cohort) is running it. At small scale this can
be minutes; at large scale — hundreds of feature teams, millions of devices,
multi-stage [canary release](canary-release.md) progressions across failure
domains — even a team that **creates** releases daily may need a week or
more to **roll out** each one safely.

That gap puts production debugging a week behind the commit that introduced a
bug. Frequent [release trains](release-train.md) and small batch sizes
counter it by minimizing how far production diverges from a known-good state
and by keeping changes recent enough that culprit-finding and rollback stay
tractable.

See also [deploy capability vs. user cadence](deploy-capability-vs-user-cadence.md)
— a team can maintain high deploy *capability* without pushing every user
through every release on the fastest possible schedule.
