---
type: concept
title: Event-Based Style
description: >
  Event-based styles decouple producers and consumers through implicit
  invocation or publish-subscribe, and documentation must cover event
  types, delivery/ordering/reliability guarantees, and subscription and
  coordination semantics.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Event-based is a [component-and-connector style](component-and-connector-view.md)
in which components interact through events rather than direct invocation
— implicit invocation (a component announces an event and any interested
component reacts) and publish-subscribe (explicit subscription to named
event types) are the common forms. The point of the style is decoupling:
a producer doesn't need to know who, if anyone, is listening.

That same decoupling is what makes the style hard to reason about from
code alone, which is why documentation carries more of the burden here
than in a [call-return style](call-return-style.md): what event types
exist, how delivery works (at-most-once, at-least-once, exactly-once), what
ordering guarantees hold across events and across consumers, how
reliability is handled when a consumer is down, how subscription is
established and torn down, and what coordination (if any) exists between
otherwise-independent reactions to the same event. Without this, tracing
"what happens when X occurs" requires reading every component's source
rather than the architecture.
