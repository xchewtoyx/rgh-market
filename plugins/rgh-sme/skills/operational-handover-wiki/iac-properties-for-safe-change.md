---
type: concept
title: Infrastructure-as-Code Properties for Safe Change
description: Four properties — reproducibility, idempotency, composability, and evolvability — that make infrastructure code safe for an unfamiliar operator to change without first understanding everything about it.
sources:
  - title: "Infrastructure as Code, Patterns and Practices"
    resource: "Infrastructure as Code, Patterns and Practices (Wang), ch. 1"
---

Four properties of well-written infrastructure code determine how safely a newcomer can change it, independent of how well the surrounding prose documentation explains it:

- **Reproducibility**: the same code deploys a clean environment identically every time. A new operator can create a disposable copy of the real system (test, staging, disaster-recovery) to learn on or validate a change against, without touching production — see [Phoenix Server Pattern](phoenix-server-pattern.md).
- **Idempotency**: re-running the same automation converges to the same end state rather than duplicating or corrupting resources. This means a nervous or uncertain operator can safely re-apply a change if they're not sure it took effect, instead of that uncertainty itself being a risk.
- **Composability**: infrastructure is decoupled into modules with clean interfaces (network, servers, load balancer as separate swappable pieces), so a change to one module doesn't require understanding or touching the others. This directly answers "what's safe to touch" — the module boundary is the safety boundary, and it's what keeps most real-world changes [local rather than nonlocal or architectural](change-scope-classification.md).
- **Evolvability**: code avoids hardcoding so the system can grow or change shape later with low risk — for example, exposing abstract outputs rather than baking in a specific provider's identifiers, so a downstream change doesn't ripple back through everything upstream of it.

## Why This Matters for Handover

These are the infrastructure-specific version of [Reducing Documentation Need Through System Design](reducing-documentation-need-through-system-design.md): rather than writing a longer runbook explaining how to change the system carefully, structure the code itself so an unfamiliar operator's mistakes are contained (composability), reversible (idempotency), and testable in isolation (reproducibility) before they ever touch production.

## Out-of-Band Changes Must Be Backported

A related discipline: when an operator makes an emergency manual fix directly against running infrastructure (an out-of-band change) rather than through the normal code-and-deploy path, that fix must be backported into the infrastructure code and committed immediately afterward. Skipping this step is exactly how a [snowflake server](snowflake-servers.md) forms — the emergency fix becomes an undocumented deviation between what the code says and what's actually running, discoverable only by the next person who assumes the code is the truth and gets surprised.
