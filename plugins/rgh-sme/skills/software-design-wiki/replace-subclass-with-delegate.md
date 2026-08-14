---
type: concept
title: "Refactoring: Replace Subclass with Delegate"
description: >
  Move a subclass's differing behavior into a separate delegate object that
  the (former) superclass holds and dispatches to, trading inheritance's
  free-but-rigid single axis of variation for delegation's more explicit,
  more flexible, but more effortful wiring.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

Inheritance is the obvious mechanism for behavior that varies by category —
common data/behavior on the superclass, each subclass overriding or adding
what it needs — but it has two structural downsides. It's a card that can
only be played once: a class can only vary along a single inheritance axis,
so if two independent categorizations both want subclassing (say,
age-category and income-level), only one of them can actually get it. And it
creates [tight two-way coupling](interface-vs-implementation-inheritance.md)
between parent and child, where changing the superclass can silently break
subclasses — a risk that worsens when parent and child are owned by
different teams or live in different modules. Delegation solves both: an
object can delegate to many different collaborators for different reasons
(no "only once" constraint), and delegation is an ordinary object
relationship with a clear interface — much looser coupling than
subclassing.

This does not mean "avoid inheritance." Reach for inheritance first, since
it does the job without friction most of the time, and move to delegation
only once problems actually surface — knowing the move is available later
is what makes defaulting to inheritance safe. Readers familiar with the Gang
of Four will recognize this as replacing subclasses with the State or
Strategy pattern; both patterns share the same underlying shape (host
delegates to a separate hierarchy), though the delegate side doesn't always
need to be a hierarchy itself.

**Two concrete triggers**, distinct from "inheritance is bad": (1) a
*better* use for the class's one inheritance axis shows up later, so the
current subclassing has to give way; (2) an object needs to switch
dynamically between categories at runtime (a booking becoming premium in
place) rather than just being rebuilt fresh next time — inheritance fixes an
object's class at construction, delegation doesn't.

**Mechanics**: if there are many callers of the subclass constructors, first
encapsulate them behind a factory function. Create an empty delegate class
whose constructor takes any subclass-specific data plus (usually) a
back-reference to the host object. Add a field on the superclass to hold the
delegate instance and wire up its creation. Then, one subclass method at a
time: [Move Function](move-function.md) it to the delegate class (without
yet deleting the original), test — expecting some transitional failures —
then add dispatch logic to the superclass method that calls the delegate
when present and falls back to the old default behavior otherwise. A method
that called `super` in the original subclass needs special handling, since
the delegate calling back into the dispatching superclass method would
recurse infinitely: either extract the superclass's real calculation under a
separate name the delegate can call safely, or recast the delegate's method
as an explicit extension point that the superclass's own result gets passed
into. If more than one subclass is involved and duplication starts
appearing across their delegates, apply
[Extract Superclass](extract-superclass.md) to the delegates themselves —
once that's done, the host's dispatching methods no longer need their
presence guard, since the delegate hierarchy's own default behavior absorbs
the "no delegate" case. An `instanceof`-style check on the delegate's
concrete type to decide dispatch is a trap to avoid — it reintroduces, in
the delegate, exactly the kind of type-conditional logic this refactoring
exists to eliminate; extracting a shared delegate superclass is the real fix
instead. Test after each move; repeat until every subclass method has been
relocated, then redirect every constructor caller to the superclass
constructor and remove the now-empty subclass.

**Honest cost**: this is one of the refactorings where the result isn't
simply "better" code in isolation — delegation adds dispatch logic, a
two-way back-reference, and real extra complexity compared to the clean
inheritance it replaced. It's worth doing only when the structural
benefits — freeing the inheritance axis, or enabling in-place category
change — outweigh that added complexity. Compare
[Replace Superclass with Delegate](replace-superclass-with-delegate.md) for
the analogous move when the *superclass* relationship (rather than a
subclass) is really a delegation relationship in disguise.
