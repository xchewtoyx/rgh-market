---
type: concept
title: Roll-Forward Remediation
description: Restoring infrastructure after a bad change by committing a new, corrective change and letting the pipeline apply it forward, rather than attempting a declarative-engine "undo."
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 11"
---

Declarative infrastructure engines don't have a real "undo" operation in production — there's no procedural inverse of an apply to run. Restoring a known-good state after a bad change means committing a new revert commit that reintroduces the previous code, advancing version history forward, and letting the [delivery pipeline](infrastructure-delivery-pipeline.md) apply that reverted version like any other change — "rolling forward" to the old state rather than rolling backward to it. This keeps the rule that a change is only ever delivered by pushing new code through the pipeline from the start, the same discipline behind [fixing a downstream pipeline failure by re-pushing from the start](infrastructure-delivery-pipeline.md) rather than patching a stage in place.

When stateful data or a complex dependency graph makes a direct code revert unsafe — reverting the code might not cleanly reverse a schema change or a data migration that already happened — the roll-forward move instead deploys a clean replacement environment (via [blue-green](blue-green-infrastructure-change.md) or a canary rollout) and decommissions the failing one, rather than trying to mechanically undo the specific change that caused the problem.

The immediate priority in an incident is restoring availability for users, not diagnosing the root cause — stabilize first with whichever roll-forward option applies, then investigate. See the [three D's troubleshooting framework](three-ds-troubleshooting-framework.md) for a structured way to find that root cause once the system is stable again.
