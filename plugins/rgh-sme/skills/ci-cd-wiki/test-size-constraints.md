---
type: concept
title: Test Size Constraints
description: >
  Test size classifies how many resources a test consumes and what runtime
  operations it may perform — enforced by testing infrastructure so fast,
  deterministic suites stay fast.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Test Size Constraints

**Test size** measures resources required to run a test — memory, processes,
time, blocking I/O — not lines of test code. Size is distinct from
[test scope](test-scope-dimensions.md) (how much code is validated). A
narrow-scoped test can be medium-sized if it needs a real browser; a
broad-scoped server test can stay small if every out-of-process dependency is
doubled.

Google encodes size as **infrastructure-enforceable constraints** so teams
cannot accidentally turn a fast suite slow or nondeterministic:

- **Small** — single process (often single thread); test code runs in the
  same process as the code under test. No separate server process, no
  third-party programs (databases, browsers). No sleep, blocking I/O, or
  network/disk access (in-memory filesystem implementations are allowed).
  Forces [test doubles](independent-testability.md) for code that normally
  touches the outside world. Matches the isolation goals of
  [commit test suite design principles](commit-test-suite-design.md).
- **Medium** — may span multiple processes and threads; blocking calls
  allowed, but network access restricted to **localhost only** — enough for
  a real database instance, combined UI/server tests, or WebDriver-driven
  browser. OS and third-party process behavior introduce more slowness and
  nondeterminism than small tests; engineers must treat constraints as
  safety rails that are now partially off.
- **Large** — no localhost restriction; test and system-under-test may span
  multiple machines (remote clusters). Highest flexibility and highest
  flakiness risk. Reserved mainly for full-system end-to-end validation of
  configuration (not code) and legacy components where doubles are
  infeasible. Often isolated from developer presubmit — see
  [presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md) and
  [large test SUT forms](large-test-sut-forms.md).

Enforcement varies by language — e.g. Java tests tagged "small" run under a
custom security manager that fails on prohibited operations such as opening a
network connection.

Google encourages writing **small tests whenever possible**, regardless of
scope, because even a few hundred tests with occasional flakes can drain
engineering time at scale — see
[a few reliable tests beat many unreliable ones](reliable-tests-over-coverage.md).
