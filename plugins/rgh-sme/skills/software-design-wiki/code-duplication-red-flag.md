---
type: concept
title: Code Duplication as a Red Flag
description: >
  Repeated or near-repeated code is a sign you haven't found the right
  abstraction, but extraction is only worth it when the resulting shared
  method keeps a simple signature.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3, Duplicated Code"
---

**Red flag: repetition** — "If the same piece of code (or code that is
almost the same) appears over and over again, that's a red flag that you
haven't found the right abstractions."

Extracting a repeated snippet into a shared method works best when the
snippet is long and the resulting method's signature stays simple. A snippet
that's only one or two lines, or one that requires many pass-by-reference
parameters because it's tangled up with a lot of local state, usually isn't
worth extracting — the new method would be [shallow](shallow-modules.md), and
the parameter list itself becomes a new source of complexity.

A second technique eliminates duplication by restructuring control flow so
the repeated snippet only needs to exist once — for example, a method with
several early error-return points that all need the same cleanup logic can
move that cleanup to one place at the end and use `goto` (or an equivalent
structured-jump construct) to reach it from each error point. This is a
narrow, deliberate exception to the general reputation of `goto` as bad
practice: reasonable specifically when escaping from nested code to a single
shared cleanup block, not as a general control-flow tool.

Every duplicate copy carries a compounding cost: it must be read carefully
for subtle differences from its siblings, and every future change has to be
hunted down and applied to each copy, not just one — this is
[change amplification](change-amplification.md) caused specifically by
duplication. See the [Rule of Three](rule-of-three.md) for a ballpark
heuristic on when duplication has accumulated enough to justify fixing.
Mechanically: same-class duplication is a direct [Extract
Function](extract-function.md); code
that's similar but not identical often needs Slide Statements first, to line
up the common parts before extraction; duplication across sibling subclasses
of a common base calls for Pull Up Method instead of Extract Function, since
the shared code belongs on the parent, not in a new sibling call.

**When the duplication crosses an independently-evolving module or
component boundary, deduplicating is not automatically the right call.**
Sharing an implementation between two components creates a real
[coupling](coupling.md) between them — a change one component needs can now
also affect the other, or forces negotiating a shared change window neither
side controls alone. The judgment call is whether the duplicated code truly
represents the *same concept* — would a change to one instance always
imply the same change to the other? — not just whether it currently reads
similarly. Code that merely looks alike today because two components
happen to serve a similar purpose (two kinds of server, two kinds of
worker) often needs to diverge as each is built out for its own use case,
and locking them into one shared abstraction too early creates
change-amplification friction in the other direction: a legitimate change
for one now has to be threaded carefully around the other's needs. A
useful rule of thumb: stay strict about eliminating duplication *within* a
single component or module, but be more permissive about tolerating
similar-looking code *across* component boundaries, since dedup there
trades a small amount of repeated text for a standing coupling that has to
be paid for on every future independent change to either side.
