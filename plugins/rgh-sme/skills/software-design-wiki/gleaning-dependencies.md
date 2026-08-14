---
type: concept
title: Gleaning Dependencies
description: >
  When a monster method mixes critical logic with low-risk secondary logic,
  test only the critical part thoroughly, then extract the secondary part
  without dedicated tests of its own, trusting that a visible break would
  be immediately obvious.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

For a [monster method](monster-methods.md) that mixes **critical logic**
(must be preserved exactly, and a silent bug could go unnoticed for a long
time) with **secondary logic** (necessary, but low-risk — if broken, the
breakage would be immediately obvious, like cosmetic display code): write
tests that pin down only the critical behavior. Once confident those are
solid, extract the *uncovered* secondary code without dedicated tests of its
own, relying on the fact that the critical-path tests would likely still
catch any accidental interference between the two.

Worked example: a method mixing a conditional display call (low risk if
broken — visibly wrong on screen) with the actual logic deciding whether and
how to add an entry to a list (higher risk — a silent bug here could hide
for a long time). Tests are written for the add-logic branches; the display
code is then extracted without its own tests, trusting it's disentangled
enough not to threaten the tested logic.

Honest self-assessment: "in some ways, Gleaning Dependencies feels like a
cop-out... but not all behaviors are equal in an application. Some are more
critical, and we can recognize that when we work." This is worth reaching
for specifically when genuinely critical logic is tangled together with
lower-stakes logic — it lets you make real progress on the untested parts
without compromising confidence in the parts that actually matter most.
