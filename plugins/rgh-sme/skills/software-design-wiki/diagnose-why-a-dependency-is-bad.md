---
type: concept
title: Diagnose Why a Dependency Is Actually Bad Before Fixing It
description: >
  Not every hard dependency needs the maximal fix of severing a whole class
  relationship — often only one method on an otherwise-fine class is the
  real problem, and only that needs isolating.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

Before reaching for full [Extract Interface](extract-interface.md) — which "brutally sever[s] the
connection to a class" — ask a more specific question: **why, exactly, is
this dependency bad?** Sometimes the type hierarchy itself makes a clean
interface extraction impractical or absurdly expensive: a field typed as a
superclass, holding either the original constructor argument or an unrelated
sibling from the same hierarchy, would force extracting a near-1:1 interface
"all the way down" the entire hierarchy just to preserve assignment
compatibility — "a ridiculous amount of work," and once every class in a
hierarchy has a parallel interface, "the design gets cluttered." (Not
forbidden if truly cornered — "if our backs are against the wall, it would
be fine" — but worth exploring alternatives first.)

Often the actual problem is narrower than the class relationship suggests:
one method on that otherwise-fine class silently does the troublesome thing
(opens a live database connection, say), while the rest of the class's
interface is harmless. In that case,
[Subclass and Override Method](subclass-and-override-method.md) on just that
one method severs the real problem without touching the class relationship
at all. This escalates back to the harder fix only if the problematic
behavior turns out to be tangled together with logic you actually need
inside one large method — at which point Extract Method is a prerequisite
before the override can isolate anything.
