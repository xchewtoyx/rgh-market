---
type: concept
title: Construction Test
description: >
  Before guessing at what blocks a class from being testable, just try to
  construct it in a test with no assertions — the compiler and runtime
  enumerate the real obstacles for you.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

The default starting move whenever a class's testability is in question:
"The best way to see if you will have trouble instantiating a class in a
test harness is to just try to do it. Write a test case and attempt to
create an object in it. The compiler will tell you what you need to make it
really work." A **construction test** has no assertions — its only job is to
get an object to compile and construct — and is typically deleted or
repurposed once real tests exist.

This turns "will this be hard to test?" from a question answered by
inspection and guesswork into one answered empirically, one compiler error
or thrown exception at a time. It's the entry point into the rest of
[dependency-breaking for testability](dependency-breaking-for-testability.md):
whatever the construction test reveals — a hard-to-build parameter, a hidden
side effect, a buried global — determines which specific technique applies.
