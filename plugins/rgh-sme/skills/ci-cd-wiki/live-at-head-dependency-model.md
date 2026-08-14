---
type: concept
title: Live at Head Dependency Model
description: >
  Always depend on the latest stable version of each dependency, with providers
  responsible for downstream CI before breaking changes land — the dependency
  analog of trunk-based development.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 23"
---

# Live at Head Dependency Model

**Live at head** drops [semantic versioning](semantic-versioning.md) ranges and
[dependency pinning](dependency-pinning.md) in favor of always building against
current stable versions — the dependency-management analog of
[trunk-based development](trunk-based-development.md).

Providers test changes against visible downstream consumers via CI before
committing. API or behavior changes that break dependents must not land unless
downstream is updated first or an automated migration is provided (critical for
closed-source consumers). Risk is **empirical** (do downstream tests pass?) not
**declared** (a version number).

Version selection collapses to "what is the most recent stable version of
everything?" Works inside a monorepo with ubiquitous tests and provider
accountability; largely unproven as an industry-wide default outside that
context.

With unlimited compute, the ideal dependency resolver converges here: run
dependents' tests against proposed changes instead of trusting SemVer labels.
Real-world barriers: missing tests, no reverse-dependency index, pinned
consumers blocking provider experiments, uneven OSS maintenance quality, and
[external consumer upgrade blocking](external-consumer-upgrade-blocking.md)
when paying customers cannot absorb toolchain upgrades on the provider's schedule.

A possible industry direction: replace maintainer-estimated compatibility
(SemVer labels fed into SAT solvers) with **experience-driven evidence** —
running downstream tests to learn whether versions actually work together.
That requires providers to test against consumers and advertise expected change
types, plus an industry shift in bilateral responsibilities — see
[dependency provider costs](dependency-provider-costs.md). Unit testing, CI,
and cheap compute could fundamentally change dependency management at scale,
but only if both sides treat compatibility as an empirical, pipeline-verified
property rather than a version-number guess.

Compare [minimum version selection](minimum-version-selection.md) as a SemVer-era
pragmatic improvement, and bundled distributions (Linux distros, frozen npm
graphs) that outsource compatibility to a distributor.
