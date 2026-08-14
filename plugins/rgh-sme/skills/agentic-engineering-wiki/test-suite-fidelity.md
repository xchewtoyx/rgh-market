---
type: concept
title: Test Suite Fidelity
description: >
  Self-written evaluator tests bound reflection quality: false positives cause
  premature wrong submits; false negatives are safer because bad tests can be
  spotted.
sources:
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    resource: "Reflexion (Shinn et al.), pp. 1–19"
---

A [self-generated test evaluator](self-generated-test-evaluator.md) is only as
good as suite diversity and coverage. Two failure modes matter for
[Reflexion](reflexion.md)-style code agents:

- **False positive** — all internal tests pass but the solution is wrong →
  premature "success" and an invalid submission with no chance to reflect.
- **False negative** — tests fail on a correct solution → reflection is
  conditioned on a bogus failure. Preferable: the agent may notice bad tests
  and keep the original completion.

Empirically, similar base pass@1 can hide very different FP rates (Shinn et
al.: MBPP Python ~16% FP vs HumanEval Python ~1%), which tracks whether
reflection *helps* or *hurts* relative to the base model. When designing
offline harness checks or agent-side TDD loops, measure FP/FN on held-out
oracles — not only suite size — and treat high FP as a
[planning failure mode](agent-planning-failure-modes.md) that silently accepts
wrong "done" states. The same risk appears when an agent’s patch **passes
necessary repo tests** but differs from the gold pattern in ways the suite
never probes (e.g. an alternate regex boundary that may match too broadly) —
held-out oracles and
[idiomatic minimal patch preference](idiomatic-minimal-patch-preference.md)
matter alongside green CI. Non-deterministic generators, impure APIs, hardware-
dependent output, and parallelism remain hard to specify as accurate I/O
mappings, so suite fidelity has structural limits beyond prompting skill.
