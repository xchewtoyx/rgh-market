---
type: concept
title: Sensing and Separation
description: >
  There are exactly two reasons to break a dependency in order to test code
  — sensing, when you can't observe a value or effect the code produces, and
  separation, when you can't even get the code running in a test harness at
  all.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 3"
---

In an ideal world, any class could be instantiated directly in a test
harness, but real dependency chains mean instantiating one object can drag in
most of the system — in some languages, link time alone can make this
impractical without breaking dependencies first.

**Sensing**: breaking a dependency because there's no other way to observe a
value the code computes or an effect it has. **Separation**: breaking a
dependency because the code can't even be gotten running in a test harness
at all. A class managing real hardware — opening real network sockets, say —
illustrates both at once: from a testing standpoint it's a closed box, since
you can't easily tell what it's doing to the hardware (sensing) and you may
not even be able to construct or run it without live hardware (separation).
Technically possible workarounds (packet-sniffing, wiring up test hardware)
are often disproportionately expensive compared to the software techniques
below.

There's no general answer to which is tougher — both come up constantly, and
often together. Separation has an entire catalog of techniques (see
[dependency-breaking for testability](dependency-breaking-for-testability.md));
sensing has one dominant technique: [fake objects](fake-objects.md).
