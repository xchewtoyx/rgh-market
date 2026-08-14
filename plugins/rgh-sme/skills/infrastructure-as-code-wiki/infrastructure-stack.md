---
type: concept
title: Infrastructure Stack
description: A collection of infrastructure resources defined, provisioned, and changed together as a unit using a stack management tool such as Terraform or CloudFormation.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

An infrastructure stack is a collection of infrastructure elements — a virtual machine, a disk volume, a subnet — that you define, provision, and update together, using a stack management tool (Terraform, CloudFormation, Azure Resource Manager, Pulumi, and similar). The stack's source code (a *stack project*) declares what the stack should contain; running the tool against a *stack instance* either creates it from nothing or reconciles it to match the current code, a process usually described as "applying" the code.

A stack is the closest thing infrastructure code has to an *architectural quantum* — an independently deployable unit with the cohesion needed to function on its own — and it is the primary unit of reuse, testing, and delivery for infrastructure code, more so than modules or libraries used within it (see [stack components vs stacks as components](infrastructure-component-coupling-and-cohesion.md)).

Stack code is written in either a [low-level or a high-level infrastructure language](low-level-vs-high-level-infrastructure-languages.md). How much to put in a single stack, versus splitting a system across multiple stacks, is a central design decision — see the spectrum from [monolithic stacks](monolithic-stack-antipattern.md) through [application group](application-group-stack-pattern.md), [service](service-stack-pattern.md), and [micro stacks](micro-stack-pattern.md), and the concept of [blast radius](blast-radius.md) that motivates keeping stacks small. A stack can also represent one or more [environments](environment-vs-stack.md) — see the [reusable stack pattern](reusable-stack-pattern.md) for how a single stack project produces multiple, independently managed stack instances.
