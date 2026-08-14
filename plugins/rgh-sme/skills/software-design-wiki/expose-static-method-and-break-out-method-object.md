---
type: concept
title: Expose Static Method and Break Out Method Object
description: >
  Two shortcuts for testing a method without wrestling its whole class into
  a harness — make it static if it barely uses instance data, or relocate it
  into a small, easily-instantiable class if it's long and unwieldy.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 10"
---

Two up-front shortcuts to try before working through the harder method-level
dependency-breaking cases: if a method doesn't rely on much instance data,
[Expose Static Method](static-as-a-staging-area.md) turns it `static`, sidestepping instantiation of
the containing class entirely for that one method's tests. If the method is
long and unwieldy, **Break Out Method Object** relocates it into a small,
purpose-built class that's much easier to instantiate on its own than the
original — a targeted version of the general move behind
[sprout class](sprout-class.md), aimed at an existing method rather than new
behavior.

Compare [Replace Function with Command](replace-function-with-command.md),
a similarly-shaped move driven primarily by decomposability rather than
testability.

These are cheap, mechanical wins tried before the more invasive per-case
fixes for an inaccessible method
([testing private methods](testing-private-methods.md)), hard-to-construct
parameters, bad side effects, or a needed collaborator that can't be sensed.

**Break Out Method Object in full** (credited to Ward Cunningham, called out
as an idea that "epitomizes the idea of an invented abstraction"): create an
entirely new class whose sole job is to perform one
[monster method's](monster-methods.md) work — the method's parameters become
the new class's constructor parameters, and the method body becomes a
`run()`/`execute()` method on the new class. This solves a specific gap:
sometimes a monster method has local variables that would make ideal
[sensing points](introduce-sensing-variable.md), but they're method-local,
not instance-scoped, so they can't be inspected the way a sensing variable
can — and promoting them to instance variables directly on the original
class would be confusing, since that state would only be meaningful for the
duration of one call. Once the method's body moves into its own small
class, those local variables can freely become instance variables of the
new, short-lived object, since their scope now naturally matches the
object's own lifecycle — making them fully available for sensing and
further internal refactoring.

Key contrast with Introduce Sensing Variable: the resulting instance
variables here are genuinely production-meaningful, not throwaway
instrumentation, so any tests built around them through this technique are
durable and worth keeping, not deleted after the refactoring session ends.

**Three difficulty tiers**, by how much the extracted method depends on the
original object: (1) it uses no instance data at all — no reference to the
original object is needed in the new class; (2) it only uses instance
*data* — that data can be bundled into a small data-holder passed as a
constructor argument, rather than passing the whole original object; (3) it
also calls instance *methods* on the original object (the hardest case) —
this requires Extract Interface on the original class so the new method
object can call back into it through a narrow interface instead of a
concrete reference, bridging the gap.

Worked example at tier 3: a graphics `draw()` method extracted into a new
`Renderer` class that still needs to call a private helper on the original
object. Satisfying the compiler forces exposing that helper (making it
public, or reachable via a getter) purely so the new class can call it — an
explicit gut-check moment: "you might have a sick feeling in the pit of your
stomach because we've made details that were private in the original class
public." The reassurance: "this isn't really the end" — once the new class
is genuinely under test, dependencies can be broken further (Extract
Interface on the original class to narrow what the new class actually
depends on) and the design keeps evolving from there.

Steps: create the new class; give it a constructor with the exact original
argument list ([Preserve Signatures](preserve-signatures.md)), prefixed with
a reference to the original object if instance state is used; turn each
constructor argument into an identically-typed instance variable assigned in
the constructor; add an empty execution method (commonly `run()`); copy the
original method's body into it and recompile,
[leaning on the compiler](lean-on-the-compiler.md) to surface every
remaining dependency on the old class; resolve each compile error (route
through the held reference, or expose members as needed); once it compiles,
rewrite the original method to construct the new class and delegate to it;
if warranted, apply Extract Interface to fully decouple the new class from
the original.
