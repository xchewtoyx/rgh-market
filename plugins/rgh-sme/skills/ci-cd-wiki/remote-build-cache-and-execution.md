---
type: concept
title: Remote Build Cache and Execution
description: >
  Sharing build action outputs across machines via a remote cache and scheduling
  actions on a worker pool, requiring reproducible artifact-based builds.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 20"
---

# Remote Build Cache and Execution

At sufficient scale, no single machine finishes a build in acceptable time.
**Remote caching** stores action outputs keyed by target plus input hash; before
building locally, the client downloads cache hits. Requires the build system to
guarantee reproducibility — same inputs → byte-identical outputs on any machine
— which [artifact-based build systems](artifact-based-build-systems.md) provide
and task-based systems struggle to offer.

**Remote execution** sends build requests to a central scheduler that decomposes
work into actions and assigns them to a scalable worker pool. Workers read and
write through the shared cache; the scheduler blocks until dependencies are
ready. This needs:

- Self-describing build environments (workers spin up without manual setup).
- Self-contained build steps (any step may run on any worker).
- Deterministic outputs (workers trust each other's artifacts).

Without those guarantees, remote execution is unreliable on task-based systems.
Cache benefit depends on download latency versus rebuild cost — measure before
assuming cache always wins.

Google's internal stack pairs Blaze with ObjFS (remote cache) and Forge
(remote execution). The pattern generalizes to open Bazel with remote cache
backends (cloud storage, Redis) and remote execution services.

Connects to [hermetic builds](hermetic-builds.md),
[binary provenance](binary-provenance.md), and the [commit stage](commit-stage.md)
— CI agents and developer laptops share the same cache namespace when inputs
match.
