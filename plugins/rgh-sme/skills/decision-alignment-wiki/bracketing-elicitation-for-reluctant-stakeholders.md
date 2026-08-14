---
type: concept
title: Bracketing Elicitation for Reluctant Stakeholders
description: >
  When a stakeholder insists they don't know a numeric threshold,
  offer absurdly loose bounds first and progressively tighten them
  until they reject one, converting "I don't know" into a usable
  range.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 19"
---

A stakeholder who genuinely believes they have no opinion on a
required number ("how fast does this need to respond?") will often
still reject a bad answer the moment they hear one — the ignorance is
about naming a value from scratch, not about recognizing when a
candidate value is unacceptable. Exploit this asymmetry directly:
propose a deliberately loose, easy-to-reject bound first ("would 24
hours be acceptable?"), let them reject it, then tighten in steps (1
hour? 5 minutes? 10 seconds?) until they land on something they can
actually live with. The stakeholder ends the exercise having stated a
real, usable range, even though they began insisting they had no
requirement at all.

This works because rejecting a proposal requires far less confidence
than generating one — a person unwilling to commit to "the number
should be X" will readily say "no, that's much too slow," and a
handful of rejections triangulate a workable bound just as
effectively as a direct answer would have. It matters that the
opening bound be genuinely loose rather than a plausible-sounding
guess: starting too close to a reasonable value risks anchoring the
stakeholder on it, whereas an obviously bad opening bound makes
rejection easy and costs the stakeholder nothing to voice.

The resulting range is often decision-relevant on its own, without
ever being narrowed to a single number — a target somewhere between
10 seconds and 100 milliseconds implies a materially different
design than one between 24 hours and 10 minutes, so extracting even a
coarse bound from a stakeholder who "doesn't know" can be enough to
commit to a direction. Use this before falling back on
[value-of-information-for-what-to-analyze](value-of-information-for-what-to-analyze.md)
to justify further measurement — a stakeholder-supplied bound is
cheaper to obtain than a formal analysis, and may already be
narrow enough that no further investigation earns its cost. It
complements
[pre-committing-success-criteria](pre-committing-success-criteria.md):
that technique locks a threshold the team already knows how to state;
this one is what to do first when nobody on the stakeholder side
believes they can state one at all.
