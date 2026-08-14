---
type: concept
title: Test Code Location Trade-offs
description: >
  Keeping tests physically alongside production code is the default for
  navigation ergonomics; forcing developers to traverse directory trees to
  reach a test acts as a tax that makes people stop writing them.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 18"
---

Default recommendation: keep test code physically alongside production code
(same directories) — simplest to navigate, at the cost of roughly doubling
deployed binary size if tests ship inside production artifacts. When
deployment size genuinely matters (commercial software running on customers'
machines), it's possible to separate test source into a physically distinct
tree while keeping it logically part of the same package or module — some
IDEs even present both directories as one unified view, softening the
navigation cost of the physical split.

The strong general caution, for languages or environments where physical
location *does* affect navigation ergonomics: forcing developers to
traverse directory trees to get between code and its tests "is like paying a
tax as you work. People will just stop writing tests, and the work will go
slower." A workable compromise is to colocate tests with production code for
developer convenience, then use build scripts to strip test code out of the
actual deployment artifact — practical once
[naming conventions](test-naming-conventions.md) make the split mechanically
easy to automate.

Closing caution against separating tests purely on aesthetic grounds
("can't stand the idea of putting production code and tests together")
without weighing the resulting navigation cost: "you can get used to having
tests right next to your production source. After a period of time working
that way, it just feels normal."
