---
type: concept
title: Static Methods as a Staging Area for Misplaced Behavior
description: >
  Making a method static when it touches no instance data doesn't violate
  encapsulation — the static area isn't really part of the class — and it
  makes a method's true, class-agnostic nature visible until you figure out
  where it actually belongs.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

**Expose Static Method**: when a method doesn't touch instance data or
instance methods but its containing class is very hard to instantiate,
converting the method to `static` lets you test it without ever constructing
the class. A method that only calls methods on its own parameters, never on
`this`, is a strong hint it might belong on a *different* class entirely —
but moving it immediately, without [Preserve Signatures](preserve-signatures.md)
guarantees and without tests, is riskier than the intermediate step of
exposing it as static first, testing it there, and only then considering the
move with real confidence.

The apparent "ugliness" of a public static utility method isn't actually an
encapsulation violation: "the static area of a class isn't really part of
the class" — in some languages it effectively belongs to a separate
metaclass. A static method that touches no instance state is provably just a
utility function, safe to expose. This reframes the static area as a
**staging area**: "if you see a method that doesn't use any instance data,
it is a good idea to make it static to make it noticeable until you figure
out what class it really belongs on" — the same framing used for
[sprout method's](sprout-method.md) accumulating static helpers, which
often signal a new class wanting to be extracted once several of them share
variables.

If worried about the exposed static becoming an attractive nuisance (other
code building new dependencies on it before it's properly placed), restrict
its visibility — package/internal scope, or accessible only via a testing
subclass.

Steps: write a test calling the method as if it were already a public
static; extract its body into a static method with Preserve Signatures,
choosing a new name (commonly built from a parameter name); compile; if
compilation fails on remaining instance-data or instance-method access,
check whether those dependencies can also be made static, and do so if
possible.
