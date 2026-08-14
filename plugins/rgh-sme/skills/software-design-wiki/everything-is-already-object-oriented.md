---
type: concept
title: All Procedural Programs Are Already Object Oriented
description: >
  Wrapping every function in a procedural program inside a single class
  changes nothing about its behavior — the old system was already, in
  effect, one giant object; the real work of introducing more objects is
  subdividing that one object, not bolting OO onto something structureless.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 19"
---

A provocative reframing aimed at procedural-language skeptics of OO: "all
procedural programs are object oriented; it's just a shame that many contain
only one object." Demonstrated with a purely mechanical thought experiment:
take every function declaration in a large C program, wrap them all inside
one class, prefix each function definition with the class name, and replace
the entry point with a `main()` that constructs an instance and calls its
method. This transformation changes nothing about behavior — the old
procedural system was, in reality, just one big object all along.

The real payoff of subsequently applying
[Encapsulate Global References](encapsulate-global-references.md)
(see
[migrating procedural code toward object seams](migrating-toward-object-seams.md))
is that it creates *additional*, smaller objects, subdividing that one giant
implicit object into more workable pieces. The framing matters: this isn't
OO being bolted onto something that lacked structure, it's latent structure
being teased apart from something that already was, trivially, "an object."
Procedural code still has genuinely fewer available techniques than OO
code, and the specific seams a given procedural language happens to offer
materially determine how hard the work is — but the gap is one of available
leverage, not of some deeper structural absence that OO magically supplies.
