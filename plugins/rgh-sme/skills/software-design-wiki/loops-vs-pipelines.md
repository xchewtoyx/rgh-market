---
type: concept
title: "Code Smell: Imperative Loops Where a Pipeline Would Read Clearer"
description: >
  Where first-class functions are available, pipeline operators like filter
  and map often make what a loop includes and does to it more visible than
  an equivalent imperative loop body.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Fowler and Beck list plain imperative loops as a smell once a language
supports first-class functions well — cure:
[Replace Loop with Pipeline](replace-loop-with-pipeline.md). Pipeline
operators (filter, map, reduce) make what's being included and what
operation is applied to it visually clearer than a hand-rolled loop body
that mixes iteration, filtering, and accumulation together in one place.
This is a narrower, more mechanical case of [replacing loops with
pipelines as a code-obviousness improvement](code-obviousness.md) — the
authors note their own earlier edition took a softer stance only because the
Java-era languages they were writing about at the time lacked good pipeline
alternatives, not because the underlying argument has changed.
