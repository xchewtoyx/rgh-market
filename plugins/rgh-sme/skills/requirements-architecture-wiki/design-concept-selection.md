---
type: concept
title: Design Concept Selection
description: >
  Finding and choosing among tactics, patterns, reference architectures,
  and off-the-shelf components is usually the hardest step in turning a
  requirement into a structure, because good options are numerous,
  scattered, and inconsistently defined.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 20"
---

See [architecture before tool selection](architecture-before-tool-selection.md)
for why this comparison has to happen before, not after, a specific
technology gets adopted.

The creative core of architectural design is not inventing a solution; it
is correctly identifying, combining, and adapting an *existing* one —
even with a well-known catalog of [tactics and
patterns](architectural-tactic.md) to draw from, this is still the hardest
single step in a method like [Attribute-Driven
Design](attribute-driven-design.md). It's hard because options are
numerous and scattered across blogs, papers, and books, often without a
canonical definition (different sources describe "the broker pattern"
inconsistently), and because a single driver can require combining several
concept types at once — a pattern, a tactic layered onto it, and a
specific framework, all addressing the same requirement together.

Three complementary ways to surface candidates: **leverage existing
catalogs** (broad, but costly to search and of uneven, hard-to-verify
quality); **leverage your own experience** (fast and confident, but risks
over-applying a familiar solution where it doesn't actually fit — "if all
you have is a hammer, all the world looks like a nail"); and **leverage
others' experience through peer brainstorming**, which draws in
backgrounds the architect doesn't personally have.

Selecting among the resulting candidates means building a pros, cons, and
cost comparison against the actual drivers — see [documenting
trade-offs](documenting-trade-offs.md) — while watching for two things a
plain quality comparison can miss: a **constraint** that eliminates an
option outright regardless of its merits (an unapproved software license
disqualifying an otherwise-ideal framework), and an **incompatibility with
a decision already made in an earlier iteration** (a web architecture
chosen in one iteration conflicting with a local-application UI framework
chosen in a later one). When the comparison itself can't resolve the
choice — genuinely new technology, no trusted information about its
fitness, unresolved configuration questions — a throwaway prototype built
purely to collect measurements is the next step; see [value of
information for prototyping](value-of-information-for-prototyping.md) for
when that prototype is actually worth its cost.
