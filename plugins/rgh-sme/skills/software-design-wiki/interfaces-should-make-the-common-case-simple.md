---
type: concept
title: Interfaces Should Make the Common Case Simple
description: >
  An interface can support many rarely-needed features and still have low
  effective complexity, as long as most callers only ever need to learn the
  commonly-used subset.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

Contrast the [classitis](classitis.md) example — Java's I/O stream stacking,
where the near-universal need for buffering must be opted into by composing an
extra wrapper object every caller must remember — with Unix system calls,
which default to sequential access (the common case) and offer `lseek` as a
separate call for the uncommon random-access case. Sequential-only callers
never need to know `lseek` exists.

The general design principle: rarely-needed variations should be **opt-out**
via a clearly separated mechanism (an alternate constructor, an extra
parameter with a sane default, a separate call) rather than **opt-in** via
composition that every caller has to remember to apply. An interface's
*effective* complexity, from a given caller's point of view, is only the
subset of the interface that caller actually has to learn — a
[deep module](deep-modules.md) can carry many features and still feel simple
if the common path is the short one.

Good defaults are a form of partial [information hiding](information-hiding.md):
they let the normal caller not even know an option exists. A recurring mistake
is requiring a value the caller could derive automatically — e.g. requiring an
HTTP response builder to be told the protocol version explicitly, when it's
always derivable from the associated request the caller already has to pass
in, or omitting a sensible default `Date` header. "The best features are the
ones you get without even knowing they exist." Violating this in the other
direction is its own named problem:

**Red flag: overexposure** — "If the API for a commonly used feature forces
users to learn about other features that are rarely used, this increases the
cognitive load on users who don't need the rarely used features."

The same simplicity that reduces cognitive load also drives adoption: an
interface that's easy to use correctly gets used correctly by default,
while a cumbersome-but-technically-safe interface gets bypassed under
pressure — see [hard-to-misuse APIs drive voluntary
adoption](hard-to-misuse-apis.md). [Fluent interfaces](fluent-interfaces-as-documentation.md)
are one concrete stylistic tool for this, worth reaching for only where the
resulting vocabulary genuinely matches how the domain is discussed.
