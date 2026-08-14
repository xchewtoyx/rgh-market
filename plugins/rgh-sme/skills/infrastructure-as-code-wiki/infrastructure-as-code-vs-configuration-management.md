---
type: concept
title: Infrastructure as Code vs Configuration Management
description: Why provisioning tools and server-configuration tools emerged as historically separate tool categories, and how this bundle treats both as facets of one Infrastructure as Code discipline.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 1, ch. 11"
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 1"
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 1"
  - title: Continuous Delivery
    resource: "Continuous Delivery (Jez Humble, David Farley), ch. 2"
---

"Infrastructure as Code" and "configuration management" are sometimes used as if they name the same thing, and sometimes used to distinguish two different tool categories — Terraform, CloudFormation, Pulumi, and similar tools on one side; Ansible, Chef, Puppet, CFEngine, and Saltstack on the other. Both usages are defensible, because these really did emerge as separate tool categories solving different problems, even though this bundle (and the field generally) now treats both as part of one discipline.

**Configuration management tools came first.** CFEngine pioneered declarative, idempotent DSLs for installing packages and managing configuration files on a server that already existed — usually a physical machine in a rack, later a VM. Puppet and Chef followed the same model; Ansible later took an agentless, push-based approach to the same problem. These tools assume compute already exists and manage what's installed and configured *on* it: packages, config files, accounts, services. See [server configuration code](server-configuration-code.md) for what that code looks like.

**Provisioning tools emerged with dynamic, API-driven cloud platforms.** Terraform, CloudFormation, and similar tools create, update, and destroy the compute, storage, and networking resources themselves — the things configuration management tools had always assumed were already there. Their defining mechanism is a dependency graph computed from declared resources, plus a reviewable diff (a "plan") of exactly what will change before anything is applied.

A useful, durable way to keep the two apart: configuration management tools answer "what should be installed and set up on this compute instance," while provisioning tools answer "what compute, storage, and network resources should exist at all." Server templating tools (Packer, Docker) sit adjacent to both, baking the output of a configuration step into a reusable image that a provisioning tool then deploys — see [baking vs frying server configuration](baking-vs-frying-server-configuration.md). Orchestration tools (Kubernetes, Nomad) add a further layer that schedules workloads across already-provisioned compute — see [application clusters as code](application-cluster-as-code.md).

This bundle's own [definition of Infrastructure as Code](infrastructure-as-code.md) treats both categories under one umbrella deliberately: the shared premise — that you change a system by changing version-controlled code and letting automation test and apply it, rather than making the change by hand — holds regardless of whether what's being changed is a cloud resource or a package on a server. The three core IaC practices (define everything as code, continuously test and deliver, build small pieces) apply equally to a Terraform stack and an Ansible role.

Where the categories genuinely diverge is in their mechanics, and that's where the practical differences actually live — not in this note, but in the notes about each mechanism: [push vs pull server configuration](push-vs-pull-server-configuration.md) for how configuration code reaches a target, [baking vs frying server configuration](baking-vs-frying-server-configuration.md) for when configuration gets applied relative to instance creation, [declarative vs imperative infrastructure code](declarative-vs-imperative-infrastructure-code.md) for how each category's languages express desired state, and [infrastructure platform layers](infrastructure-platform-layers.md) for where each category's concerns sit relative to each other. What concrete assurance each category actually gives you before a change lands is covered separately in [change assurance mechanisms by tooling](change-assurance-mechanisms-by-tooling.md).
