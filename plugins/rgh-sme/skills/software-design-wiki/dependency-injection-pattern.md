---
type: concept
title: "Dependency Injection: Named Roles"
description: >
  Dependency injection separates a client's dependencies from its behavior
  by having an external injector supply a concrete implementation of an
  interface the client depends on, rather than the client constructing or
  looking up that implementation itself.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 12"
---

Dependency injection names four roles in what [dependency
inversion](dependency-inversion-principle.md) and [extracting an
interface](extract-interface.md) produce mechanically: a **service** (the
thing being depended on), a **client** (the thing depending on it), an
**interface** (what the client actually codes against — the service
implements it, the client only knows it exists), and an **injector**
(whatever constructs a concrete service instance and hands, or "injects,"
it into the client). The client never names the concrete implementation
type; it receives one, typically through a constructor parameter, already
resolved by the injector — often at startup, sometimes per-call.

The direct payoff for testing: since the client has zero awareness of
*how* it's supplied its dependency, a test can act as the injector and
hand the client a [fake](fake-objects.md) or [mock](mock-objects.md) test
double instead of the real service, with the client's own code completely
unaware anything different happened. This is the mechanism most modern
testing frameworks build on, and it's the same underlying move as manually
threading a fake through a constructor — dependency injection just names
it and, in frameworks that support it, automates the wiring.

**Trade-offs**: injecting a different implementation for testing than
production runs means the injected instance can alter the very behavior
under test (a fake's timing or error handling rarely matches the real
service's exactly), making runtime performance and edge-case behavior of
the test less predictable as evidence about production. Dependency
injection also adds real up-front structure — an interface and an
injection point for every dependency — and asks developers to think in
inversion-of-control terms, which is a genuine shift from directly
constructing what you need where you need it.
