---
type: concept
title: Eliminating Cyclic Component Dependencies
description: >
  A component's dependency graph must form a directed acyclic graph — no
  component may depend, even transitively, on something that depends back on
  it — or build order and independent versioning both break down.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 13"
---

# Eliminating Cyclic Component Dependencies

If Component A depends on Component B, B must not depend on A, directly or
transitively. A cyclic dependency graph makes it impossible to determine a
valid build order (which one builds first?) and defeats independent
versioning and release of components, which is the entire point of splitting
an application into components in the first place — see
[component pipeline triggering](component-pipeline-triggering.md).

When two components appear to need each other, the fix is to break the
cycle: apply the Dependency Inversion Principle, or extract the shared
concern into a third component that both A and B depend on one-directionally.
This is a structural precondition for
[semantic versioning](semantic-versioning.md) and
[dependency pinning](dependency-pinning.md) to mean anything at the
inter-component level — you can't pin a version of something whose own
version depends circularly on yours.
