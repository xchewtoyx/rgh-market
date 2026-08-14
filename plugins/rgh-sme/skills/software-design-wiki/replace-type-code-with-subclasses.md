---
type: concept
title: "Refactoring: Replace Type Code with Subclasses"
description: >
  Promote a type-code field to real subclasses when conditional logic on
  it is duplicated across several functions, or when some fields or
  methods are only valid for certain values — direct subclassing when the
  type never needs to change or be reused, indirect subclassing behind a
  dedicated type object otherwise.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12 (subsumes the first edition's Replace Type Code with State/Strategy and Extract Subclass; inverse of Remove Subclass)"
---

This is the inverse of [Remove Subclass](remove-subclass.md): that
refactoring collapses a subclass whose only remaining job is holding a
fixed value back into a plain field, once the variation it represented has
migrated elsewhere or disappeared.

A type-code field (enum, symbol, string, or number — often sourced from an
external service) is usually all that's needed to represent "different
kinds of a similar thing." Two situations call for something stronger,
promoting the type code to real subclasses:

1. **Conditional logic driven by the type code appears in multiple
   functions** — subclasses let you apply
   [Replace Conditional with Polymorphism](replace-conditional-with-polymorphism.md)
   to each of them, collapsing repeated type-based dispatch into one place
   per function.
2. **Fields or methods are only valid for certain type-code values** (a
   sales quota that only makes sense for one job type). A subclass plus
   [Push Down Field](push-down-field.md) makes that restriction structural
   rather than merely enforced by ad hoc validation — a subclass makes the
   relationship more explicit than a validated field can.

**Key design fork**: should the type code become **direct** subclasses of
the class itself, or an **indirect** hierarchy behind a new type-code
*object* that the original class holds? Direct subclassing is simpler, but
has two hard limits: it can't be used if the type dimension needs to be
reused for something else (a class can only occupy one inheritance axis),
and it can't be used if the type code is **mutable**, since an object
generally can't jump between classes after construction. To reach the
indirect form starting from a plain field, first apply
[Replace Primitive with Object](replace-primitive-with-object.md) on the
type code to create a dedicated type class, then apply this refactoring to
that new class rather than to the original host class.

**Mechanics**: self-encapsulate the type code field
([Encapsulate Variable](encapsulate-variable.md)). Pick one type-code
value; create a subclass for it, overriding the type-code getter to return
that literal value. Build selector logic mapping incoming type-code values
to the right subclass — for **direct inheritance**, this selector has to
live in a factory function (via
[Replace Constructor with Factory Function](replace-constructor-with-factory-function.md)),
since a constructor generally can't cleanly host both selection logic and
field initialization together; for **indirect inheritance**, the selector
can simply stay in the constructor, since it's constructing the separate
type object, not the host itself. Test. Repeat — one subclass, one
selector-logic addition, one test — for each remaining type-code value.
Once all values have a subclass, remove the original type-code field; test.
Finally, use [Push Down Method](push-down-method.md) and
[Replace Conditional with Polymorphism](replace-conditional-with-polymorphism.md)
on any remaining methods that still branch on the type-code accessor, and
once nothing references those accessors anymore, remove them too.

A useful verification discipline once the first subclass is wired up:
deliberately break its override's return value and re-run the tests
specifically to confirm they'd actually catch a regression, before
continuing with the remaining values the same way — the same
["verify a test can fail"](verify-a-test-can-fail.md) discipline that
applies to any new test.

**The indirect type object earns a permanent place**, unlike purely
transient scaffolding: it makes explicit the relationship between the
various subclasses, and it becomes a natural home for behavior shared
across all of them — a piece of logic that awkwardly lived on the host
class purely because it depended on the type can migrate onto the type
object instead, where every variant inherits it automatically. This is a
concrete illustration of the indirect form paying for itself as a genuine
module, not just a workaround for direct subclassing's constraints.
