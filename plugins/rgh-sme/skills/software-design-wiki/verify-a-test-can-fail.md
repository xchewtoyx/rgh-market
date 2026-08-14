---
type: concept
title: Verify a Test Can Fail
description: >
  Before trusting a new test to protect anything, confirm it actually goes
  red by temporarily injecting a deliberate fault into the code it exercises
  — a test that can't fail proves nothing about the code, however
  reassuring it looks.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 4"
---

**"Always make sure a test will fail when it should."** Technique:
temporarily inject a deliberate fault into the code under test — multiply a
calculation by 2, flip a comparison — and confirm the test goes red before
trusting that it actually protects anything, then revert the fault. A test
that passes without ever having been observed to fail might be checking
nothing at all, whether from a typo in the assertion, a fixture that never
reaches the code path it claims to, or an assertion that's trivially true
regardless of the code's behavior.

This is a specific, common pattern when adding tests to code that's
presumed already correct: write the test with a placeholder expected value,
replace the placeholder with the code's actual (trusted) output, inject a
fault to confirm the test can fail, then revert the fault. See [self-testing
code](self-testing-code.md) for why the tests this technique protects are
worth having in the first place.
