---
type: concept
title: DAMP Over DRY in Test Code
description: >
  Test code should favor Descriptive And Meaningful Phrases over Don't
  Repeat Yourself — some duplication is fine when it keeps each test
  self-contained and verifiable at a glance, because tests have no test
  suite of their own.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 14"
---

Production code favors **DRY** ("Don't Repeat Yourself") because it eases
changes at the cost of reference-chasing — a good trade when a test suite
backstops correctness. Test code has no such backstop (tests can't practically
have their own tests), and tests are *meant* to break when behavior changes,
so DRY's change-easing benefit is weaker while the readability cost is worse.

Test code should favor **DAMP** — "Descriptive And Meaningful Phrases": some
duplication is acceptable if it makes a test simpler and self-contained. DAMP
complements DRY; helpers are still valuable for truly irrelevant repetitive
steps, as long as the goal is descriptiveness, not repetition reduction alone.

**Pitfalls of over-sharing**:

- **Shared module-level constants** force readers to scroll elsewhere; prefer
  helper methods with defaults (Builder pattern, named parameters) so each
  test specifies only values it cares about.
- **`@Before`/setUp shared setup** hides values specific tests depend on —
  override directly in the test when a value matters.
- **General-purpose `validate()` helpers** at the end of every test obscure
  intent and cause one bug to fail many tests; use narrow helpers asserting
  one conceptual fact.
- **Shared test infrastructure across suites** should be treated more like
  production code — many callers, harder to change, needs its own tests.

**Don't put logic in tests**: operators, loops, and conditionals force mental
computation instead of reading values off the screen. Prefer straight-line code
and duplicated literal expected values over clever test logic — even one
string concatenation building an expected URL can hide bugs visible once the
full literal is spelled out.

Write **clear failure messages**: state expected outcome, actual outcome, and
relevant parameters. Assertion libraries that receive the actual subject
(e.g. Truth's `assertThat(colors).contains("orange")`) beat boolean-only
asserts.

See [test behaviors not methods](test-behaviors-not-methods.md) and
[AAA test structure](aaa-test-structure.md).
