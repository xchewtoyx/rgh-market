---
type: concept
title: Coverage Metrics as Negative Indicator
description: >
  Code and branch coverage show what ran, not what was asserted — they are
  useful warnings when low but dangerous targets when mandated, because they
  can be gamed without improving test quality.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 1"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

**Code coverage** = lines executed ÷ total lines. Restructuring code can raise
coverage without adding test value (e.g. inlining an `if` block from 80% to
100% coverage with no new assertions).

**Branch coverage** = branches traversed ÷ total branches — more precise than
line coverage because it counts control-flow branches, not formatting.

**Two fundamental problems with any coverage metric**:

1. **No guarantee outcomes are verified** — coverage shows execution, not
   checking. A method with return value and side-effect outcomes can show full
   coverage while asserting only one. **Assertion-free tests** achieve 100%
   coverage while verifying nothing.
2. **External library paths aren't counted** — wrapping `int.Parse` can show
   full branch coverage while never exercising parse failure modes inside the
   library.

**Aiming at a coverage number is dangerous.** Coverage is a good **negative
indicator** (below ~60% signals trouble) and a bad **positive indicator** (high
coverage ≠ quality). Mandating 100% incentivizes worthless tests — teams have
written assertion-free try/catch tests solely to satisfy gates.

Analogy: treating fever as the treatment goal rather than a diagnostic signal.

Guidance: pursue high coverage in core parts; avoid mandatory numeric targets.
Judge suite quality by evaluating individual tests against [the four
pillars](four-pillars-of-a-good-unit-test.md) — no automated substitute. Google
recommends measuring coverage only from small tests to avoid inflation from
larger tests. Coverage targets become ceilings — engineers land at exactly the
minimum. Ask instead: are customer-expected behaviors tested? Are dependency
breakages caught? Are tests stable?

See [goal of unit testing](goal-of-unit-testing.md) and [test value versus
maintenance cost](test-value-vs-maintenance-cost.md).
