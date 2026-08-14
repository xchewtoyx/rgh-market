---
type: concept
title: "Pattern: Build-Time Project Integration"
description: Building and testing multiple dependent infrastructure projects together, producing a single artifact or artifact set that is versioned, promoted, and applied as one unit through the rest of delivery.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 19"
---

Build-time project integration resolves dependencies between projects (for example, [server configuration modules](server-configuration-code.md) that make up a [server image](server-image-as-code.md)) at build time, producing one output — or a versioned, promoted-as-a-group set of outputs — that stays consistent through every later delivery stage, since the same version of every constituent project is used all the way to production.

This gives the earliest possible feedback on cross-project conflicts and guarantees consistency, but at real cost: orchestrating builds across many projects gets complex fast, needs sophisticated tooling to stay fast (large-scale users like Google and Facebook run dedicated teams and specialized build tools — Bazel, Buck, Pants, Please — with dependency graphs that limit rebuilding to only what actually changed), and tends to blur the boundaries between projects, since they're built together rather than integrated at an explicit seam, which risks tighter coupling than intended. Storing all the involved projects in one repository (a **monorepo**) makes build-time integration much simpler to implement, though a monorepo and build-time integration are conceptually separate — you can technically have either without the other.

[Baking a server image](baking-vs-frying-server-configuration.md), and the [immutable server pattern](immutable-server-pattern.md) more generally, are natural examples of build-time integration: the server-configuration dependencies are resolved once, at build time, into a single artifact (the image) rather than being resolved separately each time an instance is created. The alternatives, integrating later in the pipeline, are [delivery-time](delivery-time-project-integration-pattern.md) and [apply-time project integration](apply-time-project-integration-pattern.md).
