---
type: concept
title: Benefits of Well-Written Comments
description: >
  Comments capture information that existed in the designer's mind but has
  no home in the code itself, and they map directly onto reducing cognitive
  load and unknown unknowns — the two complexity symptoms that documentation
  can actually address.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 12"
---

Comments capture information ranging from low-level rationale (a hardware
quirk motivating an odd bit of code) up to high-level concepts (why a class
exists in its current form) — information that existed in the designer's
mind but has no other home. Without that record, later developers, including
the original author after even a few weeks away, must rederive or guess at
the original reasoning, costing time and risking bugs from misunderstood
intent.

Mapped onto the three [complexity symptoms](complexity.md): good
documentation doesn't really address
[change amplification](change-amplification.md), but it substantially helps
with the other two. It reduces [cognitive load](cognitive-load.md) by
supplying exactly the needed information and letting developers safely
ignore what's irrelevant, instead of having to read large swaths of code to
reconstruct the designer's mental model. It reduces
[unknown unknowns](unknown-unknowns.md) by clarifying overall system
structure, so it's clear what information and code is actually relevant to a
given change.

Mapped onto the two root causes: since
[dependencies and obscurity](dependencies-as-a-cause-of-complexity.md) are
what produce complexity, good documentation helps by making dependencies
explicit and by filling exactly the informational gaps that create
[obscurity](obscurity.md).
