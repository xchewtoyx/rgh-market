---
type: concept
title: Sprout Class
description: >
  When you can't even instantiate the class you need to change within a
  reasonable time, put the new behavior in a brand-new, separately
  test-driven class instead, called from the untouched original.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

The class-level escalation of [sprout method](sprout-method.md), for cases
with heavy creational dependencies or deeply hidden dependencies that would
require invasive refactoring just to get the original class compiling in a
harness. Worked example: an old report-generation method builds output
inline; adding a new section is formulated instead as a tiny, separately
TDD'd class with its own single method, called from the untouched original
method.

A small naming move matters here: giving the new class a name and method
signature that fit an existing conceptual family in the codebase (rather than
an ad hoc, isolated name) can fold it into the system's vocabulary instead of
leaving it as unrelated clutter. Not every sprouted class folds in cleanly —
some remain standalone, or later reveal duplication with other sprouts and
get merged once the pattern becomes visible. The way a sprouted class looks
when first created and the way it looks a few months later are often
significantly different.

Two situations lead here, without a hard line between them: the change is
genuinely a new *responsibility* that doesn't belong crammed into the
existing class's core purpose, or pure practical necessity — the class can't
be gotten under test at all right now. Steps mirror
[sprout method](sprout-method.md) at class granularity: identify the change
point; name and stub a new class and call site (commented out); route needed
locals into the constructor; add methods for any return values; develop the
class test-first; uncomment the call.

Advantage: you move forward with confidence without invasive changes to the
existing class (in C++, its header isn't even touched, incidentally reducing
its compile-time footprint). Disadvantage: conceptual complexity — you're
moving real logic out of the class programmers expect to hold it, sometimes
purely because there's no other option available right now.
