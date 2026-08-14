---
type: concept
title: Infrastructure Dependency Patterns
description: Facade, Adapter, and Mediator patterns for how a high-level infrastructure module consumes a low-level one, chosen by how much schema translation or cross-tool orchestration the dependency actually needs.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 4"
---

Infrastructure dependencies should flow one way — from high-level resources (compute, databases, application runtimes) down to the low-level resources they need (networks, storage) — the same [no-circular-dependencies rule](infrastructure-component-coupling-and-cohesion.md) that applies to any infrastructure component. High-level modules should retrieve what they need from low-level modules' published outputs (Inversion of Control), communicating through an explicit abstraction — output attributes, module outputs, or state/API lookups — rather than a hardcoded implementation detail (the Dependency Inversion Principle); passing the resolved value in as an input argument, rather than having the high-level module reach out and discover it itself, is [dependency injection](dependency-injection-for-infrastructure.md).

Three structural shapes for the dependency itself, in increasing order of what they need to bridge:

- **Facade** — the low-level module exposes a simple, direct set of outputs (a network module exporting `vpc_id` and `subnet_id`) that the high-level module consumes as-is. Lowest effort, but does no schema translation — it only works when the two sides already agree on shape. This is the dependency-facing analogue of the [facade module pattern](facade-module-pattern.md), which wraps a single resource rather than a cross-module boundary.
- **Adapter** — translates one module's output schema into whatever shape a dependent module or a different cloud provider actually expects — for example, converting a subnet CIDR into an explicit list of host addresses for a legacy firewall rule format, or reshaping one cloud's networking output to match another cloud's expected input. This decouples real schema or multi-cloud mismatches at the cost of extra code to build and maintain.
- **Mediator** — centralizes dependency-graph resolution, ordering, and lifecycle orchestration across many modules, rather than leaving each pair of modules to wire itself up. A stack tool's own built-in DAG execution (Terraform, CloudFormation) is a mediator for dependencies *within* its scope; a custom orchestration script coordinating across tools — provisioning a Kubernetes cluster with Terraform, then triggering Helm deployments — is a mediator *across* tools, similar in spirit to a [wrapper script](wrapper-scripts-for-infrastructure-tools.md) but focused specifically on sequencing dependent systems rather than a single tool's parameters.

Pick Facade for straightforward, single-tool, schema-compatible dependencies; Adapter when schemas or providers genuinely mismatch; Mediator when orchestration spans multiple tools or a genuinely complex multi-tier dependency graph — each step up this list trades more implementation and troubleshooting effort for more decoupling and a smaller blast radius per component.
