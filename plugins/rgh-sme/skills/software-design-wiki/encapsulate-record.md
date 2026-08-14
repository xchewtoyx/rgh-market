---
type: concept
title: Encapsulate Record
description: >
  Wrapping a mutable record in a class hides which values are stored versus
  derived and smooths future renames, in exchange for the extra step of
  building a class — a cost that mostly evaporates for genuinely immutable
  values.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7 (formerly Replace Record with Data Class)"
---

The chapter this belongs to is framed by Parnas's principle that the most
important criterion for decomposing modules is identifying secrets each
module should hide from the rest of the system — data structures are the
most common secret worth hiding this way.

For **mutable** data, an object hides which values are stored versus
derived, so callers don't need to know or care — and this encapsulation
smooths future renames, since both old and new field names can be exposed as
methods while callers migrate gradually (see [Rename
Variable](rename-variable.md)). For genuinely **immutable** values, this
concern mostly evaporates: you can store all relevant values directly in the
record, and renaming is as simple as copying the field. A generic
hashmap-style record with arbitrary keys is syntactically convenient but
pays for it with implicit structure — no way to tell whether a structure
uses `start`/`end` or `start`/`length` without reading usage sites. That
implicitness is fine at small, local scope but becomes a real cost as usage
widens, at which point a proper class beats merely making an implicit record
explicit.

**Mechanics**: apply [Encapsulate Variable](encapsulate-variable.md) to the
record-holding variable, using a deliberately ugly, greppable temporary
name for the wrapping accessors. Replace the record's storage with a thin
class wrapping it, exposing an accessor for the raw record, and route the
temporary functions through that accessor; test. Add new functions that
return the *object* rather than the raw record. Migrate every caller from
the raw-record accessor to the object-returning one, reading fields via
accessors on the object; test after each swap. For a nested record, tackle
callers that **update** the data first — the higher-risk direction — before
tackling reads, and consider handing readers a copy or a read-only proxy
rather than the live structure. Once all callers are migrated, delete the
raw-data accessor and the temporary functions. If a field is itself a
nested structure, recurse: apply Encapsulate Record or [Encapsulate
Collection](encapsulate-collection.md) to it too.

A practical verification trick for confirming every mutation site has been
caught: temporarily make the raw-data accessor return a deep copy instead of
the live object — with solid test coverage, any missed direct-mutation call
site will now silently fail to take effect and a test should catch it.
