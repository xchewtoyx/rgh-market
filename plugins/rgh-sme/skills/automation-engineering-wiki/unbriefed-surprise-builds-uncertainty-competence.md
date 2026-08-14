---
type: concept
title: Unbriefed Surprise Builds Uncertainty-Management Competence
description: >
  A drill that is pre-briefed, run once, and debriefed only rehearses
  matching a known scenario to a known procedure; building the ability to
  handle genuinely unanticipated events requires exposure to surprise
  without advance warning, plus deliberate counterfactual rehearsal.
sources:
  - title: Resilience Engineering in Practice
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

# Unbriefed Surprise Builds Uncertainty-Management Competence

A training exercise that is pre-briefed, practiced once, and debriefed
eliminates exactly the thing it needs to build: the cognitive shock of a
genuine, unscripted surprise. Trainees who only ever face scenarios they
were warned about learn to match a recognized template to its procedure —
useful for the cases the procedure already covers, but it builds none of
the improvisational competence needed when the real event doesn't match any
template. Routine, homeostatic adaptation to normal daily variation doesn't
build this competence either; it only develops through recurrent exposure
to events that are actually unexpected and threatening at the time.

Two techniques that reintroduce that exposure deliberately:

- **Unbriefed simulator exposure** — running scenarios without advance
  warning, so the operator has to detect that something is wrong and adapt
  in real time, instead of executing a pre-loaded response.
- **Counterfactual mental simulation** — rehearsing "what-if" branches
  before they happen. Carthey et al. (2003) found this lowered mortality
  among pediatric cardiac surgeons, who used it to proactively rehearse
  complications before operating rather than only reacting to them once
  they occurred.

This is a more specific claim than [fire drills and game
days](confidence-decay-in-unpracticed-safeguards.md): a fire drill mainly
tests whether a *specific mechanism* (a failover, a restore path) still
works, and can be effective even when scripted. Building general
uncertainty-management competence in the *people* who'd have to improvise
past that mechanism's limits requires the drill to withhold the script —
without the surprise, repetition still produces [confidence
decay](confidence-decay-in-unpracticed-safeguards.md) in whatever wasn't
rehearsed, just more slowly. It is the concrete answer to [automation
bias](automation-bias.md)'s general prescription of "periodic manual
drills": not just running the manual path occasionally, but running it
without telling the operator in advance which failure they're about to
face.
