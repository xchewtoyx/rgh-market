---
type: concept
title: Split Phase
description: >
  When code is really doing two different things, splitting it into
  sequential phases connected only by an intermediate data structure lets
  each phase be understood and changed without the other's details in mind.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6"
---

When a piece of code is really doing two different things, separating it
into distinct modules means each concern can be understood and changed
independently — ideally, a future change touches only one module, and the
other's details never need to be held in mind at all. One especially clean
way to split: divide the behavior into two **sequential phases**,
communicating through an intermediate data structure — useful whenever raw
input doesn't already match the shape the main logic wants to work with (a
"massage the input first" step), or when a computation naturally decomposes
into stages that are qualitatively different from each other. Canonical
large-scale example: a compiler's tokenize → parse-to-syntax-tree →
transform/optimize → generate-object-code pipeline, where each phase has
bounded scope and can be understood alone. The same move applies at any
scale, down to a single function; the best signal a fragment wants
splitting is that its different stages operate on **different sets of data
and functions** — separating them into modules makes that latent difference
explicit and visible. This is one concrete way to fix the [Divergent
Change](divergent-change.md) smell when the tangled concerns form a natural
sequence.

**Mechanics**: extract the second-phase code into its own function; test.
Introduce an intermediate data structure, passed as an additional argument
into that extracted function; test. Walk each parameter of the extracted
(second-phase) function: if it's produced by the first phase, move it into
the intermediate data structure instead of passing it directly, testing
after each move; for a parameter the second phase shouldn't really depend on
directly, extract each place it's used into a field on the intermediate
structure instead. Once every needed value flows through the intermediate
structure, apply [Extract Function](extract-function.md) to the remaining
first-phase code, having it construct and return that structure.

End state: a thin two-line orchestrator calling the two phases in sequence,
with two independently-understandable, differently-scoped functions
connected only by the intermediate structure — each phase can now evolve
(more complex rules on either side) without the other phase's implementation
needing to be held in mind at the same time. See [more code for better
structure is a fine trade](more-code-for-better-structure-is-fine.md) for
the accompanying line-count tradeoff this kind of split typically makes.
