---
type: concept
title: Heuristics for Characterizing Classes
description: >
  Concrete tactics for generating characterization tests when a class's
  behavior isn't yet understood — sensing variables, cataloguing what could
  go wrong, probing edge cases, and looking for invariants — ordered to
  double as documentation for the next reader.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

Four tactics for generating [characterization tests](characterization-tests.md)
of tangled or unclear logic:

1. [Introduce a sensing variable](introduce-sensing-variable.md) to confirm
   a suspected code path
   actually executes, as a way of characterizing behavior you don't yet
   fully understand.
2. As you learn a class's or method's responsibilities, actively list things
   that could go wrong, and try to write tests that would trigger each one.
3. Deliberately probe extreme or edge-case inputs.
4. Look for [invariants](invariants.md) — conditions that should hold
   throughout an object's lifetime — and try to write tests that verify
   them; discovering these sometimes requires refactoring first, which in
   turn often surfaces new insight about how the code should be structured.

Order the resulting tests the way you'd want to learn the class if you'd
never seen it — simple mainline cases first, idiosyncrasies later — using the
fact that test files are just ordinary, file-ordered methods to intentionally
curate a learning path for the next reader. There's a natural convergence
here: the tests written to satisfy curiosity about a class often turn out to
be exactly the tests needed for the specific change about to be made,
whether or not that's a conscious goal at the time.
