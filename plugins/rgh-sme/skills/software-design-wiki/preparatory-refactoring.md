---
type: concept
title: Preparatory Refactoring
description: >
  When a feature is awkward to add because of how the code is currently
  structured, refactor first to make the feature easy to add, then add it —
  rather than wedging the new behavior into the inconvenient shape.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 1-2"
---

**"When you have to add a feature to a program but the code is not
structured in a convenient way, first refactor the program to make it easy
to add the feature, then add the feature."** The best time to refactor is
right before adding a feature, restructuring so the new capability becomes a
small, easy addition rather than something copy-pasted and left to diverge —
the seed of [code duplication](code-duplication-red-flag.md). Quoted
metaphor (Jessica Kerr): driving 20 miles to the highway to go 100 miles east
fast, rather than trudging straight through the woods.

The same logic applies when fixing a bug: refactor while fixing it, to
reduce the chance of the same bug recurring nearby.

A companion, distinct trigger is **comprehension refactoring**: refactor
code you're trying to understand so it says what it does more clearly —
moving understanding from your head into the code, testable by re-running
the software. Ralph Johnson's framing: early refactorings on unfamiliar code
are "wiping the dirt off a window so you can see beyond" — dismissing this
as mere fiddling means missing opportunities the confusion was hiding.
[Scratch refactoring](scratch-refactoring.md) is the more extreme,
throwaway-only version of using refactoring purely to learn code, kept
distinct from comprehension refactoring's intent to keep the result.

A third trigger, **litter-pickup refactoring**: when you see code that's
needlessly convoluted, fix it if cheap; if costly, note it and defer — the
"campsite rule," leave the code cleaner than you found it, applied
incrementally even if full cleanup takes months. This is small-scale
[strategic, reactive investment](strategic-vs-tactical-programming.md), and
it only works because refactoring's
[behavior-preserving](refactoring-preserves-behavior.md) discipline means the
codebase is never left broken partway through.

Across all three triggers, almost all refactoring should be **opportunistic**
— woven into the natural flow of adding features or fixing bugs, not a
separately scheduled activity, "any more than you set aside time to write if
statements." Stated principle: **"You have to refactor when you run into
ugly code — but excellent code needs plenty of refactoring too,"** because
yesterday's correct tradeoffs may be wrong for today's new feature set.
Dedicated, planned refactoring time is legitimate but should be rare — for
example, a team that has neglected refactoring doing one deliberate
catch-up effort.
