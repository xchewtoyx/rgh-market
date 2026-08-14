---
type: concept
title: Pre-Tested Commit
description: >
  A workflow where a change is tested automatically by the CI server in a
  staging queue or branch and merged into mainline only if it passes, so
  mainline is structurally protected from ever going red.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 7"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 11"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Pre-Tested Commit

Also known as a gated commit or merge queue. Instead of committing directly to
mainline and finding out afterward whether the [commit stage](commit-stage.md)
passes, the change is pushed to a staging area first; the CI server runs the
commit test suite against it there, and only merges it into mainline once it
passes.

This converts "don't check in on a broken build" from a
[continuous integration](continuous-integration.md) social rule that
developers must remember to follow into a structural property of the
workflow: mainline literally cannot receive a commit that fails the commit
stage, because the merge step itself is conditioned on a passing build.

## Presubmit checks

A refinement used at large scale: run some checks even before a change is
formally submitted for merging, as a **presubmit** step — both global checks
that apply to every change, and custom checks scoped to specific directories
or components, defined by the owners of that code. This pushes feedback
earlier than even a standard pre-tested-commit queue, catching problems
before they occupy a slot in the merge queue at all. Full treatment of what
belongs on presubmit versus postsubmit is in
[presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md).

Flaky presubmit tests are especially costly — see [CI as alerting](ci-as-alerting.md).
Teams may temporarily quarantine flaky tests from presubmit while investigating,
or allow multiple run attempts, but unreliability on the merge gate erodes the
same trust as a permanently red mainline.
