---
type: concept
title: Build Privilege Separation
description: >
  Running user-defined build steps in an environment with no access to
  signing keys or other privileges, while a separate trusted orchestrator
  sets up build state and issues the signed provenance, so a malicious build
  script can't compromise the pipeline's own trust anchors.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Build Privilege Separation

Most build systems let a non-administrative user define arbitrary commands
that will run during the build — a Makefile, a Jenkinsfile, a `BUILD` file.
This is necessary to support the variety of builds an organization needs, but
from a security standpoint it's remote code execution by design: a malicious
or compromised build command running with the build's full privileges could
steal the signing key used for
[binary provenance](binary-provenance.md), insert false information into the
provenance it produces, or interfere with another build running in parallel
or afterward on the same infrastructure.

## The mitigation

Split the build into two privilege domains: a trusted orchestrator sets up
the known-good starting state, launches the build, and — once it completes —
produces the signed provenance. All user-defined build commands execute in a
separate environment (a sandbox, or an entirely separate machine) that has no
access to the signing key or any other privileged capability. Even a fully
compromised build step, under this split, can corrupt its own build's output
but can't forge provenance, steal the key used to sign other builds, or
tamper with unrelated builds — which is exactly the class of threat
[software supply chain threat modeling](software-supply-chain-threat-model.md)
is meant to surface and price in.
