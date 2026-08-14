---
type: concept
title: Comment-Writing Time Is a Small, Worthwhile Investment
description: >
  Under constant time pressure, comments always look lower priority than the
  next feature, but the actual cost is small — roughly 10% of total
  development time at a generous upper bound — and it's the same investment
  mindset that applies to design generally.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 12"
---

The mechanism behind "I don't have time to write comments": under constant
delivery pressure, documentation always looks lower priority than the next
feature, and if it's allowed to be perpetually deprioritized, a codebase ends
up with none at all. This is exactly the trade-off in
[strategic vs. tactical programming](strategic-vs-tactical-programming.md) —
spend a bit more time upfront for a long-term payoff.

A rough cost estimate: if writing code (excluding comments) is roughly 10% of
total development time — with design, compiling, and testing making up the
rest — and comment-writing takes roughly as long as code-writing itself (a
generous upper bound), good comments add at most about 10% to total
development time. That's a cost the long-term maintainability benefit should
quickly outweigh; see
[benefits of well-written comments](benefits-of-well-written-comments.md).

Many of the *most valuable* comments — top-level class and method
documentation tied to abstractions — arguably belong to the design process
itself rather than being separate overhead: writing them well, at the right
time, is part of how a design gets checked and improved (see
[write the comments first](write-the-comments-first.md)). Time spent on
those particular comments is design time, and pays for itself immediately.
