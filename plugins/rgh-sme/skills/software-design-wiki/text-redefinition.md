---
type: concept
title: Text Redefinition
description: >
  In dynamically interpreted languages, reopen a class in the test file and
  redefine a method's body directly — the interpreter doesn't distinguish
  first definition from redefinition, but the substitution is global and
  persists for the rest of the run, risking cross-test contamination.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

In dynamically interpreted languages (Ruby is the demonstrated case), method
bodies can be redefined at runtime simply by reopening a class and providing
a new definition for the same method name — the interpreter doesn't
distinguish "first definition" from "redefinition," it just replaces
whatever was there. This isn't replacing the whole class: reopening a class
just adds or overwrites definitions on the existing class object, leaving
everything else about it untouched. No special language feature is required
beyond ordinary class-reopening semantics.

**Explicit downside**: the redefinition is global and persistent for the
remainder of the program's run — "this can cause some trouble if you forget
that a particular method has been redefined by a previous test," the same
cross-test contamination risk flagged for
[static-setter-based substitution](breaking-singleton-dependencies.md).

The same conceptual technique is achievable in C/C++ via the macro
preprocessor — see [preprocessing seams](preprocessing-seams.md) for the
equivalent mechanism in a compiled-language setting.

Steps (Ruby-specific): identify the class with definitions to replace;
require the module containing that class at the top of the test file;
reopen the class and provide alternative bodies for each method to be
replaced, before the actual tests run.
