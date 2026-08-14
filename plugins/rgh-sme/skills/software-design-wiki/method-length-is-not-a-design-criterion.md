---
type: concept
title: Method Length Is Not a Design Criterion
description: >
  Rigid rules like "split any method over N lines" are wrong — length alone
  is rarely a good reason to split a method, and developers who follow such
  rules tend to over-split.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3, Long Function"
---

Splitting a method introduces a new interface — its own
[complexity cost](design-cost-benefit-of-infrastructure.md) — and can
separate code that's genuinely related, making the whole harder to read. Long
methods are fine when they remain simple and readable: five independent
20-line blocks executed in sequence gain little from being pulled into five
separate methods, and if the blocks have complex interactions with each
other, keeping them together is actually *more* important, since separate
methods would force constant flipping back and forth to see how they
interact (see [conjoined methods](conjoined-methods.md)).

The design goal for any method is the same as for any other module: one job,
done completely, with a clean, simple interface (little information needed to
use it correctly) and [depth](deep-modules.md) (an interface much simpler
than the implementation behind it). A method with hundreds of lines but a
simple signature is a deep method — high functionality behind a simple
interface, exactly what's wanted. If a method has these properties, its line
count is essentially irrelevant. See
[splitting and joining methods](splitting-and-joining-methods.md) for when a
split (or a join) actually is warranted.

**A real tension with Fowler and Beck's "Long Function" smell is worth
naming rather than smoothing over.** They both reject raw line count as the
criterion — "the deciding factor is the semantic distance between what a
piece of code does and how it does it, not raw line count" — but land on a
much more aggressive extraction heuristic in practice: **"whenever we feel
the need to comment something, we write a function instead,"** named after
intent rather than mechanism, even for a single line, even when the
resulting call is textually longer than the code it replaces — "any function
with more than half-a-dozen lines of code starts to smell." That heuristic
would routinely split methods Ousterhout would call properly deep and leave
alone. The two views agree on the underlying test (does the split clarify
intent, or just add an interface for its own sake) but disagree sharply on
where that test tends to land in practice — Fowler's heuristic assumes
extraction is nearly free once [Extract Function](extract-function.md)
is a fast, safe, well-practiced move (part of the [refactoring
rhythm](rhythm-of-refactoring.md)), while Ousterhout weighs the new
interface's own [complexity cost](design-cost-benefit-of-infrastructure.md)
more heavily. Mechanically, Fowler's cure for an overlong function is
[Extract Function](extract-function.md) for ~99% of cases; when many parameters or temps block
extraction, first strip temps with [Replace Temp with
Query](replace-temp-with-query.md) and slim
[long parameter lists](long-parameter-list-smell.md) with [Introduce
Parameter Object](introduce-parameter-object.md) or [Preserve Whole
Object](preserve-whole-object.md); conditionals get [Decompose
Conditional](decompose-conditional.md), and a switch's branches each become
their own function; a loop body that resists a good name is probably doing
two things and should be split via [Split Loop](split-loop.md) before
extracting.
