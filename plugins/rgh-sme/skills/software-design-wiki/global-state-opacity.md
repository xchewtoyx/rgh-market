---
type: concept
title: Global State's Real Cost Is Opacity
description: >
  The core problem with globals and singletons isn't the pattern itself but
  that they hide what a piece of code can affect — ordinary parameters and
  return values are visible from the call site, global access isn't.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3, Global Data"
---

Ordinary object interactions — constructor arguments, method parameters,
return values — tell you everything a piece of code can affect just by
reading its signature. Global or singleton access breaks this: you can't
tell from a call site what shared state might be read or mutated elsewhere
in the system. This **opacity**, not the singleton pattern specifically, is
the core critique — the practical testing cost is that you must discover and
correctly configure every global a class touches before every test, which
is, from direct repeated experience, "pretty tedious... it doesn't get any
more enjoyable."

A framework's inversion-of-control style ("your code is used by the
framework, not the other way around") is noted as a related but distinct
observation: real, old-style component reuse — pulling a class out and
compiling it standalone — is rare in practice, and the inability to isolate
an "average" class in a test harness is itself evidence that this kind of
reuse claim is often illusory. See
[breaking singleton dependencies](breaking-singleton-dependencies.md) for
the specific techniques that make a global fake-able for tests, and
[localizing global dependencies](localize-global-dependencies.md) for the
more fundamental design fix.

Fowler and Beck name the same problem from a pure design (not
testability) angle as the **Global Data** smell, and phrase it as "spooky
action from a distance" — it applies equally to global variables, class
variables, and singletons. Their entry-point cure is always [Encapsulate
Global References](encapsulate-global-references.md): gain visibility and
control over access first, then shrink the data's scope as much as
possible, ideally to module- or class-local. Mutable global data is far
worse than immutable global data, if the language can enforce immutability
— they cite Paracelsus's maxim that dose makes the poison: small amounts of
global data are tolerable as long as they're still encapsulated behind a
narrow point of access.
