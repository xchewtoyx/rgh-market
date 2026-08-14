---
type: concept
title: Single-Command Build
description: >
  Anyone must be able to check out a fresh copy of the repository on a clean
  workstation and run the entire build and test suite with one command,
  independent of any IDE.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 6"
---

# Single-Command Build

A prerequisite for [continuous integration](continuous-integration.md) and the
[commit stage](commit-stage.md): the official build — compile, test, package —
must run as one command-line invocation (`./build.sh`, `mvn clean install`),
with no dependency on IDE project files or manual IDE-driven steps.

## IDE independence

Developers can use whatever editor or IDE they like day to day, but the CI
server and pipeline must never rely on IDE-specific build state. If a build
only works "from inside Eclipse," it isn't automatable and can't run
unattended in the pipeline — this is the practical test for whether the build
qualifies.

## Supporting practices

- A top-level wrapper script in the repository root (`build.sh`, `go`) that
  bootstraps the correct build-tool version, sets required environment
  variables, and invokes the real build — so "clone and run one command" is
  literally true for a new contributor or a fresh CI agent.
- Clean the build output directory before compiling, so stale artifacts from a
  previous run cannot silently leak into a new one.

See [build tool selection](build-tool-selection.md) for choosing the
underlying tool, and [deployment script design](deployment-script-design.md)
for the analogous discipline applied to deployment rather than build.
