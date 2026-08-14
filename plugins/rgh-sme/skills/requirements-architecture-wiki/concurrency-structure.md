---
type: concept
title: Concurrency Structure
description: >
  A concurrency structure documents parallelism opportunities and resource
  contention by grouping runtime work into logical threads, independent of
  which physical threads or processes it is later assigned to.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 1"
---

A concurrency structure is a [component-and-connector](component-and-connector-view.md)
style whose elements are **logical threads** — sequences of computation
that could potentially run in parallel — rather than components named for
their business responsibility. It exists to answer a different question
from a typical C&C view: not "how do components interact to do the work"
but "where can this system actually run things at the same time, and
where do those things contend for the same resource."

Documenting it early, before a physical threading or deployment model is
fixed, is the point: a logical thread records an opportunity for
parallelism that a later design or deployment decision can choose to
realize as a physical thread, a process, or a separate node — or choose
not to. Without this structure recorded separately, concurrency
opportunities and contention points are implicit in the code and only
discoverable by tracing execution, which is exactly the kind of structural
question architecture documentation exists to make explicit instead — see
[architecture as structures for reasoning](architecture-as-structures-for-reasoning.md).
