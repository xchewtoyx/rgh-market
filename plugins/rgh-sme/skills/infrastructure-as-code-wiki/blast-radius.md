---
type: concept
title: Blast Radius
description: The scope of infrastructure that a single change or command could affect — directly, the code included in that command's run, and indirectly, everything downstream that depends on it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

The immediate blast radius of a change is the scope of code that the command applying it touches — for example, everything in a Terraform project when you run `terraform apply`. The indirect blast radius extends further, to anything else in the system that depends on resources within that direct scope and could be affected if they break.

Blast radius is the central reason infrastructure design keeps coming back to splitting large [stacks](infrastructure-stack.md) into smaller ones: a bigger stack has a bigger blast radius, so a mistake or unexpected interaction has more to break, and every change to it — even a change that's obviously safe in isolation — carries the risk of everything else sharing that stack. This is the core objection to the [monolithic stack antipattern](monolithic-stack-antipattern.md) and to the [multiple-environment stack antipattern](multiple-environment-stack-antipattern.md), and the core motivation for the [service stack](service-stack-pattern.md) and [micro stack](micro-stack-pattern.md) patterns, which align stack boundaries to limit what any one change can touch.

Minimizing blast radius is also a factor when [drawing boundaries between infrastructure components](drawing-boundaries-between-infrastructure-components.md) more generally, and when deciding whether shared, cross-cutting infrastructure (like a shared network stack many application stacks depend on) is worth the coupling it introduces.
