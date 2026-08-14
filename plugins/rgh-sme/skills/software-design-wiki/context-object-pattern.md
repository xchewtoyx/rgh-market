---
type: concept
title: Context Object Pattern
description: >
  A context object holds all the state that would otherwise become
  pass-through parameters or global variables for one instance of a running
  system — an imperfect but generally preferred fix for that problem.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
---

One object per system instance holds all would-be
[pass-through](pass-through-variables.md) or global state: configuration
options, shared subsystems, performance counters, and the like. To avoid the
context itself becoming a giant pass-through parameter, a reference to it is
cached as an instance variable inside the system's major objects: when a new
object is created, its constructor grabs the context reference from whatever
object created it, so only that constructor's signature needs to mention the
context explicitly — nothing downstream has to.

Benefits: adding a new piece of global-feeling state only touches the
context's own constructor/destructor, not every call path; multiple system
instances can coexist in one process, each with its own context (unlike a
true global variable); tests can override configuration by mutating context
fields directly instead of threading test-specific parameters everywhere.

Contexts are explicitly "far from an ideal solution." They inherit most of
the disadvantages of global variables — it's not obvious from a piece of code
which context fields it actually reads or writes — and can devolve into an
undisciplined grab-bag that creates hidden dependencies, or introduce
thread-safety issues if fields are mutated carelessly. Keeping context fields
immutable where possible mitigates this. No general solution better than
contexts is claimed to exist for this problem.
