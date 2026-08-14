---
type: concept
title: "Pattern: Micro Stack"
description: Splitting the infrastructure for a single service across multiple stacks, typically along life-cycle boundaries, so pieces that change at different rates can be managed independently.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

The micro stack pattern divides the infrastructure for one service across more than one [stack](infrastructure-stack.md) — for example, separate stacks for networking, compute, and a database — rather than keeping them all in a single [service stack](service-stack-pattern.md).

The usual motivation is that different pieces of a service's infrastructure have genuinely different life cycles: application servers might be rebuilt from a fresh [server image](server-image-as-code.md) every week, while the database's storage volume changes rarely and holds state that must survive rebuilds. Splitting these into separate stacks means the fast-changing piece can be torn down and recreated aggressively — as with a [persistent or ephemeral test stack](persistent-vs-ephemeral-test-stacks.md) — without disturbing the slow-changing, stateful piece. See [aligning boundaries with component life cycles](drawing-boundaries-between-infrastructure-components.md) for the general principle.

The cost of micro stacks is added moving parts: more stacks to provision, more [dependencies to discover and integrate across stack boundaries](resource-matching-pattern.md), and more pipelines to maintain. Micro stack is the opposite end of the sizing spectrum from a [monolithic stack](monolithic-stack-antipattern.md).
