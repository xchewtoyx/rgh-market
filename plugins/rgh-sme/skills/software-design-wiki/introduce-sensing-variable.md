---
type: concept
title: Introduce Sensing Variable
description: >
  Add a temporary instance variable purely to observe whether a specific
  branch executed, write a couple of quick tests against it, then use those
  tests as a safety net for an extraction — deleting the variable once done.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

You shouldn't add production *features* while refactoring, but you can add
harmless instrumentation: a temporary boolean or tracking instance variable
purely to observe whether a specific internal branch actually executed.
Write a couple of quick tests asserting on that variable to confirm the
branch's behavior around the boundary you intend to extract, perform the
extraction with those tests as a safety net, then delete the sensing
variable (and update or remove its tests) once done.

The scope is deliberately narrow: the goal isn't to fully verify the
condition's logic, just to confirm **the same code path still executes
post-extraction** — the same calibration question as
[targeted testing](targeted-testing.md), applied specifically to unblocking
one extraction rather than to a whole planned change.

Workflow guidance: keep sensing variables in place across a whole
multi-step refactoring session, not deleted after each single step, so you
can freely reconsider or undo earlier extraction choices; delete or convert
them to permanent tests only once the session concludes. Sensing variables
let you refactor *inside* deeply nested [snarled methods](monster-methods.md)
incrementally, extracting conditions or condition-bodies piece by piece, and
the same technique can be reused repeatedly on newly extracted methods to
progressively "de-snarl" a method layer by layer.
