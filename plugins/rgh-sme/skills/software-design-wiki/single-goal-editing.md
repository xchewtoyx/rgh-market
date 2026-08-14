---
type: concept
title: Single-Goal Editing
description: >
  Programming is the art of doing one thing at a time — note down
  distractions discovered mid-change instead of chasing them immediately,
  finish and verify the current change first, then address the noted item
  as its own discrete step.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 23"
---

The "super-smart programmer who holds the whole system in their head" ideal
isn't actually correlated with better decision-making: "judgment is a key
programming skill, and we can get into trouble when we try to act like
super-smart programmers." A chaotic editing session jumping between an
in-progress feature, an impulsive cleanup, a needed method call, and a
discovered side-issue all at once can feel exhilarating in the moment, but
routinely ends with the last stretch of the session spent fixing what the
earlier jumping-around broke — genuinely inefficient, not just messy in
style. A disciplined alternative: write candidate distractions down (e.g.
"method X needs a look") rather than chasing them immediately, finish the
current change, rerun tests, and *then* address the noted item as its own
discrete step.

Personal mantra: **"programming is the art of doing one thing at a time."**
A concrete pairing practice: explicitly ask your partner (and have them ask
you) "What are you doing?" whenever attention seems to be splitting; if the
honest answer names more than one thing, pick one and defer the rest. The
claim isn't just about discipline for its own sake — "frankly, it's just
faster."

This discipline is why [pair programming](hyperaware-editing.md) is
recommended without qualification specifically for legacy dependency-
breaking work — a second person catching a wandering focus, or catching a
mistake in an untested step, matters more here than in ordinary
development: "working in legacy code is surgery, and doctors never operate
alone."
