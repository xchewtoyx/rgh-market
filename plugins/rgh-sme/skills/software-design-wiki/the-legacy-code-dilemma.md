---
type: concept
title: The Legacy Code Dilemma
description: >
  When we change code, we should have tests in place; to put tests in
  place, we often have to change the code first — this circularity is the
  central practical problem that dependency-breaking technique exists to
  resolve.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 2"
---

Wanting to change a method safely means wanting
[tests around it first](edit-and-pray-vs-cover-and-modify.md). But
instantiating the class or invoking the method in a test harness is often
blocked by its own dependencies — a constructor that requires a live database
connection, or an object that pulls in a whole web framework just to
construct. Getting the test in place requires changing the code to remove
that dependency; but changing code without a test is exactly the risky
"edit and pray" situation the test was supposed to prevent.

"Dependency is one of the most critical problems in software development.
Much legacy code work involves breaking dependencies so that change can be
easier." See
[dependency-breaking for testability](dependency-breaking-for-testability.md)
for how this circularity actually gets broken in practice, and
[the legacy code change algorithm](the-legacy-code-change-algorithm.md) for
where it fits into the overall process of making a change safely.
