---
type: concept
title: Extract and Override Call
description: >
  When one localized call — often to a static method or global — is the
  dependency problem, extract just that call into its own method and
  override the wrapper in a testing subclass; the default first choice for
  breaking dependencies on globals and statics.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

When a single, localized method call — often to a static method or a
global — is the whole dependency problem, not the containing type as a
whole: extract just that call into a new method on the current class
([Preserve Signatures](preserve-signatures.md) for the extracted method),
replace the original call site with a call to the new wrapper method, then
[subclass and override](subclass-and-override-method.md) the wrapper in a
testing subclass to substitute a fake return value.

Positioned as one of the most frequently used dependency-breaking
techniques, and the default first choice for breaking dependencies on
**globals and static methods**. An explicit boundary condition: switch to
[replacing a global reference with a getter](replace-global-reference-with-getter.md)
instead if there are *many different calls* against the *same* global —
this technique doesn't scale well to many call sites all needing the same
substitution, since each would need its own wrapper. Trivial to perform with
a safe automated Extract Method tool; the manual steps exist specifically
for doing it safely without one.

Steps: find the call to extract and copy its target method's exact
signature (Preserve Signatures); create a new method on the current class
with that signature; move the call into the new method's body, and replace
the original call site with a call to the new method.
