---
type: concept
title: Encapsulation Is a Tool for Understanding, Not an End in Itself
description: >
  When getting a class under test genuinely requires breaking encapsulation
  (e.g. Parameterize Constructor), bias toward the test coverage — it's
  often what lets you restore encapsulation safely later.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 11"
---

Many dependency-breaking techniques — [Parameterize Constructor](parameterize-constructor.md)
among them — genuinely *break* encapsulation, adding new parameters or paths
that increase, not decrease, the effect surface a reader has to trace. This
looks like a straightforward regression against
[information hiding](information-hiding.md) until the underlying purpose of
encapsulation is made explicit: **"Encapsulation helps us reason about our
code... Encapsulation isn't an end in itself; it is a tool for
understanding."**

Once that's the frame, the tie-breaker when the two goals genuinely conflict
follows directly: **"Encapsulation and test coverage aren't always at odds,
but when they are, I bias toward test coverage. Often it can help me get
more encapsulation later."** Tests are an alternate, arguably stronger tool
for reasoning about code than encapsulation alone — once they exist, later
refactoring can restore encapsulation without losing the safety net that
made the restructuring safe to attempt in the first place. This is the same
ordering claim as
[dependency-breaking for testability](dependency-breaking-for-testability.md):
the "scar" left by a dependency-breaking technique is provisional, healed
once tests make further refactoring safe.
