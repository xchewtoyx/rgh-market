---
type: concept
title: "Antipattern: Multiple-Environment Stack"
description: Defining and managing the infrastructure for several distinct environments as a single stack instance, so that a mistake affecting one environment can affect all of them.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 6"
---

A multiple-environment stack puts the code for several [environments](environment-vs-stack.md) — for example, test, staging, and production — into a single stack project managed as one stack instance. People often build this by accident: when learning a new stack tool, it feels natural to add a new environment into the existing project rather than starting a new one.

The problem is [blast radius](blast-radius.md): the scope of any update to the stack is everything in the instance, so a mistake or conflict anywhere threatens every environment sharing it — including production sitting in the same instance as a test environment that people expect to be able to break freely.

The fix is to divide environments into separate stacks. The naive way to do this is a separate stack project per environment — the [copy-paste environments antipattern](copy-paste-environments-antipattern.md) — but the better approach is the [reusable stack pattern](reusable-stack-pattern.md), where a single project defines the generic shape of an environment and is applied to a separate instance per environment, so the blast radius of any one apply is limited to that one instance.
