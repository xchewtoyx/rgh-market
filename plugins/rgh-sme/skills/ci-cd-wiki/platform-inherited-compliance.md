---
type: concept
title: Platform-Inherited Compliance
description: >
  Implementing regulatory controls once at the shared delivery-platform level
  so every application built on it inherits them automatically, instead of
  each application separately proving compliance from scratch.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 6"
---

# Platform-Inherited Compliance

Federal compliance frameworks (e.g. FISMA/NIST RMF) can require validating
hundreds of individual security controls per system — a process that
historically took months to over a year after a system was otherwise
dev-complete. 18F's `cloud.gov` platform (a PaaS built on Cloud Foundry)
demonstrated an alternative: build the platform itself to satisfy the bulk of
the controls (269 of 325, in that case), so any application deployed on top
of it inherits those controls automatically rather than re-proving them
individually. The remaining application-specific controls are what actually
still needs per-system review, shrinking a months-long process to weeks.

This generalizes beyond regulatory compliance: any control that can be
satisfied structurally by the shared platform or pipeline — encryption at
rest, audit logging, network segmentation, patched base images — should be,
because it converts an assessment every team has to repeat into an assessment
performed once and inherited by everyone building on that platform. It's the
same leverage argument as
[compliance through pipeline automation](compliance-through-pipeline-automation.md):
push controls down into automated infrastructure the pipeline and platform
themselves guarantee, rather than relying on each team re-implementing (and
re-auditing) them independently.
