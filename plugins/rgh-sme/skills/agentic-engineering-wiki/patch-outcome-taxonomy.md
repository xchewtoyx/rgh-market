---
type: concept
title: Patch Outcome Taxonomy
description: >
  Classify an applied-but-unresolved code patch by which of the fail-to-pass
  and pass-to-pass test sets it satisfies — not every non-fix is the same
  failure.
sources:
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 16–30 (Appendix C.5)"
---

A binary resolved/unresolved score collapses several structurally different
outcomes into one bucket. When a task has both **fail-to-pass** tests (tests
that should start failing and end passing once the issue is fixed) and
**pass-to-pass** tests (tests that should keep passing throughout), a patch
that applies but doesn't fully resolve the issue falls into one of five named
outcomes, from the cross of how much of each set it satisfies:

| | All P2P | Partial P2P | None P2P |
|---|---|---|---|
| **All F2P** | Resolved | Breaking Resolved | Breaking Resolved |
| **Partial F2P** | Partially Resolved | Work in Progress | Work in Progress |
| **None F2P** | No-Op | Regression | Regression |

- **Breaking Resolved** — fixes the reported issue completely but breaks
  previously-working behavior; see
  [downstream dependent blind spot](downstream-dependent-blind-spot.md) for
  the usual mechanism.
- **Partially Resolved** — doesn't fully fix the issue but doesn't break
  anything either; a safe, incomplete attempt.
- **Work in Progress** — partial progress on both fronts; ambiguous whether
  more budget would converge or diverge.
- **No-Op** — doesn't touch the reported issue and doesn't break anything —
  the patch applies and passes existing tests but is functionally
  irrelevant to the task.
- **Regression** — doesn't fix the issue and breaks something that worked
  before — strictly worse than doing nothing.

Empirically, among applied-but-unresolved patches, **No-Op and Regression
dominate** (roughly 60–70% of that pair in one setting) — safe partial
progress (Partially Resolved, Work in Progress) is the minority outcome, and
plain "doesn't help" is far more common than "helps partway." Manual
inspection attributes much of this to agents understanding the immediate
symptom but missing inter-file dependencies or callers that a pure
retrieval-based localization step doesn't surface.

This is the code-specific instance of a more general eval-design habit,
[outcome-based partial-credit grading](outcome-based-partial-credit-grading.md):
collapsing a multi-part outcome into one binary score always discards
information about *which* part succeeded or failed.

Design implications:

- Report this full taxonomy, not just resolve rate, in
  [per-task offline harness tests](per-task-offline-harness-tests.md) — a
  harness change that trades Regression outcomes for No-Op outcomes is a real
  safety improvement even if the headline resolve rate doesn't move, and one
  that's invisible to a binary pass/fail metric.
- Treat Regression specifically as the outcome to eliminate first: it costs
  more than it saves, unlike No-Op which is merely wasted effort. Prioritize
  [downstream dependent](downstream-dependent-blind-spot.md) checks and
  pass-to-pass regression testing over chasing incremental resolve-rate gains
  if Regression share is high.
- The authors' suggested mitigation — give the agent
  **execution feedback** against the test suite before it submits, rather
  than a one-shot generate-and-stop — turns unseen Breaking/Regression
  outcomes into visible failures the agent can react to. This is the
  evaluation-design case for the interactive
  [agent-computer interface](agent-computer-interface.md) pattern over
  one-shot patch generation: a harness that never runs tests before
  `submit` cannot distinguish an outcome it should keep from one it should
  revert.
