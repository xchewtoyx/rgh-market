---
type: concept
title: Self-Generated Test Evaluator
description: >
  Let a code agent write and run its own unit-test suite so sparse pass/fail
  signals ground reflection without an external oracle — enabling pass@1 loops.
sources:
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    resource: "Reflexion (Shinn et al.), pp. 1–19"
---

For programming tasks, [Reflexion](reflexion.md)'s Evaluator can be the
agent's **self-generated unit tests** rather than exact-match labels or an
external judge. Typical construction: [chain of thought](chain-of-thought-prompting.md)
prompting for diverse tests with natural-language descriptions → keep only
syntactically valid tests (e.g. AST build) → sample a small suite \(T\)
(Shinn et al. use up to \(n = 6\)). The Actor then iterates under
[verbal reinforcement learning](verbal-reinforcement-learning.md) while the
harness still reports **pass@1** against hidden benchmarks.

This grounds self-evaluation when the environment only returns compile/runtime
feedback. Ablations on hard Rust HumanEval show both halves are required:
reflection without tests *hurts* (no correctness signal → harmful edits), and
tests without natural-language self-reflection yield no gain (errors are
caught but fixes do not encode them). Blind trial-and-error debugging without
verbal reflection is especially weak on harder compiled-language tasks.

Quality is bounded by [test suite fidelity](test-suite-fidelity.md). Execute
generated code only in isolated sandboxes — suites and solutions are not
pre-validated before running.
