---
type: concept
title: "Pattern: Stack Configuration Files"
description: Managing per-instance stack parameter values in dedicated files committed to version control with the stack code, one file per environment.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

Stack configuration files hold [instance parameter](stack-parameter-design-principles.md) values in a separate file per environment (`test.properties`, `staging.properties`, `production.properties`), version-controlled alongside the stack code. Because the file is committed, it's easy to answer "what's the maximum cluster size for production", trace when a value changed and why, and audit who changed it. The pattern also enforces separation of configuration from code, since the files can't contain logic — only values.

It fits well when the set of environments doesn't change often; creating a new instance means adding a new file, which rules out spinning up environments dynamically without extra tooling (see the [ephemeral test stack pattern](persistent-vs-ephemeral-test-stacks.md) for where that limitation bites). With multiple stacks, configuration files can be organized either alongside each stack project or centralized by environment — both arrangements get messy at scale in different ways: per-stack files scatter changes that touch a whole environment, and centralized-by-environment files bury a single stack's values in a directory full of unrelated stacks' configuration.

Secrets must not go into these files if they're committed to source control; keep secret values in a separate, uncommitted configuration file layered on top, or use one of the other approaches in [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md). The main alternative that avoids this pattern's "new environment needs a new file" friction is the [stack parameter registry pattern](stack-parameter-registry-pattern.md).
