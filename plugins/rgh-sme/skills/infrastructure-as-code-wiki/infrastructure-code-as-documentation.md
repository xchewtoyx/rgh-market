---
type: concept
title: Infrastructure Code as Documentation
description: The idea that, for many purposes, a system's infrastructure code is a more useful and trustworthy record of the system than separately maintained documentation.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 4"
---

Written documentation drifts out of date because keeping it current is extra work that competes with everything else. Infrastructure code, by contrast, is always an accurate and current record of the system, because the system literally is built from it. New team members can read the code to learn how the system is built; teammates can read commits to see what changed and why; reviewers can use the code to assess what needs improving; auditors can use the code and its version history to build an accurate picture of the system for compliance purposes.

This doesn't replace all documentation — high-level context and strategy still need to be explained for stakeholders who don't work directly with the code — but it does mean architecture decision records and similar material are often best kept as versioned text alongside the code rather than in a separate, easily-stale system. Because the code is the record, you can also mechanically derive other artifacts from it — architecture diagrams, parameter references — and regenerate them automatically as part of a [delivery pipeline](infrastructure-delivery-pipeline.md) whenever the code changes, so the derived documentation can't drift from the source of truth either.
