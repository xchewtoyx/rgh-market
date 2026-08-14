---
type: concept
title: Measure Before Modifying for Performance
description: >
  Performance intuition is unreliable even for experienced developers, so
  measure before changing anything, both to find where tuning actually
  matters and to confirm afterward whether a change helped at all.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 20"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2"
---

Acting on performance intuition risks wasted effort on non-impactful changes
plus added complexity for no real gain. Measure first, for two purposes:
locating where tuning effort will actually matter — top-level system timing
alone tells you the system is slow but not *why*, so you need to measure
deeply enough to isolate a small number of specific hot spots where you also
have a concrete idea for improvement — and establishing a baseline so
post-change measurements can confirm whether the change actually helped.

The explicit discipline that closes the loop: if a change doesn't produce a
measurable improvement, back it out, unless it happened to simplify the code
anyway. There's no reason to keep added complexity that buys no real
speedup.

**Three general approaches to fast software**, contrasted by Fowler: (1)
**time budgeting** — each component gets a hard resource budget; essential
for hard real-time systems (e.g. pacemakers) but inappropriate for typical
business systems; (2) **constant attention** — every programmer optimizes
continuously; criticized as ineffective because it spreads narrow-context
"optimizations" (often based on misunderstanding compiler, runtime, or
hardware behavior) throughout the program, degrading maintainability for
little actual speed payoff, since most of a program's time is spent in a
small fraction of its code; (3) **profile-then-tune** — the recommended
approach, and the one this note's own discipline embodies: build
well-factored code ignoring performance, then run a profiler to find the
actual small hot-spot fraction of code, optimize just that in small, tested,
measured steps.

Illustrative case: on the Chrysler C3 payroll project, the team speculated
confidently about a performance bottleneck and was completely wrong — only
profiling revealed the true cause (redundant date-object creation feeding
mostly-empty range objects). The five-minute fix, returning a shared empty
singleton from a factory method that had originally been extracted purely
for clarity, doubled system speed. Stated moral: **"Even if you know exactly
what is going on in your system, measure performance, don't speculate."**
