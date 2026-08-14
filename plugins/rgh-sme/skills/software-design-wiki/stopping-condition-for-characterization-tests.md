---
type: concept
title: A Stopping Condition for Characterization Tests
description: >
  The space of possible characterization tests is infinite, so what stops
  the process is inspecting the code itself to generate hypotheses, and then
  checking specifically whether the accumulated tests would catch the
  planned change.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

Unlike black-box testing, "we are allowed to look at the code we are
characterizing" — inspecting the implementation is what generates hypotheses
worth turning into [characterization tests](characterization-tests.md), and
a test becomes a way of literally asking the code a question.

The stopping condition has two stages: write tests until you're satisfied
you understand the code's behavior, approached in a state of curiosity; then
check specifically whether your accumulated tests would actually detect
problems from the *planned* change. If not, add more until they would — and
if you still can't reach that confidence, it's safer to consider changing
the software in a different way, possibly scoping down to a smaller piece of
the intended change.

**The Method Use Rule**: before using any legacy method, check whether tests
exist for it — if not, write them first. This is a communication medium as
much as a safety practice: consistently-applied testing before use lets
people read tests to learn a method's actual contract, and the act of making
a class testable tends to raise its overall quality as a side effect.
