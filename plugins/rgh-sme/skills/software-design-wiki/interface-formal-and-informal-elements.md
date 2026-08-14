---
type: concept
title: Formal and Informal Interface Elements
description: >
  A module's interface includes both formal elements enforced by the
  language and informal elements conveyed only through comments — and for
  most interfaces the informal part is the larger, more important half.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

**Formal elements** are explicit in code and checkable by the language: a
method's signature (parameter names and types, return type, declared
exceptions), or, for a class, the full set of public method signatures and
public variable declarations.

**Informal elements** are everything a caller needs to know that the language
doesn't enforce: high-level behavioral facts ("this function deletes the file
named by its argument"), or usage constraints such as required call order.
These can only be conveyed through comments — see
[comments describe non-obvious things](comments-describe-non-obvious-things.md)
— and for most real interfaces, the informal part is larger and more complex
than the formal part.

The test for whether something belongs in the interface at all is simple: if a
developer needs a piece of information to use the module correctly, it's part
of the interface, whether or not the language happens to enforce it. A clearly
specified interface — formal and informal — is the direct antidote to
[unknown unknowns](unknown-unknowns.md): it tells developers exactly what they
need to know, and nothing they don't.
