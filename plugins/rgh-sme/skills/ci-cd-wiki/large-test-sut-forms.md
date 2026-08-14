---
type: concept
title: Large Test SUT Forms
description: >
  How the system under test is scoped — single process, single machine,
  multimachine, or shared staging/production — trading hermeticity against
  production fidelity.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Large Test SUT Forms

Large tests follow: obtain a system under test (SUT) → seed data → act → verify.
Unlike unit tests (one class in-process), larger tests usually run the SUT in
separate processes. SUT scope drives test size and cost.

Two opposing forces:

- **Hermeticity** — isolation from other users and live dependencies; less
  concurrency and infrastructure flakiness. See [hermetic testing](hermetic-testing.md).
- **Fidelity** — how closely topology, configuration, and load match production.

Forms, increasing scope:

1. **Single-process SUT** — whole app in one binary; least faithful to prod topology.
2. **Single-machine SUT** — production-like binaries on one host; common for medium tests.
3. **Multimachine SUT** — distributed like cloud prod; higher fidelity, network flakiness.
4. **Shared staging/production** — lowest setup cost; contention, wait for deploy, user impact risk.
5. **Hybrids** — partial explicit stack plus shared backends; necessary at very large scale.

Reduce scope at natural seams: API instead of full UI, in-memory DB instead of
real datastore, fakes instead of third-party APIs (cost and rate limits).
[Record/replay](hermetic-testing.md) proxies capture live traffic on postsubmit
for hermetic replay on presubmit.

In-production tests cannot block release to that environment — they arrive too
late for pre-release gates; use [production probers](production-probers.md)
for post-release signal instead.
