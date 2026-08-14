---
type: concept
title: Binary Provenance
description: >
  A signed record produced by every build describing exactly how a given
  artifact was built — its inputs, the command, the environment, and the
  entity that built it — so deployment decisions and later investigations
  can trust a specific claim about an artifact's origin.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Binary Provenance

Reverse-engineering a binary to figure out what source it came from is
prohibitively expensive; asking the build to record that information at the
moment it's produced is cheap. Binary provenance is that record — the data
[provenance-based deployment policies](provenance-based-deployment-policy.md)
are evaluated against, and the evidence
[verify artifacts, not just people](verify-artifacts-not-just-people.md)
depends on existing.

## What to include

- **Authenticity** (required): a cryptographic signature over the rest of the
  record, establishing which system produced it and why it can be trusted.
- **Outputs** (required): which artifact(s) this provenance describes,
  identified by a cryptographic hash of their content.
- **Inputs**: the sources (e.g. a specific Git commit and repository URL) and
  dependencies (libraries, build tools, compilers) the build consumed — see
  [hermetic builds](hermetic-builds.md) for why these need to be exhaustive
  and unambiguous.
- **Command**: exactly how the build was invoked, ideally in a
  machine-analyzable structured form.
- **Environment**: anything else needed to reproduce the build (architecture,
  environment variables).
- **Versioning**: a timestamp and format version, so old provenance records
  can be invalidated or reinterpreted as the format evolves, without becoming
  susceptible to rollback-style attacks.

Anything the build system doesn't itself validate is an attack surface: if a
user can pass arbitrary compiler flags, the flags themselves need validating
by whatever consumes the provenance, since a flag like `-D` can silently
redefine program behavior without changing the recorded source.

## Keeping provenance unambiguous

Looking provenance up asynchronously by artifact hash (e.g. from a shared
database) can produce many records for the same hash — trivially, many
different builds can each produce an empty output file with an identical
hash. When several records exist for one artifact and none of them clearly
passes a policy, the resulting error can't point at a specific problem, and
verification time grows with the number of matching records. Propagating
provenance inline with the artifact itself (rather than as a separate lookup)
avoids this ambiguity, keeps verification fast, and keeps error messages
specific enough to actually act on.
