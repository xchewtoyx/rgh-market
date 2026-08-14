---
type: concept
title: Simplicity and Performance Are Compatible Goals
description: >
  Simplicity and performance aren't in tension — complicated code tends to
  be slow because it does extraneous or redundant work, so clean, simple
  code is usually fast enough on its own without dedicated performance work.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 20"
---

The most important idea for performance is still [simplicity](complexity.md):
not only does simplicity improve a system's design, it usually makes systems
faster too. [Defining special cases out of existence](design-special-cases-out-of-existence.md)
removes the checks needed to detect them, directly saving cycles.
[Deep classes](deep-modules.md) are more efficient than shallow ones because
each method call accomplishes more relative to its own call overhead —
shallow classes multiply layer crossings, and every layer crossing adds
overhead.

In the rarer cases where dedicated optimization genuinely is warranted, the
same underlying value is still the operative tool: identify the truly
performance-critical paths and make *those specifically* as simple as
possible — see
[designing around the critical path](design-around-the-critical-path.md). A
worked rewrite of a buffer-management class delivered roughly a 2x speedup
*while* simplifying the design and cutting code size by 20% in the same
change — see the
[worked critical-path example](ramcloud-buffer-critical-path-example.md) —
concrete evidence that clean design and high performance are not competing
goals.
