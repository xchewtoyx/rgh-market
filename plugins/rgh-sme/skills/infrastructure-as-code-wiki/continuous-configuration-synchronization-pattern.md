---
type: concept
title: "Pattern: Continuous Configuration Synchronization"
description: Repeatedly and automatically reapplying server configuration code on a schedule, whether or not the code has changed, to catch and revert drift as soon as it appears.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 12"
---

Continuous configuration synchronization (also called *scheduled server configuration update*) reapplies configuration code to a server repeatedly and frequently, regardless of whether the code has changed. It exists because servers change in ways beyond your control even when the code doesn't: someone logs in and makes a small manual fix; a package repository serves an updated version of something you install; a value from a [configuration registry](configuration-registry.md) changes upstream. Reapplying on a schedule catches and reverts any such divergence quickly, rather than letting it silently accumulate as [configuration drift](configuration-drift.md).

Most server configuration tools (Ansible, Chef, Puppet) are designed with this pattern in mind, and it's generally easier to implement than the main alternative, [immutable servers](immutable-server-pattern.md), since updating an existing instance is quicker and less disruptive than replacing it. The risk is that any automatic, fleet-wide reapplication can also break things at scale, so this pattern depends on solid monitoring and on delivering code changes through tested [pipeline stages](infrastructure-delivery-pipeline.md) before they reach production. Implementations typically stagger run times across a fleet so servers don't all wake up and reapply at once.

This pattern is the direct antidote to the [apply on change antipattern](apply-on-change-antipattern.md) and the mechanism that breaks the [automation fear spiral](automation-fear-spiral.md): frequent, reliable reapplication is what builds the confidence to run automation unattended in the first place. Frequent, routine patching is a natural side effect — teams that reapply code weekly or daily often find security patches already rolled out before anyone asks about a newly disclosed vulnerability.
