---
type: concept
title: Environment vs Stack
description: The distinction between an environment (a conceptual collection of infrastructure serving a purpose, such as testing or a region) and a stack (the concrete code and tooling used to provision it).
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 6"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 7"
---

An environment is a collection of operationally related infrastructure resources organized around a purpose — supporting a test phase, or serving a geographic region — usually one of several environments each running an instance of the same system. A [stack](infrastructure-stack.md) is the concrete means of defining and managing a collection of infrastructure resources. You use one stack, or several, to *implement* an environment; the two concepts aren't the same thing, even though a simple system might implement one environment as exactly one stack instance.

There are two common reasons to run multiple environments: supporting a progressive delivery process (a *path to production* — test, staging, production), and running multiple independent production instances for fault tolerance, scalability, or segregation (for example, one environment per geographic region, or a dedicated environment for a customer with strict data-residency requirements).

Because environments are meant to run instances of the same system, consistency between them is one of the main reasons to adopt IaC in the first place: differences between environments risk problems that testing in one environment won't reveal in another. Some deliberate differences are unavoidable (environment sizing, naming, access privileges), which is why [stack instance configuration](stack-parameter-design-principles.md) exists — but the goal is to keep those differences minimal and explicit rather than incidental.

How you use stacks to build environments is a distinct design decision from [how you size a stack](monolithic-stack-antipattern.md) — see the [multiple-environment stack antipattern](multiple-environment-stack-antipattern.md), the [copy-paste environments antipattern](copy-paste-environments-antipattern.md), and the [reusable stack pattern](reusable-stack-pattern.md) that resolves both.

Server-configuration tools with a separate host-inventory concept give a concrete, minimal instance of this pattern: one version-controlled inventory file per environment (production, staging, dev), each mirroring the same tier/group structure but pointing at that environment's actual hostnames, run against the exact same set of playbooks and roles by passing the environment's inventory file at apply time. This is the [reusable stack](reusable-stack-pattern.md) idea applied where "stack" is a fixed playbook/role set and the environment-specific variation is pushed entirely into the inventory (and the [stack instance configuration](stack-parameter-design-principles.md) layered on top of it) — the same code runs everywhere, only the target list and its variables change.
