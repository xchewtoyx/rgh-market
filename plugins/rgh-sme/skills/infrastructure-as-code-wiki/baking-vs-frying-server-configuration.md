---
type: concept
title: Baking vs Frying Server Configuration
description: The trade-off between configuring servers into a reusable image ahead of time ("baking") versus applying configuration when each instance is created ("frying").
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 11, ch. 13"
---

**Frying** applies configuration when a new server instance is created — think "configure once per instance." Pushed to the extreme, [server images](server-image-as-code.md) stay minimal and nearly everything specific to a server is applied at creation time, which means new instances always get the latest patches, packages, and configuration, and the number of images to maintain stays small. The cost is speed (configuration steps add to every server's creation time — a particular problem when spinning up servers to absorb a load spike or recover from a failure), efficiency (many new servers separately downloading the same packages is wasteful), and reliability (creating a server now depends on every repository and service the configuration process reaches being available, which is especially painful when trying to rebuild a large number of servers quickly during an incident).

**Baking** pushes as much configuration as possible into the server image ahead of time — think "configure once per image, reuse many times." New instances then only need instance-specific configuration applied, so creation is fast and simple. This suits systems that create many similar instances quickly (autoscaling, frequent rebuilds) but requires a mature automated process for building and rolling out new image versions — see [server images as code](server-image-as-code.md) — and image builds themselves are typically slow (10–60 minutes), which matters when an urgent fix needs to reach production.

Most teams use both together, deciding per element based on how long it takes to apply and how often it changes: slow-to-apply, rarely-changing things (application server software) are good candidates to bake; quick-to-apply, frequently-changing things (an in-house application under active daily development) are better fried. A common middle pattern bakes a slower-moving base image and fries faster-moving updates on top of it, periodically folding the fried updates back into a refreshed baked image. This trade-off directly enables [immutable servers](immutable-server-pattern.md), which push almost everything to baking so that no instance is ever changed once created.
