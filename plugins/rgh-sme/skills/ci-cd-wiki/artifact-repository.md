---
type: concept
title: Artifact Repository
description: >
  A central, versioned store for both build outputs and cached third-party
  dependencies, used so the pipeline never depends on rebuilding artifacts or
  reaching an external repository at deploy time.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 2"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Artifact Repository

The artifact repository is where the [commit stage](commit-stage.md) publishes
every binary it produces, keyed by build/version, so that
[build once, deploy everywhere](build-once-deploy-everywhere.md) has somewhere
durable to promote artifacts from and to.

It serves a second purpose: caching third-party dependencies (libraries,
frameworks, OS packages) internally, rather than letting automated builds pull
directly from a public remote repository (e.g. Maven Central, npm) on every
run. Examples of this class of tool: Nexus, Artifactory.

## Why not build directly against public repositories

- **Determinism**: an external repository can change or remove a version out
  from under a build; a local cache pins exactly what was available when the
  build ran.
- **Availability**: builds must not fail because an upstream repository is
  unreachable.
- **Auditability**: every dependency actually used is traceable to a specific
  cached artifact rather than "whatever was upstream at build time."

Transitive dependencies should also be explicitly declared and version-locked
rather than left to float, so an upstream breaking change in a dependency's own
dependency cannot silently alter a build's behavior.

## Trusting third-party and open-source dependencies

How much scrutiny a cached third-party dependency needs before it's trusted
in a build scales with how much the pipeline actually trusts the people who
maintain it, the version control system it comes from, and whether that
project itself enforces something like
[mandatory code review](mandatory-code-review.md). If that trust is high,
pulling it in like any first-party dependency is reasonable. If it's lower,
review the dependency's own code before first import, and consider keeping
an internal copy and reviewing subsequent upstream patches rather than
pulling new versions in unreviewed. Regardless of trust level, monitor
imported dependencies for newly disclosed vulnerabilities and apply security
patches promptly — trust established at import time doesn't stay valid
forever.
