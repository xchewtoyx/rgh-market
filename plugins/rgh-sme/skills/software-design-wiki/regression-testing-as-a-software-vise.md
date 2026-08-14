---
type: concept
title: Regression Testing as a Software Vise
description: >
  Tests that detect change, rather than trying to prove correctness, hold a
  piece of behavior fixed in place like a vise — but only pay off if they
  run fast enough to be run after every small change.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 2"
---

Traditional development testing tries to show correctness, usually after the
fact, by a separate team, with a feedback loop measured in weeks or months.
The alternative useful for legacy work is regression testing in the classic
sense: periodically re-running tests that check known-good behavior to detect
whether the software still behaves as it did before. Once such tests are in
place, "the behavior of the code is fixed in place... we're in control of our
work" — a **software vise**.

The traditional way regression testing is practiced undercuts this: it's
usually done at the application or system interface (web, CLI, GUI), which is
coarse-grained, slow (overnight batch runs scheduled through a scarce shared
QA resource), and hard to attribute to a specific change when several people
were editing at once ("tests AE1021 and AE1029 failed overnight" — by whom,
for what?).

Contrast a class with roughly twenty fine-grained unit tests: refactoring in
small steps and rerunning the small suite after every tiny change can catch
an introduced bug (an inverted conditional, say) within about a minute. "Do
you want your feedback in a minute or overnight?" This is the practical case
for [fast, isolated unit tests](unit-testing-fundamentals.md) over
coarse-grained, slow ones — the same underlying mechanism, applied where
feedback speed actually matters.
