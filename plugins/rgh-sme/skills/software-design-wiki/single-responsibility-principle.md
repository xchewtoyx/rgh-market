---
type: concept
title: Single Responsibility Principle
description: >
  Every class should have a single purpose and only one reason to change,
  but "responsibility" is a cluster of related methods, not literally one
  method — and the ideal fully-separated decomposition it implies is often
  overkill in practice.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

"Every class should have a single responsibility: it should have a single
purpose in the system, and there should be only one reason to change it."
A responsibility isn't literally "one method" — it's a cluster of related
methods serving one purpose. Worked example: a rule-expression evaluator
dissected by grouping its methods by apparent purpose reveals four distinct
responsibilities (parsing, expression evaluation, term tokenization,
variable management) hiding inside what looks like one class with one public
entry point.

An explicit, important caveat: the fully-separated design this kind of
analysis suggests can be overkill in practice — small interpreters often
merge parsing and evaluation for convenience, and a candidate extraction
might add so little beyond a plain data structure that it isn't worth its
own class. The grounding point for legacy work specifically: **the goal is
identifying responsibilities and moving incrementally toward more focused
ones, not designing the theoretically ideal decomposition from scratch.**
See [seeing responsibilities via method grouping](group-methods-heuristic.md)
for how to actually locate the clusters this principle asks you to separate,
and [cohesion](cohesion.md) for the formal, probabilistic definition behind
"single purpose."
