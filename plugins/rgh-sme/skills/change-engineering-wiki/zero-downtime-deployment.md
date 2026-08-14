---
type: concept
title: Zero-Downtime Deployment
description: >
  The requirement that production deployments happen during normal
  business hours without user-visible disruption, which rules out
  maintenance-window-based release strategies for continuous platforms.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 5"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 13"
---

# Zero-Downtime Deployment

Zero-downtime deployment is the capability to execute production
deployments during normal business hours without disrupting users. For a
system operating continuously (24x7, global, multi-region), the traditional
alternative — a scheduled offline maintenance window — is not viable: at
fleet scale, across hundreds or thousands of instances and multiple
regions, there is no "quiet" window that doesn't cost real availability
somewhere.

Zero-downtime deployment is the outcome that [blue-green deployment](blue-green-deployment.md),
[rolling deployment](rolling-deployment.md), and [canary release](canary-release.md)
each achieve by different mechanisms — none of them require taking the
whole system offline to switch versions. It also depends on
[independent deployability](independent-deployability.md): a system that
must be deployed as one indivisible block cannot avoid a visible cutover
moment.

Achieving it for stateful changes additionally requires
[schema and data migrations](expand-and-contract-schema-migration.md) that
don't force application code and database structure to change in lockstep.
