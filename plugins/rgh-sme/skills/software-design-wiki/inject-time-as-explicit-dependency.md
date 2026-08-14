---
type: concept
title: Inject Time as Explicit Dependency
description: >
  Time-dependent tests fail when Act and Assert read different clocks;
  inject a fixed DateTime or clock service rather than using ambient static
  time, preferring plain values over services where feasible.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 11"
---

Time-dependent tests risk false positives when the time read during act differs
from the time used in assert.

**Anti-pattern — ambient context**: static `DateTimeServer.Now` initialized
once with real or fixed clock. Pollutes production code; static/shared state
makes tests interfere like integration tests. Same class of problem as
[code pollution for testing](code-pollution-for-testing.md).

**Preferred — explicit dependency**: inject `IDateTimeServer` (service) or a
plain `DateTime` (value). Prefer injecting the **value** where possible —
values are easier in production code and trivial to supply in tests. When DI
frameworks handle values poorly, inject the service at the start of an
operation and thread the resulting timestamp through the rest of that
operation.

See [virtualizing external resources for testing](virtualize-external-resources-for-testing.md)
for the same substitution pattern applied to clocks and other nondeterministic
dependencies.
