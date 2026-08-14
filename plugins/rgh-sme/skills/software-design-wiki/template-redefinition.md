---
type: concept
title: Template Redefinition
description: >
  For a dependency embedded as a concrete member type, templatize the class
  on that type and alias the original name to the original type via
  typedef, so production code needs zero changes while tests instantiate
  the template with a fake type — a last resort behind inheritance-based
  techniques.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Languages with generics or templates offer a substitution mechanism beyond
inheritance, useful particularly when the dependency to break is a
**concrete member type embedded directly in the class**, not reachable via
ordinary subclassing. Mechanism: convert the class into a template
parameterized on the problematic type, rename the templated version (an
`Impl` suffix, say), and use a type alias to preserve the original class
name bound to the original concrete type — so existing production code
needs zero changes, while test code can instantiate the same template with
a fake type instead.

Praises the type-alias trick specifically as "the sweetest thing about this
technique" — it avoids the otherwise-tedious task of updating every
reference to the class throughout the codebase to add an explicit template
argument; in generics-supporting languages without a type-aliasing
mechanism, you're stuck [leaning on the compiler](lean-on-the-compiler.md)
to find and fix every reference instead.

Templates can also swap out *method* implementations, not just data
members, but this is flagged as "a little messy" in C++ specifically, since
the language forces some template parameter to exist — sometimes an
arbitrarily chosen or artificially introduced one purely to enable
templating. Explicit guidance: treat this as a last resort, preferring
inheritance-based techniques (like [Subclass and Override Method](subclass-and-override-method.md))
first.

**Named structural downside specific to C++**: templatizing a class forces
its implementation to move from source files into the header, which
increases compile-time coupling — anyone depending on the header must now
recompile whenever the (now header-resident) implementation changes, the
opposite of a [compilation firewall](compilation-firewall.md). This
reinforces a general bias toward inheritance-based dependency-breaking in
C++, reserving Template Redefinition mainly for code that's *already*
templatized, where changing which type parameter is passed is a natural,
low-cost move.

Steps (C++-flavored, may vary in other generics-supporting languages):
identify the features to replace; templatize the class on the variables
needing replacement, moving method bodies into the header; rename the
templated class; add a type alias restoring the original name bound to the
original type; in test files, include the template definition and
instantiate it directly with fake types.
