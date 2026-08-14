---
type: concept
title: "Anti-pattern: Anemic Domain Model"
description: >
  An anemic domain model is a whole object model built from data classes —
  fields and getters/setters with no behavior — while all the logic that
  should live with that data sits in separate "service" classes instead.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 10"
---

An anemic domain model is the [data class](data-class.md) smell scaled up to
an entire object model: every domain object (`Quiz`, `Order`, `Account`, ...)
is a bag of fields with getters and setters and no behavior, while a matching
"service" or "manager" class (`QuizApplicationService`, `OrderManager`) holds
every operation that touches that data. The model looks object-oriented — it
has classes named after domain nouns — but none of the objects actually do
anything; all the logic is elsewhere, manipulating the data from outside.

The fix mirrors Data Class's cure: trace where the service class reads and
writes an object's fields to perform some operation, and Move Function that
behavior onto the object itself. A `Quiz` gains real methods —
`start()`, `complete()`, `pause()`, `resume()` — each of which validates the
object's own current state before transitioning it, rather than a
`QuizApplicationService` reaching into a passive `Quiz`'s getters and setters
to do the same validation from outside. This is the same underlying
diagnosis as [encapsulation is a tool, not a goal](encapsulation-is-a-tool-not-a-goal.md):
an anemic model has the encapsulation boundary (a class per concept) without
the substance (behavior enforcing that concept's own rules), so callers are
left to enforce those rules correctly and consistently every time they touch
the data — the opposite of [information hiding](information-hiding.md).

Two related design rules describe where this behavior should and shouldn't
live: an [aggregate enforces its invariants through a single
root](aggregate-consistency-boundary.md), and the orchestration layer
above the domain model should stay [free of business logic
itself](application-service-orchestration-only.md).
