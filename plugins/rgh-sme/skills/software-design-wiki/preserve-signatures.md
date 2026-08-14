---
type: concept
title: Preserve Signatures
description: >
  When extracting a method before tests exist, keep its exact original
  signature so the whole argument list can be cut/copy/pasted verbatim
  rather than retyped, eliminating an entire class of transcription
  mistakes at the moment you're least able to catch them.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 23"
---

Refactoring is inherently more invasive and error-prone than routine edits,
yet the very earliest [dependency-breaking techniques](dependency-breaking-vs-refactoring.md)
are, by definition, done *before* any tests exist to catch mistakes — so
they need to be unusually conservative. A confessional anti-example: trying
to "improve the design" *while* breaking a dependency — turning a method's
plain argument list into freshly-invented helper objects in the same step as
extracting it — produces foolish, untested mistakes that surface "far later
than they needed to."

**Preserve Signatures** is the fix: when extracting a method, keep its
**exact original signature** — same parameter list, same types, same
order — so the entire argument list can be cut/copy/pasted verbatim between
the old and new declarations rather than retyped or restructured. A
mechanical six-step procedure makes this automatic: (1) copy the full
original argument list to the clipboard; (2) type a bare new method
declaration with empty parens; (3) paste the argument list in; (4) type a
bare call to the new method with empty parens; (5) paste the same argument
list into the call; (6) go back and strip the types from the call, leaving
just argument names. With practice this becomes automatic, freeing attention
for the other genuine risks in the extraction — like accidentally shadowing
or overriding a base-class method of the same name.

Preserve Signatures applies beyond plain method extraction too — it's the
same mechanism used to generate the full instance-method parameter list when
doing [Break Out Method Object](expose-static-method-and-break-out-method-object.md),
and the same discipline underlies the backward-compatibility trick in
[Parameterize Constructor](parameterize-constructor.md).
