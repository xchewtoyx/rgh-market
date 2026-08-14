---
type: concept
title: Extract Variable
description: >
  Extracting part of a complex expression into a named local variable is a
  decision about naming a piece of logic, which raises a scope question —
  if the name would matter beyond this function, extract a function instead.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6 (formerly Introduce Explaining Variable; inverse of Inline Variable)"
---

Complex expressions are hard to read; a local variable lets you name a
sub-part of the logic, aiding both comprehension and debugging — a named
variable is an easy hook for a breakpoint or a print statement. Deciding to
extract a variable is really deciding to *name* a piece of logic, which
raises a scope question: if the name is only meaningful within the current
function, a plain local variable is right. If it would be meaningful more
broadly, prefer promoting it to a method instead (usually via [Extract
Function](extract-function.md)), so other call sites can reuse the
expression by name rather than repeating it. The tradeoff is effort:
promoting to a wider-context function costs more up front, so if it's not
cheap, it's fine to defer that promotion (via [Replace Temp with
Query](replace-temp-with-query.md)) — but if it's cheap, such as when you're already inside a class where Extract
Function is trivial, do it immediately.

**Mechanics**: confirm the expression is side-effect-free; declare an
immutable variable set to a copy of the expression; replace the original
expression with the variable and test; if the same expression recurs,
replace each occurrence with the variable, testing after each.

Inside a class specifically, names that are meaningful for the object as a
whole — not just one calculation — are worth extracting as accessor methods
on the class rather than local variables, since **objects provide a natural
shared context that makes it cheap and worthwhile to name common hunks of
logic as first-class, reusable abstractions** available to any method on the
object. The payoff of this scales with the class's size and complexity.
