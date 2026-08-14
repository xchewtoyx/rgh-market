---
type: concept
title: Done Means Released
description: >
  A feature is not complete when a developer finishes writing code — it is
  complete only once it is running in production, or has been verified as
  passing every deployment-pipeline gate required for production release.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 9, 11"
---

# Done Means Released

Redefines "done" from a development-team-internal state ("I finished coding
and it passed my tests") to a delivery-pipeline state: a change is done when it
has cleared every stage of the [deployment pipeline](deployment-pipeline.md)
and is either live in production or held back from production only by a
deliberate business decision, not by unfinished pipeline work.

This closes a common gap where "feature complete" work sits unreleased for
weeks accumulating integration and deployment risk — the same risk
[bring the pain forward](bring-the-pain-forward.md) exists to eliminate. It
also gives [cycle time](cycle-time.md) a well-defined endpoint: cycle time only
reaches zero contribution to risk when "done" and "released" are the same
event.

## A weaker but useful intermediate bar

Even short of full release, a stricter definition of "done" than "runs on my
laptop" pays off: code should only count as done once it has been built,
deployed, and confirmed running as expected in a production-like environment
(see [ephemeral test environments](ephemeral-test-environments.md)), ideally
under production-like load and data — not merely once it compiles locally.
By forcing this integration work into every iteration instead of deferring it
to release time, the bulk of environment-integration problems get found and
fixed while they're still cheap, the same logic behind
[bring the pain forward](bring-the-pain-forward.md).

A further tightening ties this bar directly to
[trunk-based development](trunk-based-development.md): code counts as done
only once it's been built from trunk via a one-click process and validated
by the automated test suite — not from a private branch, and not by a manual
build. This closes the gap where a feature technically "runs in a
production-like environment" but only via a bespoke, undocumented build a
developer ran by hand, which proves nothing about whether the pipeline can
reproduce that result on demand.
