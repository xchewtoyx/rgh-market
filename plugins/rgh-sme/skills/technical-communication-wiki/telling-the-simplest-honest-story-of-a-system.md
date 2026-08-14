---
type: concept
title: Telling the Simplest Honest Story of a System
description: >
  Force yourself to explain a complex system using only its handful of
  most essential concepts, as if to someone who knows nothing about it,
  then add detail back in layers — the discomfort of what you have to
  leave out reveals what's actually essential versus merely accumulated.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 17"
---

A useful exercise for understanding (or re-explaining) a system that's grown complicated over time: have someone ask "what is this system, really?" and force an answer built from only a handful of core concepts, pitched as if to a reader who knows nothing about it — then progressively layer in the next-most-important facts, one at a time, naming explicitly what each added layer is a simplification of. The discomfort of leaving something out ("but it also has to handle X!") is the exercise working correctly, not a flaw to fix by cramming X back in immediately: being forced to omit something is what makes the difference between essential and merely-accumulated complexity visible in the first place, a difference that's invisible when everything is described at once and with equal weight.

The resulting simplified story is not a spec and doesn't need to be literally true in every detail — it's a working guide, and a system that ends up more complicated than its own simplest honest story is not automatically a problem, since real, useful systems accumulate necessary complexity over time that a first-pass story can't capture. Where this becomes genuinely diagnostic is at decision time: when two ways of extending or changing a system are otherwise comparable, prefer whichever one keeps the team's honest simple story of the system true, or requires the least strained new addition to it. A change that can't be folded into the existing story without a jarring new exception is a sign the change itself, or the story, needs rethinking — divergence between what a team can honestly say a system does and what the system actually does is itself a warning sign, in either direction.

This exercise works best done conversationally with at least one other person listening and pushing back on omissions, rather than written alone — a listener's "but what about..." interruptions are exactly what surfaces the boundary between essential and incidental. See [choosing a different altitude than what it's explaining](choosing-a-different-altitude-than-what-its-explaining.md) for the underlying single-explanation version of the same discipline, and [conversational vocabulary as a documentation diagnostic](conversational-vocabulary-as-a-documentation-diagnostic.md) for a related technique that uses the same gap — between how people naturally talk about something and how it's actually described — as a signal of where documentation or code has drifted from the team's real mental model.
