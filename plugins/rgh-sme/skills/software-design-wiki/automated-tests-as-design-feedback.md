---
type: concept
title: Automated Tests as Design Feedback
description: >
  Tests surface coupling and responsibility problems early as first clients of
  the code — and a trusted suite is prerequisite for confident change at modern
  development speed.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

Two motivations for automated testing: preventing bugs from reaching users (cost
grows exponentially the later a bug is found) and supporting confident change
(refactors, redesigns, new features). Companies that iterate faster adapt better;
robust testing lets teams embrace change rather than fear it.

**Tests improve design** — as "first clients" of the code, tests surface problems
early: tight database coupling, unsupported use cases, unhandled edge cases —
pushing toward more modular software. This aligns with [testability as a good
negative indicator](goal-of-unit-testing.md) of structure.

Creating and maintaining a healthy suite takes real effort. As codebases grow,
suites face instability and slowness; failing to address these cripples value.
Tests derive worth from **engineer trust** — a bad suite can be worse than none.

## Scale lesson (Google Web Server)

Early Google assumed smart engineers made testing unnecessary. GWS (search web
server) suffered worst: by 2005, productivity slowed, releases got buggier, and
engineers lacked change confidence — over 80% of production pushes contained
user-affecting bugs requiring rollback. Engineer-driven automated testing (all
new changes require tests, run continuously) cut emergency pushes by half within
a year despite record growth. Today GWS has tens of thousands of tests and
releases almost daily.

Key insight: even one bug per engineer per month across a large team produces
many new bugs daily; fixing one can cause another. Automated tests turn
collective wisdom into a shared resource — one engineer writes a test, everyone
benefits — versus each engineer debugging the same bug repeatedly.

Modern applications (millions of lines, hundreds of libraries, many platforms,
multiple daily releases) cannot be manually validated at scale. Automation is the
only scalable answer: writing tests (shared across engineering), running tests
(constantly), reacting to failures (minutes, not days).

## Benefits

- **Less debugging** — regressions caught before production; a test written once
  pays dividends across dozens of future modifications.
- **Confident changes** — important behaviors continuously verified; encourages
  [refactoring](refactoring-preserves-behavior.md) when behavior is preserved.
- **Executable documentation** — clear, focused tests document behavior (when kept
  concise).
- **Simpler reviews** — verify each case has a passing test.
- **Thoughtful design** — difficulty testing new code signals too many
  responsibilities or unmanageable dependencies.
- **Fast releases** — daily releases require a healthy automated suite.

## Beyoncé Rule

Test everything you don't want to break: "If you liked it, then you shoulda put
a test on it." Infrastructure-wide changes rely on this — if changes pass all
your tests but break your product, add the missing tests.

## Testing for failure

Write tests simulating common failure modes — exceptions in unit tests, RPC errors
and latency in integration/end-to-end tests. Predictable response to adverse
conditions marks reliable systems.

See [test value versus maintenance cost](test-value-vs-maintenance-cost.md),
[coverage metrics as negative indicator](coverage-metrics-as-negative-indicator.md),
and [test size versus test scope](test-size-vs-test-scope.md).
