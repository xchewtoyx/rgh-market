---
type: concept
title: Sandwich Technique
description: >
  State the goal at both the start and the end of a long prompt so a refocus
  after intervening context restores precise operational intent.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 6"
---

The sandwich technique places what you want the model to do at both ends of the
prompt: an **introduction** that sets document type and focus, then a long
middle of context, then a **refocus** that re-asks the question with precise
operational detail (and often output-format constraints). In a chat
transcript this can look like a system message plus a first user turn stating
the goal, a long back-and-forth of context-gathering turns, then a final
assistant turn signaling something like "I believe this is all the
information I need," followed by a final user turn re-asking the question.

Introduction vs refocus: the [introduction](prompt-introduction.md) stages
("thinking about book suggestions for X"); the refocus commands ("recommend
the best next book, narrative prose, currently available"). After heavy
context gathering — chat turns, retrieved blocks, tool traces — the original
ask is easy to bury in the [Valley of Meh](valley-of-meh.md), the weak band
[lost in the middle](lost-in-the-middle.md) attention creates; the trailing
restatement recovers it. A short extra refocus at the very end can lock
format. Often merge the refocus with the
[prompt transition](prompt-transition.md) by beginning the answer as a problem
restatement the model must complete.
