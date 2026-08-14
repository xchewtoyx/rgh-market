---
type: concept
title: Hard-to-Misuse APIs Drive Voluntary Adoption
description: >
  An API that is easy to use correctly gets adopted voluntarily and used
  correctly by default; a technically-correct API that is cumbersome gets
  adopted slowly, misused, or bypassed.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 6, Considering API Usability"
---

A correctness- or safety-preserving API design (see [parse, don't
validate](parse-dont-validate.md) and [define errors out of
existence](define-errors-out-of-existence.md)) only pays off if callers
actually use it. If the API is cumbersome relative to the unsafe
alternative, developers are slow or reluctant to adopt it, and route around
it under time pressure. The fix is to make the safe path not just
correct but genuinely easier to use than the unsafe one — "the double
benefit of making your code more understandable and allowing developers to
focus on the logic of your application" while the API quietly builds
correct behavior in by construction.

A contextually autoescaping HTML template system is the sharpest example:
from the caller's side it behaves like an ordinary template — supply data,
get markup back — except the caller no longer has to remember to add
escaping or validation directives at all. The safety property (freedom from
injection) is bought entirely inside the template system's implementation;
the caller-facing interface is *simpler* than the unsafe alternative, not
more burdensome, which is what makes adoption a byproduct of normal
development rather than a discipline callers must be reminded to uphold.
This is the same [make the common case simple](interfaces-should-make-the-common-case-simple.md)
principle, applied specifically to safety-relevant behavior: hiding the
safe-vs-unsafe choice entirely rather than exposing it as an opt-in flag
beats documenting the correct flag value and hoping every caller reads the
docs.

The limit: a library or framework designed this way can only prevent the
class of mistake it specifically targets. A crypto library that makes
low-level primitive misuse hard to make (nonce reuse, unauthenticated
encryption) does not prevent a caller from choosing the wrong primitive
altogether (hashing a low-entropy value like a credit card number instead
of using authenticated encryption) — that is a design-level mistake one
layer above the API's contract, and no amount of interface polish inside
the library closes it. Knowing precisely what a hard-to-misuse API does and
does not guarantee is part of using it correctly.
