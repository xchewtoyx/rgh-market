---
type: concept
title: Idempotent Provisioning
description: >
  A configuration-management script is idempotent if running it any number of
  times converges the system to the same end state without duplicate side
  effects or errors, which is what makes automated re-provisioning safe.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 11"
---

# Idempotent Provisioning

Idempotence is the property that lets environment automation be re-run freely
— to fix drift, to rebuild a [phoenix server](phoenix-server.md) from scratch,
or to provision a fresh [ephemeral test environment](ephemeral-test-environments.md)
— without worrying about whether the target already has some of the desired
state applied. A non-idempotent script might, for example, fail on a second run
because it tries to create a directory or user that already exists, or silently
duplicate a configuration entry each time it runs.

Configuration-management tools (Puppet, Chef, CFEngine, Ansible) are built
around idempotence by design: their primitives describe desired end state
("this package is installed," "this file has this content") rather than
imperative steps, so re-applying a definition is safe and converges rather than
compounds.

## Verifying idempotence automatically

Idempotence shouldn't be an assumed property — it should be an automated
pipeline check, exactly like any other test: run the provisioning script,
then immediately run it again against the same target, and assert the second
run reports zero changes and zero failures. A second run that reports any
change means the script isn't actually idempotent, and that gap should fail
the pipeline the same way a failing unit test would. See
[testing infrastructure code as a pipeline stage](infrastructure-code-testing-in-pipeline.md)
for where this check fits among the other infrastructure-code checks.

## Where convergence stops being the right model

Convergent, idempotent tooling assumes every intermediate state on the way
to convergence is acceptable to sit in. That assumption breaks for processes
with a mid-flight invariant — a live database cutover that must never leave
clients without access, for instance — where
[direct orchestration](direct-orchestration-for-stateful-cutovers.md) of an
explicit step sequence is the better fit than declaring a desired end state
and letting a convergence engine find its own path there.
