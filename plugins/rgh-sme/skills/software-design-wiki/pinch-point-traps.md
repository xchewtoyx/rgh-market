---
type: concept
title: Pinch Point Traps
description: >
  Pinch-point tests are a legitimate first step in legacy code but a de
  facto integration test if kept permanently — the goal is to shrink them
  away once each individual class gets its own narrower unit tests.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 12"
---

A [pinch-point](pinch-point.md) test instantiates several real collaborators
together to test the cluster as a whole. This risks the same drift unit
tests always risk toward de facto integration tests: it increases confidence
but, at scale, produces "big, bulky unit tests that take forever to run" —
the same speed problem [unit testing fundamentals](unit-testing-fundamentals.md)
warns about generally. The standard remedy for *new* code is to test classes
as independently as possible, faking out collaborators, since "the job of a
unit test isn't to see how a cluster of objects behaves together, but rather
how a single object behaves."

**For legacy code specifically, the tables are turned**: deliberately
carving off and characterizing a whole cluster at a pinch point is a
legitimate, even necessary, *first* step, precisely because getting each
class independently testable up front may be prohibitively expensive.
Pinch-point tests are meant to be a temporary scaffold, not the end state:
once narrower unit tests exist for each individual class touched while
working in that area, "the tests at the pinch point can go away."

Closing metaphor: pinch-point tests are like walking into a forest and
drawing a line declaring "I own all of this area" — a claim of territory
that lets you develop (refactor, add finer tests) safely inside it, with the
broad boundary tests eventually deletable once each class inside has its own
proper coverage.
