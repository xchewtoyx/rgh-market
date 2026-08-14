---
type: concept
title: Pipelines as Code
description: >
  Declaring pipeline tasks and their dependencies in code so an orchestration
  engine can interpret and run them, instead of configuring jobs by hand.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Pipelines as code is the practice underlying modern orchestration
([orchestration vs. plain scheduling](orchestration-vs-scheduling.md)):
an engineer declares tasks and their dependencies in code — typically
Python — and the orchestration engine interprets that declaration and runs it
against whatever compute resources are available, rather than a human
manually wiring up each job.

This is what makes pipeline definitions version-controllable, testable, and
deployable through the same review and CI process as application code (the
deployment and testing of that code is `ci-cd`'s concern; the pipeline design
expressed in it is this bundle's). It's also the precondition for automated,
tested deployment of pipeline changes — without pipelines as code, a change to
a job's dependency graph is a manual edit with no diff, no review, and no
rollback.
