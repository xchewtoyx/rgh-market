---
type: concept
title: Continuous Integration
description: >
  Team members integrate work into a shared mainline at least daily, with every
  integration verified by an automated build and test run, so integration
  errors surface within minutes rather than accumulating for weeks.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 3"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Continuous Integration

Continuous Integration (CI) is primarily a **social practice**, not a tool:
the team agrees that fixing a broken build takes priority over any new feature
work. The tooling (a CI server) exists to enforce and make visible whether the
team is honoring that agreement.

## Prerequisites

- A shared version-control repository every developer commits against.
- A single-command automated build: compile, test, inspect, package.
- A fast automated unit-test suite that validates correctness on every commit.
- Team agreement that a broken build is the team's top priority.

## Essential practices

1. Commit to mainline at least once a day, ideally more often — small commits
   keep merge conflicts small. See
   [trunk-based development](trunk-based-development.md).
2. Never commit on top of a build that is currently broken.
3. When a build breaks, stop other work and fix it within minutes (rule of
   thumb: 10 minutes) — or revert the offending commit immediately if a fast
   fix isn't available. Never leave mainline broken while working on something
   else.
4. Run the fast unit-test suite locally before committing.
5. After committing, watch the CI server's result for that commit rather than
   assuming it passed.
6. Never comment out or delete a failing test to make the build green — that
   destroys the suite's ability to catch the regression it just caught.

## CI server flow

The CI server watches version control for new commits (webhook or polling),
checks out a clean copy, runs the single-command build script (compiling,
running unit tests, running static analysis), collects results, and publishes
pass/fail status plus archived binary artifacts. This is the automation
underneath the [commit stage](commit-stage.md) of the
[deployment pipeline](deployment-pipeline.md).

## Extreme feedback

Broadcasting build status via ambient signals (build lights, audible alerts,
dashboards visible to the whole team) makes a broken build impossible to
ignore, reinforcing practice 3 above.

## Failure mode this prevents

See [integration hell](integration-hell.md) for what happens when integration
is deferred instead of continuous.

## Terminology: CI vs. "CI+"

Plain development usage of "continuous integration" often means only "merge
to trunk frequently and pass unit tests." Some sources use a stricter
definition — sometimes labeled "CI+" — that also requires running on a
production-like environment and passing acceptance/integration tests before
a change counts as integrated. When a source's "continuous integration"
claims seem to already cover what this bundle treats as a separate
[automated acceptance testing](automated-acceptance-testing.md) gate, this
terminology difference is usually why — check which definition is in play
rather than assuming the two always mean the same scope.

## Restoring green: the Andon cord

The specific discipline of stopping work the moment the build breaks, and
what happens if a team doesn't sustain it, is developed further in
[Andon cord discipline](andon-cord-discipline.md).

## Broader ecosystem integration

For distributed and microservice systems, dependencies extend beyond the
immediate repository — upstream services, ingested data, ML models, OS/runtime
changes, devices, and platform APIs. CI in that world is the continuous
assembling and testing of the **entire evolving ecosystem**, not only unit
tests on one repo. From a testing perspective, CI informs which tests run when
and how to compose the system under test at each stage, balancing fidelity
against setup cost — presubmit SUTs generally must not call real production
backends; staging often can. See [presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md)
and [hermetic testing](hermetic-testing.md).

The benefit is verifiable, timely proof that the application can progress to
the next pipeline stage — not merely hoping contributors were careful. Fast
feedback loops stack from local edit-compile-debug through presubmit,
postsubmit, staging, and production; [CI as alerting](ci-as-alerting.md)
frames how strictly each loop must stay green.
