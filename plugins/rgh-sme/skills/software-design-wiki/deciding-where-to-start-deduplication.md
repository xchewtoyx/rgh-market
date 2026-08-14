---
type: concept
title: Deciding Where to Start When Several Groupings Are Possible
description: >
  Different starting points for extracting a repeated sequence often
  produce structurally equivalent alternate groupings — pick whichever
  grouping yields a name that makes sense in context, since either can be
  refactored into the other later.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 21"
---

A repeated call sequence often admits more than one reasonable way to
group it into extracted methods. Abstract illustration: a sequence of calls
`a(); a(); b(); a(); b(); b();` could be grouped as "two a's, then b, then a,
then two b's" or split differently — different starting points produce
structurally equivalent alternate groupings, and neither is a wrong or final
choice, since either can be refactored into the other later if it turns out
not to fit.

The tie-breaker: **choose based on which grouping yields a name that makes
sense in context** — a grouping with no good name is a signal it doesn't
correspond to a real concept yet, even if it's mechanically valid. Secondary
heuristic when a name doesn't immediately settle it: prefer removing the
smallest pieces of duplication first, since clearing small duplication
clarifies the bigger picture and often makes the right grouping, and its
name, obvious in hindsight. See
[designs emerge from zealous duplication removal](duplication-removal-as-emergent-design.md)
for how this plays out across a whole worked refactoring sequence.
