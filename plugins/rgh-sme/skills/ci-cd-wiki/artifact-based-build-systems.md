---
type: concept
title: Artifact Based Build Systems
description: >
  Build systems that declare artifacts and dependencies in a fixed rule set
  rather than arbitrary task scripts, enabling safe parallelism, incrementality,
  and remote execution.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 20"
---

# Artifact Based Build Systems

**Task-based** build systems (Ant, Maven, Gradle, Rake) define arbitrary scripts
as tasks in a dependency graph. Because tasks can run any code, the system
cannot know what they touch — parallelization and incremental builds require
conservative full reruns or risky engineer-maintained shortcuts that cause
staleness bugs.

**Artifact-based** systems (Blaze/Bazel) invert control: engineers declare
*what* to build in a manifest (targets, sources, deps); the system chooses
*how* — analogous to describing a pure function (sources + tools → binaries)
and letting the engine schedule work.

Benefits:

- **Parallelism** — independent targets build concurrently when the rule type
  is known (e.g. `java_library` only compiles Java).
- **Incrementality** — unchanged inputs reuse prior outputs; only transitive
  dependents rebuild after a leaf change.
- **Sandboxed actions** — each step runs in a filesystem sandbox exposing only
  declared inputs; undeclared writes and network access are blocked — the
  build-time counterpart to [hermetic builds](hermetic-builds.md).
- **Deterministic externals** — third-party artifacts require cryptographic
  hashes in a workspace manifest; hash mismatch fails the build.

Custom behavior extends via **rules** and **actions** with declared inputs and
outputs rather than ad hoc shell. Task-based systems remain workable for many
projects; artifact-based systems pay off when scale, correctness, and
[distributed build caching](remote-build-cache-and-execution.md) matter.

Most builds at Google are triggered automatically — CI presubmit, postsubmit,
release assembly, and cross-repo library testing all sit on the build system.

## Fine-grained modules

Google favors many small targets (often **1:1:1** — one package, one target,
one BUILD file per directory) over one module per project. A production binary
may depend on tens of thousands of targets; moderate teams own hundreds.
Finer granularity improves parallel builds, incremental rebuilds, and
[test impact analysis](test-impact-analysis.md). BUILD maintenance is offset
by tooling that auto-manages dependency lists.

**Visibility** on each target (`public`, `private`, allowlist) limits who may
depend on it — the inverse of a dependency edge. Minimize visibility; most
internal targets stay directory-private.

**Strict transitive dependencies** fail the build when code uses a symbol without
declaring a direct dep on its library — preventing silent reliance on transitive
deps that later removal breaks. Verbose BUILD files, but safer refactors.

External deps are versioned manually in a workspace manifest — never floating
"latest" ranges. See [one version rule](one-version-rule.md) and
[dependency pinning](dependency-pinning.md).
