---
type: concept
title: Skin and Wrap the API
description: >
  Define your own interfaces mirroring a third-party API's surface, wrap
  each real API class behind an implementer of the matching interface, and
  let tests substitute fakes — full isolation at the cost of a thin,
  mechanical delegation layer to maintain.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 14-15"
---

Define your own interfaces that mirror a library's API as closely as
possible, then wrap each real API class behind an implementer of the
matching interface, using [Preserve Signatures](preserve-signatures.md) to minimize mistakes while
doing so. Production code delegates through the wrapper to the real API;
tests substitute a [fake](fake-objects.md) implementing the same interface.

Best suited when the API surface is small, when you want to fully sever
dependency on a specific third-party library (see
[library lock-in from scattered calls](library-lock-in-from-scattered-calls.md)),
or when you have no tests at all and literally cannot exercise the API
surface directly. The payoff: everything except the thin, mechanical
delegation layer becomes independently testable.

It doesn't always work cleanly. A worked negative case: wrapping a mail
API's session/transport objects fails partway when you don't directly
construct the object needing wrapping (it's returned by a factory method
elsewhere in the API) and the class itself is `final`, blocking
subclass-based wrapping outright. See
[wrapping sealed or final third-party classes](wrapping-sealed-third-party-classes.md)
for the specific fallback ([Adapt Parameter](adapt-parameter.md)) when sealing closes off the
direct route. Even when skinning a class turns out to be a poor fit for the
API's actual shape, it can still be "the safest course," if no refactoring
tool is available to do something less invasive safely.

Contrast with [responsibility-based extraction](responsibility-based-extraction.md),
a lighter-weight alternative with a different trade-off profile — many teams
end up using both together.

The same wrapping shape, motivated instead by protecting your own model's
vocabulary and assumptions from a foreign or unstable one rather than by
testability, is called an [anticorruption layer](anticorruption-layer.md).
