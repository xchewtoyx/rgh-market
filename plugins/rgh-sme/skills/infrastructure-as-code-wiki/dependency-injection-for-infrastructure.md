---
type: concept
title: Dependency Injection for Infrastructure
description: Separating a stack's core definition code from the mechanism used to discover its dependencies, by having an external script pass discovered values in as ordinary parameters.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 17"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 7, ch. 8"
---

However a [cross-stack dependency is discovered](resource-matching-pattern.md) — by [resource matching](resource-matching-pattern.md), [stack data lookup](stack-data-lookup-pattern.md), or [integration registry lookup](integration-registry-lookup-pattern.md) — embedding that discovery logic directly in a stack's definition code mixes two concerns: what the stack actually needs (a VLAN to attach a server to) and how to go find it. This coupling adds cognitive overhead even when it doesn't block anything, and it makes the stack harder to test in isolation and harder to reuse in a different context, since its code is now tied to one specific discovery mechanism.

Dependency injection (DI) — the same idea from object-oriented software design, applied here — has the stack declare what it needs as an ordinary [instance parameter](stack-parameter-design-principles.md), and pushes the responsibility for discovering the actual value out to an external orchestration script (see [wrapper scripts for infrastructure tools](wrapper-scripts-for-infrastructure-tools.md)). The script can use any discovery pattern, or a completely different value, and passes the result in like any other parameter.

This keeps the stack's own code simpler and more broadly reusable: on a laptop, or against a local mock, the injected value can be trivial; in a more production-like environment, it can come from a fully realized provider stack. It also makes [progressive testing](progressive-testing-for-infrastructure.md) easier, because different discovery sources — including [test fixtures](test-fixtures-for-infrastructure-stacks.md) — can be swapped in at different pipeline stages without touching the stack's own code.

A single-run version of the same idea shows up inside server-configuration tools that provision compute and then immediately configure it in one execution: after a task creates a new instance, its freshly-assigned identity (IP address, name) and any values discovered about it are added directly into the tool's in-memory inventory for the rest of that run, along with whatever connection variables the following configuration steps need — rather than the configuration steps hardcoding how to go find that instance themselves. This is the same separation-of-concerns benefit dependency injection provides at the pipeline level, just collapsed into a single run: the configuration steps that follow only see an injected host with parameters, with no knowledge of — or coupling to — whichever [provisioning mechanism](evaluating-third-party-infrastructure-modules.md) or cloud API actually created it, which is exactly what keeps the same configuration code reusable [across different provisioning backends](multicloud-strategies.md).
