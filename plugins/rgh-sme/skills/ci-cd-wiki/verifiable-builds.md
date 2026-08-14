---
type: concept
title: Verifiable Builds
description: >
  A build is verifiable if its binary provenance can be trusted — achieved
  through a trusted build service, an independent rebuild, or a quorum of
  independent rebuilders, each with different trust trade-offs.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Verifiable Builds

Whether a build's [provenance](binary-provenance.md) can be trusted is a
question of architecture, not just cryptography. Three approaches:

- **Trusted build service**: the verifier simply trusts that a specific
  build service performed the build, because that service signs provenance
  with a key only it can access. Cheapest — build once, no need for
  reproducibility — but concentrates trust entirely in that one service.
- **Self-rebuild**: the verifier reproduces the build itself and checks that
  the result matches. Requires the build to be
  [reproducible](reproducible-builds.md), and doesn't scale well — a build
  that takes minutes or hours can't run again inline with a deployment
  decision that needs to complete in milliseconds.
- **Rebuilding service (quorum)**: some number of independent rebuilders each
  reproduce the build and attest to the result; a verifier checks that enough
  of them agree. A hybrid that avoids concentrating trust in a single service
  without paying the self-rebuild latency cost on every deployment decision —
  used by projects like Debian where no single central authority is
  acceptable.

## Design considerations for a verifiable build system

- **Untrusted inputs**: many build systems let users define arbitrary build
  steps (a Makefile, a Jenkinsfile) — functionally "remote code execution by
  design." A malicious build step running with the build's full privileges
  could steal a signing key or falsify its own provenance. See
  [build privilege separation](build-privilege-separation.md).
- **Unauthenticated inputs**: any dependency fetched insecurely (e.g. over
  plain HTTP) is a place an attacker can substitute a different artifact in
  transit. [Hermetic builds](hermetic-builds.md) address this by requiring
  every input to be declared and fetched only by a trusted orchestrator,
  rather than by arbitrary user-controlled build steps.

It's usually desirable, though not strictly required, for a verifiable build
to also be hermetic and [reproducible](reproducible-builds.md) — those
properties make the provenance easier to trust, but verifiability itself is
really about whether *this particular architecture* gives a verifier good
reason to believe the provenance is accurate.
