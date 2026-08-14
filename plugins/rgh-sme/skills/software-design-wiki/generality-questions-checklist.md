---
type: concept
title: Self-Check Questions for Calibrating Generality
description: >
  Three questions for checking whether a module's interface is landing at
  the "somewhat general-purpose" sweet spot, rather than too special-purpose
  or over-generalized.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 6"
---

Recognizing a good [general-purpose module](general-purpose-modules-are-deeper.md)
is easier than creating one from scratch, so it helps to have concrete
questions to ask of a draft interface:

1. **"What is the simplest interface that will cover all my current needs?"**
   Fewer methods without losing capability usually signals a more
   general-purpose design (three deletion methods collapsing into one).
   Caveat: this only counts if each method's own signature stays simple —
   offloading complexity into a pile of extra parameters isn't real
   simplification, it's [information leakage](information-leakage.md) by
   another name.
2. **"In how many situations will this method be used?"** A method designed
   for exactly one call site is a [red flag](red-flags-as-design-smells.md)
   for being too special-purpose; look for a way to fold several such methods
   into one general method.
3. **"Is this API easy to use for my current needs?"** Checks the opposite
   failure mode — over-generalizing. A text class built only around
   single-character `insert`/`delete` would be maximally simple and general,
   but would force calling code into loops for every multi-character
   operation and be inefficient for large edits — built-in range operations
   are the right call despite being "less minimal."
