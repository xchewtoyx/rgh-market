---
type: concept
title: Normalization of Deviance
description: >
  Vaughan's mechanism by which incremental nonconformity becomes the accepted
  local norm, because each small rule departure is rewarded immediately and
  punished only eventually, if ever.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 5"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
  - title: Managing the Unexpected
    resource: "Managing the Unexpected (Weick, Sutcliffe), ch. 3"
---

Normalization of deviance (Diane Vaughan, 1996, from her analysis of the
Challenger launch decision) names the ratchet at the core of [drift into
failure](drift-into-failure.md): a small departure from a rule or design
assumption produces an immediate efficiency or production reward and no
immediate adverse safety consequence, so the group absorbs it as the new
baseline. The next departure is measured against that baseline, not the
original standard. Deviance is thus normalised incrementally — no one ever
decides to be unsafe.

Key properties:

- It is a *social and organisational* process, not individual recklessness:
  the departures are discussed, rationalised, and often formally accepted.
- The reward asymmetry does the work: production rewards are immediate and
  certain; safety costs are delayed and probabilistic (see [goal
  conflicts](goal-conflicts-and-production-pressure.md)).
- From inside, each step looks like learning ("we now know this margin is
  conservative"), which is why participants pass every test of [local
  rationality](local-rationality-principle.md).
- Labelling it "violation" after the fact is [hindsight
  bias](hindsight-bias.md) — at the time, the deviant practice *was* the norm,
  which is also why counting rule violations reveals little (see
  [work-as-imagined vs work-as-done](work-as-imagined-vs-work-as-done.md)).

Vaughan's original Challenger analysis frames the mechanism as a repeating
six-step cycle: (1) the starting belief that a redundant, well-tested system
has risk under control; (2) a signal of potential danger appears; (3) an
official act acknowledges the signal (a review is called); (4) the evidence
is reviewed; (5) an official act *normalises* the risk as "in-family" or
expected, reasoning that redundancy exists elsewhere or that the technology
has already earned confidence; (6) operation continues on that basis,
because nothing went wrong and the review pronounced things under control.
Each pass through the cycle both reinforces the belief that risk is under
control and resets the baseline for the next signal — the mechanism behind
[decrementalism](decrementalism.md).

The launch-eve instruction to a hesitating Challenger engineer to "take off
his engineering hat and put on his management hat" is the moment this cycle
meets [managerial buffer failure](middle-managers-as-safety-buffer.md)
directly: a normalised risk assessment only holds if nobody with contrary
evidence is empowered to reopen it, and switching a specific person's
operative identity at the decision point is one concrete way that
empowerment gets removed.

The mechanism also digests live warnings: before the Columbia disaster
(2003), engineers reported the launch foam strike immediately, and were told
foam dislodgement was a known, never-yet-catastrophic "maintenance problem"
— the normalised category absorbed the signal (see [ambiguous
threats](ambiguous-threats.md)).

Detection requires comparing today's actual practice against the original
assumptions, not against yesterday's practice — one reason [chronic
unease](chronic-unease.md) prescribes actively seeking bad news and minority
viewpoints rather than trusting the absence of incidents.
