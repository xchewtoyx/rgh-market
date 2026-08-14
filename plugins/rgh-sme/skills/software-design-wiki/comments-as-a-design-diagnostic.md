---
type: concept
title: Comments as a Design Diagnostic
description: >
  A method or variable that needs a long comment to explain is a red flag
  that the underlying abstraction isn't good — writing comments early turns
  documentation into a tool for finding design problems, not just recording
  them.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 15"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3, Comments"
---

Comments are the only mechanism that can fully capture an
[abstraction](abstraction.md), so writing them early — as part of
[writing the comments first](write-the-comments-first.md) — lets you review
and refine the abstraction before committing to implementation code that
embodies it. To write a good comment you must identify the true essence of a
variable or piece of code; doing that early keeps you designing rather than
just assembling code.

**Red flag: hard to describe** — "The comment that describes a method or
variable should be simple and yet complete. If you find it difficult to
write such a comment, that's an indicator that there may be a problem with
the design of the thing you are describing." This connects directly to
[module depth](deep-modules.md): a genuinely deep, simple-interfaced method
should be describable in a short, complete interface comment; if no such
short comment is possible without also describing major implementation
details, the method is [shallow](shallow-modules.md). The same logic applies
to variables — one that needs a long comment to fully explain likely signals
a poor decomposition, where the variable is trying to represent too much, or
the wrong thing.

The important caveat: this diagnostic is only valid when the comment itself
is honestly written — complete and clear. A comment that's short merely
because it's incomplete, or cryptic rather than genuinely simple, doesn't
actually demonstrate a good abstraction; it just hides the problem instead of
revealing it.

Fowler and Beck put the same diagnostic to work in the opposite direction,
as a smell to act on rather than a habit to adopt: comments themselves
aren't a bad smell — "a sweet smell" — but they flag a common deodorant
masking bad code underneath, since heavily commented code is often heavily
commented *because* the code beneath it is bad. Their prescribed order of
operations: refactor away the underlying smell first; the comment frequently
becomes superfluous once that's done. Stated rule: **"When you feel the need
to write a comment, first try to refactor the code so that any comment
becomes superfluous."** Concretely — a comment explaining a block becomes
[Extract Function](extract-function.md) named for what the comment said; a
function that's already extracted but still needs an explanatory comment
gets a better name via
[Change Function Declaration](change-function-declaration.md) instead; a
comment stating a required invariant becomes an assertion in the code
rather than prose beside it. Legitimate
comments that survive this treatment: ones flagging genuine uncertainty ("I
don't know what to do here"), and ones explaining *why* a decision was made
— which helps future modifiers, "especially forgetful ones."
