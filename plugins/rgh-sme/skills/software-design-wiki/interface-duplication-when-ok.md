---
type: concept
title: When Interface Duplication Is OK
description: >
  Same-signature methods across classes aren't automatically a
  pass-through-style design flaw — they're fine when each one contributes
  significant, distinct functionality of its own.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
---

The test for whether a shared method signature is a problem is not "do these
look alike?" but "does each one do something real?" —
[pass-through methods](pass-through-methods.md) fail this test because they
add no functionality of their own. Two legitimate patterns pass it:

- **Dispatcher**: a method that inspects its arguments to select and invoke
  one of several other methods, often sharing the dispatcher's own signature.
  The selection logic itself is real functionality — a web server's request
  dispatcher examining an incoming URL and routing to a file-serving handler,
  a script handler, and so on, via a (possibly intricate) rule set, is doing
  genuine work even though every branch shares a signature.
- **Interchangeable implementations of one interface** — for example, disk
  drivers for different disk types. A shared signature here actually reduces
  [cognitive load](cognitive-load.md), since learning one implementation's
  interface transfers directly to the others. These are typically peers
  within the same layer and don't call each other, unlike the
  dispatcher/pass-through cases, which cross layers.
