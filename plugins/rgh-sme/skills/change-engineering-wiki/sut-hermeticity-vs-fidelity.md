---
type: concept
title: SUT Hermeticity vs Fidelity
description: >
  Larger tests trade isolation from flaky shared infrastructure against
  accuracy to production topology — pipeline stage choice is where on that
  curve to test.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# SUT Hermeticity vs Fidelity

Large tests compose a **system under test (SUT)** — often multiple processes
or machines — then seed data, act, and verify. SUT scope drives test scope:
bigger SUT, bigger test.

Two factors trade off directly:

- **Hermeticity** — isolation from other components' usage and shared
  infrastructure; high hermeticity reduces concurrency and infrastructure
  flakiness.
- **Fidelity** — how closely the SUT reflects production configuration,
  topology, and dependencies.

Forms from smallest to largest scope: single-process packaged binary;
single-machine multi-binary (production launch configs); multimachine
cloud layout; shared staging/production; hybrids (explicit frontends hitting
shared backends — common at scale when full copies of every dependency are
infeasible).

**Hermetic SUTs enable earlier gates.** Tests against production or shared
staging can't block release *to* that environment — the SUT arrives too late.
Shared staging still gates on code reaching the environment; reservation
systems don't scale with engineer count. Cloud-isolated or machine-hermetic
SUTs avoid conflicts and support [presubmit vs postsubmit test
gating](presubmit-vs-postsubmit-test-gating.md) and [release candidate
regression testing](release-candidate-regression-testing.md) before promotion.

See [pre-production fidelity limits](pre-production-fidelity-limits.md) for
why fidelity can never reach production completeness, and [record replay
dependency isolation](record-replay-dependency-isolation.md) for shrinking
external dependencies while keeping useful fidelity on one machine.
