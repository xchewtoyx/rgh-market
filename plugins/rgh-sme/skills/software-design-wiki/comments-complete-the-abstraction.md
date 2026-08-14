---
type: concept
title: Comments Complete the Abstraction
description: >
  "Good code is self-documenting" is a myth — a large amount of design
  information cannot be represented in code at all, and comments are what
  supply it, which makes them essential to abstraction itself rather than
  optional polish.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 12"
---

Good practices like strong variable names reduce the *need* for some
comments but don't eliminate it. Only the [formal interface](interface-formal-and-informal-elements.md)
— a method's signature — is expressed in code; the informal interface — a
method's high-level behavior, the meaning of its results, the rationale for
a design decision, the conditions under which it should be called — can only
live in comments. A bare method declaration (name plus parameter and return
types) is not a sufficient [abstraction](abstraction.md) by itself: a
substring-style method taking `start`/`end` can't tell a reader, from its
signature alone, whether `end` is inclusive or what happens if
`start > end`. Comments are what complete the abstraction by supplying
exactly the information callers need while still hiding implementation
detail.

"Just read the method's code instead of documenting it" doesn't hold up
either: deducing a method's abstract behavior by reading its implementation
is slow and error-prone, and it creates a bad incentive — if you expect users
to read implementations, you'll be pushed toward writing many very short
methods to keep each one "readable," producing the exact proliferation of
[shallow methods](method-length-is-not-a-design-criterion.md) that hurts
elsewhere. It doesn't even really succeed at being easier to read, since
understanding the top-level method then requires understanding all its
helper methods too — reading code to learn behavior does not scale to large
systems. If using a method requires reading its code, there is no real
abstraction; all its complexity is exposed.

Comments are deliberately written in natural language rather than a formal
notation: less precise than code, but far more expressive, enabling simple,
intuitive descriptions that a formal spec can't easily match. If you want to
use abstractions to hide complexity, comments are essential — this isn't
optional documentation hygiene, it's a load-bearing part of the design.

(The common objection "every comment I've seen is worthless" has real merit
— most existing documentation genuinely is mediocre — but that's a solvable,
skill-based problem, not evidence that commenting is inherently futile; see
[comments describe non-obvious things](comments-describe-non-obvious-things.md)
for the skill itself.)
