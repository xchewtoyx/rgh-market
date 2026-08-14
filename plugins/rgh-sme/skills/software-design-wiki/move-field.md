---
type: concept
title: "Refactoring: Move Field"
description: >
  Relocate a field to the record it actually belongs with, recognized by
  fields that always travel together into the same functions, fields whose
  changes force a change in another record, or a value duplicated across
  structures that should be updated in only one place.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

A program's real strength comes from its data structures more than its
behavior code: good data structures matching the problem keep the behavior
code simple, while poor ones force code into existence purely to work
around bad data shape, both bloating the code and obscuring what the
program actually does. Initial data-structure design is routinely wrong in
ways only discovered through continued work on the problem — a design
decision that was reasonable one week can become wrong the next — so fixing
a recognized data-shape blemish is urgent: leaving it in place keeps
confusing future thinking and code.

**Concrete triggers** for moving a field: (1) a field from one record is
always passed alongside another record into the same functions — a sign the
two belong together in one record; (2) a change to one record's field
routinely forces a change to a field in a *different* record — a sign the
field is homed in the wrong place; (3) the same logical value has to be
updated in multiple structures — move it somewhere it only needs updating
once. This is usually done as part of a broader change: after moving, many
of a field's users are often better off reading it through the new home
directly, prompting further follow-up refactorings; conversely, usage
patterns sometimes must be refactored *first* before the move itself
becomes possible.

This refactoring is markedly easier with **classes** than with bare
records, because encapsulation means clients go through accessor methods —
moving the underlying data and updating just the accessors leaves callers
unaffected. With a bare record lacking that indirection, apply
[Encapsulate Record](encapsulate-record.md) first to turn it into a class,
then proceed normally.

**Mechanics**: ensure the source field is
[encapsulated](encapsulate-variable.md) first; test. Create the
corresponding field and accessors on the target. Run static checks. Ensure
there's a way to get from the source object to the target object — an
existing field or method may already provide this; otherwise add a cheap
method that does, or as a last resort a (possibly temporary) new field on
the source purely to hold the target reference. Update the source's
accessors to read/write through to the target field. Test. Remove the
now-redundant source field; test.

**When the target will be shared across multiple source objects**
(collapsing a one-per-source field into a one-per-target field — a
many-to-one relationship) the move is only truly behavior-preserving if
every source object sharing a target already agrees on the value. Verify
this before committing: have the setter update both target and source
fields in parallel and add an [assertion](introduce-assertion-for-fail-fast.md)
(or logging, or a direct data query for persisted data) to catch any
divergence, and only cut over to the target exclusively once confident
nothing diverges. This generalizes beyond this one refactoring: whenever a
change risks silently collapsing several independent values into one shared
value, verify the assumption of current equivalence before treating the
change as behavior-preserving. The mirror-image operation for behavior
instead of data is [Move Function](move-function.md).
