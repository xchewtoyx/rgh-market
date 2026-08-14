---
type: concept
title: Virtualize External Resources to Make Them Testable
description: >
  Route access to a resource outside the system's own control — wall-clock
  time, a data source, memory or battery limits — through an abstraction a
  test can substitute, so behavior that depends on that resource becomes
  reachable and repeatable in a test.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 12"
---

Some behavior is naturally gated by a resource the system doesn't control
— wall-clock time, an external data source, available memory or battery.
Testing that behavior directly means waiting for the real resource to
reach the triggering condition, which is often impractical (waiting for an
actual Daylight Saving transition or midnight rollover to test a
time-boundary bug) or outright impossible to induce reliably (a low-battery
condition, a full disk). The fix is the same shape as [dependency
injection](dependency-injection-pattern.md) and [fake
objects](fake-objects.md) applied specifically to a resource rather than a
collaborator object: put an abstraction between the code and the resource
— a clock interface instead of a direct system-time call, a data-source
interface instead of a direct database or file read — so a test can
substitute a **virtualized** version that reports whatever value the test
needs, on demand, instead of waiting for or faking the real resource's
actual state.

This buys two things at once: the specific edge condition becomes
directly reachable (set the virtual clock to one second before midnight
and observe the rollover, rather than waiting for real midnight), and the
system under test can be isolated from the real resource's consequences
entirely — an isolated, **sandboxed** instance can run experiments (fault
injection, scenario exploration, training simulations) without any risk to
real data or real infrastructure, which matters most exactly where a real
failure would be costly. [Stubs, mocks, and dependency injection are the
simplest, most effective way to build this virtualization](fake-objects.md);
reaching for a full simulator or environment emulator is only worth its
much higher cost when the resource's behavior itself is complex enough
that a simple substitute wouldn't exercise the interesting cases.
