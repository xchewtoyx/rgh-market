---
type: concept
title: Persistent vs Ephemeral Test Stack Instances
description: The trade-off between keeping a test stack instance running between pipeline runs (fast but prone to accumulating broken state) and recreating it every run (clean but slow).
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 9"
---

A **persistent test stack** stays running between test runs; each run applies the latest code as an update and leaves the resulting instance in place for next time. It's much faster than rebuilding from scratch, which speeds up the whole pipeline's feedback loop — but it's prone to becoming "wedged": a failed change can leave the instance in a state where further applies also fail, sometimes so badly the tool can't even destroy it to start over. Breaking [stacks](infrastructure-stack.md) into smaller, simpler pieces with fewer inter-stack dependencies (per [drawing boundaries between infrastructure components](drawing-boundaries-between-infrastructure-components.md)) tends to lower how often this happens.

An **ephemeral test stack** creates a fresh instance for every run and destroys it afterward, guaranteeing a clean environment with no leftover cruft from a previous run — at the cost of provisioning time added to every single feedback cycle, which only fits changes infrequent enough (or infrastructure fast enough to provision) to tolerate the delay.

Combining both by running every change through parallel persistent and ephemeral stages (nicknamed *dual persistent and ephemeral stack stages*, or the *nightly rebuild antipattern*) is tempting but usually combines the disadvantages of both rather than their advantages: the team still has to manually fix a wedged persistent instance, while also paying for and waiting on the slower ephemeral stage — and it costs roughly double the infrastructure. Two milder variations split the difference: **periodic stack rebuild** keeps a persistent instance but tears it down and rebuilds it on a schedule (useful mainly for cost control or clearing accumulated resource usage, and a poor substitute for fixing whatever makes updates unreliable); **continuous stack reset** rebuilds the instance out-of-band immediately after every passing test run, trading some visibility (a background rebuild can quietly fail without turning the pipeline red) for both fast feedback and a clean slate each time, and for a pipeline that faithfully exercises the same update path production will actually go through.
