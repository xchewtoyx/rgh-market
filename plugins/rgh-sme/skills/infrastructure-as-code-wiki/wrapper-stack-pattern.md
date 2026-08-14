---
type: concept
title: "Pattern: Wrapper Stack"
description: Giving each stack instance its own thin stack project that only sets parameter values and imports a shared module containing the real infrastructure code.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

A wrapper stack uses a separate, minimal [infrastructure stack](infrastructure-stack.md) project per instance, whose only job is to set parameter values and import a shared code module (see [infrastructure DSLs and modules](infrastructure-domain-specific-languages.md)) that defines the actual infrastructure. This lets a team use the stack tool's own module versioning, dependency management, and artifact repository to promote infrastructure code through a [delivery pipeline](infrastructure-delivery-pipeline.md) — something most stack tools don't otherwise support at the whole-project level — and it lets the logic for provisioning and configuring a stack live in the same language used to define infrastructure, rather than a separate scripting language as with [scripted parameters](scripted-parameters-pattern.md).

The cost is an extra layer of indirection between the wrapper and the module it imports, and a temptation to add custom, per-instance logic into individual wrapper projects, which reintroduces the inconsistency of the [copy-paste environments antipattern](copy-paste-environments-antipattern.md) if left unchecked. Because parameter values live in wrapper projects under version control, this pattern isn't suitable for secrets on its own — pair it with an approach from [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md). Terragrunt is an example of a tool built around this pattern.
