---
type: concept
title: Test Size Versus Test Scope
description: >
  Test size (resources consumed) and test scope (code validated) are related
  but distinct dimensions — Google encodes size as infrastructure constraints
  to keep small tests fast and flake-resistant at scale.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

Every test has two distinct dimensions:

- **Size** — resources required to run (memory, processes, time), determined by
  *how* the test runs, not lines of code.
- **Scope** — how much code is validated (narrow unit → broad end-to-end).

Executing a line differs from verifying it worked; size and scope correlate but
do not always align.

## Test sizes (Google)

- **Small** — single process (often single thread); test and SUT in same process;
  no sleep, blocking I/O, network, or disk (in-memory filesystem allowed).
  Cannot hit main slowness/nondeterminism sources. [Test doubles](test-doubles-overview.md)
  required for I/O-dependent code.
- **Medium** — multiple processes, threads, blocking calls; network to localhost
  only (real database, WebDriver browser). "Safety is off" — more slowness/flake
  risk.
- **Large** — no localhost restriction; multi-machine; reserved for full-system
  validation and legacy without feasible doubles. Often isolated to build/release.

**Flaky tests are expensive**: 0.1% flake rate × 10,000 daily runs ≈ 10
investigations/day. As flakiness approaches 1%, teams lose trust and stop
reacting — the suite loses all value. Most flakes stem from test nondeterminism
(clocks, threads, network, rendering).

**Properties for all sizes**:

- **Hermetic** — contains all setup/execute/teardown information; no assumed
  shared environment or execution order.
- **Obvious upon inspection** — only information needed to exercise the behavior;
  no control flow (conditionals, loops) in tests. "Write the test you'd like to read."

## Test scope

- **Narrow (unit)** — validates logic in a small focused part (class/method).
- **Medium (integration)** — verifies interactions between a few components.
- **Large (functional/end-to-end/system)** — validates several parts or emergent
  behaviors.

"Narrow scope" refers to code *validated*, not code *executed* — unit tests
naturally invoke dependencies. Google [prefers real implementations in
tests](prefer-real-implementations-in-tests.md) when feasible. A broad-scoped
server-endpoint test can still be small with doubles for all out-of-process deps;
a narrow UI date-picker test may require a browser (medium size).

See [test pyramid](test-pyramid.md) and [four pillars of a good unit test](four-pillars-of-a-good-unit-test.md).
