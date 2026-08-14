---
type: concept
title: Complexity (Software Design)
description: >
  Complexity is anything about a system's structure that makes it hard for a
  person to understand and modify, and it is the central problem software
  design exists to manage.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), Preface, ch. 1-2"
---

Programming's binding constraint isn't a physical law but human ability to
hold a system in mind. As a system grows, complexity accumulates in the form
of dependencies and obscure interactions between its parts. Left unmanaged,
this complexity compounds: it slows development and causes bugs, and fixing
those bugs under time pressure tends to add more complexity rather than
remove it, which slows the next round of development further. A codebase can
decay this way even though every individual change was locally reasonable.

Because complexity is a property of the system as experienced by the people
working on it, not an objective measure of the problem being solved, a
simpler design for the same problem is always possible in principle — the
goal of design is to find it. Complexity is not the same thing as size or
sophistication: a large, sophisticated system that stays easy to work on is
not complex by this definition, and a small, unsophisticated one can be. It
is also not evenly distributed or evenly experienced: overall complexity is
better modelled as a sum over the system's parts of each part's complexity
weighted by how much time developers actually spend working in that part
(`C = Σ cp·tp`). A messy corner of the code that's rarely touched costs the
project far less than a messy corner on the critical path — isolating
complexity somewhere it's seldom touched is nearly as good as eliminating it.

Complexity is also more apparent to readers of code than to its writer: if
you believe your code is simple but the people who have to work with it find
it complex, it *is* complex — that gap is worth investigating rather than
dismissing, because the job is to write code others can work with easily, not
just code you personally find easy.

There are two general strategies for fighting complexity, and most design
techniques are an instance of one or the other: see
[eliminating vs. encapsulating complexity](eliminating-vs-encapsulating-complexity.md).
Complexity shows up in three observable symptoms —
[change amplification](change-amplification.md),
[cognitive load](cognitive-load.md), and
[unknown unknowns](unknown-unknowns.md) — produced by two underlying causes,
[dependencies](dependencies-as-a-cause-of-complexity.md) and
[obscurity](obscurity.md). It also
[accumulates incrementally](incremental-accumulation-of-complexity.md) rather
than arriving in one catastrophic mistake.
