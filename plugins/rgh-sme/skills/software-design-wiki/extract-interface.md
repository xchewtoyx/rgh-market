---
type: concept
title: Extract Interface
description: >
  One of the safest dependency-breaking techniques, since a compiler catches
  most mistakes immediately — extract only the methods actually in use,
  driven by compile errors, rather than mirroring the whole class up front.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Extract Interface is one of the safest dependency-breaking techniques
available, because in most statically typed languages any misstep is caught
immediately by the compiler — very low risk of silently introducing a bug.
This is the mechanism behind
[the dependency inversion principle](dependency-inversion-principle.md) and
[compilation firewalls](compilation-firewall.md) in practice.

Three ways to perform it, ranked by safety and convenience: an automated
refactoring tool (best case — some even update every reference
automatically); incremental manual extraction, driven method-by-method off
compiler errors; or bulk cut/copy/paste of several method declarations at
once — less safe, but sometimes the only practical option without tooling
when builds are slow.

**Incremental method, worked example**: reference a not-yet-existing fake
implementation in a test first, forcing the compiler to demand it exist.
Create an **empty** new interface, make the real class implement it (trivial
to compile, since it has no methods yet), create the fake implementing it
too, then swap the dependency's declared type from the concrete class to the
new interface and let the resulting compile errors — one at a time —
dictate exactly which method signatures actually need to be added to the
interface and stubbed in the fake.

**Key efficiency insight**: "when you extract an interface, you don't have
to extract all of the public methods on the class you are extracting from.
[Lean on the compiler](lean-on-the-compiler.md) to find the ones that are
being used." The goal is covering exactly what's needed to get the code
under test, not producing a "complete," symmetrical interface as an end in
itself — completeness can come incrementally later, once more of the
codebase is under test.

**Naming**: the historical `I`-prefix convention (`Account` → `IAccount`)
traces to a desire to avoid thinking about naming at extraction time, but
risks inconsistent prefixing across a codebase and a name that becomes "a
subtle lie" if a class later stops needing the interface but keeps the `I`.
For new code, start with plain simple class names and only convert to an
interface later via [Extract Implementer](extract-implementer.md) if and
when actually needed, deferring the interface-vs-class decision until it's
forced by a real requirement.

**The non-virtual method gotcha** (C++ and, more cautiously, C# — Java
sidesteps this entirely since all instance methods are virtual there):
pulling a **non-virtual** method's signature into a new interface and making
it `virtual` there **retroactively makes the base class's own method
virtual too** — silently changing dispatch behavior for any subclass that
happens to define a method with the same name and signature, even if that
subclass never touches the new interface at all. A base method previously
always resolved at compile time can start resolving polymorphically to a
subclass override instead — a silent behavior change purely from the "safe"
act of extracting an interface. Extracting a non-virtual method into an
interface is safe **only if the class has no subclasses**; if it does, add a
*new*, differently-named virtual method to the interface that delegates to
the existing non-virtual (or static) method instead of promoting the
original signature directly, and verify the delegation is correct for every
subclass beneath the one being extracted from.

Steps: create the new interface with the desired name and zero methods;
make the source class implement it (behaviorally inert, since it has no
methods yet, but compile and test anyway to confirm); change the target
usage site's declared type from the concrete class to the interface;
recompile, and for each resulting compiler error, add exactly the needed
method declaration to the interface (and a stub implementation to the fake)
until the build succeeds.
