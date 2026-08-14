---
type: concept
title: "Code Smell: Repeated Switches"
description: >
  A single switch statement is not inherently a problem; the real smell is
  the same switching logic duplicated at multiple call sites, where every
  added case has to be hunted down and updated in every copy.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Fowler and Beck explicitly walk back the first edition's blanket "switch
statements are bad" stance, written when polymorphism was less commonly
reached for. A single switch is not inherently a problem, especially with
modern, richer conditional constructs. The real smell is the *same*
switching logic — a switch/case or an if/else cascade — duplicated at
multiple call sites: every new case added to the underlying concept then
requires hunting down and updating every one of those duplicated copies,
which is exactly [change amplification](change-amplification.md) triggered
by adding a variant rather than by an ordinary change.

Cure: [Replace Conditional with Polymorphism](replace-conditional-with-polymorphism.md),
which collapses the duplicated dispatch logic into one place instead of one
place per call site.
