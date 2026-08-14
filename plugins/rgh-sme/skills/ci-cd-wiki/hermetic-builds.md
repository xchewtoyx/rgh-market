---
type: concept
title: Hermetic Builds
description: >
  A build is hermetic when every input it depends on is explicitly and
  unambiguously declared up front — source, toolchain, and every dependency —
  rather than read from ambient host state or fetched live from the network
  during the build.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 8"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 20"
---

# Hermetic Builds

A stricter form of [build once, deploy everywhere](build-once-deploy-everywhere.md)'s
reproducibility guarantee, applied to the build step itself rather than to
deployment. A hermetic build declares every input it depends on — source
code, toolchain, compiler version, every dependency — explicitly and pulls
them only from version control or a pinned, locked source (see
[dependency pinning](dependency-pinning.md)). It never silently reads
whatever happens to be installed on the build machine, and never reaches out
to the live network during the build. Google's Blaze/Bazel build tool is
built around this property specifically to eliminate builds that only work
"on this particular build server" because of some unrecorded ambient state.

## Why it matters beyond ordinary reproducibility

Hermeticity is distinct from but closely related to
[reproducibility](reproducible-builds.md): reproducibility is the guarantee
that the same declared inputs always produce a bit-for-bit identical output,
and it almost always *requires* hermeticity first — an unreproducible build
is usually a sign that some input wasn't actually pinned. Hermeticity on its
own is what makes trusting the [artifact repository](artifact-repository.md)
and [artifact integrity verification](artifact-integrity-verification.md)
meaningful: if two different build agents can produce different bits from
the same commit because one of them silently depended on ambient host state,
a checksum mismatch could mean either tampering or just environmental
variance, and you can no longer tell which. Hermeticity removes that
ambiguity by removing the variance's source entirely.

## Other benefits of hermeticity

- **Build input analysis**: because every dependency is explicitly declared,
  it becomes possible to automatically check the full input set against a
  vulnerability database, license policy, or disallowed-library list —
  something not possible when inputs are only implicitly whatever happened
  to be on the build machine.
- **Cherry-picking**: a hermetic build lets a bug fix be built and shipped in
  isolation, without accidentally pulling in unrelated changes from a
  different compiler or toolchain version — which matters most exactly when
  an emergency fix has less time for full testing than a routine release; see
  [emergency fixes follow the same pipeline](hotfix-through-pipeline.md).

## Build sandboxing

[Artifact-based build systems](artifact-based-build-systems.md) run each build
action in a filesystem sandbox exposing only declared inputs and prior outputs;
undeclared writes are discarded and network access is blocked. That makes
"silent conflicting writes" between parallel tasks structurally impossible —
the build-time analogue of [hermetic testing](hermetic-testing.md)'s isolated
runtime environments.
