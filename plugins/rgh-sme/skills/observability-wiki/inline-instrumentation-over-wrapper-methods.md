---
type: concept
title: Write Instrumentation Inline, Not Behind a Single-Call-Site Wrapper
description: Pulling a log or metric emission out into its own dedicated method (e.g. a `logRpcOpenError` helper called from exactly one place) usually adds indirection without adding value — the call site and the wrapper end up needing to be read together anyway, so the telemetry statement is often clearer written directly at the point where the event is detected.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 9"
---

A common instinct is to extract instrumentation calls into their own methods — a `logRpcOpenError(req, dest, exception)` helper invoked from the one `catch` block that detects that error — on the theory that this keeps call sites tidy. In practice this usually backfires: the wrapper method is typically shallow (often a single line, needing more documentation than code) and used from exactly one place, so a reader has to jump between the call site and the wrapper to understand either one. That back-and-forth is a general code smell that shows up whenever a piece of code can't be understood without also reading another piece it's been artificially separated from — the wrapper adds an interface with no reuse payoff.

The fix is usually to write the log statement, metric increment, or span attribute directly at the point where the condition is detected — inline in the `catch` block or `if` branch — rather than behind a dedicated single-use method. This keeps the telemetry statement next to the context that explains why it's there (what was being attempted, what inputs were involved), which is exactly the context a wrapper method's parameters have to re-derive or re-pass anyway. It also avoids inventing an interface (the wrapper's signature) that exists purely to serve one caller, which is pure added complexity with no reuse payoff.

This isn't an argument against factoring out genuinely shared instrumentation logic — a helper that computes a redaction rule, formats a common set of fields, or is called from several genuinely similar sites is a legitimate abstraction. The distinction is the same one that applies to any method extraction: pull logic into its own function when it's reused or when it meaningfully simplifies the call site, not by default just because "logging code" feels like it belongs somewhere else. See the [instrumentation litmus test](instrumentation-litmus-test.md) for the complementary question of *whether* to instrument a given change at all — this note is about *where* the instrumentation code should physically live once you've decided to add it.
