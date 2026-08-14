---
type: concept
title: Better Together or Better Apart?
description: >
  Whether two pieces of functionality should live in one module or be split
  apart is a recurring design question at every scale, and the naive
  intuition that smaller components are always simpler is wrong — splitting
  has its own complexity costs.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
---

This question recurs at every level — functions, methods, classes,
services. Subdividing adds its own complexity, in four ways:

1. **Component count** — more things to track and find, and usually more
   interfaces, each imposing its own
   [complexity cost](design-cost-benefit-of-infrastructure.md).
2. **Management overhead** — code that used one object before subdivision may
   now have to juggle several.
3. **Separation** — subdivided pieces end up farther apart (different
   classes, different files). This is good when the pieces are truly
   independent, letting a developer focus on one at a time; it's bad when
   they're actually dependent, since developers must flip back and forth
   between them — and may not even realize the dependency exists, risking
   bugs. See [conjoined methods](conjoined-methods.md) for the sharpest form
   of this failure.
4. **Duplication** — code present once before subdivision may need
   duplicating across the new pieces; see the
   [repetition red flag](code-duplication-red-flag.md).

Joining is most beneficial when two pieces are genuinely related, which shows
up as one or more of four signals:

- **They share information** — e.g. both depend on the same document format's
  syntax. See [class size as an information-hiding decision](class-size-as-a-hiding-decision.md)
  for the read/parse example this drives.
- **They're used together bidirectionally.** A one-way pairing isn't enough:
  a disk block cache almost always uses a hash table, but hash tables are used
  in plenty of contexts without block caches, so despite the pairing they
  should stay separate.
- **They overlap conceptually** under one natural higher-level category —
  substring search and case conversion are both "string manipulation"; flow
  control and reliable delivery are both "network communication."
- **It's hard to understand one piece without the other.**

Combining related pieces can also simplify the resulting interface directly —
eliminating an intermediate interface that only existed to pass data between
the separated pieces, or letting functionality happen automatically and
invisibly instead of requiring an extra step (the case against splitting
buffering out of the base I/O class; see
[decorators tend to be shallow](decorator-pattern-and-shallow-classes.md)).

The inverse failure — joining things that should stay apart — is
[special-general mixture](special-general-mixture.md): combining a
general-purpose mechanism with knowledge specific to one use of it. See
[separating general- and special-purpose code](separate-general-and-special-purpose-code.md)
for the discipline that prevents it. The decision should always be driven by
the actual complexity outcome: choose whichever structure yields the best
[information hiding](information-hiding.md), the fewest inter-module
[dependencies](dependencies-as-a-cause-of-complexity.md), and the
[deepest](deep-modules.md) resulting interfaces — not a fixed rule like
"smaller is simpler" or "N lines means split it" (see
[method length is not a design criterion](method-length-is-not-a-design-criterion.md)).
