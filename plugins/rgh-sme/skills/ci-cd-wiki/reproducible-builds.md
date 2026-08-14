---
type: concept
title: Reproducible Builds
description: >
  A build is reproducible when running the same build commands on the same
  inputs is guaranteed to produce a bit-for-bit identical output, which
  almost always requires the build to be hermetic first.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Reproducible Builds

Distinct from, but closely related to, [hermetic builds](hermetic-builds.md):
hermeticity means every input is explicitly declared; reproducibility means
that, given the same declared inputs, the build's output is bit-for-bit
identical every time it runs. Reproducibility almost always requires
hermeticity — an unreproducible build is often a symptom that some input
wasn't actually pinned (a floating dependency version, an unset timestamp, an
ambient environment variable) even if it looked hermetic on paper.

To make a build reproducible: remove every source of nondeterminism (fix or
externally record embedded timestamps, for instance), and fully specify the
entire toolchain and operating system, since different versions commonly
produce slightly different output even from identical source.

## Why it matters

- **Verifiability**: a [verifiable build](verifiable-builds.md)'s
  "self-rebuild" or "rebuilding service" architectures are only possible if
  the build is reproducible enough that redoing it produces the same result
  to check against.
- **Early hermeticity detection**: continuously testing for reproducibility
  is a good way to catch a hermeticity gap early, before it causes a subtler
  problem — a build that stops being reproducible has usually stopped being
  hermetic first.
- **Build caching**: a reproducible build's intermediate artifacts can be
  cached and reused with confidence, since the same inputs are guaranteed to
  produce the same output — valuable in large build graphs with many shared
  dependencies between targets.
