---
type: concept
title: Configuration Management (Delivery Discipline)
description: >
  The discipline of identifying, tracking, and controlling changes to every
  artifact a build, test, or deployment depends on, so the full state of the
  system is reconstructible from version control alone.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Configuration Management (Delivery Discipline)

In a continuous-delivery context, configuration management means everything
required to construct, test, provision, and deploy an application is checked
into version control — not just application source code. This is the "single
source of truth" principle: complete auditability and reproducible builds
depend on nothing relevant living only on someone's machine or a server's
undocumented state.

See [version control everything](version-control-everything.md) for what
specifically belongs in version control, and
[environment drift](environment-drift.md) /
[snowflake server](snowflake-server.md) for the failure mode this discipline
prevents.

## Configuration deserves the same rigor as code

A configuration change is just as capable of causing a security or
reliability incident as a code change — pointing a production frontend at a
testing backend, or restricting a cloud storage bucket's ACLs incorrectly,
are configuration mistakes with the same blast radius as a code bug. Yet
configuration is, in practice, far less consistently version-controlled and
reviewed than code: engineers who would never build production from a
locally modified source tree often don't think twice about pushing a
configuration change without saving it to version control first. Applying
[mandatory code review](mandatory-code-review.md) to configuration changes,
not only application code, closes this gap — and where a deployment process
reads its configuration from a version-controlled file (a Kubernetes YAML
manifest, for example), restricting deployment to only the reviewed,
checked-in version makes misconfiguration significantly harder.
