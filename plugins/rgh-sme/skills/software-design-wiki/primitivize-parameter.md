---
type: concept
title: Primitivize Parameter
description: >
  A last-resort escape hatch for a class too pervasively entangled to test
  directly — write the needed logic as a free function over a simplified,
  primitive representation of the class's data, test that in isolation,
  then wrap it in a thin real method.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

An escape hatch for the extreme case where a class is so pervasively
entangled — transitively depending on nearly every other class in the
system, all tied into a persistence framework, say — that bringing it under
test directly would stall feature work for an unacceptable length of time.
Rather than writing the needed logic as a real method on the untestable
class, write it as a **free function operating on a primitive or simplified
representation** of the class's relevant data (a plain array of numbers
instead of a collection of domain objects), fully test *that* function in
isolation, then add a thin real method on the actual class that converts its
own state into the primitive representation and delegates to the free
function.

Unusually candid self-critique, explicitly listed as "horrible": it exposes
the internal representation of the original class; it makes the class's
real implementation harder to understand by scattering logic into an
unrelated free function; the new glue code that builds the primitive
representation is itself untested; it duplicates data in the system; and it
**prolongs** the real underlying problem — the dependency tangle — rather
than solving it. Despite all of that: "we were able to add a tested
feature." Personal stance: "I don't like to do this refactoring, but I will
use it if my back is against the wall." Better alternatives when available:
add the code directly to the original class, or use
[Sprout Class](sprout-class.md) to build a proper new abstraction as a
foundation — Primitivize Parameter is a plausible *predecessor* to Sprout
Class, since the free function can later be wrapped in a proper class. Only
reach for this when confident the untested class will genuinely be brought
under test later, at which point the free function can be folded back in as
a real method.

Steps: write a free function performing the needed logic against an
intermediate, simplified representation; add a method to the original class
that builds that representation from its own state and delegates to the
free function.
