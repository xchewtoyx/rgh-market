---
type: concept
title: "Pattern: Apply-Time Project Integration"
description: Pushing each dependent infrastructure project through its own delivery pipeline independently, integrating with whatever version of its dependencies happens to be live in a given environment at the moment code is applied.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 19"
---

Apply-time project integration (also called *decoupled delivery* or *decoupled pipelines*) pushes each project through its own independent pipeline; integration between dependent projects happens only implicitly, each time code is applied to an environment, by whatever version of the dependency happens to already be running there. A [stack](infrastructure-stack.md) that depends on shared networking managed by a separate stack simply attaches to whatever networking exists in that environment when it's applied — regardless of which version of the networking stack's code produced it.

This minimizes coupling between teams: changes can reach production without coordinating a joint release, which matters at scale, where lock-step delivery across many autonomous teams becomes impractical. The cost is that consistency across the pipeline is no longer guaranteed — a project pushed through faster than its dependencies may integrate with a different dependency version in production than it did in test — so the interfaces between projects need to be treated as genuine, carefully maintained contracts. **Consumer-driven contract testing** is the standard technique here: a team consuming a provider project's resources writes tests that run in the *provider's* pipeline, so the provider team understands and is warned about breaking the expectations its consumers depend on, before those consumers ever see the change.

Apply-time integration is the natural fit for [frying configuration onto a server instance](baking-vs-frying-server-configuration.md) at creation time — the dependency (the latest promoted server configuration module) is resolved fresh, at apply time, on every new instance — in contrast to [build-time integration](build-time-project-integration-pattern.md), where that same dependency would already be locked into a [baked server image](server-image-as-code.md).
