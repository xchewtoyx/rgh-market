---
type: concept
title: Know Your Language's Scoping Guarantees Before Trusting Them
description: >
  Effect tracing depends on knowing exactly where a language's
  visibility rules mechanically block propagation — and on checking
  whether an apparent guarantee, like a const method, has been locally
  circumvented.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 11"
---

The central tool for [effect analysis](effect-propagation-mechanisms.md)
isn't a piece of software but deep knowledge of a language's own
scoping/visibility "firewalls" — the places propagation is mechanically
blocked, so you know when it's safe to stop tracing. A class with strictly
`private` fields only propagates effects through its own methods, regardless
of subclassing; the same class with package-scoped fields lets any class in
the same package (or a subclass, if the fields were `protected`) mutate them
directly, invisibly to someone reading only method signatures.

Even an apparent language guarantee can be locally circumvented: a C++
method marked `const` looks read-only, but a class can declare a field
`mutable`, explicitly permitting `const` methods to modify it anyway.
"This use of mutable is particularly odd, but... we have to look for effects
regardless of how odd they might be." Don't take a language guarantee at
face value without checking whether it's been locally overridden somewhere
in the hierarchy. One-line takeaway: **"Know your language."**

Programming gets easier in general as effects narrow — pushed to the
extreme, this is the appeal of pure functional languages. In mainstream
object-oriented languages, deliberately restricting effects still
meaningfully eases testing, "and there aren't any hurdles to doing it."
