---
type: concept
title: "Kent Beck's Four Rules of Simple Design"
description: >
  A component's design is simple, in priority order, if it passes its
  tests, reveals its intention, has no duplication, and has the fewest
  elements — a compact checklist for judging whether a design is done.
sources:
  - title: Infrastructure as Code, 2nd Edition
    resource: "Infrastructure as Code (Morris), ch. 15 (rules originated by Kent Beck)"
---

Kent Beck's four rules, applied in priority order — each rule is only
worth pursuing once the ones before it are satisfied:

1. **Pass its tests** — the code does what it's actually supposed to do.
   Nothing else on this list matters if the code is wrong.
2. **Reveal its intention** — the code is clear and easy to understand; a
   reader can tell what it does and why without extensive study. See
   [code should be obvious](code-obviousness.md) for what this looks like
   in practice.
3. **Have no duplication** — see [code duplication as a red
   flag](code-duplication-red-flag.md) and the [Rule of
   Three](rule-of-three.md) for when duplication has accumulated enough to
   justify removing it.
4. **Include the fewest elements** — no unnecessary classes, methods, or
   parameters beyond what's needed to satisfy the first three rules. This
   is the last priority deliberately: chasing "fewest elements" ahead of
   clarity or duplication removal produces code that's merely short, not
   simple — see [more code for better structure is
   fine](more-code-for-better-structure-is-fine.md) for why fewer lines
   isn't itself the goal.

The ordering matters as much as the list. A design that satisfies rule 4
(minimal elements) at the expense of rule 2 (revealing intention) —
terse, clever, hard to read — has optimized the wrong thing; the rules are
meant to be applied as a priority cascade, not a set of independent boxes
to check in whatever order is convenient.
