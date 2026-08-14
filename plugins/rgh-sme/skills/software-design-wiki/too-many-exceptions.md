---
type: concept
title: Too Many Exceptions
description: >
  Over-defensive programming produces unnecessary exceptions, and throwing
  one is often just punting a hard problem to the caller — the actionable
  lever is reducing the count of places exceptions must be handled, not how
  many are detected.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

Developers taught "detect and report errors" often over-interpret this as
"the more errors detected, the better," producing
[exceptions](exception-handling-complexity.md) that didn't need to exist. A
self-critique example: Tcl's `unset` command originally threw an error if the
named variable didn't exist, on the reasoning that deleting a nonexistent
variable "must be a bug." In practice, `unset` is heavily used for cleanup of
temporary state whose exact prior existence is hard to predict, especially
after a partial or aborted operation — so the natural usage pattern is
"delete this if it exists," which the original design made awkward, forcing
callers to wrap every `unset` in a `catch`. See
[define errors out of existence](define-errors-out-of-existence.md) for how
this was actually fixed.

Throwing an exception is often really just punting a hard problem to the
caller under the guise of flexibility ("callers can each handle it their own
way") — but if the implementer couldn't figure out the right behavior, the
caller usually can't either, so this just relocates and multiplies the
complexity rather than resolving it.

A class's exceptions are part of its interface — in languages like Java,
declared right alongside method signatures — so more exceptions mean a more
complex, [shallower](shallow-modules.md) interface. Exceptions are unusually
complex interface elements because they can propagate through multiple stack
frames, potentially affecting many callers' interfaces, not just the
immediate one.

The key strategic insight: throwing exceptions is easy; *handling* them is
hard. The complexity cost lives in the handling code, so the actionable lever
is reducing the count of places where exceptions must be handled — not the
count of conditions checked. Four techniques do this:
[defining errors out of existence](define-errors-out-of-existence.md),
[masking exceptions](exception-masking.md),
[exception aggregation](exception-aggregation.md), and, for genuinely
unhandleable errors, [just crashing](crash-on-unrecoverable-errors.md). For
the errors that remain after applying these, see [error-reporting
mechanism is part of an interface's
contract](error-reporting-mechanisms-in-interfaces.md) for choosing and
documenting *how* they get reported.
