---
type: concept
title: Handling Bugs Found During Characterization
description: >
  Characterizing legacy code inevitably surfaces bugs, roughly in proportion
  to how little the code was previously understood — the response differs
  for undeployed versus deployed systems.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

Writing [characterization tests](characterization-tests.md) inevitably
surfaces bugs, usually in direct proportion to how little the surrounding
code was understood beforehand. For an undeployed system, just fix the bug
outright. For a deployed system, first consider whether some caller may
already — perhaps unknowingly — depend on the buggy behavior, which requires
more careful analysis before changing it, since "fixing" it could itself be
the behavior-breaking change. A reasonable default: fix clear-cut bugs
immediately, but for merely *suspected* bugs, mark the test as suspicious in
the code and escalate quickly to resolve the ambiguity rather than let it
linger unaddressed.
