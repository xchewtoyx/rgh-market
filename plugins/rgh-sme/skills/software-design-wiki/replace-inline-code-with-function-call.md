---
type: concept
title: "Refactoring: Replace Inline Code with Function Call"
description: >
  Swap inline code that visibly matches an existing function's behavior for
  a call to that function, but only when the match is conceptual rather
  than coincidental — the test is whether the function's name would
  honestly describe what the inline code does.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

Functions package behavior two ways at once: a name explains *purpose*
instead of forcing the reader through mechanics, and calling one instead of
duplicating its logic means future implementation changes happen in one
place instead of requiring a hunt for every look-alike copy — checking
whether *callers* need updating along the way is comparatively rare and
easy. When inline code visibly matches what an existing function already
does, replace it with a call to that function — **unless the resemblance is
coincidental**, i.e. you would *not* want this inline code's behavior to
change if the existing function's implementation changed later.

**The practical test**: does the function's *name* make sense standing in
for this inline code? If not, either the function is badly named — fix with
[Change Function Declaration](change-function-declaration.md) — or its
purpose genuinely differs from what's needed here, in which case don't call
it; the similarity really was coincidental. Doing this against **library
functions** is particularly satisfying, since it also means not having to
write or maintain the function body at all.

**Mechanics**: replace the inline code with a call to the existing
function; test.
