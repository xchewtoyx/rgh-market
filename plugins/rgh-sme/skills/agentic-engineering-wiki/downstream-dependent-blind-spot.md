---
type: concept
title: Downstream Dependent Blind Spot
description: >
  Editing a function without knowing what else in the codebase depends on its
  current behavior can silently corrupt callers instead of only under-fixing.
sources:
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 46–52"
---

Editing the right function is necessary but not sufficient: a function's
behavior can be relied on by callers the agent never inspected, so a change
that locally addresses the issue can **corrupt** correct downstream behavior
rather than merely leaving the bug half-fixed. Example (scikit-learn
`KernelPCA` sign non-determinism): the issue is that eigenvector sign/parity
flips nondeterministically across runs. The gold fix imports `svd_flip` and
enforces deterministic eigenvector signs in `_fit_transform`, then sorts
eigenvectors — a fix scoped to *how the values are produced*. The model
instead edits the function's **return value** (`return K` →
`return K / self.lambdas_`), changing what every caller of `_fit_transform`
receives — wrong localization *and* wrong semantics, and unlike an
[under-scoped or missing-branch patch](idiomatic-minimal-patch-preference.md),
this failure actively **breaks previously-correct behavior** for any caller
depending on the original return semantics, not just the reported case.

This is a distinct failure axis from
[single-site edit blind spot](single-site-edit-blind-spot.md) (missing
sibling occurrences of a *pattern*) and from idiomatic minimal patch
preference (over- or under-building the fix *at* the right site): here the
edit site is plausible-looking but the agent never established what the
function's current contract actually promises to its callers before changing
it. Harness implications:

- Before editing a function's signature, return shape, or side effects,
  prompt the agent to enumerate call sites (`search_file`/`grep` for the
  function name across the repo) as a required localization step, not an
  optional one — [issue-grounded localization](issue-grounded-localization.md)
  finds the edit site but does not by itself establish blast radius.
- Score candidate patches on **pass-to-pass regression**, not only
  fail-to-pass success, in
  [per-task offline harness tests](per-task-offline-harness-tests.md) — a
  patch that breaks working callers is a worse outcome than one that merely
  fails to fix the target, and test-passing alone conflates the two.
  [Test suite fidelity](test-suite-fidelity.md) covers the general false-
  positive risk; this is the specific mechanism (unexamined dependents) that
  produces the worst case of it, a passing-looking submit that regresses
  other behavior.
- Prefer fixing *how a value is produced* over changing *what is returned*
  when both are locally plausible — a production-side fix is far less likely
  to violate an implicit contract that downstream code already relies on.
