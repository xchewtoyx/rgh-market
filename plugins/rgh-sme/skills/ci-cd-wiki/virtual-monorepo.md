---
type: concept
title: Virtual Monorepo
description: >
  Stitching fine-grained repositories into a consistent dependency graph and
  trunk-like head via build-system and VCS linkage without one physical repo.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Virtual Monorepo

A physical **monorepo** makes [one version rule](one-version-rule.md) nearly
automatic — one place to see canonical versions and build state. Many
organizations cannot use one repo (secrecy, legal, scale, Git limits on binary
history).

A **virtual monorepo (VMR)** synthesizes monorepo *functionality* from
separate repos: agreed commit ordering, unpinned inter-repo dependencies at
head/trunk, and build-system linkage (Git submodules, Bazel externals, CMake
subprojects). Goal: developers still have no choice about which version of a
shared library to use — dependencies track org-wide head.

Trade-offs vs. true monorepo: better isolation for compliance boundaries and
clone performance; more machinery to maintain consistent CI and version bumps
across repos. Rule of thumb: identical secrecy/legal requirements across
projects favor monorepo; mixed requirements favor VMR.

See [source-level vs. binary-level component integration](source-vs-binary-component-integration.md).
