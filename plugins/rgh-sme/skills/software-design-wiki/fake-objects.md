---
type: concept
title: Fake Objects
description: >
  A fake object impersonates a real collaborator during a test, exposing a
  narrow interface to the production code and a separate test-only
  inspection side used only by the test itself.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 3"
---

Worked example, a point-of-sale `Sale` class whose `scan(barcode)` method
must show an item's name and price on a cash register display: extract all
display-talking code out of `Sale` into its own class (a behavior-preserving
move — the system does exactly what it did before), introduce a `Display`
interface (`void showLine(String line)`) implemented both by the real display
class and by a new `FakeDisplay`, and have `Sale` take a `Display` via
constructor injection, calling `display.showLine(...)` internally rather than
talking to hardware directly. In tests, `Sale` is constructed with a
`FakeDisplay` whose `showLine()` just records the last line into a field,
exposed via `getLastLine()` for assertions:
`sale.scan("1"); assertEquals("Milk $3.99", display.getLastLine());`

**"Fake objects support real tests"** anticipates the objection "that's not
really testing" — a fake-based test won't catch a broken real display
driver. The rebuttal: no single test, not even one inspecting literal pixels
on real hardware, can validate software against every possible hardware
combination, so that objection proves too much. The fake-based test has a
narrower, still-valuable purpose: it isolates and confirms exactly how
`Sale` affects the display abstraction, aiding error localization — a bug
found elsewhere is now known *not* to be in `Sale`'s interaction logic.
"When we write tests, we have to divide and conquer."

**The two sides of a fake object**: the interface side it presents to
production code (`showLine`, the only method the `Display` interface
declares and the only one `Sale` ever sees), and a test-only inspection side
(`getLastLine`) used only by the test. This is why the test variable is
declared as the concrete `FakeDisplay` type rather than the `Display`
interface type — otherwise the inspection-only methods wouldn't be visible.

The technique generalizes beyond object orientation: in procedural
languages, a "fake" can be an alternate function implementation that records
values into an accessible global data structure for the test to inspect.

See [mock objects](mock-objects.md) for a heavier-weight escalation of the
same idea, [dependency injection](dependency-injection-pattern.md) for the
named roles in how a fake gets supplied to the code under test,
[virtualizing external resources](virtualize-external-resources-for-testing.md)
for applying the same substitution idea to a resource like time or a data
source rather than a collaborator object, [contract tests for fakes](contract-tests-for-fakes.md)
for keeping fakes aligned with real APIs, and [prefer real implementations in
tests](prefer-real-implementations-in-tests.md) when fidelity and speed allow.
