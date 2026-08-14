---
type: concept
title: Call-Return Style
description: >
  Call-return styles organize synchronous invocation between components —
  main-program/subroutine, client-server, and tiered forms — making
  control flow explicit at the cost of coupling and blocking.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Call-return is a [component-and-connector style](component-and-connector-view.md)
built on synchronous invocation: a caller invokes an operation and blocks
until it returns. Common forms are main-program/subroutine (a single
control thread calling into library-like components), client-server (one
component offers services that others invoke over a network), and tiered
architectures (a chain of client-server relationships stacked into layers,
e.g. presentation calling business logic calling data access).

The style's advantage is that control flow is explicit and easy to trace
from the diagram: you can follow who calls whom and in what order. The
cost is coupling and blocking — a caller cannot proceed until the callee
responds, so a slow or unavailable callee directly stalls the caller, and
callers generally need to know the specific interface of who they're
calling. Document which tier or layer is permitted to call which other —
this is effectively a [layered view](layered-view.md) constraint applied
to the runtime call structure — and whether calls cross process or network
boundaries, since that changes the failure modes involved even though the
logical style looks the same on the page.
