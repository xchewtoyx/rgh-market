---
type: concept
title: Temporal Decomposition
description: >
  Temporal decomposition is a design smell where code structure mirrors the
  runtime order of operations rather than the knowledge each piece needs,
  which reliably produces information leakage.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
---

**Red flag: temporal decomposition** — "execution order is reflected in the
code structure: operations that happen at different times are in different
methods or classes. If the same knowledge is used at different points in
execution, it gets encoded in multiple places, resulting in
[information leakage](information-leakage.md)."

Canonical example: an app that reads a file, modifies it, and writes it back,
split naively into a Reader class, a Modifier class, and a Writer class. Both
Reader and Writer independently need to understand the file format, so the
format knowledge — and its parsing logic — ends up duplicated between them.
The fix is to merge the format-understanding pieces (reading and writing) into
one class used at both points in the timeline.

This is an easy trap because execution order is naturally on your mind while
coding a feature. But order should show up in the *flow of control* — which
methods call which, in what sequence — not in *which module owns which
knowledge*, unless the different temporal stages genuinely operate on disjoint
information. A recurring instance of this trap: splitting "read raw bytes off
a socket" from "parse the request" when the amount to read depends on parsing
a length header first — both ends up needing to understand the wire format.
The fix, as in the general case, is to merge them: one class handling both
reading and parsing keeps all format knowledge in one place and gives callers
a single method instead of an order-dependent pair. The broader lesson is that
[information hiding](information-hiding.md) can often be improved by making a
class *larger* — to gather all the code related to one piece of knowledge, or
to raise a interface's level of abstraction — not just by splitting classes
apart; see [class size as a hiding decision](class-size-as-a-hiding-decision.md).
