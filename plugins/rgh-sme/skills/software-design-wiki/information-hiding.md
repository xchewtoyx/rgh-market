---
type: concept
title: Information Hiding
description: >
  Information hiding encapsulates a design decision inside a single module's
  implementation so nothing outside the module depends on it, which is what
  simple interfaces and deep modules actually are underneath.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
---

Attributed to David Parnas: each module should encapsulate a few pieces of
knowledge — design decisions — entirely inside its implementation, invisible
from its interface. Hideable knowledge can be low-level (a page size, a disk
block-mapping scheme) or high-level and conceptual (an assumption that most
files are small). Two benefits follow directly: a simpler interface with lower
[cognitive load](cognitive-load.md) for callers, and easier evolution — if
nothing outside the module depends on a hidden decision, changing that
decision (e.g. swapping a TCP congestion-control algorithm) stays contained to
the one module instead of rippling outward.

**Making a field or method `private` is not information hiding.** Private
state exposed through a getter/setter pair is exactly as leaked as if it were
public — the data's nature and usage escape through the accessor just the
same. Real hiding requires the *knowledge*, not just the storage keyword, to
stay inside the module; see
[accessor methods should hide representation](accessor-methods-should-hide-representation.md)
for what a non-leaking accessor looks like.

Hiding doesn't have to be all-or-nothing: if a feature is needed by only a
few callers and reached through a separate method kept out of the common-case
path, that information is "mostly hidden" and creates fewer dependencies than
something exposed to every caller — see
[interfaces should make the common case simple](interfaces-should-make-the-common-case-simple.md).
Hiding is also only appropriate when the information genuinely isn't needed
outside the module; see
[limits of information hiding](limits-of-information-hiding.md) for when it
must be exposed instead.

Information hiding and [module depth](deep-modules.md) are two views of the
same phenomenon: hiding more knowledge tends to grow a module's functionality
while shrinking its interface (making it deeper); hiding little means the
module is either thin on functionality or has a complex interface — shallow
either way. The failure mode of not hiding enough is
[information leakage](information-leakage.md).
