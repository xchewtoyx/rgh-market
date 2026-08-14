---
type: concept
title: Extract Small Methods to Expose an Undetectable Side Effect
description: >
  When a method's real effects are invisible because it delegates to other
  objects' void methods, mechanically extract each side-effecting chunk
  into its own small, honestly-named method until the decision logic
  underneath can be tested with the side effects overridden away.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 10"
---

Some methods have real effects a caller can never observe because they
delegate entirely to other objects' void/no-return methods — a GUI event
handler that pops up a second window, waits, and reads a value back out of
it is the canonical case: "There is no decent place to sense what this code
does." A step-by-step sequence, each step a safe, mechanical
[Extract Method](splitting-and-joining-methods.md) (tool-assisted where
available), makes it testable without understanding or redesigning the whole
thing up front:

1. Extract the entire handler body into a plain method taking only the data
   it actually needs, decoupling it from a framework-specific event type so
   it's callable directly from a test.
2. Promote any collaborator references the extracted logic needs into
   instance fields so later extraction steps can reference them.
3. Extract each side-effecting chunk into its own small, named
   [command or query](command-query-separation.md) method, choosing names
   that describe what the method accomplishes for the class, not how it does
   it — deliberately hiding the framework plumbing behind the new names.
4. [Subclass and override](subclass-and-override-method.md) just those small
   methods in a test-only subclass, leaving the actual decision logic
   exercisable and assertable in a plain unit test.

An honest self-critique matters here: some of the extracted methods may
still be individually awkward on their own (a "setter" that both constructs
and displays something, unsafe to call twice) — this is an acceptable coarse
**first step**, not a finished design. The real payoff surfaces once the
extraction is done: seeing that some extracted methods only touch one
collaborator and others only touch a different one is the signal for a
further split into separate responsibility-holding classes, with the
original class free to stay tied to its framework for now, business logic
finally isolated underneath.

Reiterated permission for the whole sequence: **"it is okay to extract
methods with poor names or poor structure to get tests in place. Safety
first"** — cleanup can follow once tests exist. A reliable refactoring tool
only guarantees the *automated* extraction step is behavior-preserving,
which shifts remaining risk onto whatever you edit by hand between tool
operations — see
[automated refactoring tools don't guarantee behavior preservation](automated-refactoring-tool-caution.md).
