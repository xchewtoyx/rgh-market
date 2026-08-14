---
type: concept
title: Automated Refactoring Tools Don't Guarantee Behavior Preservation
description: >
  Not every "refactoring" a tool offers actually verifies that behavior is
  preserved — a structurally reasonable automated transformation can still
  change behavior if it interacts with a side effect the tool doesn't
  account for.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 5"
---

[Refactoring](refactoring-preserves-behavior.md), by Fowler's canonical
definition, is "a change made to the internal structure of software to make
it easier to understand and cheaper to modify without changing its existing
behavior" — a change is only a refactoring if behavior doesn't change. Not
all refactoring tools actually verify this; some don't really check, risking
subtle bugs. Vet a tool yourself with sanity checks — does it flag an error
if an extracted method's name collides with an existing method on the class
or a base class? If not, an automated "refactoring" could silently introduce
an override and change behavior.

Even a trustworthy tool can produce a behavior change if a refactoring
interacts with a side effect it doesn't model. Worked example: a method with
the side effect of incrementing a field every time it's called. An
"extract/remove local variable" refactoring that inlines the method call
directly into a loop body, removing a local variable that had cached its
single result, looks structurally reasonable — but it changes the code from
calling the method once (incrementing the field once) to calling it on every
loop iteration (incrementing the field many times). The tool did something
locally sound while breaking behavior it had no way to see.

The practical policy: put tests around code before leaning on automated
refactoring, and personally stress-test what a given tool's operations do and
don't check before trusting it. If a tool proves trustworthy enough to use
*without* tests already in place, it becomes a way to get code into a more
testable state in the first place — but that trust has to be earned per
tool, not assumed.
