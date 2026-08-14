---
type: concept
title: Compilation Firewall
description: >
  Applying Extract Interface (or Extract Implementer) on both sides of a
  package boundary lets implementation classes change freely without forcing
  recompilation of their callers, shrinking incremental build times.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 7"
---

Worked example: `AddOpportunityFormHandler` depends directly on concrete
classes `ConsultantSchedulerDB` and `AddOpportunityXMLGenerator`. Applying
[Extract Interface](extract-interface.md) (Java) or
[Extract Implementer](extract-implementer.md) (C++ — described as
slightly easier, since it avoids updating every reference site) to each
concrete dependency makes `AddOpportunityFormHandler` depend on the
interfaces instead. A test fake can now substitute for the concrete
implementation, and — as important for this technique — future edits to
`ConsultantSchedulerDBImpl` no longer force `AddOpportunityFormHandler` to
recompile, since its compile-time dependency is now on the rarely-changing
interface. Made explicit at the package/library level (e.g. an
`OpportunityProcessing` package with zero dependency on DB implementation
classes), this becomes a **compilation firewall**: implementation classes
change freely without forcing recompilation of anything on the far side of
the boundary.

The technique is symmetric: once a class is the only public production class
in its package, anything depending on it still forces a recompile on every
change to *it*. Applying Extract Interface/Implementer to that class too, so
outside packages depend on its interface, "shield[s] all of the users of
this package from recompilation when we make most changes." Building the
firewall on both sides of a boundary is what actually insulates each side
from the other's churn — a firewall on only one side still lets change
propagate through the unprotected direction.

Explicit tradeoff: introducing more interfaces and package boundaries
slightly increases the cost of a **full** rebuild (more files to compile
overall) but can dramatically reduce **average incremental** build time
(rebuilding only what actually changed) — judged "a fair price to pay,"
alongside a non-free but worthwhile cost in added conceptual and navigational
indirection. The isolation work for a given cluster of classes is a one-time
cost: "you have to do it only once for that set of classes; afterward, you
get to reap the benefits forever." This is the concrete mechanism behind
[reducing lag time](lag-time.md), and an instance of
[the dependency inversion principle](dependency-inversion-principle.md)
applied deliberately at the package-boundary level rather than to a single
class.
