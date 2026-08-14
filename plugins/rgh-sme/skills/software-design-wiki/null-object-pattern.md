---
type: concept
title: Null Object Pattern
description: >
  Return a do-nothing stand-in object instead of null or throwing, so
  callers don't need explicit null-checks — appropriate specifically when a
  caller genuinely doesn't need to know whether an operation "really"
  happened.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

See [Introduce Special Case](introduce-special-case.md) for the more
general refactoring this pattern is one instance of, and its staged
migration mechanics.

Instead of returning `null` (forcing every caller to null-check) or throwing,
return a do-nothing stand-in object — e.g. a `NullEmployee` in place of a
missing `Employee` — that implements the same interface with harmless,
no-op behavior. Callers can then invoke methods on the result unconditionally
without special-casing absence.

The pattern has a real failure mode when misused: a loop that calls
`e.pay()` on every employee and then increments a payment counter will
silently over-count if some `e` values are null objects whose `pay()` does
nothing but the counter increments regardless. Null objects are appropriate
specifically when the caller genuinely doesn't need to know whether the
operation "really" happened — as soon as a caller needs to distinguish "did
something" from "did nothing," a null object silently breaks that
distinction. This is the production-code counterpart to
[Pass Null as a test-only technique](pass-null.md) — Pass Null trades a
runtime crash for test simplicity; the null object pattern trades a silent
no-op for call-site simplicity, and each is safe only in the situation it's
meant for.
