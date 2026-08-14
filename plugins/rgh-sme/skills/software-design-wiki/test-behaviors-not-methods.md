---
type: concept
title: Test Behaviors Not Methods
description: >
  A behavior is a guarantee about response to inputs in a given state;
  methods and behaviors are many-to-many — so name and structure tests around
  behaviors, not production method names.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 14"
---

The instinctive pattern — one test method per production method — degrades as
production methods grow complex, because a single method often implements
several behaviors with edge cases.

A **behavior** is any guarantee a system makes about its response to inputs
in a given state, expressible as given/when/then (e.g. "Given an empty
account, when withdrawing money, then the transaction is rejected"). Methods
and behaviors are many-to-many: most nontrivial methods implement multiple
behaviors; some behaviors span multiple methods.

Splitting method-oriented tests into one test per behavior costs boilerplate
but reads more like natural language, expresses cause/effect clearly, and
makes coverage gaps easier to spot.

Every behavior has **given** (setup), **when** (action), and **then**
(validation) — also called arrange/act/assert. Making this structure explicit
(via comments, whitespace, or BDD frameworks) supports three reading levels:
test name (rough), given/when/then (formal), code (precise). The common
violation is interspersing assertions among calls (merging when and then).

**Name tests after the behavior**: method-oriented names like `testUpdateBalance`
lose information. Behavior-driven names describe action, outcome, and sometimes
starting state — critical because the test name is often all that appears in
failure reports. A reliable trick: start with "should" (e.g.
`shouldNotAllowWithdrawalsWhenBalanceIsEmpty`). If a name needs "and," split
the test — it probably covers multiple behaviors.

A test should be **complete** (body contains everything needed to understand
how it reaches its result) and **concise** (nothing else distracting). Hide
irrelevant setup in helpers; expose the specific inputs that matter directly
in the test body.

See [AAA test structure](aaa-test-structure.md), [given-when-then as AAA
for non-programmers](aaa-test-structure.md), and [DAMP over DRY in test
code](damp-over-dry-in-tests.md).
