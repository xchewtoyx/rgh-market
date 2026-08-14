---
type: concept
title: Event-Driven Infrastructure as Code
description: Executing small, tightly-scoped infrastructure modules automatically in response to real-time operational events, rather than on a schedule or through a pipeline triggered by a code push.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 13"
---

Event-driven IaC runs a minimal, narrowly-scoped infrastructure module automatically in direct response to an operational system event — for example, auto-provisioning a firewall rule the moment a new application pod launches, rather than through a scheduled or manually-triggered pipeline run. Because these modules fire in real time and often in the critical path of some other operation, they need to be architecturally constrained in ways a normal pipeline-triggered stack doesn't have to be: touching a minimal number of resources, executing in seconds rather than minutes, and strictly [idempotent](idempotent-infrastructure-code.md), since the same event might legitimately fire more than once.

[GitOps](gitops.md) is best understood as a specific, narrower case of this general idea: it's event-driven IaC where the triggering event is specifically a Git commit, or a continuous-reconciliation service detecting drift between a source branch and an environment — the same continuous-application mechanism, just with a specific, code-centric event source rather than an arbitrary operational trigger.
