---
type: concept
title: "Refactoring: Decompose Conditional"
description: >
  Extract a conditional's condition and each of its branch bodies into
  separately named functions, so the code states what's being branched on
  and why each branch exists instead of leaving both buried in mechanics.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 10"
---

Complex conditional logic is one of the most common sources of program
complexity — long functions are already hard to read, and conditionals
compound the problem because both the condition checks and the branch
bodies tend to describe *what* happens while obscuring *why*. The fix is
the same instinct as breaking up any long block: decompose it, replacing
each chunk with a function call named after its intent. Applied to
conditionals specifically, extract *both* the condition itself and each of
the branch bodies — this simultaneously highlights what's being branched on
and why. This is really just a particular case of applying
[Extract Function](extract-function.md), but one that's proven remarkably
good value often enough to warrant its own named entry.

**Mechanics**: apply Extract Function to the condition and to each leg of
the conditional.

Once each piece is separately named, a two-branch conditional often
collapses cleanly into a ternary — a single named condition choosing
between two named outcomes reads at a glance, where the original branches
of raw logic did not.
