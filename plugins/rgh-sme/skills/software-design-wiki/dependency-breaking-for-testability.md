---
type: concept
title: Dependency-Breaking for Testability
description: >
  Getting an untestable class into a test harness means removing just
  enough of a specific dependency to allow instantiation, done
  conservatively and mechanically since there's no test safety net yet — a
  deliberate, sometimes ugly trade that a later test suite can heal.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 2"
---

Worked example: a class needing a database connection and a servlet object
in its constructor can't be instantiated in a test without either. Breaking
the dependency on the servlet by passing only the specific data actually
needed (an invoice ID collection) instead of the whole servlet object is the
[Primitivize Parameter](primitivize-parameter.md) refactoring. Breaking the
dependency on the database connection by introducing an interface and
coding against it instead of the concrete connection class is
[Extract Interface](extract-interface.md). Both are
part of the broader
[dependency-breaking catalog](dependency-breaking-vs-refactoring.md).

These refactorings are done *without* tests — that's the whole point of
[the legacy code dilemma](the-legacy-code-dilemma.md) they resolve — so they
must be done conservatively and mechanically. Being aggressive here risks
introducing errors with no safety net to catch them.

There's an honest trade-off: dependency-breaking sometimes produces code that
looks worse from a pure design standpoint — unneeded-looking parameters,
oddly split classes — purely to enable testing. "There might be a scar left
in your code after your work, but everything beneath it can get better." If
the area around the broken dependency can later be covered with tests, that
scar can be healed with an ordinary, test-backed
[refactoring](refactoring-preserves-behavior.md) pass.
