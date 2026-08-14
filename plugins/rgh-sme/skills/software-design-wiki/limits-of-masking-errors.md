---
type: concept
title: Limits of Masking and Defining Away Errors
description: >
  Eliminating or masking an error is only valid when the information it
  carried genuinely isn't needed outside the module doing the hiding —
  errors that carry information callers legitimately need must be exposed
  instead.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

This is [limits of information hiding](limits-of-information-hiding.md)
applied specifically to errors: both
[defining errors out of existence](define-errors-out-of-existence.md) and
[masking exceptions](exception-masking.md) held up in their worked examples
(Tcl `unset`, Java `substring`, NFS) because situations that genuinely needed
the special-case information still had some other way to get it.

Cautionary counter-example: a student networking module masked *all* network
exceptions unconditionally — any network error was silently caught,
discarded, and ignored. The consequence was that applications built on the
module had no way to detect a lost message or a peer/server failure, making
it impossible to build anything robust on top of it. In this case the
exceptions carried genuinely important information, and it needed to be
exposed even at the cost of a more complex module interface.

The general design discipline: correctly identify what's important versus
unimportant. Unimportant things should be hidden as much as possible, but
anything actually important must be exposed, even when that costs interface
simplicity.
