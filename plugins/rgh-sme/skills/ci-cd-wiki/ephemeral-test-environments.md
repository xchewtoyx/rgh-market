---
type: concept
title: Ephemeral Test Environments
description: >
  Test environments provisioned automatically and torn down after use, so every
  pipeline run tests against a clean, known-good copy of the target environment
  rather than one whose state has accumulated from prior runs.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2, 5"
  - title: "Terraform: Up & Running"
    resource: "Terraform: Up & Running, 3rd ed. (Yevgeniy Brikman), ch. 9"
---

# Ephemeral Test Environments

Using virtual machines or [container images](container-image-as-pipeline-artifact.md),
a [deployment pipeline](deployment-pipeline.md)
stage can spin up an isolated environment on demand, deploy the candidate into
it, run its tests, and tear it down afterward. This depends on
[idempotent provisioning](idempotent-provisioning.md): the environment has to
be reproducible from automation alone for spinning up a fresh copy to be
cheap and reliable.

The payoff is that "deploy to a clean copy of the target environment" becomes
routine rather than exceptional — a stale environment can't cause a false pass
or false fail, because there is no persistent environment state to go stale.
This is what makes it safe to run acceptance, capacity, and nonfunctional test
stages in parallel without them contaminating each other's results.

## Teardown has to be defensive, not just present

When the ephemeral environment is real billed cloud infrastructure rather
than a local container, a crashed test run or an interrupted pipeline job
can skip the teardown step entirely, leaving orphaned resources that quietly
accumulate cost — the ephemeral-environment pattern only holds if teardown
is guaranteed, not merely attempted. Two complementary safeguards: run
teardown as a deferred/`finally`-style step tied to the test process itself
rather than a separate pipeline step that a crash can skip, and run an
independent scheduled sweep that finds and destroys anything matching the
test-environment naming convention older than some threshold, as a backstop
for whatever the first mechanism misses. Namespacing every test run's
resources uniquely (e.g. a run ID in the resource name) makes both of these
safe to run concurrently across parallel test runs without colliding.
