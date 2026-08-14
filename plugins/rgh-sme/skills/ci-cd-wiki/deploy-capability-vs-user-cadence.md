---
type: concept
title: Deploy Capability vs. User Cadence
description: >
  Building the pipeline and architecture to deploy at high frequency does not
  obligate exposing every release to users at that frequency — deploy readiness
  and user-facing update cadence are separate decisions.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Deploy Capability vs. User Cadence

With a mature [deployment pipeline](deployment-pipeline.md), **how often a
viable release is created** can be decoupled from **how often users receive
one**. A team can be capable of hourly or daily deploys while intentionally
shipping to users weekly, per platform policy, or only when a feature justifies
the download and disruption cost — especially on mobile and other
client-delivered software where bloat and update friction matter.

Much of continuous delivery's value comes from having the **structures** in
place — documented process, real-time health metrics, rollback/rollforward,
configuration managed like code — even when maximum cadence is not used every
day. Products like Search, Maps, and YouTube do not ship wildly different
binaries to every user daily, but being *able* to requires that infrastructure.

Modular architecture and per-device or per-locale configuration (shipping only
relevant translations, architectures, or feature bundles) keep client size down
when release *creation* outpaces user-facing cadence. Pair with [feature toggles](feature-toggle.md)
so deployed code can sit in production verified but inactive until a separate
[release](deploy-vs-release.md) decision.
