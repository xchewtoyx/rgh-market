---
type: concept
title: Design Special Cases Out of Existence
description: >
  The logic behind defining errors out of existence generalizes to special
  cases of any kind — the best fix for an edge-condition branch is usually a
  normal-case design that transparently subsumes it, requiring no extra code
  at all.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

Special-case branches (an `if` handling an edge condition) make code harder
to understand and more bug-prone, the same way unnecessary
[exceptions](define-errors-out-of-existence.md) do. The fix is the same
shape: design the normal-case logic so it transparently subsumes the special
case. See [Introduce Special Case](introduce-special-case.md) for the
mechanical refactoring that collapses duplicated special-case-handling call
sites into a single special-case object, one concrete way to carry out this
principle in existing code.

Worked example, from a text-editor exercise: most implementations of text
selection used an explicit boolean/state flag for "does a selection currently
exist," which then required scattered special-case checks throughout the
selection-handling code for the "no selection" condition. The fix is to make
the selection *always* exist as a data structure, representing "no visible
selection" as simply an **empty range** (start position equal to end
position), rather than as a distinct absent/present state. The consequences
then ripple through cleanly with no extra checks: copying an empty selection
naturally inserts zero bytes elsewhere, as long as the copy logic is written
generally; deleting a selection on a single line by concatenating the
pre-selection and post-selection fragments naturally regenerates the original
unchanged line when the selection is empty — again with zero extra code.

This is [different layer, different abstraction](different-layer-different-abstraction.md)
in miniature: "no selection" is a meaningful concept at the user-facing
interaction layer, but that doesn't obligate the implementation to represent
it as a distinct internal state. Collapsing it into "empty selection" — still
a selection, just an empty one — is a simpler internal representation for the
same external behavior.
