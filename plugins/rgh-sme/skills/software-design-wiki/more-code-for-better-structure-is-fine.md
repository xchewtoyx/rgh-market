---
type: concept
title: More Code for Better Structure Is a Fine Trade
description: >
  Introducing extra functions or an intermediate data structure to separate
  concerns can raise the total line count, and that's an acceptable price
  when it buys clarity and reuse — brevity is not the goal.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 1"
---

Splitting a calculation from its rendering (see [Split
Phase](split-phase.md)) or otherwise introducing structure to separate
concerns often makes total line count go up, purely from the wrapping that
introducing functions and data structures requires. "If all else is equal,
more code is bad, but rarely is all else equal" — the extra structure
separates concerns and enables reuse without duplication, which is worth
more than the raw line-count increase.

**"Brevity is the soul of wit, but clarity is the soul of evolvable
software."** This complements [designing for ease of reading, not
writing](design-for-reading-not-writing.md): both reject optimizing for how
little the author has to type, but this note is specifically about accepting
a larger total surface area (more functions, an added intermediate
structure) as the price of separating concerns cleanly, rather than about
choosing better names or types for a given amount of code.
