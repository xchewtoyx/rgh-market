---
type: concept
title: Seeking Ever-Weaker Failure Signals
description: >
  As an organisation gets better at solving problems it must lower its
  threshold for what counts as a problem, or learning stalls exactly when
  the remaining risks become invisible.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
  - title: Managing the Unexpected
    resource: "Managing the Unexpected (Weick, Sutcliffe), ch. 1"
---

Steven Spear's characterisation of resilient organisations: they are
"skilled at detecting problems, solving them, and multiplying the effect by
making the solutions available throughout the organization … responding to
crises is not idiosyncratic work. It is something that is done all the time.
It is this responsiveness that is their source of reliability."

Weick and Sutcliffe frame the same requirement as [strong response to weak
signals](strong-response-to-weak-signals.md): the normal instinct is weak
response to weak signal, strong response to strong signal — managing the
unexpected requires the opposite.

Sustaining that responsiveness requires a moving threshold: as incidents
become rare, what counts as an "incident" must shrink, so the learning
stream never dries up. Alcoa under Paul O'Neill is the model — once
workplace accidents became rare, O'Neill extended his 24-hour notification
requirement to *near-misses* (see the Alcoa case in [Vision
Zero](vision-zero.md)). Spear's observation on what that surfaced: safety
problems "reflected process ignorance," and the same ignorance was
manifesting as quality, timeliness, and yield problems — weak safety
signals were a window into systemic health generally.

Why the lowering matters:

- In mature systems, strong signals are gone by construction; what remains
  before a catastrophe are weak, ambiguous ones — and whether those are
  investigated or dismissed is a mindset question ([ambiguous
  threats](ambiguous-threats.md)).
- The reported-event stream maps survivable trouble, not fatal
  vulnerability ([Wald's bomber paradox](walds-bomber-paradox.md)); lowering
  the tolerance pushes attention toward [normal work and its
  workarounds](studying-normal-work.md), where drift actually lives.
- A falling incident count read as "we can relax" is the overconfidence
  [chronic unease](chronic-unease.md) exists to counter; read correctly, it
  is the cue to lower the threshold another notch.

The precondition is cheap, safe reporting: people only surface near-misses
and oddities in a culture where messengers are trained rather than shot
([Westrum](westrum-typology.md), [blame suppresses
reporting](blame-suppresses-reporting.md)).
