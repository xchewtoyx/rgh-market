---
type: concept
title: Difficulty Explaining Something Signals a Problem With the Thing Itself
description: >
  When a short, honest, complete explanation of something keeps eluding
  you, the likeliest cause is that the thing being explained doesn't yet
  have a clean, single idea at its core — so write the explanation
  early and treat the struggle to write it as design feedback.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 15"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Martin Fowler, with Kent Beck), ch. 3, Comments"
---

There's a natural order that feels safe: build or finish the thing, then write the explanation of it once it's stable enough that the description won't need revising. This order has a real cost. By the time the artifact is finished, the writer has moved on mentally and wants to be done, so the explanation gets rushed — and rushed explanations of finished work tend to just narrate what's there rather than say what actually matters about it, because the writer is looking at the result rather than recalling the reasoning that produced it. Reasoning fades fastest of all: the rationale for a choice, the alternative that was rejected, the constraint that shaped the final form — all of it is freshest at the moment of deciding and hardest to reconstruct later, which means an explanation written last is missing exactly the content it should most want to capture.

Writing the explanation *before* the thing is finished — a summary of an approach before all its details are settled, a description of a section before its final prose is drafted — avoids that loss and gets a second benefit besides: the act of writing a short, complete, honest explanation forces a level of clarity about what the thing actually is that's easy to skip while still building it. An explanation drafted early isn't just documentation of a decision that already happened; writing it is itself part of making the decision well.

This gives explanation-writing a diagnostic use beyond its ordinary communicative one: **if a short, complete, and honest explanation keeps eluding you, that's evidence the thing being explained doesn't have a clean idea at its core yet** — not evidence that you personally need to try harder at writing. A struggle to summarize something in a sentence or two, where every attempt either omits something essential or balloons past what a summary should be, usually means the underlying material is doing two unrelated jobs, or lacks a single organizing point, and the fix is to rework the material rather than to keep drafting sentences. The one caveat that keeps this diagnostic honest: it only works if the short explanation is actually complete and clear. An explanation that's short because it's vague, or cryptic rather than genuinely simple, isn't evidence of anything good — it's just a different way of hiding the same unresolved problem, exactly the failure [choosing the right altitude](choosing-a-different-altitude-than-what-its-explaining.md) is meant to catch.

The same diagnostic shows up at the scale of a single comment: a strong urge to write an explanatory comment next to a piece of code is itself a signal worth investigating before it's satisfied by writing the comment. The recommended order is to try first to reshape the thing so that the comment becomes unnecessary — an unclear block becomes its own well-named unit, an already-separated piece that still needs explaining gets a better name — and only write the comment if that reshaping genuinely can't capture what needs saying. Treating the impulse to explain as a prompt to first check whether the thing itself can be made to need less explaining, rather than as a prompt to explain more, applies equally to prose sections as it does to code.
