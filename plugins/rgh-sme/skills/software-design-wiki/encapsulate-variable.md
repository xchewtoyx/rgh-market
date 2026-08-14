---
type: concept
title: Encapsulate Variable
description: >
  Data has no equivalent of a function's forwarding shim — moving it means
  every reference must update in one atomic pass — so route wide-scope
  mutable data through accessor functions first, turning a hard data-move
  problem into an easier function-move problem.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6 (formerly Self-Encapsulate Field, Encapsulate Field)"
---

Functions are easy to move or rename because the old one can stay in place
as a thin forwarding shim while callers migrate. Data has no equivalent
trick: moving it means every reference must be updated in one atomic pass,
and the difficulty scales with the data's scope — precisely why [global
data](global-state-opacity.md) is so painful to work with. The standard
workaround: route **all** access to widely-scoped data through accessor
functions first, converting "the difficult task of reorganizing data" into
"the simpler task of reorganizing functions." Encapsulation also creates a
natural chokepoint for adding validation or side-effect logic on updates
later. Stated habit: any mutable data whose scope exceeds a single function
should be encapsulated behind accessor functions — the wider the scope, the
more this matters. This is the underlying rationale for object orientation's
emphasis on private fields: any visible public field is a candidate for this
refactoring.

Self-encapsulation — routing even *internal* same-class references through
accessors — is called generally excessive: "if a class is so big that I need
to self-encapsulate its fields, it needs to be broken up anyway," though
it's a legitimate intermediate step just before splitting a class via
[Extract Class](extract-class.md). Immutable data needs much less of this treatment: no validation hook is
needed pre-update, and it can be freely copied rather than relocated, so
stale-reference concerns disappear — **"immutability is a powerful
preservative."**

**Encapsulating the value, not just the reference, is a deeper problem.**
Wrapping access to a *reference* to a mutable object doesn't stop callers
from mutating the object's *contents* after retrieving it — two aliased
references can each see the other's edits. Two remedies: the getter can
return a defensive copy, which is especially favored for lists, letting
callers mutate their copy freely without it propagating back (though this
can silently break code that actually expected to mutate shared state — a
risk your tests need to catch); or the value can be wrapped in a class whose
fields are exposed only via read-only accessors, so any attempted external
mutation errors outright instead of silently diverging. Both approaches only
protect one level deep in a nested structure — deeper structures need
recursive copying or wrapping. Overall: "encapsulating data is valuable, but
often not straightforward" — what and how much to encapsulate depends on
actual usage patterns, with effort justified in proportion to how widely the
data is used.
