---
type: concept
title: Dependency Pinning
description: >
  Production release builds must lock every dependency to an exact, immutable
  version rather than a floating range, so the same commit always resolves to
  the same set of dependencies.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 13"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 14"
---

# Dependency Pinning

Floating version ranges (`1.x`, `LATEST-SNAPSHOT`) let a build silently
resolve to a different dependency version each time it runs, which breaks the
core promise of a [release candidate](release-candidate.md): that the exact
same artifact was tested and is what gets deployed. A build that resolves
different dependency versions on different runs can pass today and fail
tomorrow without a single line of the project's own code changing.

Pinning means locking every dependency — including transitive ones — to an
exact, immutable version number for release builds. This is what makes the
[artifact repository](artifact-repository.md) trustworthy as a cache: the
same pinned version always resolves to the same cached artifact, and an
upstream publisher changing or removing that version afterward can't retroactively
alter a build that already ran.

See [semantic versioning](semantic-versioning.md) for how pinned version
numbers communicate the risk of moving to a newer pin. Pinning also makes a
[software bill of materials](software-bill-of-materials.md) trustworthy: an
inventory of dependency versions is only useful for vulnerability response if
those are genuinely the versions that get deployed.

## Pinning at the organization level

Pinning solves reproducibility per build, but an organization with many
services each independently pinning the same shared library can still end up
running dozens of divergent versions of it in production simultaneously —
most of them behind on security patches, because upgrading feels risky and
nobody outside the owning team is responsible for it. The countermeasure is
assigning each shared library an owner responsible for keeping every
consumer building and passing tests against the current version, and for
actively migrating consumers forward — turning "pin and forget" into "pin,
and someone is accountable for moving the pin." This is easiest inside a
single [source-level integration](source-vs-binary-component-integration.md)
build, where the owner can see every consumer directly; at binary-level
integration it requires the artifact repository to also track who consumes
which published version.

Concretely, pinning is enforced via a lockfile the build reads instead of
resolving versions fresh each time (`package-lock.json`, `Cargo.lock`, a
Maven POM's explicit versions with checksums) — never an open-ended wildcard
or `latest` specifier, which is exactly the floating-range problem this note
warns against, just spelled differently per ecosystem. Wrapping a third-party
SDK or vendor library behind an internal interface is a further layer of
protection: it isolates the rest of the codebase from a vendor's breaking
change, confining the blast radius of a version bump to the wrapper itself
rather than every call site.
