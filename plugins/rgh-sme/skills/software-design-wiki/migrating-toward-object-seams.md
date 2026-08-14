---
type: concept
title: Migrating Procedural Code Toward Object Seams
description: >
  Object seams beat link and preprocessing seams for three concrete
  reasons — worth a mechanical, deliberately minimal migration (Encapsulate
  Global References plus Parameterize Constructor) wherever a procedural
  language has an OO path available.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 19"
---

[Object seams](object-seams.md) beat link and
[preprocessing seams](preprocessing-seams.md) for three concrete reasons: they're easier to notice in code; they naturally decompose
code into smaller, understandable pieces; and seams introduced purely for
testing purposes often turn out useful later for genuine feature extension
too — "object seams are good for far more than getting tests in place. Link
and preprocessing seams are great for getting code under test, but they
really don't do much to improve design beyond that." Several procedural
languages have OO successors or extensions (Visual Basic's late move to full
OO, OO extensions for COBOL and FORTRAN, C compilers that can compile C++);
where one exists, migrating toward it unlocks the richer OO toolkit.

**Mechanical migration path**, illustrated moving a C function with a
troublesome global dependency to C++, using
[Encapsulate Global References](encapsulate-global-references.md),
[Parameterize Constructor](parameterize-constructor.md), and
[Preserve Signatures](preserve-signatures.md) throughout to keep each individual step
behaviorally inert:

1. Recompile the file as C++ — a project-wide decision, doable all at once
   or incrementally.
2. Wrap the free function inside a new class whose method of the same name
   delegates to the original global function — no behavior change, just a
   new indirection layer.
3. Declare one **global instance** of that new class, and recompile — the
   resulting compiler errors mechanically point to every call site that
   needs updating to go through the object instead of the bare function
   name ([leaning on the compiler](lean-on-the-compiler.md)).
4. Update callers to go through the global instance instead of the free
   function directly — behavior is still unchanged (same delegation chain),
   but a live object now stands between the call site and the real
   implementation.
5. Wrap the original calling function into its own new class, then apply
   Parameterize Constructor so it accepts the dependency's type as a
   parameter, defaulting to the production global instance via a no-arg
   constructor overload, or a caller-supplied test double via the
   parameterized overload.

Self-assessment of the result: **"These changes are pretty safe and pretty
mechanical. They aren't great examples of object-oriented design, but they
are good enough to use as a wedge to break dependencies and allow us to test
as we move forward."** This is a deliberately minimal, low-risk stepping
stone, not an end-state OO redesign — see
[everything is already object-oriented](everything-is-already-object-oriented.md)
for why this migration is teasing apart latent structure rather than
imposing something foreign on the code. Once OO facilities are available,
the natural next step is incremental design improvement — grouping related
functions into classes and applying
[Extract Method](splitting-and-joining-methods.md) liberally to split
tangled responsibilities.
