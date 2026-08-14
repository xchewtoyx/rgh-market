---
type: concept
title: Feature Toggle
description: >
  Wrapping new code in a conditional switch controlled by remote configuration
  so incomplete or unreleased functionality can be merged and deployed
  continuously without being exposed to users until explicitly turned on.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Feature Toggle

Also called a feature flag. A feature toggle is the mechanism that implements
[deploy vs. release](deploy-vs-release.md) at the code level: the new code
path is merged to mainline and deployed through the pipeline like any other
change, but sits behind a flag that keeps it inactive for users until product
management flips it on — deployment and release become genuinely independent
events.

This is also what makes
[trunk-based development](trunk-based-development.md) practical for large or
multi-week features: instead of keeping the work on a long-lived branch until
it's "done," it merges to trunk continuously behind a toggle, avoiding
[integration hell](integration-hell.md) while the feature is still incomplete.

## Flag guarding in continuous delivery

Reliable continuous releases require **flag guarding** every change: new code
lives alongside the old codepath behind a flag; both can run, only the new path
is gated. Once validated, the old path is removed in a subsequent release.
Stable shipped features stay enabled in both development and release builds;
in-development features stay enabled only in development builds, with build
tooling stripping disabled code entirely where the language permits.

Flag values can update independently of a binary release via dynamic
configuration — enabling a press announcement to flip at the last moment
without timing a binary rollout to marketing. That independence is not free:
configuration changes themselves need safe rollout (never flip to 100% of users
all at once); a configuration service that manages staged config promotion is
worth the investment.

Flag guarding is not a perfect safety net for sensitive features — code can
still be scraped or analyzed if not obfuscated, and not every feature can hide
behind a flag without excessive complexity. For rollouts where user-visible
behavior must not change, see [change-neutral release](change-neutral-release.md).

## Technical debt discipline

A toggle is meant to be temporary. Once a feature is permanently released (or
permanently rejected), the toggle and the dead code path it guards must be
removed. Toggles that accumulate indefinitely turn the codebase into a
combinatorial mess of flag states that were never meant to be a long-term
architecture.

## Other uses beyond deploy/release decoupling

- **Graceful degradation**: disable a non-essential but resource-intensive
  feature (e.g. recommendations) under extreme load, trading functionality
  for preserved overall availability rather than an outage.
- **Resilience for dependent features**: ship a feature that depends on a
  downstream service before that service is finished or fully reliable,
  behind a toggle — enable it once the dependency is ready, disable it
  automatically if the dependency fails, without redeploying either side.
- **Progressive exposure**: combine with [canary release](canary-release.md)
  patterns to expose a feature to internal employees, then a small customer
  percentage, then everyone — each step controlled by the same toggle rather
  than a new deployment.

## Testing implications

Automated acceptance tests should run with every toggle in its ON state, not
just the default — an untested toggle path is exactly as risky as untested
code. The toggle mechanism itself (correctly reading its configuration,
correctly gating the code path) needs its own test coverage too, since a
broken toggle can silently expose or hide the wrong thing.
