---
type: concept
title: Assumption Verification Via Runtime Instrumentation
description: Checking an assumed equivalence or invariant against live data with an assertion or log before committing to a change or claim that depends on it.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring: Improving the Design of Existing Code (2nd ed.) (Martin Fowler), ch. 8, Moving Features — Move Field"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring: Improving the Design of Existing Code (2nd ed.) (Martin Fowler), ch. 9, Organizing Data — Replace Derived Variable with Query"
---

# Assumption Verification Via Runtime Instrumentation

Some claims of equivalence ("these two values are always the same," "this consolidation changes nothing observable") cannot be checked by reading the code or reasoning in the abstract — they depend on what real, live data actually looks like, which may include cases the reasoner never considered. **Assumption verification via runtime instrumentation** is the practice of adding a cheap, temporary check (an assertion, a log statement, or a direct data query) that fires on real execution paths or real stored data, and observing it for a period before treating the assumption as established.

## The technique

1. Identify the specific assumption a planned change or claim depends on (e.g., "every record of type X currently agrees with record of type Y on this field").
2. Instrument both sides of the assumed equivalence with a check that fires during normal operation — an `assert(a === b)` on a live code path, a log line recording any mismatch, or a one-off query across stored data.
3. Let the instrumentation run against real traffic or real data before relying on the assumption. Only once it has run without contradiction do you have actual evidence for the claim, as opposed to a plausible-sounding belief about it.
4. Only then complete the change that assumes equivalence (e.g., delete the now-redundant field, collapse two code paths into one).

A second, common variant of the same technique: when a stored value could instead be computed on demand, add an assertion that the stored value and the freshly-computed value agree at the point of use, run it under real test/production traffic, and only delete the stored value once the assertion has never fired. The assertion is doing real evidentiary work here — it is "the step that actually validates the underlying hypothesis" that the two are interchangeable, not a formality performed after the decision is already made.

## Why this differs from ordinary testing

Ordinary tests exercise cases the author thought to write down. This technique instead observes real, already-occurring cases the author may not have anticipated — compare [production fault injection verification](production-fault-injection-verification.md), which does not wait for a real fault to occur naturally but deliberately manufactures one in production to generate the needed evidence faster — it substitutes population-scale evidence for a hand-picked sample. It is the natural verification step whenever a change's safety hinges on a claim of the form "X and Y never actually disagree in practice," which cannot be settled by inspecting the code that produces X and Y, only by watching what they actually produce. See [test oracle self-validation](test-oracle-self-validation.md) for the related but distinct check of confirming a verification mechanism can detect a violation at all, and [non-conclusive evidence still shifts probability](non-conclusive-evidence-still-shifts-probability.md) for why an instrumentation window with no observed contradiction is evidence in favor of the assumption without being proof of it.
