---
type: concept
title: "Refactoring: Replace Function with Command"
description: >
  Wrap a complex function's parameters and local state as fields on a
  dedicated command object, so its body can be decomposed with Extract
  Function without variable-scoping headaches — reached for only when a
  plain function's flexibility genuinely isn't enough.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11 (formerly Replace Method with Method Object)"
---

Sometimes a plain function isn't flexible enough and it's worth wrapping it
in its own object — a **command object**, built around a single primary
method whose invocation is the object's whole purpose (the Gang-of-Four
Command pattern). A command's added flexibility over a bare function:
complementary operations like undo; methods to build up parameters
incrementally across a richer lifecycle; customization via inheritance and
override hooks; substituting for missing first-class-function support in a
language that lacks it; and — the use case emphasized most here — in *any*
language, wrapping a complex function's state as fields on a command object
makes it much easier to decompose that function's body with
[Extract Function](extract-function.md) without getting tangled in
variable scoping, and the resulting sub-methods can be called and tested
directly. Explicit cost/benefit stance: given the choice between a
first-class function and a command, the function wins the vast majority of
the time — reach for a command only when a specific facility a simpler
approach can't provide is actually needed.

Compare [Expose Static Method and Break Out Method
Object](expose-static-method-and-break-out-method-object.md), a similarly-
shaped legacy-code technique aimed specifically at making an unwieldy
method testable by relocating it into its own small class — the same
underlying move (parameters and locals become fields on a purpose-built
object), applied for a different primary reason.

**Mechanics**: create an empty class named after the function. Use
[Move Function](move-function.md) to relocate the function's body into the
new class, keeping the original function around as a forwarding stub at
least until the refactoring is done. Follow the host language's naming
convention for the command's main method, or default to something generic
like `execute`/`call` if there's no convention. Consider giving each of the
function's original arguments its own field, moved into the constructor
one at a time (rather than staying as parameters on the execute method) —
this matters less for a simple decomposition case but is very handy when a
command needs a richer parameter-setting lifecycle or customization.
Converting each remaining local variable in the body into a field follows
the same pattern.

Once every input and intermediate value is a field rather than a parameter
or local, [Extract Function](extract-function.md) can be applied freely
inside the execute method without any of the scoping headaches that would
otherwise come from threading local variables into and out of extracted
sub-methods — the command starts to behave much like a nested function
would, with the added benefit that its sub-methods can be called and tested
directly in isolation, something a nested function typically can't offer.
