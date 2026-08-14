---
type: concept
title: Generate Radically Different Alternatives
description: >
  Compare options that differ fundamentally from each other, not
  minor variations on the same idea — including a deliberately
  weak alternative when you're confident only one approach is sane.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 11"
---

An options analysis earns nothing if its alternatives are all small
variations on the same underlying approach — comparing near-twins
tells you which twin is marginally better, not whether the whole
family is the right family. Deliberately choose candidates that are
**radically different** from one another: different underlying
mechanisms, different assumptions about who does the work, different
tradeoffs entirely — because the real learning happens at the points
where alternatives disagree fundamentally, not where they differ by
degree.

This holds even when you are confident there is only one sane
approach. Sketch a second, deliberately weaker alternative anyway,
and work out specifically *why* it is worse. Articulating a
concrete, named weakness in the alternative sharpens your
understanding of what actually makes the favored option good — a
recommendation that has never been compared against anything
concrete is a recommendation whose merits you have only asserted,
not demonstrated, even to yourself.

Set the evaluation criteria before ranking alternatives, and expect
different levels of a decision to warrant different criteria: a
choice between external-facing options (which one is easier for
others to work with, or more general-purpose) is a different
question from a choice between internal implementations of whichever
option wins (which one is simpler, or more efficient) — don't
evaluate both levels against the same criteria just because they
came from the same comparison exercise.

This is a generation-quality discipline that complements
[compare-and-contrast-framing](compare-and-contrast-framing.md): that
note argues for putting multiple named options on the table at all;
this one argues for making sure those options are actually different
enough from each other to teach you something. See
[synthesize-across-compared-alternatives](synthesize-across-compared-alternatives.md)
for what to do once a genuinely diverse set of alternatives has been
compared.
