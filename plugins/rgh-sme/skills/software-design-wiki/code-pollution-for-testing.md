---
type: concept
title: Code Pollution for Testing
description: >
  Production code added solely to support tests — environment switches,
  ambient contexts — raises production maintenance cost; prefer interfaces
  with fakes over test-only branches in production paths.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 11"
---

**Code pollution** is production code existing only because tests need it.
Common form: boolean switches (e.g. `Logger(isTestEnvironment)` that
no-ops `Log()` in tests). This mixes test and production concerns and
increases production maintenance burden.

**Fix**: introduce an interface with two implementations — real for production,
[fake](fake-objects.md) for tests — and inject the interface. The interface
itself is milder pollution (no executable test-only path accidentally reachable
in production), but still a design cost to weigh against alternatives.

Same anti-pattern applies to **ambient context** for time: a static
`DateTimeServer.Now` shared across tests pulls tests toward integration-style
interference. Prefer [injecting time as an explicit dependency](inject-time-as-explicit-dependency.md)
— a value or service passed in, not a static clock.

See [test doubles overview](test-doubles-overview.md) and [humble object
pattern](humble-object-pattern.md) for separating testability concerns from
domain logic structurally rather than with flags.
