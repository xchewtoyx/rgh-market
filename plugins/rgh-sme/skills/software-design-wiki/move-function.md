---
type: concept
title: "Refactoring: Move Function"
description: >
  Relocate a function to the context it references most, or to wherever its
  callers and upcoming enhancements need it, moving its dependency cluster
  along with it starting from whichever member has the fewest dependencies.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

[Modularity](module-interface-and-implementation.md) — the ability to make
most changes while understanding only a small part of the system — depends
on grouping related elements together with easy-to-follow links between
groups. Understanding of the "right" grouping evolves as you learn more
about a domain, so elements need to keep moving to reflect that growing
understanding. Every function lives in some context (global scope, a
module, a class, or nested inside another function).

**When to move**: the most straightforward trigger is a function that
references elements of some *other* context more than its current one —
moving it alongside those elements usually improves encapsulation and
reduces other code's dependence on this module's internals; this is the
standard cure for [Feature Envy](feature-envy.md). A second trigger is the
location of its callers, or where an upcoming enhancement needs to call it
from — e.g. promoting a locally-useful nested helper to a more accessible
scope, or shifting a method to a different class where it's easier to use
from there. Deciding where a function belongs is rarely clean-cut; sometimes
the right destination is a whole new context, built via
[Combine Functions into Class](combine-functions-into-class.md) or
[Extract Class](extract-class.md). Reassuringly, **the more difficult this
choice, often the less it matters** — it's fine to place a function
somewhere, learn how well it fits from experience, and move it again later
if it doesn't.

**Mechanics**: examine every program element the function uses in its
current context and consider whether each should move too — if a called
function should also move, move it *first*, so a cluster of functions gets
relocated starting from whichever member has the fewest dependencies on the
rest of the group. If a high-level function is the sole caller of some
sub-functions, it can be simpler to inline those sub-functions into it
first, move the whole thing, then re-extract at the destination. Check
whether the function is a polymorphic method (requiring attention to
super/subclass declarations). Copy the function into the target context and
adapt it to fit — any source-context elements it needs must become
parameters or a reference back to the source context; the move often forces
a better name to be found for the new context. Run static analysis. Figure
out how the source context will reference the moved target function, and
turn the original function into a pure delegating call; test. Finally,
consider [Inline Function](inline-function.md) on the now-delegating source
stub — it's fine to leave it in place indefinitely as a forwarding shim, but
if callers could just as easily call the target directly, removing the
middle man is preferable (the same
[Hide Delegate](hide-delegate.md) / [Remove Middle Man](remove-middle-man.md)
tradeoff applies here).

**A recurring design decision when moving a method between classes**:
whether a value the moved function still needs from its old home should be
passed as a plain parameter, or whether the *whole originating object*
should be passed in instead so the function can reach into it directly.
Passing the whole object is preferable once the moved function is likely to
need more from that object over time — see
[Preserve Whole Object](preserve-whole-object.md) for the general refactoring
that applies this tradeoff, independent of Move Function specifically. The mirror-image operation for data instead of behavior is
[Move Field](move-field.md).
