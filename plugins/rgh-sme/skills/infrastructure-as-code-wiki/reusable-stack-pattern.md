---
type: concept
title: "Pattern: Reusable Stack"
description: An infrastructure stack source project used, unmodified, to create and update multiple independent stack instances — the primary pattern for building consistent environments and production replicas.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 6"
---

A reusable stack is a single [infrastructure stack](infrastructure-stack.md) source project applied to more than one instance, rather than being copied or combined with other environments. Running the stack tool against the project, with a different instance identifier each time, either creates a new instance or reconciles an existing one to match the code — the same version of the code producing consistent, comparable instances for test, staging, production, or per-customer deployments.

Reusable stacks are the fix for both stack-and-environment antipatterns: they avoid the shared [blast radius](blast-radius.md) of the [multiple-environment stack antipattern](multiple-environment-stack-antipattern.md), because each instance is separate, and they avoid the drift of the [copy-paste environments antipattern](copy-paste-environments-antipattern.md), because there's only one copy of the code to edit and test.

The pattern requires two other things to work well: a way to vary a stack instance slightly without duplicating its code (see [stack parameter design principles](stack-parameter-design-principles.md) and the family of [patterns for configuring stack instances](stack-configuration-files-pattern.md)), and confidence from testing the code before applying it to a business-critical instance (see [progressive testing for infrastructure](progressive-testing-for-infrastructure.md)). Reusable stacks should be the default, workhorse pattern for managing infrastructure at any nontrivial scale; the technique generalizes to [building environments from multiple reusable stacks](environment-vs-stack.md) when a system is too large for a single stack.
