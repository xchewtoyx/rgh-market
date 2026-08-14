---
type: concept
title: "Code Smell: Speculative Generality"
description: >
  Machinery built for an imagined future need — hooks, parameters, and
  special cases nobody currently uses — makes code harder to understand for
  no present payoff, the smell-level counterpart to violating YAGNI.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3 (credited to Brian Foote)"
---

Speculative Generality, credited to Brian Foote, is machinery built for an
imagined future need — "we'll probably need to do X someday" — that adds
hooks, parameters, and special cases nobody currently uses, making the code
harder to understand for no present payoff: "if all this machinery were
being used, it would be worth it. But if it isn't, it isn't." This is the
smell-level symptom of violating [YAGNI](yagni.md).

Cures: [Collapse Hierarchy](collapse-hierarchy.md) for an underused abstract
class; [Inline Function](inline-function.md) or [Inline
Class](inline-class.md) for unnecessary delegation; [Change Function
Declaration](change-function-declaration.md) to strip parameters nothing
currently passes. A useful diagnostic tell: if a
function or class's only caller is a test, delete the test and remove the
dead code — the machinery was never actually needed by production code in
the first place.
