---
type: concept
title: Information Leakage
description: >
  Information leakage is when a single design decision is reflected in
  multiple modules, creating a dependency between them wherever that
  decision changes — one of the most important design red flags to develop
  sensitivity to.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
---

**Red flag: information leakage.** If information appears in a module's
interface, it's leaked by definition, so simpler interfaces correlate with
better [information hiding](information-hiding.md). But leakage can also
happen through a "back door" with no interface exposure at all — for example,
two classes, one that reads a file format and one that writes it, both
independently encoding knowledge of that format without either exposing it
publicly. Back-door leakage is more pernicious than interface leakage
precisely because it isn't obvious from either class's interface.

The remediation heuristic: ask "how can I reorganize these classes so this
knowledge only affects a single class?" Either merge small, tightly-coupled
classes that share the knowledge, or extract the shared knowledge into a new
class with a genuinely abstracting interface. A new class that just
re-exposes the same details through its own interface doesn't fix anything —
it only converts interface-leakage into a different flavor of the same
problem.

[Temporal decomposition](temporal-decomposition.md) is the most common way
leakage gets introduced by accident.
