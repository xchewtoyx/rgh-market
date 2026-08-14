---
type: concept
title: Four Pillars of a Good Unit Test
description: >
  A valuable test scores on all four — protection against regressions,
  resistance to refactoring, fast feedback, and maintainability — because
  multiplying near-zero on any one pillar drives overall value to zero.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 4"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 14"
---

A good automated test (unit, integration, or end-to-end) has four foundational
attributes:

1. **Protection against regressions** — catches bugs when behavior breaks.
   Stronger when more relevant code is exercised with meaningful assertions,
   especially complex, domain-significant logic. Trivial code rarely rewards
   testing.

2. **Resistance to refactoring** — survives behavior-preserving production
   changes without false positives (false alarms). Coupling to
   [implementation details rather than observable behavior](observable-behavior-vs-implementation-details.md)
   causes false positives that erode trust — developers ignore real failures
   and stop refactoring. **Non-negotiable** among the first three: it is
   essentially binary, unlike the other two which are more continuous.

3. **Fast feedback** — slow tests discourage frequent runs, delaying bug
   discovery and raising fix cost.

4. **Maintainability** — easy to understand (size and clarity matter as
   much as in production code) and easy to run (no heavy out-of-process
   setup).

**Accuracy framing**: protection guards against false negatives (missed bugs);
resistance guards against false positives (spurious failures). Both matter.

**Value estimate** (multiplicative):

```
Value ≈ [0..1] × [0..1] × [0..1] × [0..1]
```

A test scoring zero on any pillar has zero overall value. An ideal test (1 on
all four) is impossible — the first three are mutually exclusive in the limit:

- **End-to-end tests**: high regression protection and refactoring resistance,
  but slow.
- **Trivial tests**: fast and refactor-resistant, but negligible regression
  protection.
- **Brittle tests**: fast and catch regressions, but fail on equivalent
  refactors (e.g. asserting exact SQL strings).

**Resolution**: maximize maintainability and resistance to refactoring always;
trade off regression protection versus fast feedback on a slider. Eradicating
brittleness is the first priority.

**Dynamics over time**: early in a project, false negatives dominate concern;
as code ages, false positives become equally damaging — weight both equally on
medium/large projects.

CAP-theorem analogy: as partition tolerance is non-negotiable in distributed
systems, resistance to refactoring is non-negotiable in test design; the real
slider is between regression protection and fast feedback.

See also [brittle tests and unchanging tests](brittle-tests-and-unchanging-tests.md),
[goal of unit testing](goal-of-unit-testing.md).
