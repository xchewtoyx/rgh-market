---
type: concept
title: Test and Fake Class Naming Conventions
description: >
  Consistent prefix/suffix conventions for test, fake, and testing-subclass
  names cluster related files alphabetically, and the actual governing
  criterion is navigation ergonomics, not any specific scheme.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 18"
---

Absent deliberate convention, test code proliferates until it's hard to
tell test files from production files at a glance. A workable scheme:

- Name each test class as a variant of the class it tests — either
  `Test`-prefixed or `Test`-suffixed. The suffix form has a practical edge:
  alphabetical class listings then place a class directly next to its test.
- Prefix [fake objects](fake-objects.md) with `Fake` (e.g. `FakeAccountOwner`)
  — clusters all fakes together alphabetically, separate from the
  production classes they're often subclassed from.
- Prefix throwaway [Subclass and Override Method](subclass-and-override-method.md)
  test subclasses with `Testing` (e.g. `TestingCheckingAccount`) — clusters
  all such subclasses together too.

This is explicitly non-dogmatic about the exact scheme: "ergonomics is
important... how easy will it be to navigate back and forth between your
classes and your tests" is the actual governing criterion, not any
particular naming convention per se. See
[test code location](test-code-location-tradeoffs.md) for the complementary
decision about where these files physically live.
