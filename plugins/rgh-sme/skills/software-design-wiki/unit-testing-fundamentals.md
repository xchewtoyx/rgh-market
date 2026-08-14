---
type: concept
title: Unit Testing Fundamentals
description: >
  A unit test exercises the most atomic behavioral units of a system in
  isolation, and must run fast and localize failures well — a test that
  touches a database, network, filesystem, or special environment setup
  isn't a unit test, whatever harness it runs in.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 2"
---

Units are the most atomic behavioral units of a system — functions in
procedural code, classes in object-oriented code. True isolation is rare in
practice, since classes almost always collaborate with other classes. A
**test harness** is the generic term for the testing code written to
exercise some piece of software, plus whatever code is needed to run it.

Large, high-level tests matter too, but they have three specific problems
compared to small ones: **error localization** — the further a test is from
what it exercises, the harder it is to pinpoint the cause of a failure;
**execution time** — large tests are slow, and slow tests stop getting run;
and **coverage** — it's hard to trace which code paths a high-level test
actually exercises, and adding new code may require a lot of extra work to
exercise it at that level. Error localization is achievable with large tests
too, in principle, *if* you run them often enough after every small change —
but slow execution time makes that impractical, which is exactly the vicious
cycle that keeps large test suites from being run.

Two qualities define a good unit test: it runs fast, and it helps localize
problems. A quantified claim worth internalizing: "A unit test that takes
1/10th of a second to run is a slow unit test." The math matters at scale —
3,000 classes with 10 tests each is 30,000 tests; at 0.1s each that's nearly
an hour to run the full suite, but at 0.01s each it's 5-10 minutes. Test speed
is directly tied to how often people are willing to run the suite, and hence
to how quickly they get [feedback](regression-testing-as-a-software-vise.md).

A test is explicitly *not* a unit test if it does any of the following: talks
to a database, communicates across a network, touches the file system, or
requires special environment setup (editing config files) to run. These
other kinds of tests aren't bad, and are often worth writing — even inside
unit-test harnesses — but must be kept clearly separable from the true fast
unit-test set. Higher-level tests spanning multiple classes still have a
place: they can pin down behavior for a group of classes at once, which can
in turn make it easier to subsequently write per-class unit tests.

How easy a piece of code is to get into this kind of harness at all is a
property of the code's own design, not just of testing skill — see
[testability](testability.md). The [classical versus London unit testing
schools](classical-vs-london-unit-testing-schools.md) disagree on whether
collaborators must be replaced in unit tests; classical style allows
exercising several in-process classes together when tests don't share mutable
state.
