---
type: concept
title: Probe Boundary Conditions, Not Just the Happy Path
description: >
  Deliberately trying to break your own code at its edges — empty
  collections, zero and negative values, blank input — finds more bugs per
  test than happy-path coverage, and surfaces implicit domain questions you
  might not otherwise think to ask.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 4"
---

Rule: **"Think of the boundary conditions under which things might go wrong
and concentrate your tests there."** This is a concrete instance of the
broader principle of [targeting testing effort at the code you're actually
worried about](risk-driven-test-selection.md) rather than spreading it
evenly. Concrete boundary categories worth
deliberately targeting: empty collections, zero values, negative values, and
blank or empty-string input — the last of these often arises specifically
because a UI or parsing layer hands raw strings to lower code, and those
strings can be blank in ways a well-typed value never could be. The stance
to take while doing this is playing "enemy to my code" — deliberately trying
to break it — described as "both productive and fun," not adversarial
busywork.

A secondary benefit beyond bug-finding: boundary testing surfaces implicit
domain questions that might not otherwise get asked — for example, whether
negative demand should even be legal input, or whether a setter should
clamp or reject it. Writing the boundary test forces that decision to be
made explicitly rather than left as accidental behavior; deciding to reject
rather than clamp is the same judgment call examined from the production
code's side in [introduce assertion to fail fast on bad
input](introduce-assertion-for-fail-fast.md).
