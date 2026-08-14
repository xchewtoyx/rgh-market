---
type: concept
title: Class Size as an Information-Hiding Decision
description: >
  Whether to merge or split a class should be decided by what improves
  information hiding, not by a size target — a bigger class is sometimes the
  design that hides more, not less.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3, Large Class"
---

Observed from a recurring classroom exercise (students implementing an HTTP
server): the most common mistake was splitting into many shallow classes,
which caused [information leakage](information-leakage.md) via
[temporal decomposition](temporal-decomposition.md) — for instance, separate
classes for "read request bytes off the socket" and "parse the request
string," both of which ended up needing to understand HTTP structure because
the total request length depends on a parsed header.

Merging such classes achieves two things at once: it consolidates all
knowledge of one format or capability into a single place (better
[information hiding](information-hiding.md)), and it can raise the interface's
level of abstraction by replacing several step-by-step methods that had to be
called in a fixed order with one method that performs the whole computation.
A caller that previously had to invoke "read" then "parse" in the right order
now just gets a request object back.

This cuts directly against "classes and methods should be small" taken as an
unqualified target — see [classitis](classitis.md). The caveat runs the other
way too: this logic doesn't extend to merging everything into one giant class
for an entire application; see
[better together or better apart](better-together-or-apart.md) for
where the line sits.

Fowler and Beck's **Large Class** smell gives concrete diagnostics for the
opposite failure — a class that's grown too big — and a matching cure
vocabulary. A class trying to do too much typically shows up as too many
fields first, which then breeds duplicated code; common prefixes or suffixes
on field names are a tell for where a split line falls. Cure: Extract Class
to bundle related variables together into their own type, or — if the split
fits inheritance better — [Extract Superclass](extract-superclass.md) or
[Replace Type Code with Subclasses](replace-type-code-with-subclasses.md).
Fields that are never all used simultaneously suggest room to
repeat the extraction more than once. For a class bloated with code rather
than fields, the same duplication-elimination instinct applies: several
near-duplicate long methods often collapse into several short methods
sharing a handful of small extracted helpers. Clients' actual usage patterns
are a good practical guide for where to split — a subset of features used
together by some clients suggests a natural class boundary.
