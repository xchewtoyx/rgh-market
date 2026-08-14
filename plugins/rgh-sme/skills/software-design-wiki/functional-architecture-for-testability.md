---
type: concept
title: Functional Architecture for Testability
description: >
  Maximize purely functional decision code in a core and push all side effects
  to a thin mutable shell — a subset of hexagonal architecture taken toward
  the testability extreme.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 6"
---

**Functional architecture** maximizes code written as immutable, side-effect-free
decisions and minimizes code that performs side effects. Side effects can't be
eliminated in useful applications — they are the point — but mixing decision
logic with side effects multiplies complexity.

Two segregated responsibilities:

- **Functional core** — decisions via [pure functions](referential-transparency-and-pure-functions.md).
- **Mutable shell** — converts decisions into visible side effects (DB, bus, files).

Cooperation: shell gathers inputs → core produces decisions → shell applies
side effects. Decision objects must carry enough information that the shell
need not decide further — keep the shell "as dumb as possible." Cover the core
with [output-based tests](output-based-testing.md); leave the shell to fewer
integration tests.

**Versus hexagonal**: both separate concerns with one-way dependency flow.
Hexagonal allows in-memory side effects within the domain (mutate objects;
controller persists). Functional architecture pushes *all* side effects to the
shell — "hexagonal taken to an extreme."

**Drawbacks**:

- **Applicability** — breaks when mid-decision out-of-process queries are needed;
  remedies trade performance (query upfront) versus purity (decision bit in shell).
  Domain code must depend on collaborator *products* (values), not collaborators.
- **Performance** — production may read more data per operation (read-decide-act)
  than inlined side effects.
- **Code size** — upfront separation cost; apply strategically by complexity
  and importance.

Most OOP codebases mix output-based, state-based, and some communication-based
tests — goal is as many output-based tests as reasonably possible, not total
conversion.

See [defer side effects for testability](defer-side-effects-for-testability.md)
and [humble object pattern](humble-object-pattern.md).
