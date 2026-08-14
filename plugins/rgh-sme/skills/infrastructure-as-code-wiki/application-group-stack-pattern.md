---
type: concept
title: "Pattern: Application Group Stack"
description: A stack that provisions the infrastructure for several related applications or services together, as an intermediate step between a monolithic stack and per-service stacks.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

An application group stack groups the infrastructure for several related applications or services into a single [infrastructure stack](infrastructure-stack.md), so it's provisioned, tested, and destroyed as one unit. It fits well when a single team owns the deployment and infrastructure of all the grouped pieces, letting the stack's boundary align with the team's area of ownership — see [aligning boundaries with organizational structures](drawing-boundaries-between-infrastructure-components.md).

The cost is that it couples the pace and risk of change across everything in the group: every change, even one touching only a single service inside the stack, carries the [blast radius](blast-radius.md), provisioning time, and test scope of the whole group. It's inefficient if some of the grouped services change much more often than others.

An application group stack is often used as a stepping stone from a [monolithic stack](monolithic-stack-antipattern.md) toward a design where each service gets its own [service stack](service-stack-pattern.md) — and, left unchecked, it can also grow back into a monolith if the group keeps absorbing more unrelated services.
