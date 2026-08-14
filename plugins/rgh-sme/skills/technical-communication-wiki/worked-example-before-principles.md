---
type: concept
title: Lead With a Worked Example Before Stating Principles
description: >
  For material a reader needs to internalize as a skill rather than
  just look up, one extended concrete example that builds intuition
  first makes the generalized definitions and rules that follow
  actually stick, instead of landing as abstract vocabulary with
  nothing yet to attach to.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Martin Fowler, with Kent Beck), ch. 1–2"
---

Two orderings are available for teaching a technical practice: state the definitions and rules first and illustrate them afterward, or walk through one substantial concrete example first and only afterward name the general principles it demonstrated. The second ordering is the stronger default whenever the goal is for the reader to internalize a skill, not just look up a fact — a reader who meets a term like "extract a function to remove duplication" before having seen a single case where that mattered has nowhere to hang the definition; the same reader who has just spent several pages watching one piece of code get incrementally reshaped already has a concrete referent in mind, and the subsequent principle reads as a description of something they just watched happen rather than a new, arbitrary rule to memorize.

The technique works best with one continuous, realistic example followed start-to-finish rather than a scattering of small, disconnected snippets — a single running scenario lets each successive step build on a state the reader already understands, and lets the writer show *why* a given move was made at that specific point (what problem it was solving right then), which a rule stated in isolation can't convey. This is the inverse of [the pyramid structure](pyramid-structure.md)'s discipline of leading with the conclusion: pyramid structure serves a reader who wants the point fast and the support only as needed, which fits reference and decision material; worked-example-first serves a reader who is building a mental model from scratch and needs the concrete case to make an abstraction meaningful at all, which fits tutorials and skill-building material. Choosing between them is a genre decision — is this reader looking something up, or learning to do something — not a matter of one ordering being more rigorous than the other.

A generalization chapter that follows a worked example can then afford to be genuinely abstract and definitional, because it is doing a different job than a first-touch introduction would be: naming and cross-referencing what the reader already has intuition for, rather than building that intuition from nothing.
