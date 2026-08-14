---
type: concept
title: Eval Saturation
description: >
  A capability eval near 100% pass rate has stopped giving improvement
  signal, and near-saturation score deltas understate real capability gains
  because only the hardest remaining tasks can still move the number.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Going from zero to one: a roadmap to great evals for agents"
---

A [capability eval](capability-vs-regression-evals.md) starts useful by
design — a low pass rate on purpose, giving a target to climb toward. That
usefulness has an expiry date: as agents improve, pass rate climbs toward
100%, and an eval that every agent already passes has run out of headroom to
distinguish "good" from "better." This is **saturation**: the eval still
correctly reports whether an agent can do the thing, but it can no longer
tell you how much further ahead one agent is than another, because there's
no remaining room above the ceiling to show it.

**Saturation makes score deltas deceptive, not just uninformative.** As an
eval approaches its ceiling, only the hardest tasks remain unsolved, so a
genuinely large capability jump can register as a small score increase
(going from 92% to 96% may represent solving several previously-intractable
problem classes, not four more easy points). Reading a saturating eval's
score at face value, the same way an unsaturated eval's score is read,
understates real progress — teams have been misled into judging a model
unimpressive because a saturating eval's headline number barely moved, when
a fresh eval built around the model's newly-unlocked capabilities showed
clear gains.

Design response: watch pass rate trend over time as a signal to retire or
replace an eval, not just to celebrate it. A saturating capability eval
should [graduate into the regression suite](capability-vs-regression-evals.md)
(repurposed as "can we still do this," not "can we do this at all") while a
*new* capability eval targeting the next tier of difficulty takes its place
as the thing actually being climbed toward — see
[eval-driven development](eval-driven-development.md) for building that next
eval ahead of the capability that will eventually clear it.
