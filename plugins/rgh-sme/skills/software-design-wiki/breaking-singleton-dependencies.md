---
type: concept
title: Breaking Singleton Dependencies for Testing
description: >
  Introduce Static Setter or a resettable static field let a singleton be
  swapped for a fake in tests; relaxing the constructor's visibility often
  removes the need for a true singleton at all, since most singleton usage
  is really just a convenient global variable.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

Two mechanical fixes make an existing Singleton fake-able without giving up
the pattern: **Introduce Static Setter** — add a static
`setTestingInstance(...)` so each test's setup can install a fresh,
test-configured instance — preferred when the singleton depends on external
resources that tests can't safely touch (also useful together with
subclassing the singleton to override just the problem methods, exposing
test-setup methods on the subclass). Its sibling, **`resetForTesting()`**,
nulls the singleton's static instance field so it lazily rebuilds fresh each
test — preferred when the singleton's existing public API is already
sufficient to configure it for every test scenario.

Where the singleton's dependencies are scattered across many methods rather
than isolated in one, escalate to full [Extract Interface](extract-interface.md) on the singleton
and repoint all usages at the interface type — heavier, but mechanically
findable by [leaning on the compiler](lean-on-the-compiler.md): change the type, let every
resulting compile error point at a call site that needs updating, and work
through them one by one rather than trying to enumerate call sites by
reading.

None of this removes the underlying [global dependency](global-state-opacity.md)
itself — it only makes it fake-able for tests.
[Parameterize Method](parameterize-method.md)/[Constructor](parameterize-constructor.md) are the actual
dependency-removal tools, each with its own cost (Parameterize Method risks
method-signature bloat that obscures a class's real interface; Parameterize
Constructor risks per-object field bloat if too many objects end up needing
the same field just to thread it through).

**Why teams reach for a single instance in the first place** — three
legitimate reasons: (1) modeling something genuinely singular in the real
world (one circuit board, one permit database); (2) avoiding correctness
risk from two instances independently operating on the same real resource
without awareness of each other; (3) avoiding the resource cost of
duplicate instances (memory, disk, license seats). The claim worth
internalizing: most real-world singleton usage is actually none of these —
it's really just wanting a convenient global variable without the burden of
passing it around. When *that's* the real motive, there's no reason to keep
true singleton enforcement (a private constructor blocking all external
instantiation) at all — just relax the constructor's visibility.

**Practical relaxation** when instance-uniqueness genuinely does matter for
one of the three legitimate reasons: keep the constructor `protected`
(blocks external `new`, but still allows subclassing), and subclass for
tests (e.g. a version backed by an in-memory collection instead of a real
database) rather than fighting the singleton's enforcement mechanism head-on.

**Why globals are worth this trouble in the first place**: "I don't like
global mutable data" — it's the most common obstacle teams hit when trying
to isolate classes into a test harness, since every global has to be
tracked down and driven into the right state for each test scenario.
"Quantum physicists didn't discover 'spooky action at a distance'; in
software, we've had it for years." The ethical framing for deliberately
weakening access protection to fix this: "the purpose of access protection
is to prevent errors. We are putting in tests to prevent errors also. It
just turns out that, in this case, we need the stronger tool." The residual
risk that a loosened constructor could be misused to create a second real
instance in production is mitigated socially, not mechanically: "if it is
important to have only one instance of an object in a system, the best way
to handle it is to make sure everyone on the team understands that
constraint."

**Global factories** (objects handing out a *fresh* instance on every call,
rather than serving one shared instance) get the same fix in a different
shape: make the factory delegate to a swappable strategy object, itself
defaulting to real production behavior, with a static setter tests can use
to install a fake producing strategy instead.

**Shared-state test hygiene**: any static-setter-based substitution mutates
state visible to *every* test, so use a test framework's teardown hook to
restore known-good state wherever a leftover value could mislead a later
test — but not as a blanket rule. If a substituted fake genuinely doesn't
matter across tests (a fake mail sender, say), resetting it is pointless
busywork; reset only state whose staleness could actually cause a
misleading result (a shared counter, for instance).

**The longer-term remedy** beyond making a global fake-able: look for a
common superclass shared by classes that need the same global service, and
pass that service in at construction time instead, incrementally weaning
the system off the global entirely. This mirrors
[localizing rather than eliminating global dependencies](localize-global-dependencies.md)
— an embedded system that encapsulated memory management and error
reporting as passed-in objects, rather than globals, via a shared
superclass reported the change as barely noticeable in practice once done,
contrary to the common fear that "every class in the system will require
some global."
