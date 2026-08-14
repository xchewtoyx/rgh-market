---
type: concept
title: Orthogonality and the Open/Closed Principle
description: >
  Orthogonality means one place to go for one behavior change; removing
  duplication tends to produce it, and code with orthogonal "knobs" for
  each behavior naturally satisfies the Open/Closed Principle — extensible
  by adding a subclass rather than editing existing code.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 21"
---

**Orthogonality** means independence: "if you want to change existing
behavior in your code and there is exactly one place you have to go to make
that change, you've got orthogonality." Picture a system as a big box with
knobs surrounding the outside — good design means one knob per behavior.
Duplicated code is the opposite: multiple knobs for the same behavior,
because changing that behavior (a wire-protocol terminator byte, say)
requires edits in every duplicated location — "no single-purpose knobs."
[Removing duplication](duplication-removal-as-emergent-design.md)
mechanically collapses these multiple knobs back into one, which is why
orthogonality tends to fall out of deduplication work rather than needing to
be designed in separately.

**The Open/Closed Principle** (attributed to Bertrand Meyer): "code should
be open for extension but closed to modification" — good design lets you
add features without editing existing code much. A hierarchy that's had its
duplication removed down to per-subclass constructors and single-method
overrides typically satisfies this automatically: adding a new variant means
subclassing and providing the one differing piece, not editing shared logic.
This is the same discipline as
[Programming by Difference](programming-by-difference.md) for *adding* a
feature via subclassing, now viewed from the other end — as the natural
consequence of a codebase that's already had its duplication squeezed out.
**"When we remove duplication, our code often naturally starts to fall in
line with the Open/Closed Principle."**
