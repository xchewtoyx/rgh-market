---
type: concept
title: The Signal Perception vs Translation Gap
description: >
  Failing to act on a weak signal is not always a failure to notice it — an
  organisation can perceive a diffuse anomaly perfectly well and still fail
  at the separate, structurally distinct step of translating that perception
  into a recognised, escalatable safety issue.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 10"
---

A regulatory inspection of Swedish nuclear power plants found a specific,
narrower failure than the usual diagnosis of "organisations miss weak
signals." Operators were, in fact, perceiving diffuse deviations and vague
problem symptoms without difficulty — most routine problems were being
anticipated and managed fine, where the plant maintained a constant working
state of unease and clear reporting channels. **The actual failure sat one
step later**: the organisation could not reliably *translate* a perceived
weak signal into a formally recognised safety issue with escalation
potential. Perception worked; translation did not.

This sharpens [ambiguous threats](ambiguous-threats.md) and [seeking
ever-weaker failure signals](seeking-weaker-failure-signals.md) into a more
precise diagnostic question. Those concepts describe *whether* a weak
signal gets investigated at all, and depend on an organisation's operating
mindset and how low its detection threshold is set. This concept describes
a distinct, later pipeline stage: even where the mindset is right and the
signal has already been noticed, a structural translation step can still
fail — and the fix for a translation failure is not the same fix as for a
perception failure (lowering a detection threshold does nothing if the
problem is that noticed signals have nowhere structurally sound to go).

**Where translation concretely broke down**: the daily forum meant to
perform this translation — a morning planning meeting nominally serving as
the primary defence against vague, diffuse issues — was dominated by an
"operations view," with attendance from other relevant departments
(maintenance, chemistry, technical analysis, independent safety) left
optional. Independent safety representatives who did attend frequently sat
as passive listeners rather than actively challenging what was raised.
Leadership believed this meeting functioned as a real barrier; in practice
it was, in the inspectors' words, "a barrier full of holes" — present on
paper, but structurally unable to perform the translation work it was
relied on for, because the range of perspectives needed to recognise a
diffuse symptom as significant was never actually in the room. [Diversity
as a safety resource](diversity-as-a-safety-resource.md) covers what
fixing a forum like this structurally requires.
