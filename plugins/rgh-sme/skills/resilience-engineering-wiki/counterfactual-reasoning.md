---
type: concept
title: Counterfactual Reasoning in Investigations
description: >
  Explanations of the form "they should have / failed to / if only they had"
  describe a utopian world that never existed and explain nothing about why
  people actually did what they did.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 2"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
---

Counterfactuals are statements about what did *not* happen: "they shouldn't
have…", "they failed to…", "if only they had…". They lay out a path the
investigator can see only with the outcome in hand, then measure real
behaviour against it. As explanation they are empty: a description of a
non-existent, hindsight-constructed reality says nothing about why
practitioners acted as they actually did.

Official reports are full of them:

- **USAir 1016 (windshear)**: the NTSB computed that the aircraft could have
  survived given a maintained 15-degree pitch, 1.93 EPR thrust, and a
  particular gear-retraction schedule — utopian post-hoc arithmetic no crew
  in the encounter could have performed.
- **Royal Majesty grounding (1995)**: the NTSB noted the officers "should not
  have missed" GPS/Loran-C coordinate discrepancies. From inside the tunnel,
  facing forward with the instruments they trusted, the ship *was* on track.

Detection and repair:

- Treat every "should have / failed to" in a draft finding as a flag: it
  marks a place where the analysis substituted the investigator's
  [hindsight](hindsight-bias.md) for the operator's situation.
- Convert each counterfactual into the [local rationality
  question](local-rationality-principle.md): what made the path actually
  taken the sensible one at the time — what cues, expectations, and [goal
  pressures](goal-conflicts-and-production-pressure.md) pointed there?
- Counterfactuals often smuggle in [judgmental
  language](judgmental-language.md); the two travel together.
- The rule is operational in mature review cultures: Etsy's blameless
  post-incident reviews explicitly disallow "would have" and "could have"
  statements, on the grounds that they describe the system as imagined
  rather than the system that actually exists ([work-as-imagined vs
  work-as-done](work-as-imagined-vs-work-as-done.md)).
