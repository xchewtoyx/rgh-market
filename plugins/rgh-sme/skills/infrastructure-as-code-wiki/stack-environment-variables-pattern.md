---
type: concept
title: "Pattern: Stack Environment Variables"
description: Setting stack instance parameter values as environment variables that the stack tool or its code reads, rather than passing them on the command line.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

This pattern sets [stack instance](stack-parameter-design-principles.md) parameter values as environment variables before running the stack tool, either read directly by the stack code or passed through by an orchestration script. It's easy to implement because nearly every platform and tool supports environment variables, and teams already using them elsewhere in their system find it a natural fit.

It's not a complete solution on its own — something still has to set those environment variables, so it's normally paired with another pattern such as [scripted parameters](scripted-parameters-pattern.md) or [pipeline stack parameters](pipeline-stack-parameters-pattern.md). Referencing environment variables directly from stack code also couples that code to its runtime environment; reading the variables in an orchestration script and passing the values through as ordinary stack parameters keeps the stack code portable. Setting secrets as environment variables can also expose them to other processes on the same machine, so this pattern needs care when used for [secrets](handling-secrets-in-infrastructure-code.md).
