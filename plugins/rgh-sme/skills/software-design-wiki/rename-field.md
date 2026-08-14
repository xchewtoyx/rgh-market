---
type: concept
title: "Refactoring: Rename Field"
description: >
  Rename a record field or accessor pair through a staged, one-surface-at-
  a-time transition — internal field, then constructor, then public
  accessors — so a widely-used name can improve without a flag-day cutover
  across every caller.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 9"
---

Field names in widely-used record structures carry outsized importance —
Fred Brooks: "Show me your flowcharts and conceal your tables, and I shall
continue to be mystified. Show me your tables, and I won't usually need
your flowcharts; they'll be obvious." Data structures are the key to
understanding what a program is doing, and understanding of the data model
keeps improving as you work on a system — that improved understanding needs
to be reflected back into the code, via renaming, as it develops. This
applies equally to plain record fields and to a class's getter/setter pair,
since from the outside, accessor methods function as the class's "field"
from a caller's perspective. See
[Rename Variable](rename-variable.md) for the analogous, lighter-weight
mechanics when a value's scope is local rather than a widely-shared record.

**Mechanics**: if the record has only local, limited scope, it's enough to
just rename every access directly and test — the heavier mechanics below
aren't needed. Otherwise: if not already encapsulated, apply
[Encapsulate Record](encapsulate-record.md) first. Rename the private
internal field and adjust internal methods accordingly; test. If the
constructor references the old name, apply
[Change Function Declaration](change-function-declaration.md) to update it
— during the transition, having the constructor accept *either* the old or
new key lets every call site migrate to the new argument name at its own
pace, without a single cutover moment; delete the fallback only once every
caller has switched. Finally, apply the same renaming to the public
accessors.

This full staged sequence — internal field, constructor, accessors, each
its own tested step — is reserved for widely-shared data structures,
deliberately trading what looks like one big rename for four independently-
changeable, independently-testable surfaces: smaller steps mean fewer things
that can go wrong in any one step, which is a net reduction in total effort
once you accept that not making mistakes at all isn't realistic. Test
failures partway through are the practical signal that a structure actually
needed this more gradual procedure rather than a one-shot rename. In a
language with true immutable data structures, the encapsulation step can
often be skipped entirely: copy the value under the new name, migrate users
gradually, and delete the old name once done. Duplicating a value under two
names is a recipe for disaster with mutable data specifically, since the two
copies can drift out of sync — one more reason immutable data is easier to
work with during a rename like this.
