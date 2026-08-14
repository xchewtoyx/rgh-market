---
type: concept
title: Source-Level vs. Binary-Level Component Integration
description: >
  Integrating multiple components by compiling them together from source (a
  monorepo or submodules) trades fast breakage visibility for slower builds;
  integrating via published binaries trades fast builds for delayed breakage
  visibility.
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 13"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 23"
---

# Source-Level vs. Binary-Level Component Integration

- **Source-level integration** (Git submodules, monorepo): all components
  compile together in a single build pipeline. A breaking change in one
  component is visible immediately, in the same build, to everything that
  depends on it. Cost: compilation time scales with the size of the entire
  combined repository, not just the component that changed.
- **Binary-level integration** (via an [artifact repository](artifact-repository.md)):
  each component publishes versioned binaries; consumers build against
  pre-built binaries rather than source. Cost: a breaking interface change
  isn't discovered until the downstream component's own
  [integration pipeline](component-pipeline-triggering.md) happens to build
  against the new version — which could be much later than when the change
  was made.

Neither is universally correct; the trade-off is between build speed and how
quickly a breaking change surfaces. A team with fast, reliable
[downstream integration pipelines](component-pipeline-triggering.md) that
trigger automatically on every upstream publish narrows binary-level
integration's main weakness considerably, since the delay between "breaking
change published" and "breaking change detected downstream" shrinks to
roughly one pipeline run.

Google's guidance: **prefer source-control problems over dependency-management
problems** — expanding "organization" to the whole company via monorepo or
[virtual monorepo](virtual-monorepo.md) plus [one version rule](one-version-rule.md)
when policy allows. Binary integration with weak downstream CI delays
[diamond dependency problem](diamond-dependency-problem.md) discovery until
upgrade time.
