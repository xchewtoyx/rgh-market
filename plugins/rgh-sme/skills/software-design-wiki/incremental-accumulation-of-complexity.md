---
type: concept
title: Complexity Accumulates Incrementally
description: >
  Software complexity is almost never the result of one catastrophic
  decision; it builds from hundreds of individually insignificant
  dependencies and obscurities, which is what makes it hard to control.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

Each small shortcut — a slightly hardcoded value, a slightly unclear name, one
more special case — is individually easy to rationalize: "a little complexity
from my change is no big deal." But if every developer reasons this way on
every change, the small amounts compound, and eventually every task touches
several of these accumulated issues at once.

This incremental nature also makes complexity resistant to after-the-fact
cleanup: fixing any single instance doesn't visibly improve anything, because
the system's difficulty was never attributable to that one instance in the
first place — which removes the usual incentive to clean it up. The
implication is a "zero tolerance" stance toward introducing *any* new
complexity, however small, rather than waiting to address complexity once it's
become a visible problem; see
[strategic vs. tactical programming](strategic-vs-tactical-programming.md) for
the mindset this requires.
