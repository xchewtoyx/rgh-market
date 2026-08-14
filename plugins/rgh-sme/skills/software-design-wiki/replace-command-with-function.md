---
type: concept
title: "Refactoring: Replace Command with Function"
description: >
  Collapse a command object back down to a plain function once its
  decomposability, multi-method invocation, or staged construction isn't
  actually being used — the command pattern's power comes at a real
  structural cost that isn't always worth paying.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11"
---

The inverse of [Replace Function with Command](replace-function-with-command.md).
The command pattern's power — decomposable via shared fields, invokable
through multiple methods, buildable in stages — comes at a real structural
cost. Most of the time, all that's actually wanted is to call a function
and have it do its thing; if the function isn't especially complex, a
command object is overkill and should be collapsed back down to a plain
function.

**Mechanics**: apply [Extract Function](extract-function.md) around both
the command's construction and its execution-method call together — this
produces the eventual replacement function. For each supporting method the
execution method calls, apply [Inline Function](inline-function.md) to
fold it back in (if a supporting method returns a value, first
[Extract Variable](extract-variable.md) on the call site, then Inline
Function). Use [Change Function Declaration](change-function-declaration.md)
to move all of the constructor's parameters onto the execution method
itself instead. For each field, redirect its references inside the
execution method to use the corresponding parameter directly, testing after
each change. Inline both the constructor call and the execution-method call
together into the wrapping caller function created in the first step. Test.
Finally, apply [Remove Dead Code](delete-unused-code.md) to clear away the
now-unused command class.

A useful verification technique while redirecting field references to
parameters: deliberately leave the now-redundant constructor field
assignments in place rather than deleting them immediately, so that a
missed field-to-parameter conversion causes a test to fail — rather than
silently continuing to work off stale field state — instead of quietly
succeeding for the wrong reason.
