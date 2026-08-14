---
type: concept
title: Hyperaware Editing
description: >
  Classify every keystroke as changing behavior or not, in the moment you
  type it, not just after — fast tests make this sustainable, and the
  resulting flow state is refreshing, not exhausting, compared to editing
  without feedback.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 23"
---

Unlike metal, wood, or plastic, code doesn't fatigue from use — "if you
leave it alone, it never breaks." The only source of faults is human
editing, and editing is mechanically trivial (anyone can type arcane
nonsense into a compiler) — "code is pretty fragile material," and
developers are the primary fault-injection mechanism.

The central discipline: classify every keystroke as either changing behavior
or not, *while typing it*, not just after the fact. A comment — no change. A
string literal — usually yes, unless in dead code. Even whitespace is,
technically, refactoring in a micro sense; changing a numeric literal is a
functional change, not a refactoring. "This is the meat of programming,
knowing exactly what each of our keystrokes does."

A sub-second test harness (see
[unit testing fundamentals](unit-testing-fundamentals.md) and
[lag time](lag-time.md)) is what makes this awareness sustainable rather
than exhausting: it lets you run tests after nearly every keystroke-group
and get a near-continuous read on whether behavior just changed. This
produces a distinct mental state — **hyperaware editing**, comparable to a
flow state achievable through fast testing or pair programming — that's
refreshing rather than tiring: "I get far more tired when I'm not getting
any feedback." The real fatigue is the alternative: anxious effort spent
mentally tracking what's changed, half-expecting an undetected break.
