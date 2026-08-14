---
type: concept
title: ML Incident Anatomy Review Questions
description: A set of questions specific to reviewing an ML-centric outage, distinguishing fixing the immediate problem from prospective quality-improvement work that looks similar but isn't follow-up.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

Reviewing an ML-centric outage benefits from working through the same
underlying questions a [blameless postmortem](blameless-postmortems.md) or
[after action review](after-action-review.md) asks, but each carries an
ML-specific wrinkle worth asking explicitly:

- **Architecture and underlying conditions**: which pre-incident decisions
  set the stage for the outage?
- **Impact start**: how is the start of impact actually determined, given
  [ML outage boundary ambiguity](ml-outage-boundary-ambiguity.md) makes this
  harder to pin down than for a conventional outage?
- **Detection**: how easy was detection, and how did it actually happen —
  see [ML outage visibility gap](ml-outage-visibility-gap.md) for why the
  answer is often "a user noticed first."
- **Troubleshooting and investigation**: who was involved, and in what
  roles — was the investigation as wide as [ML incident organizational
  breadth](ml-incident-organizational-breadth.md) suggests it might need to
  be?
- **Impact**: what did the incident actually cost users, and how is that
  cost measured — quality-based ML impact rarely reduces to a single
  availability number.
- **Resolution**: how much confidence exists that the fix actually
  addressed the cause, rather than merely correlating with recovery?

The distinctly ML-flavored question is on follow-up: can *fixing* the
specific incident be cleanly distinguished from *improving* the model
generally, and how does the reviewer know follow-up work is actually done
rather than having quietly turned into ordinary prospective model-quality
engineering? Because every model is expected to keep improving after the
fact anyway, an ML incident's follow-up work can blend into the team's
regular improvement backlog in a way a conventional service's bug fix
doesn't — making it easy for a review to lose track of whether the
incident's specific action items were ever actually closed, as opposed to
superseded by general progress.

The recommended guard against that blending: define the model's ongoing
improvement process — what's tracked, what metrics matter, who reviews
progress — clearly enough, *before* incidents happen, that an incident's
findings can be fed into that existing process as reprioritized input
rather than spawning an ad hoc, uncontained "improve model performance"
project of their own. Without that pre-existing container, a review's
follow-up section tends to expand into open-ended improvement work with no
natural closing point, which is itself a review-quality failure distinct
from — but easy to mistake for — a properly scoped [action
item](action-item-quality.md).
