---
type: concept
title: Self-Service Deployment Capability
description: >
  Structuring build, test, and deploy as independently accessible
  capabilities anyone authorized can trigger on demand, so deployment doesn't
  require a specialist operator or a ticket queue.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
---

# Self-Service Deployment Capability

Developer self-deployment capability tends to erode over time as
organizations add oversight for security and compliance reasons, typically
by routing all deployments through a separate operations team as a
[separation-of-duties](compliance-through-pipeline-automation.md) control.
That control can be achieved without a deployment bottleneck by structuring
three capabilities so each is independently self-service:

- **Build**: the pipeline packages a deployable artifact from version
  control, for any environment including production — see
  [build once, deploy everywhere](build-once-deploy-everywhere.md).
- **Test**: anyone can run any part of the automated test suite locally or
  against a test system on demand — see
  [independent testability](independent-testability.md).
- **Deploy**: anyone with the right authorization can deploy a
  version-controlled artifact to any environment they're authorized for,
  via [version-controlled deployment scripts](deployment-script-design.md),
  without waiting on a specialist to act on their behalf.

Once every deployment automatically produces the audit trail described in
[compliance through pipeline automation](compliance-through-pipeline-automation.md)
— who deployed what, when, and what tests it passed — *who* physically
triggers the deployment stops being where risk control needs to live, and
the control moves to what the pipeline requires before it will deploy
anything at all (a passing test suite, an authorized identity) rather than to
who's allowed to press the button.
