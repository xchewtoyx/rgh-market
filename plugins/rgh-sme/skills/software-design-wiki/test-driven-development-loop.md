---
type: concept
title: The Test-Driven Development Loop
description: >
  TDD's basic cycle — write a failing test, get it to compile, make it pass,
  remove duplication, repeat — and the discipline of stubbing new code to
  fail loudly rather than plausibly until it's genuinely implemented.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 8"
---

The core loop: (1) write a failing test case, (2) get it to compile, (3) make
it pass, (4) remove duplication, (5) repeat. Two disciplines make the loop
trustworthy rather than a false sense of safety:

**Stub to fail loudly, not plausibly.** When step (2) requires stubbing a
not-yet-implemented method, return a value guaranteed to fail (e.g. `NaN`)
rather than a plausible-looking placeholder. This makes sure the test is
actually exercising real logic once implemented, not silently passing on a
coincidence — a stub that happens to return the right-looking value defeats
the point of writing the test first.

**Duplicate before generalizing.** When a second case is structurally
similar to a first (e.g. a second statistical method whose body differs from
the first by one line), the disciplined move is to copy-paste the passing
body and tweak the one differing line, deliberately deferring generalization:
"our only job right now is to make it compile. We can generalize later."
Only once both cases pass does step (4) extract the shared logic and rewrite
both call sites as thin callers. This copy/rename/modify move lets new logic
sit side by side with old logic for direct comparison, and gives a safety
net (the old code is still there to fall back to or learn from) while
working out the right generalization — but it's only safe to do "quickly and
brutally" *because* tests exist to let you remove the resulting duplication
afterward without fear.

TDD's core value here is letting you concentrate on exactly one of two modes
at a time — writing new code, or refactoring — never both simultaneously.
This is a legacy-code-specific application distinct from
[general skepticism of TDD as a whole-system design methodology](skepticism-of-test-driven-development.md):
that skepticism is about TDD substituting for up-front design of a new
abstraction; here the loop is scoped narrowly to adding one already-
understood piece of behavior, once [the change point is already under test](tdd-for-legacy-code.md).
