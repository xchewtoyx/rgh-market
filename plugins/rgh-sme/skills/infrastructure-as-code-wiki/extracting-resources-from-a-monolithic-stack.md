---
type: concept
title: Extracting Resources from a Monolithic Stack
description: A safe order and state-migration procedure for breaking a monolithic infrastructure codebase apart without destroying or recreating the live resources it already manages.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 10"
---

Breaking up a [monolithic stack](monolithic-stack-antipattern.md) is safest done in a specific order, from the edges of the dependency graph inward: first extract standalone high-level resources that nothing else depends on (a standalone DNS record); next extract dependent high-level resources (application clusters, database fleets), wiring their low-level dependencies back in explicitly via [dependency injection](dependency-injection-for-infrastructure.md) rather than leaving them hardcoded; and only last extract the foundational low-level resources (networks, subnets, storage) that everything else was built on top of, once nothing still references them directly from within the monolith.

Physically moving a resource's *management* from the monolith's state into a new module's state, without touching the real underlying resource, is a state-migration operation, not a resource change: copy the resource's code into the new module with updated inputs; transfer ownership of the live resource between state files (Terraform's `terraform state mv` or `terraform import`, or the declarative [`moved` block](safe-infrastructure-refactoring-with-moved-blocks.md)); confirm with a dry run on both the old and new module code that the plan shows zero additions, updates, or destructions — proof the extraction changed nothing about the real infrastructure; and only then delete the old code and state reference from the monolith.

This is a concrete, ordered procedure for reaching the split-stack designs described by [drawing boundaries between infrastructure components](drawing-boundaries-between-infrastructure-components.md) and the [micro stack pattern](micro-stack-pattern.md), starting from an existing monolith rather than designing the split from scratch.
