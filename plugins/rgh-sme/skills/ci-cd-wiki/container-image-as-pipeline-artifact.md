---
type: concept
title: Container Image as Pipeline Artifact
description: >
  Packaging a build's binary together with its OS-level dependencies into a
  container image gives a pipeline a single promotable artifact that starts
  in seconds and is portable across any standard-compliant runtime engine.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 16"
---

# Container Image as Pipeline Artifact

[Build once, deploy everywhere](build-once-deploy-everywhere.md) requires an
artifact that carries everything it needs to run identically in every
downstream environment. A container image is a common way to realize that:
it bundles the built binary with its OS-level dependencies (libraries,
runtime, base filesystem) into one artifact stored in the
[artifact repository](artifact-repository.md), so "works in staging" and
"works in production" stop depending on what happened to be manually
installed on the host.

This is the concrete mechanism behind the deployability tactic of
**packaging dependencies**: rather than relying on a target server already
having the right library versions, the pipeline ships them inside the
artifact itself.

## Why containers over full VM images for this role

A VM image bundles an entire operating system, so promoting a new version
means transferring and booting gigabytes of mostly-unchanged OS content —
minutes of transfer plus boot time before a new version is even running. A
container shares its host's kernel and is built in **layers**: a base OS
layer, then one layer per dependency added on top (a language runtime, then
a framework, then the application itself). Promoting a change to only the
top layer — the actual application code — means only that thin layer has to
move through the pipeline, cutting promotion time from minutes to
milliseconds. This is what makes container images practical as the
per-commit artifact a [commit stage](commit-stage.md) produces and promotes
on every run, rather than something built and pushed only for occasional
releases.

Changing a lower layer (a base image update, a runtime version bump) forces
every layer above it to rebuild, so a pipeline that treats an unchanged
application layer as cheap to promote can still be surprised by an
expensive rebuild triggered from a dependency layer changing underneath it.

## Portability across runtimes

The interface between a container and its runtime engine is standardized
(the Open Container Initiative), so an image built once is not locked to
the tool that built it — a pipeline can build with one engine and deploy to
environments running a different compliant one. This is what lets a
container image genuinely be *the* build-once artifact rather than one more
environment-specific rebuild target.

## Consequences for pipeline and test design

- Container **build scripts belong under the same discipline as application
  code**: version-controlled, reviewed, and tested, per
  [version-control everything the pipeline depends on](version-control-everything.md)
  — an unreviewed change to a base image is exactly the kind of untracked
  drift a pipeline exists to prevent.
- Fast container start/stop times are what make
  [ephemeral test environments](ephemeral-test-environments.md) practical at
  pipeline speed: spinning up a fresh, disposable instance per test run costs
  seconds rather than the minutes a full VM boot would add to every pipeline
  stage.
- Pulling a public base image you didn't build introduces exactly the kind
  of unverified, third-party input a
  [software supply chain threat model](software-supply-chain-threat-model.md)
  has to account for — an unpinned or unscanned base image is a supply-chain
  entry point, not just a convenience.
