---
type: concept
title: Wrapper Scripts for Infrastructure Tools
description: The custom scripting most teams write to orchestrate their infrastructure tools, and the design discipline needed to stop it becoming as complicated as the infrastructure code it supports.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 19"
---

Most teams end up writing custom scripts (Bash, Python, PowerShell, or a build tool like Make or Rake) to orchestrate their [stack](infrastructure-stack.md) and [server configuration](server-configuration-code.md) tools — assembling configuration values, resolving and fetching dependencies, packaging code for delivery, promoting it between stages, sequencing multiple stacks in dependency order, running the underlying tool with the right arguments, and setting up and tearing down tests. Left unchecked, this supporting code routinely grows at least as complicated as the infrastructure code it wraps, and teams end up spending more time debugging the wrapper scripts than improving the actual infrastructure.

The recurring cause is mixing concerns that should be kept separate. Practical guidance for avoiding this: split the script per life-cycle phase (build, promotion, apply) rather than one script that tries to do all three, with clear, contract-like boundaries for what passes between phases; separate the distinct *tasks* within a phase (assembling configuration, packaging, executing the tool) rather than tangling them together; decouple any script that orchestrates *across* multiple projects from the scripts that run tasks *within* a single project, so each project's tasks can still be run on their own; and keep wrapper code ignorant of what any specific project's infrastructure code actually does, so the same generic wrapper works for any project of a given shape.

Assembling configuration values is one of the more complex wrapper responsibilities in practice — resolving a hierarchy of shared, per-environment, and per-component defaults into a final value for a given instance gets messy quickly, whichever [configuration source](stack-parameter-design-principles.md) it draws from, and is a common source of confusing, hard-to-trace bugs. Wrapper scripts deserve the same engineering discipline as any other infrastructure code: tested, linted (`shellcheck` and similar), and designed with the same principles — [coupling, cohesion, and clear domain-oriented boundaries](infrastructure-component-coupling-and-cohesion.md) — that apply to infrastructure code generally.
