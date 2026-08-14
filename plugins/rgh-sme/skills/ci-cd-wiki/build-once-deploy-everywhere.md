---
type: concept
title: Build Once, Deploy Everywhere
description: >
  Binaries are compiled and packaged exactly once, in the commit stage, and the
  identical artifact is promoted through every later environment rather than
  being recompiled per environment.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 5"
---

# Build Once, Deploy Everywhere

Also called the single-binary principle. The [commit stage](commit-stage.md) of
the [deployment pipeline](deployment-pipeline.md) is the only place a binary
artifact is compiled and packaged. That exact artifact is stored in the
[artifact repository](artifact-repository.md) and promoted, unmodified, through
every subsequent test and production environment. A
[container image](container-image-as-pipeline-artifact.md) is a common
concrete form for that artifact, since it bundles the binary's OS-level
dependencies alongside it rather than relying on the target environment
already having them installed.

## Why it matters

- Recompiling per environment reopens the possibility that what was tested is
  not what gets deployed — a different compiler flag, dependency resolution,
  or toolchain version could produce different behavior.
- It forces environment-specific values out of the binary and into external
  [configuration injected at deploy or runtime](configuration-injection.md),
  since packaging config into the binary at build time would require rebuilding
  per environment (an anti-pattern).
- It underwrites the [release candidate](release-candidate.md) principle: a
  build that passed every pipeline stage *is* the thing that gets released, not
  a stand-in for it.

## Anti-pattern

Packaging environment-specific configuration files into the binary at build
time. This breaks the single-binary principle because it forces a rebuild for
each target environment, reintroducing the "what we tested may not be what we
ship" risk this practice exists to eliminate.
