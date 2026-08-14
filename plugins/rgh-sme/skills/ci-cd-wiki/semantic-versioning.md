---
type: concept
title: Semantic Versioning
description: >
  Assigning explicit MAJOR.MINOR.PATCH version numbers to components and
  dependencies so a version number alone communicates whether a change is
  breaking, additive, or a pure bug fix.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 13"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 14"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 23"
---

# Semantic Versioning

`MAJOR.MINOR.PATCH`:

- **MAJOR**: incompatible, breaking API changes.
- **MINOR**: backward-compatible new functionality.
- **PATCH**: backward-compatible bug fixes.

Every internal and external dependency should carry an explicit version
following this scheme, published to the
[artifact repository](artifact-repository.md) as part of a
[component's own pipeline](component-pipeline-triggering.md). The payoff is
that a consumer can decide how much risk a version bump carries just from the
number — a MAJOR bump requires deliberate review; a PATCH bump usually
doesn't — without inspecting the change itself.

This only holds if version numbers are trustworthy, which is why
[dependency pinning](dependency-pinning.md) matters: a floating version range
defeats semantic versioning's whole purpose, since the actual version
resolved at build time is no longer a single, reviewable number.

## Handling a MAJOR bump gracefully

Because a MAJOR bump signals a genuinely breaking change, a producer owes
consumers more than just the version number change: see
[API version coexistence](api-version-coexistence.md) for running old and
new major versions side by side rather than cutting consumers over all at
once, and the [tolerant reader pattern](tolerant-reader-pattern.md) for
reducing how often a change needs to be MAJOR in the first place by having
consumers ignore fields they don't recognize.

## Limitations at scale

SemVer numbers are **human estimates**, not provable compatibility facts.
Constraint solvers treat them as boolean safe/unsafe — the problem is
NP-complete — but breaking-ness depends on actual usage (Hyrum's Law): patch
changes to log format, import order, or iteration order can break real
consumers. SemVer can **overconstrain** (major bump when only unused APIs
changed) and **underprotect** (patch labeled safe but behavior observable).

SemVer works "well enough" only when providers are accurate, dependencies are
fine-grained, and usage stays within promised surfaces — properties that
degrade as graphs grow. Feeding human risk estimates into constraint solvers
turns lossy labels into absolutes, producing **overconstraint** (dependency
hell) or **underconstraint** (versions that should not combine but do).

A dependency is a **contract**: providers and consumers both have rights and
responsibilities; providers should be clear about promised stability over time.
Importing a dependency establishes an ongoing trust relationship — not a
one-time copy — with support costs on both sides. See
[dependency provider costs](dependency-provider-costs.md).

Alternatives: [minimum version selection](minimum-version-selection.md),
bundled distributions, downstream CI as empirical compatibility evidence (see
[live at head dependency model](live-at-head-dependency-model.md)) inside
monorepos with provider accountability. Major-version bumps as new import paths
(Go, Clojure) force explicit compatibility breaks rather than silent majors.
