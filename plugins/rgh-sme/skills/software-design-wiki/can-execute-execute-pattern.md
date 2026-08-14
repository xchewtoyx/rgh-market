---
type: concept
title: CanExecute Execute Pattern
description: >
  Split a guarded command into CanExecute (eligibility check returning an
  error or null) and Execute (precondition-enforced mutation) so controllers
  stay thin and eligibility rules stay unit-testable on the domain object.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 7"
---

When conditional logic needs more out-of-process data mid-flow, or writes depend
on intermediate results, the clean read-decide-act structure breaks. Three
options each sacrifice one of domain testability, controller simplicity, or
performance — pushing all I/O to the edges wastes calls; injecting out-of-process
deps into the domain destroys testability; granular steps preserve performance
and testability at the cost of controller complexity.

**CanExecute/Execute** mitigates fragmented guards: add `CanChangeEmail()`
returning an error or null, and make `Precondition.Requires(CanChangeEmail() == null)`
the first line of `ChangeEmail()`.

Benefits:

- Controller calls `CanChangeEmail()` once — can bundle many validations.
- Precondition guarantees `ChangeEmail()` cannot run without the check — no
  duplicate decision logic to test in the controller.
- Eligibility rules stay on the domain object, unit-testable in memory.

Refinement: use a proper `Result` type instead of bare strings for errors.

Contrast placing the check only in the controller (fragments rules, lets other
callers bypass) versus inside `ChangeEmail` alone (may fetch data unnecessarily).

See [domain events for deferred side effects](domain-events-for-deferred-side-effects.md)
and [defer side effects for testability](defer-side-effects-for-testability.md).
