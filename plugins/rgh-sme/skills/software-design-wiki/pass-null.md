---
type: concept
title: Pass Null (as a Dependency-Breaking Technique)
description: >
  When a constructor parameter is hard to construct and isn't actually
  needed for the behavior under test, pass null and let a runtime exception
  reveal whether that assumption was wrong — safe in managed languages,
  dangerous in C/C++.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

When a constructor parameter is hard to construct in a test and isn't
actually exercised by the behavior under test, just pass `null`. If the code
path under test does try to use it, a runtime exception surfaces immediately
and is caught by the test harness — that failure is the signal the parameter
*is* needed there after all, and only then is it worth building a real or
[fake](fake-objects.md) value for it.

This is safe in Java, C#, and any language with runtime null-dereference
exceptions, where an unexpected dereference fails loudly and immediately.
It is **not safe in C/C++** unless you specifically know the runtime traps
null-pointer errors — otherwise a null dereference risks silent memory
corruption in your tests rather than a clean failure, defeating the purpose.

This is a test-only license — the rule for production code is the opposite:
**"Don't pass null in production code unless you have no other choice."**
The production-code alternative for a collaborator that might legitimately
be absent is the [null object pattern](null-object-pattern.md), not passing
null and hoping callers check.
