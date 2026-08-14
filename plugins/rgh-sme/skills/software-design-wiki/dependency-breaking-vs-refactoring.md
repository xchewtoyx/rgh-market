---
type: concept
title: Dependency-Breaking Techniques vs. Ordinary Refactoring
description: >
  Ordinary refactoring assumes a test suite already exists as a safety net;
  dependency-breaking techniques are a distinct catalog of transformations
  meant to be performed without tests, specifically to get tests in place.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), Introduction"
---

Ordinary refactoring, in the sense most commonly taught, assumes you already
have a test suite to catch regressions while you restructure code. That
assumption doesn't hold for [legacy code](legacy-code-definition.md) by
definition — there are no tests yet, which is exactly the problem that needs
solving.

Dependency-breaking techniques exist for this specific situation: a distinct
catalog of transformations, deliberately performed *without* the safety net
of tests, whose purpose is to loosen a piece of code's dependencies just
enough to get it under test at all. Once tests exist, ordinary refactoring
becomes possible again. This ordering matters: attempting standard,
test-assuming refactoring moves on untested legacy code carries real risk,
because there's nothing to catch a mistake — the dependency-breaking
catalog is deliberately narrower and more conservative for exactly that
reason. See [seams](seam.md) for the underlying mechanism most of these
techniques rely on.
