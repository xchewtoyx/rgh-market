---
type: concept
title: Mock Only Types You Own
description: >
  Wrap third-party unmanaged dependencies in your own adapters and mock those
  adapters — never mock library types directly, because you can't predict
  upgrades and mocked behavior rarely matches reality.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 9"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

Attributed to Freeman and Pryce (*Growing Object-Oriented Software, Guided by
Tests*): write adapters atop third-party libraries; mock **your** adapters, not
library types.

Reasons:

- Rarely deep enough understanding of third-party code to mock behavior
  faithfully, even when the library ships interfaces.
- Adapters express the relationship in **your domain language** and hide
  non-essential detail — an **anticorruption layer** (Evans, DDD).

`IBus` over a message-bus SDK confines upgrade blast radius to the adapter.

Does **not** apply to in-process managed dependencies you don't mock anyway
(clock APIs used only against invisible databases). Wrapping those is optional
and rarely worth the effort.

Pairs with [interfaces for unmanaged dependencies only](interfaces-for-unmanaged-dependencies-only.md)
and [mock at system edges](mock-at-system-edges.md).

When a nontrivial collaborator needs a fake, prefer the **owning team** provide
and maintain it — see [overabstracted tests](tests-should-assert-behavior-not-call-mechanics.md).
