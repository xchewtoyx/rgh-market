---
type: concept
title: The Social Redundancy Fallacy
description: >
  Adding human checking layers does not stack reliability the way redundant
  components do — human checkers are interdependent, so double-checking can
  increase error rates instead of reducing them.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 5"
---

Engineering redundancy works because redundant components fail independently.
People do not. When a second person is added to check the first — two nurses
cross-checking a drug dose, a reviewer countersigning a calculation — the
checkers become interdependent: each relies on the other's competence and
diligence, attention diffuses ("someone else is looking at this"), and social
dynamics discourage challenging a trusted colleague. Studies of double-checking
regimes show error rates can *increase* after the second checker is added.

This is a limitation of the [Swiss cheese model](swiss-cheese-model.md)'s
plug-the-holes strategy: a new human barrier layer is not an independent
defence, and adding it may weaken the layers it touches.

Implications:

- Distrust countermeasures of the form "add a sign-off / a second pair of
  eyes / an approval step" as the fix after an incident — they are a classic
  [quick fix](fallacy-of-the-quick-fix.md) that adds [safety
  clutter](safety-clutter.md) while leaving the conditions that produced the
  error untouched.
- Where cross-checking genuinely helps, it is because the second person brings
  a *different perspective or information source*, not mere repetition of the
  same check.
