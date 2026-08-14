---
type: concept
title: Mock Objects
description: >
  A mock object is a fake that additionally performs assertions internally,
  rather than just passively recording state for the test to check
  afterward — more powerful but heavier-weight, and worth reaching for only
  once hand-writing plain fakes becomes burdensome.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 3"
---

Where a [fake object](fake-objects.md) passively records what happened for
the test to inspect afterward, a mock object performs the assertion itself.
Worked example: a test calls `display.setExpectation("showLine", "Milk
$3.99")` before exercising the code, then `display.verify()` afterward,
which fails the test if the expected call didn't happen as specified.

Mock object frameworks exist for many languages but not all. "Simple fake
objects suffice in most situations" — mocks are an escalation to reach for
once hand-writing many fakes becomes burdensome, not a default first choice.

A specific risk of leaning on mocks: it's easy to slide into asserting the
exact mechanics of a call — order, arguments — rather than the system's
actual behavior. See [overabstracted tests: asserting call mechanics
instead of behavior](tests-should-assert-behavior-not-call-mechanics.md),
[mocks versus stubs taxonomy](mocks-vs-stubs-taxonomy.md), and [mock at system
edges](mock-at-system-edges.md).
