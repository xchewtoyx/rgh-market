---
type: concept
title: Testing Infrastructure Code as a Pipeline Stage
description: >
  Infrastructure-as-code (provisioning scripts, config-management definitions)
  should pass through pipeline stages analogous to application testing:
  syntax check, a real run to completion, an idempotence check, and a
  functional assertion — before being trusted for any environment.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 11"
---

# Testing Infrastructure Code as a Pipeline Stage

Infrastructure-as-code deserves the same pipeline discipline application code
gets, not a manual "looks right" review. Four checks, roughly analogous to
the [test automation pyramid](test-automation-pyramid.md)'s layers but
scoped to infrastructure:

1. **Syntax check**: fast, cheap validation that the configuration parses —
   catches formatting and structural errors before anything is actually run.
   This is the infrastructure equivalent of a compile step and belongs at the
   very start of the pipeline, the same place the
   [commit stage](commit-stage.md) puts compilation.
2. **Run to completion**: apply the configuration against a fresh, disposable
   target (a container or VM stood up specifically for the test, then torn
   down — see [ephemeral test environments](ephemeral-test-environments.md))
   and confirm it succeeds without errors.
3. **Idempotence check**: run it again immediately and confirm the second run
   reports zero changes and zero failures. This directly operationalizes
   [idempotent provisioning](idempotent-provisioning.md) as an automated,
   pass/fail pipeline assertion rather than an assumed property.
4. **Functional check**: assert that the thing the infrastructure code was
   supposed to accomplish actually happened — e.g. confirm a service the
   config installs is actually reachable, not just that the apply step
   reported success. A clean apply that doesn't produce a working system is
   still a failure.

## Matrix testing across target platforms

Where infrastructure code needs to support multiple OS versions or platforms,
running these four checks against each supported target in parallel —
using fresh, disposable containers per target rather than a single shared
long-lived test machine — catches platform-specific breakage the same way
[capacity test environment fidelity](capacity-test-environment-fidelity.md)
catches environment-specific performance problems: by testing against
something close enough to every real target to be predictive.
