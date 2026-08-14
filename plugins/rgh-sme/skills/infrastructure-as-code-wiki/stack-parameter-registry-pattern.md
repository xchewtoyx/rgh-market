---
type: concept
title: "Pattern: Stack Parameter Registry"
description: Storing stack instance parameter values in a central configuration registry that the stack tool queries at apply time, rather than in files or scripts bundled with the stack code.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

A stack parameter registry stores [instance parameter](stack-parameter-design-principles.md) values in a central [configuration registry](configuration-registry.md) rather than with the stack code; the stack tool fetches the relevant values for a given instance when it applies the code. This separates configuration from implementation — values can be set, viewed, and used by different tools and languages, which reduces coupling and lets a tool-agnostic registry double as a system of record (a lightweight CMDB) that's useful for reporting and auditing, especially in regulated contexts.

The trade-off is that the registry becomes an extra moving part and a dependency for provisioning: if it's unavailable, you may not be able to re-provision or update the stack, which is painful specifically in disaster-recovery scenarios where the registry sits on the critical path. Managing values in a separate system from the code that uses them also means changes happen in two places instead of one, adding coordination overhead.

Compared to [stack configuration files](stack-configuration-files-pattern.md), a registry lets other teams create new stack instances from a shared reusable project without needing to add files to that project themselves — useful when a team maintains infrastructure that other teams consume. A registry doubling as a stack parameter registry is often the same registry used to [discover dependencies across stacks](integration-registry-lookup-pattern.md) or to store [secrets](handling-secrets-in-infrastructure-code.md).
