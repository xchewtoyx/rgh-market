---
type: concept
title: Downstream Pipeline Triggering on Component Publish
description: >
  When a component publishes a new versioned artifact, every pipeline for an
  application or component that depends on it should trigger automatically to
  build and test against the new version.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 13"
---

# Downstream Pipeline Triggering on Component Publish

For [binary-level component integration](source-vs-binary-component-integration.md)
to catch breaking changes quickly, publishing a new component version can't be
the end of that component's pipeline — it has to be the start of every
dependent's:

```
[Component A commit] -> [Component A pipeline pass] -> [Publish Component A v1.4.0 to artifact repo]
                                                                   |
                                                                   v
                                              [Trigger integration pipeline for
                                               App B using Component A v1.4.0]
```

This turns a multi-component system's pipelines into a graph that mirrors the
[dependency graph](cyclic-dependency-elimination.md) itself: a change
propagates outward automatically, and any break is caught at the first
downstream pipeline that consumes the new version rather than sitting latent
until someone manually bumps a pinned version and finds out.

This is one point on a spectrum of choices about when to lock dependency
versions together — see [project integration timing
patterns](project-integration-timing-patterns.md) for how it compares to
integrating everything at build time or deferring integration all the way
to apply time.

## Applied to ML model dependencies

The same trigger-on-publish structure applies when the "component" is a
machine learning model and the "dependent" is a downstream model consuming
its output (e.g. an ASR model feeding an NLP model) — except the failure
mode a downstream pipeline needs to catch is a silent metric regression from
data drift, not a broken API contract. See [ML dependency regression
gate](ml-dependency-regression-gate.md) for how the eval pipeline this
triggers differs from an ordinary integration build.
