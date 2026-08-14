---
type: concept
title: Brittle Over-Specified Tests
description: >
  Tests that over-specify expected outcomes or rely on heavy mock boilerplate
  resist refactoring and fail on unrelated changes — eventually discouraging
  the code changes the suite was meant to enable.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Brittle Over-Specified Tests

As codebases grow, **brittle tests** become change blockers: they fail when
unrelated features change — a five-line feature update breaking dozens of
tests — and teams grow reluctant to refactor. Common causes:

- **Over-specified assertions** — checking incidental details (exact log
  strings, call order, internal state) instead of the behavior that matters.
- **Misused mocks** — elaborate mock setup that encodes implementation
  details rather than boundaries; at Google, mock misuse was severe enough
  that some teams adopted "no more mocks" policies. See
  [independent testability](independent-testability.md) for when doubles and
  service virtualization are appropriate.

Brittle tests violate the purpose of
[continuous integration](continuous-integration.md): automation should increase
confidence to change, not freeze structure. Remedies align with
[tests obvious upon inspection](test-obvious-upon-inspection.md) and
[commit test suite design principles](commit-test-suite-design.md) — prefer
real dependencies when feasible, stub only at true system boundaries, and
delete or rewrite tests that fail without product regressions.

Pair with [developer-owned test suite maintenance](developer-owned-test-maintenance.md):
the authors of production code are best positioned to keep tests maintainable.
