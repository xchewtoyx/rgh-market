---
type: concept
title: Code Simplicity for Security
description: >
  Simple code has fewer places for security and reliability bugs to hide —
  avoid deep nesting and speculative generality, budget for technical
  debt, and never mix refactoring with functional change.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 12"
---

# Code Simplicity for Security

Simplicity is a security control: fewer opportunities for mistakes, and
mistakes that do occur are easier to see — the code-level face of
[design for understandability](design-for-understandability.md).

- **Avoid multilevel nesting.** Unit tests cover the happy path;
  error-handling paths in deeply nested code often go untested, and a
  swapped error branch there can be a crash (reliability) or a mishandled
  authorization-check error (security). Flattening checks so each error
  is handled where detected makes such bugs visible at a glance.
- **Eliminate YAGNI smells.** Speculative "might need it later"
  parameters and interfaces must be documented, tested, and maintained,
  and force callers to handle cases that never occur. Implement only
  what's needed; generalize later from real examples (incremental
  design) — it's easier to design the right interface from several
  concrete classes than to guess.
- **Repay technical debt deliberately.** TODO/FIXME shortcuts are fine
  *with a process*: erroneous exception handling and workaround
  complexity breed vulnerabilities that testing misses (rare paths) and
  that surface in production. Tools: code-health dashboards (coverage,
  TODO age, complexity metrics), linters with autofix, alerts on
  threshold drops, and cultural support — fixit weeks, recognition for
  health contributions.
- **Refactor — but never mix refactoring and functional changes in one
  commit.** Refactoring commits are large and hard to review; a hidden
  functional change is where bugs slip in. For inherited codebases, first
  raise test coverage to a level that makes refactoring safe (and
  remember 100% coverage with meaningless tests proves little — fuzzing
  complements it).
