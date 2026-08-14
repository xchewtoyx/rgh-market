---
type: concept
title: Connector Semantics
description: >
  Documenting a connector means naming which interaction mechanism it
  actually is — call/return, message queue, shared data, event, or
  stream — because that choice determines what can be reasoned about it.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

In a [component-and-connector view](component-and-connector-view.md), the
connector is not a neutral line between two boxes — it is itself an
architectural element with semantics that must be made visible, not left
for the reader to guess from the diagram. The standard vocabulary of
connector kinds is: call/return (synchronous invocation), message queue,
shared data, event, and stream. Each implies different guarantees about
ordering, blocking, delivery, and failure — a "call/return" connector that
is actually implemented as a message queue with retries behaves very
differently under partial failure than the diagram suggests if that
distinction isn't documented.

This is why an arrow drawn between two components, without stating which
of these mechanisms it is, actively conceals information rather than
merely omitting detail: a reader cannot tell whether the interaction is
synchronous or async, ordered or unordered, at-most-once or at-least-once,
without it. Document the mechanism explicitly for every connector type
used in a [component-and-connector view](component-and-connector-view.md),
alongside its topology and properties.
