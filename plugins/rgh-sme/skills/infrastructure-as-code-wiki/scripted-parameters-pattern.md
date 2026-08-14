---
type: concept
title: "Pattern: Scripted Parameters"
description: Hardcoding per-instance stack parameter values into a version-controlled script that runs the stack tool, rather than typing them by hand each time.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

Scripted parameters hardcode the values for each [stack instance](stack-parameter-design-principles.md) into a script — either one script per environment, or a single script that branches on an environment argument — and commit that script to version control alongside the stack it provisions. This avoids the unreliability of the [manual stack parameters antipattern](manual-stack-parameters-antipattern.md): values are used consistently every time, and every change to them is tracked.

It's a good fit for a fixed set of environments that doesn't change often, and needs no extra moving parts beyond the script itself. The trade-off is that provisioning scripts tend to accumulate complexity over time, especially as more parameters and edge cases pile up — see [wrapper scripts for infrastructure tools](wrapper-scripts-for-infrastructure-tools.md) for how to keep them maintainable. Secrets must never be hardcoded into these scripts; combine this pattern with a secrets-handling approach from [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md), such as fetching a value from a secrets manager at run time.

Committing the script into the same project as the stack it provisions keeps the two in sync — when a parameter is added to the stack code, it's added to the script in the same change, so there's never ambiguity about which script version goes with which stack version.
