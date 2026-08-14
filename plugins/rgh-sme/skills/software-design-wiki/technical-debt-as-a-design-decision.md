---
type: concept
title: Technical Debt as a Design Decision
description: >
  Deferring design quality to ship faster is a real, sometimes rational
  trade-off, but it is a decision with compounding costs, not a neutral
  default — and once a codebase has decayed far enough, it becomes very hard
  to reverse.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 3"
---

Teams under acute delivery pressure — startups especially — often rationalize
skipping design investment with "we'll hire people to clean it up later if we
succeed." The trouble is that once a codebase has turned to a tangle of
[complexity](complexity.md), it's nearly impossible to fix from the inside,
and the elevated development cost tends to persist for the product's whole
life. The [tactical](strategic-vs-tactical-programming.md) shortcut may not
even win the very first release, since the design-versus-speed payoff arrives
within a few months, not years.

There's also a talent feedback loop: hiring excellent engineers rather than
more engineers is one of the strongest levers for lowering long-run cost,
since top engineers are far more productive without costing proportionally
more — but top engineers also care about working in a well-designed codebase
and will avoid or leave a wrecked one, which pushes hiring toward mediocre
candidates and accelerates further decay.

Debt at the level of a whole codebase's file relationships — not just one
module's internal quality — can be detected and its remediation quantified
directly from historical data; see [architecture debt hotspot
anti-patterns](architecture-debt-hotspot-anti-patterns.md) and
[quantifying refactoring ROI](quantifying-refactoring-roi.md) for turning
"this codebase feels bad to work in" into specific, prioritized,
business-justified refactoring targets.

Facebook's early "move fast and break things" culture is the illustrative
case: real short-term success, but a codebase that became unstable, hard to
understand, under-commented, and painful to work in, prompting a later shift
to "move fast with solid infrastructure." Google and VMware, by contrast, took
the strategic approach from early on and built a technical reputation that
helped them win top talent. Both paths can produce a successful company —
technical debt is a choice with knowable costs, not an emergency that only
happens to unlucky teams.
