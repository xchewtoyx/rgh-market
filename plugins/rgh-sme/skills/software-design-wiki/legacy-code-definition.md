---
type: concept
title: Legacy Code Is Code Without Tests
description: >
  The actionable definition of legacy code isn't age or ugliness — it's the
  absence of tests, because without tests there's no way to verify whether a
  change made the code better or worse.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), Preface"
---

The common industry sense of "legacy code" is old, tangled, difficult to
change, or inherited from someone else. The more useful, actionable
definition: code without tests. Code without tests is bad code, regardless of
how well written it is — "it doesn't matter how pretty or object-oriented or
well-encapsulated it is." With tests, a change to behavior can be made
quickly and verifiably; without them, there's no way to know whether the
codebase is getting better or worse as it's modified.

This holds even for very clean, well-structured code: changing it at scale
without tests is "aerial gymnastics without a net." Teams with exceptionally
clear code are rare, and even they are slower to change safely without tests
than teams that have both clarity and tests. This definition matters because
it points directly at the fix: getting a piece of code under test is the
actionable first step for making it safe to change, independent of how old or
how clean it already is. See
[dependency-breaking techniques](dependency-breaking-vs-refactoring.md) for
the specific discipline of getting tests in place around code that doesn't
have them yet.
