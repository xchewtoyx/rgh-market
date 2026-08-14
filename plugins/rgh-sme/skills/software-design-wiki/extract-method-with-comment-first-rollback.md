---
type: concept
title: Extract Method With a Comment-First Rollback
description: >
  When tests already thoroughly exercise a method, comment out the code
  being extracted rather than deleting it, so a failed extraction attempt
  has an immediate, zero-effort path back to a passing state.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), Appendix"
---

This is the tests-*present* counterpart to the tests-*absent* extraction
techniques detailed in
[monster methods](monster-methods.md) and the dependency-breaking
catalog — this version assumes tests already thoroughly exercise the method
being split. Extract Method is called "perhaps the most useful" of all
refactorings: systematically breaking large methods into smaller ones both
improves readability and enables reuse of the extracted pieces elsewhere.
"In poorly maintained code bases, methods tend to grow larger... methods can
end up doing two or three different distinct things for their callers. In
pathological cases, they can end up doing tens or hundreds. Extract Method
is the remedy in these cases."

Steps: identify the code to extract and **comment it out** rather than
deleting it outright; invent a name for the new method and create it as an
empty stub; place a call to the new (still-empty) method where the
commented-out code used to be; copy the commented-out code into the new
method's body; [lean on the compiler](lean-on-the-compiler.md) to discover
exactly which parameters must be passed in and what value must be returned;
adjust the new method's signature accordingly; run the tests; once passing,
delete the commented-out original code.

**Rationale for the comment-first discipline**: "if I make a mistake and a
test fails, I can easily go back to what I had, get the test to pass, and
then try again." The commented-out original acts as an immediate,
zero-effort rollback point during the extraction itself — distinct from,
and complementary to, version control, which would require a much coarser
context-switch to recover the same state mid-refactoring. With a capable
automated refactoring tool, this entire manual dance collapses to selecting
a code region and invoking Extract Method directly, with the tool both
verifying extractability and prompting for the new method's name — see
[automated refactoring tools don't guarantee behavior preservation](automated-refactoring-tool-caution.md)
for why that trust still has to be earned per tool.

Extract Method is "a core technique for working with legacy code" precisely
because it does triple duty: extracting duplication (see
[designs emerge from zealous duplication removal](duplication-removal-as-emergent-design.md)),
separating responsibilities (see
[grouping methods to find hidden responsibilities](group-methods-heuristic.md)),
and breaking down long methods (see [monster methods](monster-methods.md)).
