---
type: concept
title: Infrastructure Delivery Pipeline
description: An automated sequence of pipeline stages that tests and promotes a version of infrastructure code from commit through to production, without manual intervention beyond review and approval.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 8, ch. 19"
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 5"
---

An infrastructure delivery pipeline implements [progressive testing](progressive-testing-for-infrastructure.md) together with the promotion of code across the path to production. Every change pushed to the source repository moves automatically through a series of stages, each of which may have a *trigger* (what starts it — an upstream push, a prior stage passing, or a manual approval), an *activity* (what it does — apply code, run tests, destroy a stack), an *approval* mechanism (automatic pass/fail, or a human sign-off, sometimes doubling as a governance checkpoint), and *output* (artifacts, reports).

People may review changes and conduct exploratory testing, but should not run commands by hand to apply changes or pick configuration on the fly — those decisions belong in code, executed by the pipeline, so the process is carried out identically every time. When a downstream stage finds an error, the fix goes back to the start of the pipeline as a new run, rather than being patched in place partway through — this guarantees every change that reaches production has gone through every stage, unmodified. See [applying code from a centralized service](applying-code-from-a-centralized-service.md) for why the pipeline, not a person's workstation, should be the only thing that ever applies code to a shared instance.

Three measures indicate whether a pipeline is actually doing its job: **cycle time** — how fast a change can move end to end, which rapid or several-times-daily delivery makes impossible if any stage requires mandatory human intervention or cross-team coordination; **traceability** — whether every artifact that produced a given deployed element (code, dependency versions, test results, the tooling itself) can be recovered after the fact, usually by recording version numbers for all of them in an artifact database, since a tooling error inside the pipeline can itself cause a production problem that needs tracing back; and **repeatability** — whether the same inputs reliably produce the same result, which is easy to lose without noticing (a build step that resolves a dependency to "latest" isn't repeatable, and neither is a test that mutates shared state without restoring it afterward, since it can corrupt a later run's results).

Pipeline tooling ranges from general-purpose build servers (Jenkins, TeamCity, GitHub Actions) retrofitted with pipeline features, to CD-native tools built around the pipeline concept directly (GoCD, ConcourseCI), to a handful of tools built specifically for infrastructure (Atlantis, Terraform Cloud) that provide narrower functionality than a general pipeline. See [GitOps](gitops.md) for a variation of this delivery model built around continuously reconciling against a source branch rather than triggering discrete pipeline runs, and [governance in a pipeline-based workflow](governance-in-pipeline-based-workflow.md) for how a pipeline changes where and how compliance gets enforced.
